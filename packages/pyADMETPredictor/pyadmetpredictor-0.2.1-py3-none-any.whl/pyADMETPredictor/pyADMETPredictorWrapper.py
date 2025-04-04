import requests
import asyncio
import logging
import tempfile
import subprocess
import os
import shutil
import pandas as pd
import numpy as np
from rdkit import Chem
from pathlib import Path
from io import StringIO
from datetime import datetime, timedelta
from collections import defaultdict
from PIL import Image

LOGGER = logging.getLogger(__name__)
DEFAULT_LOG_FILE_NAME = 'ADMET_Predictor_Errors.log'

class Wrapper():
    def __init__(self) -> None:
        """
        Abstract class
        """
        pass

class RESTWrapper(Wrapper):
    def __init__(self, config: dict) -> None:
        """ REST wrapper constructor

        Args:
            config (dict): configuration of the REST connection
        """
        self.config = config

    def create_full_address(self, endpoint: str, sep="/") -> str:
        """_summary_

        Args:
            endpoint (str): the name of the ADMET Predictor endpoint
            sep (str, optional): separator Defaults to "/".

        Returns:
            str: _description_
        """
        colon = ":"
        slash = "/"
        return self.config["protocol"]+ colon + slash + slash + self.config["host"] + colon + self.config["port"] + slash + endpoint

    def create_prediction_payload(self, mols: list, ids: list, props: list) -> dict:
        """_summary_

        Args:
            mols (list): collection of RDKit molecules
            ids (list): collection of identifiers
            props (list): collection of properties to be calculated

        Returns:
            dict: _description_
        """
        payload = {}
        compounds = []
        for mol, id in zip(mols, ids):
            single_mol = {}
            single_mol["id"] = id
            single_mol["mol"] = mol
            compounds.append(single_mol)

        payload["compounds"] = compounds
        payload["properties"] = props
        return payload
    
    def get_admet_properties(self) -> requests.Response:
        """consumes the /getprops_admet endpoint

        Returns:
            requests.Response: HTTP response
        """
        endpoint = "getprops_admet"
        full_address = self.create_full_address(endpoint)
        return requests.get(full_address)
    
    def get_admet_params(self) -> requests.Response:
        """consumes the /getparams_admet endpoint

        Returns:
            requests.Response: HTTP response
        """        
        endpoint = "getparams_admet"
        full_address = self.create_full_address(endpoint)
        return requests.get(full_address)
    
    def get_fafb_properties(self) -> requests.Response:
        """consumes the /getprops_fafb endpoint

        Returns:
            requests.Response: HTTP response
        """           
        endpoint = "getprops_fafb"
        full_address = self.create_full_address(endpoint)
        return requests.get(full_address)
    
    def get_fafb_params(self) -> requests.Response:
        """consumes the /getparams_fafb endpoint

        Returns:
            requests.Response: HTTP response
        """             
        endpoint = "getparams_fafb"
        full_address = self.create_full_address(endpoint)
        return requests.get(full_address)
    
    def get_optdose_properties(self) -> requests.Response:
        """consumes the /getprops_optdose endpoint

        Returns:
            requests.Response: HTTP response
        """           
        endpoint = "getprops_optdose"
        full_address = self.create_full_address(endpoint)
        return requests.get(full_address)
    
    def get_optdose_params(self) -> requests.Response:
        """consumes the /getparams_optdose endpoint

        Returns:
            requests.Response: HTTP response
        """                   
        endpoint = "getparams_optdose"
        full_address = self.create_full_address(endpoint)
        return requests.get(full_address)
    
    def get_atomic_properties(self) -> requests.Response:
        """consumes the /getprops_atomic endpoint

        Returns:
            requests.Response: HTTP response
        """            
        endpoint = "getprops_atomic"
        full_address = self.create_full_address(endpoint)
        return requests.get(full_address)
    
    def get_metab_enz_properties(self) -> requests.Response:
        """consumes the /getprops_metab_enz endpoint

        Returns:
            requests.Response: HTTP response
        """   
        endpoint = "getprops_metab_enz"
        full_address = self.create_full_address(endpoint)
        return requests.get(full_address)
    
    def get_metab_params(self) -> requests.Response:
        """consumes the /getparams_metab endpoint

        Returns:
            requests.Response: HTTP response
        """           
        endpoint = "getparams_metab"
        full_address = self.create_full_address(endpoint)
        return requests.get(full_address)
    
    def consume_admet_service_endpoint(self, endpoint, request_type="GET", payload=None) -> requests.Response:
        """consumes the generic endpoint GET/POST endpoint

        Returns:
            requests.Response: HTTP response
        """           
        #endpoint = "getparams_metab"        
        full_address = self.create_full_address(endpoint)
        print(full_address)
        if request_type=="GET":
            response = requests.put(full_address)
        elif request_type=="POST":
            response = requests.post(full_address, json=payload)
        else:
            raise NotImplementedError
        return response
    
    def get_errorlog(self, jobid: int) -> requests.Response:
        """consumes the /geterrorlog endpoint

        Returns:
            requests.Response: HTTP response
        """         
        endpoint = "geterrorlog"
        full_address = self.create_full_address(endpoint)
        payload = {"jobid": jobid}
        response = requests.post(full_address, json=payload)
        return response

    async def get_results(self, endpoint: str, jobid: int, id:str=None) -> requests.Response:
        """asynchronous await for the completion of the calculation

        Returns:
            requests.Response: HTTP response
        """              
        payload = {"jobid": jobid}
        full_address = self.create_full_address(endpoint)
        if id:
            payload["id"] = id

        while True:
            response = requests.post(full_address, json=payload)
            #if response.status_code == 200:
            if response.json()["status"] == "complete":
                return response
            await asyncio.sleep(0.1)

    async def retrieve_results(self, endpoint: str, jobid: int, id: str=None, awaitime: int=5) -> asyncio.Task:
        """asynchronous retrieval of the results of the calculations

        Returns:
            requests.Response: asyncio.Task
        """        
        task = asyncio.create_task(self.get_results(endpoint=endpoint, jobid=jobid, id=id))
        then = datetime.now()
        delta = timedelta(seconds=awaitime)
        while True:
            now = datetime.now()
            status = task.done()
            if status: 
                break
            if now > then + delta: 
                task.cancel()
                break
            await asyncio.sleep(0.1)
        return task
    
