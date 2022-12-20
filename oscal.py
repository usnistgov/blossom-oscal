#%% Install Libraries (You can uncomment below and execute to install.)
# import sys
# !{sys.executable} -m pip install chevron
# !{sys.executable} -m pip install pydantic
# !{sys.executable} -m pip install PyYAML
# !{sys.executable} -m pip install diagrams

# Note: You may need to install this: https://www.graphviz.org/

#%% Import Libraries
import os
import chevron
import json
import datetime
from pathlib import Path
from uuid import UUID,uuid4
from typing import List, Optional
from pydantic import BaseModel,ValidationError,Field
from yaml import safe_load,YAMLError,dump

from oscalic import SystemSecurityPlan as SSP
from oscalic import ControlAssembly as Control
from oscalic import validation


#%% Setup
today = datetime.datetime.now()
today_format = '%Y-%m-%dT00:00:00.0000-04:00'
today = today.strftime(today_format)
control_list = list()

#%% Paths
partial_path = 'system-security-plan/partials'

#%% Read Partials
partials = os.listdir(partial_path)
this_system_component_uuid = uuid4()
ssp_controls=list()

#%% Interpret Partials
print(len(partials))
for partial in partials:
    if partial.startswith('template.'):
        continue

    partial_file = os.path.join(os.getcwd(), partial_path, partial)
    partial_template = Path(partial_file).read_text() #.replace('uuid.','uuid:')
    # print(partial_template)

    uuid_content = {
        'uuid:control':         uuid4(),
        'uuid:statement':       uuid4(),
        'uuid:component-uuid':  this_system_component_uuid, 
        'uuid:by-component':    uuid4(), 
    }

    args = {
        'template': partial_template,
        'data': uuid_content
    }

    partial_content = chevron.render(**args)
    # print(partial_content)
    try:
        partial_yaml = safe_load(partial_content)
        # print(f"PARSED: {partial_file}")
    except YAMLError as e:
        print(f"{partial_file}:\nYAML ERROR: Could not interpret ({e.problem}). Skipping.\n")
    

    try:
        control = Control(**partial_yaml[0])
        ssp_controls.append(control)
        print(f"SUCCESS: {partial_file}")
    except validation.OSCALValidationError as e:
        print(f"{partial_file}:\nVALIDATION ERROR: {e.json()}\n")


#%% Run above here for partial validation.
###################################################################################################
## Prepare Document

# %% Controls in List
len(ssp_controls)
    
# %% Build SSP Document
ssp = SSP(
    uuid=str(uuid4()),
    controls=ssp_controls
)

#%% Print JSON result
# print(json.dumps(json.loads(ssp.json(by_alias=True)), indent=4))

#%% Print YAML result
result = dump(ssp.dict(by_alias=True,exclude_unset=True), sort_keys=False)
print(result)

#%% Save YAML output
Path('SSP.output.yaml').write_text(result)


#%% Make Profile
profile_file = os.path.join(os.getcwd(), partial_path, 'template.profile.yaml')
profile_template = Path(profile_file).read_text()

profile_data = {
    'uuid:document':        uuid4(),
    'uuid:statement':       uuid4(),
    'uuid:component-uuid':  this_system_component_uuid, 
    'uuid:by-component':    uuid4(),
    'version':              '0.0.1',
    'modified_date':        f"{today}"
}

args = {
    'template': profile_template,
    'data': profile_data
}

profile_content = chevron.render(**args)

try:
    partial_yaml = safe_load(profile_content)
except YAMLError as e:
    print(f"{partial_file}:\nYAML ERROR: Could not interpret ({e.problem}). Skipping.\n")

partial_yaml


#%% Make SSP
ssp_file = os.path.join(os.getcwd(), partial_path, 'template.ssp.yaml')
ssp_template = Path(ssp_file).read_text()

ssp_data = {
    'uuid:document':         uuid4(),
    'uuid:statement':       uuid4(),
    'uuid:component-uuid':  this_system_component_uuid, 
    'uuid:by-component':    uuid4(), 
    'version':              '0.0.1'
}

args = {
    'template': ssp_template,
    'data': ssp_data
}

ssp_content = chevron.render(**args)

ssp_content

# %%
