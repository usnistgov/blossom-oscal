# Event Dossier: Amazon Security Hub Finding

### Amazon Security Hub Compliance Analyzer Result to OSCAL
- **Description**: Translates Amazon Security Hub Compliance Analyzer Result to OSCAL System Security Plan (SSP) Schema.
- **Event References**:
    - [NIST OSCAL Site](https://pages.nist.gov/OSCAL/)
    - [OSCAL System Security Plan JSON Schema](https://pages.nist.gov/OSCAL-Reference/models/v1.1.2/system-security-plan/json-reference/)
    - [OSCAL GitHub Repository](https://github.com/usnistgov/OSCAL)

# Transforming Compliance Control Information to OSCAL System Security Plan (SSP) Schema

This document provides a detailed mapping and example for transforming compliance finding information into the OSCAL System Security Plan (SSP) model.

## OSCAL Version: 1.1.2

- **Document Metadata:**
  - `metadata.version`: `1.1.2`
  - `metadata.title`: `Compliance Findings`
  - `metadata.last-modified`: `{{current_date}}`
  - `metadata.oscal-version`: `1.1.2`

## Mapping CSV Fields to OSCAL SSP Schema

The following table outlines the mapping from the CSV fields to the corresponding OSCAL SSP fields:

| CSV Field                  | OSCAL SSP Field                                                                |
|----------------------------|--------------------------------------------------------------------------------|
| `compliance_control_id`    | `control-implementation.implemented-requirements[].control-id`                 |
| `compliance_status`        | `system-implementation.users[].description`                                    |
| `percentage`               | `control-implementation.implemented-requirements[].remarks`                    |
| `rule_id`                  | `control-implementation.implemented-requirements[].statements[*].description`  |
| `lastobservedat`           | `metadata.last-modified`                                                       |
| `narrative`                | `control-implementation.implemented-requirements[].description`                |

## Additional Required Data

The following data is required for the OSCAL SSP but cannot be derived directly from the CSV:

- **UUIDs**: Unique identifiers for various elements (e.g., system, users, components, statements). These must be generated or provided manually.
- **Import Profile**: The `import-profile.href` must be provided.
- **System Information**: Descriptions, titles, and sensitivity levels need to be appropriately detailed.
- **Authorization Boundary**: A description of the authorization boundary must be provided.
- **Component Details**: Components should include type, title, description, and status.

### Table of Data Needed but Not Included in Source CSV

The following table outlines additional data required for the OSCAL SSP that is not included in the source CSV:

| Data Field                     | Description                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------|
| `system-name`                 | The name of the system being documented.                                            |
| `system-characteristics.description` | A detailed description of the system.                                          |
| `security-sensitivity-level`  | The sensitivity level of the system (e.g., low, moderate, high).                     |
| `import-profile.href`         | The URL or reference to the import profile.                                          |
| `authorization-boundary.description` | A description of the system's authorization boundary.                        |
| `components[].uuid`           | A unique identifier for each system component.                                       |
| `components[].type`           | The type of each system component (e.g., software, hardware).                        |
| `components[].title`          | The title or name of each system component.                                          |
| `components[].description`    | A detailed description of each system component.                                     |
| `components[].status.state`   | The operational status of each system component (e.g., operational, under-development).|

## Fields in Raw CSV Data Not Used in Transformation

The following fields from the raw CSV data are not used in the OSCAL SSP schema transformation:

None

## Mapping of Raw CSV Data to Transformed OSCAL SSP Data

### Used Fields from Raw CSV Data
- **compliance_control_id** → `control-implementation.implemented-requirements[].control-id`
- **compliance_status** → `system-implementation.users[].description`
- **percentage** → `control-implementation.implemented-requirements[].remarks`
- **rule_id** → `control-implementation.implemented-requirements[].statements[*].description`
- **lastobservedat** → `metadata.last-modified`
- **narrative** → `control-implementation.implemented-requirements[].description`

### Additional Required Data Not Available in Raw CSV Data
- **metadata.version**: "1.0.0" (Static value provided)
- **metadata.oscal-version**: "1.1.2" (Static value provided)
- **import-profile.href**: "profile-uuid" (Static value provided, needs to be supplied manually)
- **system-characteristics.system-name**: "AWS" (Static value provided)
- **system-characteristics.description**: "Mission Owner Environment" (Static value provided)
- **system-characteristics.security-sensitivity-level**: "moderate" (Static value provided)
- **system-characteristics.system-ids**: "111111111111" (Static value provided)
- **system-characteristics.status.state**: "operational" (Static value provided)
- **system-characteristics.authorization-boundary.description**: "Authorization boundary description" (Static value provided)
- **system-implementation.users[].uuid**: "123e4567-e89b-42d3-a456-426614174000" (Static value provided)
- **system-implementation.users[].title**: "AC-17(2)" (Static value provided)
- **system-implementation.components[].uuid**: "123e4567-e89b-42d3-a456-426614174000" (Static value provided)
- **system-implementation.components[].type**: "software" (Static value provided)
- **system-implementation.components[].title**: "System Component" (Static value provided)
- **system-implementation.components[].description**: "An inventory item" (Static value provided)
- **system-implementation.components[].status.state**: "operational" (Static value provided)
- **control-implementation.implemented-requirements[].statements[*].uuid**: "123e4567-e89b-42d3-a456-426614174000" (Static value provided)
- **control-implementation.implemented-requirements[].statements[*].statement-id**: "statement-1" (Static value provided)

"""