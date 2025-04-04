
import json

from time import time
from copy import deepcopy

from ratio1 import Logger, const
from ratio1.bc import DefaultBlockEngine
from uuid import uuid4



if __name__ == '__main__' :
  l = Logger("ENC", base_folder='.', app_folder='_local_cache')
  eng = DefaultBlockEngine(
    log=l, name="default", 
    config={
        # "PEM_FILE": "aid01.pem",
      }
  )
  
  _time = time()  #- 25 * 3600
  
  hex_time = hex(int(_time * 1000))
  app_name = "some_app_name"
  app_id = "app_40b23285"
  
  NODES = [
    "0x4bc05c6d0856ea0F437C640B77415e8fCaB09Bd0",    
    "0x4Bb528D985f11e2530ADb3eaB22F4c5AA028Fe13"
  ]
  
  CREATE_REQUEST = {
    "app_alias" : app_name,
    "plugin_signature" : "A_SIMPLE_PLUGIN",
    "nonce" : hex_time, # recoverable via int(nonce, 16)
    "target_nodes" : NODES,
    "target_nodes_count" : 0,
    "app_params" : {
      "IMAGE" : "repo/image:tag",
      "CR" : "docker.io",
      "CR_USERNAME" : "user",
      "CR_PASSWORD" : "password",
      "CONTAINER_RESOURCES" : {
        "cpu" : 1,
        "memory" : 2,
        "gpu" : 0,
      },      
      "PORT" : 5000,
      "OTHER_PARAM1" : "value1",
      "OTHER_PARAM2" : "value2",
      "OTHER_PARAM3" : "value3",
      "OTHER_PARAM4" : "value4",
      "OTHER_PARAM5" : "value5",
      "ENV" : {
        "ENV1" : "value1",
        "ENV2" : "value2",
        "ENV3" : "value3",
        "ENV4" : "value4",
      }
    },
    "pipeline_input_type"  : "ExampleDatastream",
    "pipeline_input_uri" : None,       
  }
  
  GET_APPS_REQUEST = {
    "nonce" : hex_time, # recoverable via int(nonce, 16)    
  }
  
  DELETE_REQUEST = {
    "app_id" : app_id,
    "target_nodes" : NODES,
    "nonce" : hex_time, # recoverable via int(nonce, 16)    
  }  
  
  
  create_request = deepcopy(CREATE_REQUEST)
  get_apps_request = deepcopy(GET_APPS_REQUEST)
  delete_request = deepcopy(DELETE_REQUEST)

  l.P(f"CREATE_REQUEST:\n{json.dumps(create_request, indent=2)}")
  l.P(f"GET_APPS_REQUEST:\n{json.dumps(get_apps_request, indent=2)}")
  l.P(f"DELETE_REQUEST:\n{json.dumps(delete_request, indent=2)}")