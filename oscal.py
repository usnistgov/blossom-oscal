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
from oscal_helpers import oscalize,deoscalize
from pathlib import Path
from uuid import UUID,uuid4
from typing import List, Optional
from pydantic import BaseModel,ValidationError,Field
from yaml import safe_load,YAMLError,dump

#%% Paths
partial_path = 'system-security-plan/partials'

#%% Set Up OSCAL Model for SSP Controls
class SetParameter(BaseModel):
    param_id: str = Field(alias='param-id')
    values: List[str] = []

class ByComponent(BaseModel):
    uuid: str | UUID
    component_uuid: str | UUID = Field(alias='component-uuid')
    description: str

class Statement(BaseModel):
    uuid: str | UUID
    statement_id: str = Field(alias='statement-id')
    by_components: List[ByComponent] = Field(default=None, alias='by-components')

class Control(BaseModel):
    uuid: str | UUID
    control_id: str = Field(alias='control-id')
    set_parameters: List[SetParameter] = Field(default=None, alias='set-parameters')
    statements: List[Statement] | None
    by_components: List[ByComponent] = Field(default=None, alias='by-components')

# I know this is not valid.
class SSP(BaseModel):
    uuid: str | UUID
    controls: List[Control] | None


#%% Read Partials
partials = os.listdir(partial_path)
this_system_component_uuid = uuid4()
ssp_controls=list()

#%% Interpret Partials
print(len(partials))
for partial in partials:
    if partial.endswith('template.yaml'):
        continue

    partial_file = os.path.join(os.getcwd(), partial_path, partial)
    partial_template = Path(partial_file).read_text().replace('uuid.','uuid:')
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
    except ValidationError as e:
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


# %%

# %%
