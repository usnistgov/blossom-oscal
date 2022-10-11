# BloSS@M OSCAL Editing Tools

## Purpose

This document references the discussion that took place [here](https://github.com/usnistgov/blossom/issues/80).

Bloss@M's goals include thorough security documentation, which requires that all developers can author and edit OSCAL artifacts in a way that is compatible with BloSS@M's development process.

## Requirements

The tool we use must meet a few criteria in order for it to fit within BloSS@M's vision for "shifting left" into the development process.

- **Portability**: The tool must be easy to install, allowing for developers to edit artifacts without significant lift or server resources. If the tool is too complex for any developer to install, it would potentially deter them from using it.
- **Git Integration**: The tool must produce artifacts that live in the `git` repository's source tree, or at the very least can be easily be exported to a `git` repository. The rationale is for approval to take place using the same mechanism that is used to approve commits, and for the code to evolve in lock-step with the documentation.
- **Automation Friendly**: The tool should, to the greatest extent possible, allow automated execution for core functionality or key functions for important use cases. Key use cases may include automate validation, checking of content, conversion of data between formats, and act as a pipeline step with simple to use inputs and outputs to integrate with other tools in our CI/CD platform, like GitHub Actions.
- **Compatibility**: The tool supports OSCAL features that are crucial to the documentation of the BloSS@M project.
- **Flexibility**: The core OSCAL models are stable, but this project will likely pilot the use of features to OSCAL that are not yet stable at this time. A key focus of the BloSS@M pilot is automated testing as part of automated security assessment. Features of OSCAL that support focus are not yet stable, like [Rules](https://github.com/usnistgov/OSCAL/issues/1058) and [Checks](https://github.com/usnistgov/OSCAL/issues/1059). Many software packages will write complex, nested code directly targeting a specific stable release of OSCAL. Reconfiguring such code to use the version of OSCAL specified in trunk development or feature branch is often onerous or impossible.
- **Ease of Use**: The tool must simplify the editing process beyond editing the OSCAL artifacts by hand.

### OSCAL Use Cases

When using OSCAL-enabled tools for this project, the BloSS@M Team will need the tool to support key use cases and scenarios.

1. A tool must be able to peform profile resolution with valid, well-formed OSCAL catalogs.
1. A tool must be able to resolve profiles with the FedRAMP catalog and its custom fields.
1. A tool must be able to define 800-60 information types, set FIPS-199 categorization data, and set the overall low/moderate/high risk level for a system in the SSP before documenting implemented controls. (NOTE: this is presumed for conventional use cases of tailoring and applying a custom OSCAL profile, but most tools do not implement this natively.)
1. A tool must be able to edit SSP "front matter" (`metadata`, `system-characterisitcs`, `system-implementation`), not only the `statement`s of `implemented-requirement`s in `control-implementation` structures.
1. A tool must be able to manage components within an OSCAL SSP.
1. A tool should be able to manage components in `component-definition`s, and then subsequently import a local version into an OSCAL SSP.
1. A tool must be able to edit or maintain a leveraged authorization relationship between a leveraged system (e.g. AWS services) and the leveraging system (this information system, the BloSS@M service).
1. A tool must be able to properly create an OSCAL system security plan with custom FedRAMP extension fields.
1. A tool must be able to validate a custom OSCAL catalog, profile, system security plan, assessment plan, and assessment result, with or without custom FedRAMP extension data.
1. If the tool uses a database to store normalized security data, it must be able to import and export all OSCAL content programmatically, with a simple command or HTTP request, that validates against the official OSCAL schemas.
1. The tool should support saving files in a routinely consistent state to limit noisy change reporting with `git diff`. (NOTE: XML standards define the order of elements is important, but JSON and YAML do not. The OSCAL standard, for JSON and YAML, do not require strict element ordering so some tools can significantly reorder and restructure documents even for minor text changes as conversion and/or automation processes are performed.)
1. A tool must not inhibit the use of specific targeted versions of stable, alpha, or beta releases of OSCAL functionality, specifically around the OSCAL Rules construct as explained above.

## Tools

Below are the tools that were selected as possible candidates.

### Compliance Trestle

Project homepage: https://github.com/IBM/compliance-trestle

IBM's Trestle provides a markdown-based editing workflow, where documentation can be transformed from specifically formatted markdown documents into well-formed OSCAL JSON or XML output.

The ease of use and tight integration with Git makes this tool initially very attractive.

### ATO Blueprint

Project homepage: https://github.com/CMSgov/ato-blueprint

ATO Blueprint is a fork of GovReady-Q, a very user friendly web-based compliance documentation and assessment system that can ingest and export to OSCAL. The project is very simple to deploy and it provides a lot of nice features.

### OPAL

Project homepage: https://github.com/EOP-OMB/opal

OMB's OPAL is a simple Django-based web application that provides the ability to produce and edit SSPs in OSCAL.

### OSCAL-gen-tool

Project homepage: https://github.com/GSA/oscal-gen-tool

GSA's OSCAL-gen-tool is an ASP.NET web application that provides the ability to produce OSCAL SSP, SAP and SAR documents.

### EasyDynamics' OSCAL Editor

Project homepage: https://github.com/EasyDynamics/oscal-editor-deployment

EasyDyamics' OSCAL Editor is a simple web-based tool built on top of their [OSCAL React library](https://github.com/EasyDynamics/oscal-react-library) and [OCSCAL Rest Service](https://github.com/EasyDynamics/oscal-rest-service), allowing users to edit OSCAL artifacts in the browser. The tool is easy to use and can load OSCAL artifacts directly off of a disk, or via a URL, allowing for use in the context of editing or reviewing changes.

## Conclusion

Given the requirements and the matrix of supported use cases, we recommend the BloSS@M Team edit OSCAL JSON documents manually, store them in a `git` repository, and use the EasyDynamics OSCAL Editor for visual feedback during edits or for presentation to stakeholders outside the BloSS@M Team. Many of the tools have incomplete functionality or lack the flexibility needed for this pilot.

Below is a table summarizes how we grade each tool given our requirements after evaluating the tool around specific aforementioned use cases.

| Tool               | Portability | Git Integration | Automation Friendly | Compatibility | Flexibility | Ease of Use |
| ------------------ | ----------- | --------------- | ------------------- | ------------- | ----------- | ----------- |
| Compliance Trestle | ✔           | ✔               | ✔                   | ❌            | ✔           | ✔           |
| ATO Blueprint      | ⚠           | ❌              | ❌                  | ❌            | ❌          | ✔           |
| OPAL               | ⚠           | ❌              | ❌                  | ✔             | ❌          | ⚠           |
| OSCAL-gen-tool     | ❌          | ❌              | ❌                  | ✔             | ❌          | ⚠           |
| EasyDynamics OSCAL | ✔           | ✔               | ✔                   | ✔             | ❌          | ⚠           |
