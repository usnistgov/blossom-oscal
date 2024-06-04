# Event Dossier: Amazon Security Hub Finding
### Amazon Security Hub Cloud Security Posture Management (CSPM) finding in ASFF format
- **Description**: Translates Amazon Security Hub CSPM finding in ASFF format to OSCAL.
- **Event References**:
    - [NIST OSCAL Site](https://pages.nist.gov/OSCAL/)
    - [OSCAL Assessment Results JSON Schema](https://pages.nist.gov/OSCAL-Reference/models/v1.1.2/assessment-results/json-reference/)
    - [OSCAL GitHub Repository](https://github.com/usnistgov/OSCAL)


# Transforming Compliance Findings from Security Hub in ASFF to OSCAL Assessment Results Schema

This document provides a detailed mapping and example for transforming compliance finding information into the OSCAL Assessment Results model.

## OSCAL Version: 1.1.2

- **Document Metadata:**
  - `metadata.version`: `1.1.2`
  - `metadata.title`: `Compliance Findings`
  - `metadata.last-modified`: `{{current_date}}`
  - `metadata.oscal-version`: `1.1.2`

## Mapping Raw Security Hub Fields to OSCAL Assessment Results Schema

The following table outlines the mapping from the raw Security Hub fields to the corresponding OSCAL Assessment Results fields:

| Raw Security Hub Field                 | OSCAL Assessment Results Field                                                                |
|----------------------------------------|-----------------------------------------------------------------------------------------------|
| `Id`                                   | `assessment-results.uuid`                                                                     |
| `Region`                               | `assessment-results.results[].props[]`                                                        |
| `AwsAccountId`                         | `assessment-results.results[].props[]`                                                        |
| `FirstObservedAt`                      | `assessment-results.results[].observations[].collected`                                       |
| `LastObservedAt`                       | `assessment-results.results[].observations[].props[]`                                         |
| `Title`                                | `assessment-results.results[].title`                                                          |
| `Description`                          | `assessment-results.results[].description`                                                    |
| `Severity.Label`                       | `assessment-results.results[].props[]`                                                        |
| `Remediation.Recommendation.Url`       | `assessment-results.results[].links[]`                                                        |
| `Compliance.Status`                    | `assessment-results.results[].reviewed-controls[].control-selections[].description`           |
| `Compliance.RelatedRequirements`       | `assessment-results.results[].reviewed-controls[].control-selections[].description`           |
| `Compliance.SecurityControlId`         | `assessment-results.results[].reviewed-controls[].control-selections[].include-controls[]`    |

## Additional Required Data

The following data is required for the OSCAL Assessment Results but cannot be derived directly from the raw Security Hub data:

- **UUIDs**: Unique identifiers for various elements (e.g., system, users, components, statements). These must be generated or provided manually.
- **Import Profile**: The `import-profile.href` must be provided.
- **System Information**: Descriptions, titles, and sensitivity levels need to be appropriately detailed.
- **Authorization Boundary**: A description of the authorization boundary must be provided.
- **Component Details**: Components should include type, title, description, and status.

### Table of Data Needed but Not Included in Raw Security Hub Data

The following table outlines additional data required for the OSCAL Assessment Results that is not included in the raw Security Hub data:

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

## Fields in Raw Data Not Used in Transformation

The following fields from the raw Security Hub data are not used in the OSCAL Assessment Results schema transformation:

- `SchemaVersion`
- `ProductArn`
- `ProductName`
- `CompanyName`
- `GeneratorId`
- `Types`
- `CreatedAt`
- `UpdatedAt`
- `Severity.Normalized`
- `Severity.Original`
- `Remediation.Recommendation.Text`
- `ProductFields`
- `Resources`
- `Compliance.AssociatedStandards`
- `WorkflowState`
- `Workflow.Status`
- `RecordState`
- `FindingProviderFields`
- `ProcessedAt`