class CMDWrapper(Wrapper):
    def __init__(self, config: dict) -> None:
        """asynchronous retrieval of the results of the calculations

        Returns:
        """    
        self._config = config
        self._script = None
    
    def extract_content_from_script(self, script_file: str) -> dict:
        """extraction of the script content

        Returns:
            dict: script as dictionary
        """            
        with open(script_file, "r") as f:
            content = f.readlines()

        extracted_content = []
        for l in content:
            if l[0].strip() != "#" and l != "\n":
                extracted_content.append(l.replace("\n", ""))

        extracted_content_d = {}
        for l in extracted_content:
            ecs = l.split(" ")
            k = ecs[0]
            if type(ecs[1:]) == list:
                v = " ".join(ecs[1:])
            elif type(v) == str:
                v = ecs[1]
            extracted_content_d[k] = v
        return extracted_content_d

    def _store_script_on_file(self, script, file_name):
        """storing the script on file

        Returns:
        """
        sep = " "
        eol = "\n"
        with open(file_name, "w") as f:
            for key, value in script.items():
                f.write(key+sep+value+eol)

    def _turn_mols_into_df(self, mols):
        merged_dict = defaultdict(list)
        
        dcts = [item.GetPropsAsDict() for item in mols]
        all_keys = set().union(*dcts)
        for d in dcts:
            for key in all_keys:
                merged_dict[key].append(d.get(key, None))
        merged_dict = dict(merged_dict)
        smiles = [Chem.MolToSmiles(item) for item in mols]
        df = pd.DataFrame(merged_dict)
        df = pd.concat([pd.DataFrame(smiles, columns=['SMILES'], index=df.index), df], axis=1)
        return df

    def execute(self) -> dict:
        """execute CMD task, either script or command line arguments-driven calculation

        Returns:
            dict: results, content depends on the CMD task
        """          
        LOGGER.info("Entering the pyADMET CMDWrapper execution...")
        htpk_calculation = False
        with tempfile.TemporaryDirectory() as tmpdir:
            output_postfix = '.dat'
            ap_command = [self._config["AP_executable"]]
            if self._config["script"] is not None:
                # create a filename of the script in the tmp location
                file_name_from_config = Path(self._config["script"]).name
                file_name = Path(tmpdir)/file_name_from_config
                # add prefixes to the output and log files
                output_file = Path(tmpdir)/Path(self._script["outputFile"]).name
                log_file = Path(tmpdir)/Path(self._script['logFile']).name
                self._script["outputFile"] = output_file.as_posix()
                self._script["logFile"] = log_file.as_posix()
                # store script in the in the tmp location
                self._store_script_on_file(self._script, file_name)
                ap_command.append(file_name.as_posix())
                # output files are considered to be only the structure and log
                # some script-specific adjustments can be considered later
            else:
                # not script case
                for k, v in self._config.items():
                    if k=='AP_executable' or k=='script': 
                        continue
                    elif k=='input_structures':
                        # Input structures, should be the last in json file, a weak part
                        input_file = Path(v)
                        input_structures_exists = input_file.is_file()
                        if not input_structures_exists:
                            logging.error('Problem with locating the file with input structure, '+input_file.as_posix())
                            raise FileNotFoundError()
                        input_structures_file = input_file.name
                        shutil.copyfile(v, Path(tmpdir)/input_structures_file)
                        ap_command.append(input_structures_file)
                        output_file = Path(tmpdir)/Path(input_file.stem + output_postfix)
                        continue
                    elif k=='-SimHIA_hia' or k=='-SimRIA_hia' or k=='-SimMIA_hia':
                        # HTPK case
                        htpk_calculation = True
                        ap_command.append(k)
                        hia_file_path = Path(v)
                        hia_file_exists = hia_file_path.is_file()
                        if not hia_file_exists:
                            logging.error('Problem with locating the file with hia file, '+hia_file.as_posix())
                            raise FileNotFoundError()
                        hia_file = hia_file_path.name
                        shutil.copyfile(v, Path(tmpdir)/hia_file)
                        ap_command.append(hia_file)
                        continue
                    elif k=='-u':
                        if v.lower()=='sdf':
                            output_postfix = '_ADMET_2D.sdf'
                        elif v.lower()=='rdf':
                            output_postfix = '_ADMET_2D.rtf'
                        else:
                            output_postfix = '.'+v.lower()
                        ap_command.append(k)
                    else:
                        ap_command.append(k)
                    if type(v) is list:
                        if k=="-m": sep=","                                                        
                        ap_command.append(sep.join(v))
                    else:
                        if v != '': ap_command.append(v)
                log_file = Path(tmpdir)/DEFAULT_LOG_FILE_NAME

            # carry out the calculation
            process = subprocess.Popen(ap_command, cwd=tmpdir)
            stdout, stderr = process.communicate(timeout=600)
            
            if output_file.suffix == ".sdf":
                with open(output_file.as_posix(), "rb") as f:
                    suppl = Chem.ForwardSDMolSupplier(f, removeHs=False)
                    mols = list(suppl)
                # turn mols into df
                df_spreadsheet = self._turn_mols_into_df(mols)
            elif output_file.suffix == ".dat" or output_file.suffix == ".smi":
                df_spreadsheet = pd.read_csv(output_file.as_posix(), sep="\t")
            elif output_file.suffix == '' and output_file.name == '_name_':
                # pka imges case
                df_spreadsheet = None
            else:
                logging.error('Unknown output file.')
                raise NotImplementedError
            # parse log file
            if os.path.exists(log_file):
                with open(log_file, 'r') as f:
                    log_content = f.read()
                if self._config["script"] is not None:
                    # TODO: Potential read of the ADMET_Predictor_Errors.log from the AppData space
                    pass
            else:
                log_content = None

            ret_content = {'properties': df_spreadsheet, 'log_content': log_content}

            if htpk_calculation:
                # read in the Cp curves
                file_name = ap_command[-1].split('.')[0]+'_cpt.txt'
                cp_curves_df = pd.read_csv(Path(tmpdir)/file_name, sep='\t', index_col=False)
                ret_content['cp_curves'] = cp_curves_df

            # script-specific parsers
            if self._config["script"] is not None:
                if self._script['processName'] == 'GENERATE_METABOLITES':
                    if self._script['createImages'] == '1':
                        image_suffix = self._script['imageFormat']
                        image_files = [item for item in os.listdir(tmpdir) if item.lower().endswith(image_suffix.lower())]
                        images_dict = {}
                        for image_file in image_files:
                            img = np.array(Image.open(Path(tmpdir)/image_file))
                            images_dict[image_file] = img
                        ret_content['images'] = images_dict
                elif self._script['processName'] == 'PKA_IMAGES':
                    image_suffix = self._script['imageFormat']
                    image_files = [item for item in os.listdir(tmpdir) if item.lower().endswith(image_suffix.lower())]
                    images_dict = {}
                    for image_file in image_files:
                        img = np.array(Image.open(Path(tmpdir)/image_file))
                        images_dict[image_file] = img
                    ret_content['images'] = images_dict
                elif self._script['processName'] == 'GENERATE_3DCOORDINATES':
                    with open(output_file.as_posix(), "rb") as f:
                        suppl = Chem.ForwardSDMolSupplier(f, removeHs=False)
                        mols = list(suppl)
                    ret_content['mols'] = mols

        LOGGER.info("Leaving the pyADMET CMDWrapper execution...")
        return ret_content
    
    @property
    def Script(self):
        return self._script

    @Script.setter
    def Script(self, value):
        self._script = value

