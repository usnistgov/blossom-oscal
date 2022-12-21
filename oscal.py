#%% Install Libraries (You can uncomment below and execute to install.)
# import sys
# !{sys.executable} -m pip install chevron
# !{sys.executable} -m pip install pydantic
# !{sys.executable} -m pip install PyYAML
# !{sys.executable} -m pip install diagrams

# Note: You may need to install this: https://www.graphviz.org/

#%% Import Libraries
import os, sys
import chevron
import json
import datetime
from pathlib import Path
from yaml import safe_load,YAMLError,dump

from oscalic.system_security_plan import SystemSecurityPlan as SSP
from oscalic.control import ControlAssembly as Control
from oscalic import Template, Helper, Validation

error_condition = None

#%% Setup
today = datetime.datetime.now()
today_format = '%Y-%m-%dT00:00:00.0000-04:00'
today = today.strftime(today_format)
control_list = list()

#%% Paths
partial_path = 'system-security-plan/partials'

#%% Read Partials
partials = os.listdir(partial_path)
this_system_component_uuid = Helper.get_uuid()
ssp_controls=list()
print(len(partials))

#%% Start SSP
ssp_template = os.path.join(os.getcwd(), partial_path, 'template.ssp.yaml')
ssp_data = {
    'uuid:document':        Helper.get_uuid(),
    'uuid:statement':       Helper.get_uuid(),
    'uuid:component':       this_system_component_uuid, 
    'uuid:user':            Helper.get_uuid(),
    'uuid:party':           Helper.get_uuid(), 
    'uuid:by-component':    Helper.get_uuid(), 
    'version':              '0.0.1',
    'modified_date':        f"{today}",
}
ssp_content = Template.apply(ssp_template, ssp_data)
ssp = Helper.from_yaml(SSP, ssp_content)

#%% Start Profile
profile_template = os.path.join(os.getcwd(), partial_path, 'template.profile.yaml')
profile_data = {
    'uuid:document':        Helper.get_uuid(),
    'uuid:statement':       Helper.get_uuid(),
    'uuid:component-uuid':  this_system_component_uuid, 
    'uuid:by-component':    Helper.get_uuid(),
    'version':              '0.0.1',
    'modified_date':        f"{today}"
}


#%% Interpret Partials
for partial in partials:
    if partial.startswith('template.'):
        continue

    partial_file = os.path.join(os.getcwd(), partial_path, partial)

    uuid_content = {
        'uuid:control':         Helper.get_uuid(),
        'uuid:statement':       Helper.get_uuid(),
        'uuid:component-uuid':  this_system_component_uuid, 
        'uuid:by-component':    Helper.get_uuid(), 
    }

    partial_content = Template.apply(partial_file, uuid_content)

    try:
        control = Helper.from_yaml(Control, partial_content)
        ssp.system_security_plan.control_implementation.implemented_requirements.append(control)
        print(f"SUCCESS: {partial_file}")
    except Validation.OSCALValidationError as e:
        print(f"{partial_file}:\nVALIDATION ERROR: {e.json()}\n")
        error_condition = 1


#%% Run above here for partial validation.
###################################################################################################
## Prepare Document

#%% Save Profile
profile_content = Template.apply(profile_template, profile_data)
Path('Profile.output.yaml').write_text(profile_content)

#%% Save SSP
Path('SSP.output.yaml').write_text(Helper.to_yaml(ssp))

#%%
# try:
# ssp = SSP.from_yaml(partial_content)
#     ssp_controls.append(control)
#     print(f"SUCCESS: {partial_file}")
#     print(control.to_yaml())
# except Validation.OSCALValidationError as e:
#     print(f"{partial_file}:\nVALIDATION ERROR: {e.json()}\n")

# Path('SSP.output.yaml').write_text(result)

# %%
if error_condition:
    exit(error_condition)

#%%