import pandas as pd
from .pyADMETPredictorWrapper import RESTWrapper


def pyAP_get_ADMET_properties_names(rest_configuration, exclude_3D=True):
    rw = RESTWrapper(rest_configuration)
    admet_props = rw.get_admet_properties()
    prop_groups = ["PCB", "TRN", "MET", "TOX", "DIL", "DSC", "USR"]
    admet_props_split = {}
    for item in prop_groups: admet_props_split[item] = []
    for prop in admet_props.json()["properties"]:
        if prop["name"].endswith("3D") and exclude_3D:
            continue
        admet_props_split[prop["module"]].append(prop)
    return admet_props_split    

async def pyAP_get_descriptors_via_REST(smiles: list, ids: list, rest_configuration: dict, smiles_prop="SMILES", index_prop="Identifier", properties_modules=["DSC", "PCB"], 
                         exclude_3D=True, infer_dtypes=True, await_time=600) -> pd.DataFrame:
    """_summary_

    Args:
        mols (list): list of SMILES
        rest_configuration (dict): configuration of the rest connection
        smiles_prop (str, optional): name of the property containing the smiles code. Defaults to "SMILES".
        index_prop (str, optional): name of the property containing the index/identifier. Defaults to "Name".
        properties_modules (list, optional): properties to be calculated in the module resolution. Defaults to ["DSC", "PCB"].
        exclude_3D (bool, optional): flag if 3D descriptors should be excluded. Defaults to True.
        infer_dtypes (bool, optional): flag if the data types of resulting data frame should be inferred. Defaults to True.
        await_time (int, optional): await time in the asynchronous call to AP service /get_results endpoint (seconds). Defaults to 600.

    Returns:
        pd.DataFrame: reulting data frame with the results
    """
    rw = RESTWrapper(rest_configuration)
    admet_props = rw.get_admet_properties()

    admet_props_split = {"PCB": [], "TRN": [], "MET": [], "TOX": [], "DIL": [], "DSC": [], "USR": []}
    for prop in admet_props.json()["properties"]:
        admet_props_split[prop["module"]].append(prop)

    REQ_descriptors = []
    for module in properties_modules:
        module_desc = [item["name"] for item in admet_props_split[module] if item["type"] == "Real" or item["type"] == "Integer"]
        if exclude_3D:
            module_desc = [item for item in module_desc if not item.endswith("3D")]
        REQ_descriptors += module_desc

    # smiles = [item.GetProp(smiles_prop) for item in mols]
    # ids = [item.GetProp(index_prop) for item in mols]
    
    payload = rw.create_prediction_payload(smiles, ids, REQ_descriptors)
    rsp = rw.consume_admet_service_endpoint(endpoint="predict_admet", request_type="POST", payload=payload)
    jobid = rsp.json()["jobid"]
    task = await rw.retrieve_results(endpoint="getstatus", jobid=jobid, awaitime=await_time)
    descriptors = pd.DataFrame(task.result().json()["results"]).T.map(lambda x: x["value"])

    if infer_dtypes:
        for col in descriptors.columns:
            dt = infer_col_dtype(descriptors[col])
            descriptors[col] = descriptors[col].astype(dt)
        
    return descriptors.copy()

def infer_col_dtype(col):
    """
    Infer datatype of a pandas column, process only if the column dtype is object. 
    input:   col: a pandas Series representing a df column. 
    """

    if col.dtype == "object":
        # try numeric
        try:
            col_new = pd.to_datetime(col.dropna().unique())
            return col_new.dtype
        except:
            try:
                col_new = pd.to_numeric(col.dropna().unique())
                return col_new.dtype
            except:
                try:
                    col_new = pd.to_timedelta(col.dropna().unique())
                    return col_new.dtype
                except:
                    return "object"
    else:
        return col.dtype