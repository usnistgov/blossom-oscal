# System Requirements for BloSS@M

## Mission

NIST ITL CSD [Secure Systems and Applications (SSA) Group](https://csrc.nist.gov/Groups/Computer-Security-Division/Secure-Systems-and-Applications)’s security research focuses on identifying emerging and high-priority technologies, and on developing security solutions that will have a high impact on the U.S. critical information infrastructure. The group conducts novel research and develops cutting-edge technology on behalf of government and industry, aiming to demonstrate, through proofs-of-concept, reference and prototype implementations, and demonstrations, secure, best practices starting with the earliest stages of technology development. SSA works to transfer new technologies to industry, produce new standards and guidance for federal agencies and industry, and develop tests, test methodologies, and assurance methods.

As part of this mission, the SSA Group is evaluating a next-generation approach to software asset management as an alternative to [the GSA Software License Management Service (SLMS)](https://www.gsa.gov/cdnstatic/Software%20License%20Management%20Service.pdf).

## Business Functions

The business unit that will design, implement, and operate this next-generation software asset management solution will emulate that of the GSA OCIO's SLMS business unit. These four business functions are centered on four key objectives, known as "The Four C's":

1. **Customization** for software asset management needs of different organizations
1. **Cutting costs** for the acquisition and maintenance of software
1. **Complying** with the relevant mandates for that software
1. Enhancing **Cybersecurity** posture around the use of said software

To that end, the solution developed and operated by the BloSS@M Team will, in a production scenario, realize the following business functions.

1. Usage analysis for software in a given agency
1. License optimization for proprietary licensed software
1. Maintenance analysis for that software
1. Cyber-threat detection
1. Audit prevention for software license usage
1. Standardized data collection and reporting on the above

## Business Processes

The BloSS@M Team, in a production scenario, would realize and augment business processes similar to that of the GSA OCIO SLMS Team. In particular, the development and operation focuses on the first three business functions exclusively: Program Management Activities, Inventory Collection, and Contracts (particularly around audit defense and compliance). These business processes are itemized below, grouped by category.

- Program Management Activities
  - Phase 1 Gap Analysis
  - Phase 2 Customized Engagement with Agency Customers
  - Phase 3 Asset Management Toolset and IT Assessment Program Management
- Inventory Collection
  - Baseline Inventory Analysis
  - Toolset Evaluation
  - Analysis of Alternative Software Solutions
- Contracts
  - Audit Defense and Compliance
  - Audit Resolution
  - ELA Review
  - T&C Development
  - Pricing analysis
- Vendor Negotiation
  - Market Analysis
  - Negotiation Execution
- Strategy
  - Cloud Roadmap Development
  - Data Center Consolidation Advisory Services
  - Vendor Management Strategy
- IT Acquisition
  - EBC Development
  - MGT Act Budgets Requests
  - Development of Acquisition Package Components
  - Spend Analysis, Strategic Sourcing, Supplier Management, Procurement and Financial Management

## Information System Stakeholders

The stakeholders that will interact with this BLOSSOM system are:

1. Acquisition officers of customer agencies
1. Commercial software vendors selling software to customer agencies
1. Business owners for customer agencies' IT asset management function
1. Agency information security officials and mission-specific security officials for the asset management function in custom agencies
1. Chief Information Officers of customer agencies
1. BloSS@M development, operations, and cybersecurity staff that will operate this environment in a production scenario

NOTE: Although not all these stakeholders represent active users of the system, they are part of the application, design, implementation, and maintenance lifecycle of the the system.

## Information System Assets

The BloSS@M Team has outlined the following as key information assets for the system.

1. Authentication and authorization principles for system users
1. Software licenses
1. Software usage and license metadata
1. Authority-to-Operate (ATO) metadata (e.g. ATO status, date of ATO approval, date of ATO expiration)
1. Supply-chain risk scores for one or more software packages

Detailed analysis of sub-assets as implemented can be reviewed by looking at [the project's actively maintained threat model](../threat_model/index.md).

## Information System Types

Below are [the 800-60 Volume 2 Revision 1 information types](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-60v2r1.pdf) selected for this information system.

The provisional FIPS-199 impact levels for confidentiality, integrity, and impact levels are Moderate, Moderate, and Moderate, respectively.

The overall provisional impact level and security categorization are FIPS-199 Moderate.

| Information Type ID | Information Type | Confidentiality Impact | Integrity Impact | Availability Impact | Public Value? | Custom NIST Value? | Notes |
|---------------------|------------------|------------------------|------------------|---------------------|---------------|-------------------|-------|
| C.2.8.9 | Personal identity and authentication information | M | L | M | | X | Data is limited to federal employees and is for identification of these federal employees only. |
| C.3.4.2 | Inventory control | L | L | L | X | | |
| C.3.4.3 | Logistics management | L | L | L | X | | |
| C.3.4.4 | Services acquisition | L | L | L | X | | |
| C.3.5.2 | Lifecycle / change management | L | M | L | X | | |
| C.3.5.5 | Information security | L | M | L | X | | |
| C.3.5.6 | Record retention | L | L | L | X | | |
| C.3.5.7 | Information management | L | M | L | X | | |
| C.3.5.9 | Information sharing | M | M | M | | X | Since Information Sharing, as a function, is receiving and disseminating data [other information types] from business areas already identified, this BRM information type will not require its own impact assessment. Therefore, agency personnel should identify the information sharing information type as a pure resource management support activity for the evaluated information system. |
| D.19.1 | Scientific and technological research and innovation | L | M | L | | X | |
| D.20.1 | Research and development | L | M | M | X | | |
| D.20.4 | Knowledge dissemination | L | L | L | X | | |

<details>
<summary>Detailed Breakdown of SP 800-60 Volume 2 Revision 1 Types</summary>

- C.2: Services delivery support functions provide the critical policy, programmatic, and managerial foundation to support Federal government operations. Security objectives and impact levels for service delivery support information and systems are generally determined by the natures of the supported direct services and constituencies being supported. If a system stores, processes, or communicates national security information, it is defined as a national security system, and is outside the scope of this guideline. Service delivery support activities are defined in this section.
  - [ ] C.2.1: Controls and oversight: Controls and Oversight information is used to ensure that the operations and programs of the Federal government and its external business partners comply with applicable laws and regulations and prevent waste, fraud, and abuse.
    - [ ] C.2.1.1: Corrective action
    - [ ] C.2.1.2: Program evaluation
    - [ ] C.2.1.3: Program monitoring
  - [ ] C.2.2: Regulatory development: Regulatory Development involves activities associated with providing input to the lawmaking process in developing regulations, policies, and guidance to implement laws.
    - [ ] C.2.2.1: Policy and guidance development
    - [ ] C.2.2.2: Public comment tracking
    - [ ] C.2.2.3: Regulatory creation
    - [ ] C.2.2.4: Rule publication
  - [ ] C.2.3: Planning and budgeting: Planning and Budgeting involves the activities of determining strategic direction, identifying and establishing programs and processes to enable change, and allocating resources (capital and labor) among those programs and processes.
    - [ ] C.2.3.1: Budget formulation
    - [ ] C.2.3.2: Capital planning
    - [ ] C.2.3.3: Enterprise architecture
    - [ ] C.2.3.4: Strategic planning
    - [ ] C.2.3.5: Budget execution
    - [ ] C.2.3.6: Workforce planning
    - [ ] C.2.3.7: Management improvement
    - [ ] C.2.3.8: Budget and performance integration
    - [ ] C.2.3.9: Tax and fiscal policy
  - [ ] C.2.4: Internal risk management and mitigation: Internal risk management and mitigation involves all activities relating to the processes of analyzing exposure to risk and determining appropriate counter-measures. Note that risks to information and information systems associated with internal risk management and mitigation activities may inherently affect the resistance to compromise/damage and recovery from damage with respect to a broad range of critical infrastructures and key national assets.
    - [ ] C.2.4.1: Contingency planning
    - [ ] C.2.4.2: Continuity of operations
    - [ ] C.2.4.3: Service recovery
  - [ ] C.2.5: Revenue collection: Revenue Collection includes the collection of Government income from all sources. Note: Tax collection is accounted for under the Taxation Management information type in the General Government mission area.
    - [ ] C.2.5.1: Debt collection
    - [ ] C.2.5.2: User fee collection
    - [ ] C.2.5.3: Federal asset sales
  - [ ] C.2.6: Public affairs: Public Affairs activities involve the exchange of information and communication between the Federal Government, citizens and stakeholders in direct support of citizen services, public policy, and/or national interest.
    - [ ] C.2.6.1: Customer services
    - [ ] C.2.6.2: Official information dissemination
    - [ ] C.2.6.3: Product outreach
    - [ ] C.2.6.4: Public relations
  - [ ] C.2.7: Legislative relations: Legislative Relations involves activities aimed at the development, tracking, and amendment of public laws through the legislative branch of the Federal Government.
    - [ ] C.2.7.1: Legislation tracking
    - [ ] C.2.7.2: Legislation testimony
    - [ ] C.2.7.3: Proposal development
    - [ ] C.2.7.4: Congressional liaison operations
  - C.2.8: General government: General Government involves the overhead costs of the Federal Government, including legislative and executive activities; provision of central fiscal, personnel, and property activities; and the provision of services that cannot reasonably be classified in any other service support area. As a normal rule, all activities reasonably or closely associated with other service support areas or information types shall be included in those service support areas or information types rather than listed as a part of general government. This service support area is reserved for central government management operations; most service delivery (mission-based) management activities would not be included here. Unlike the other service support functions, some general government information types are associated with specific organizations (e.g., Department of the Treasury, Executive Office of the President, Internal Revenue Service).
    - [ ] C.2.8.1: Central fiscal operations
    - [ ] C.2.8.2: Legislative functions
    - [ ] C.2.8.3: Executive functions
    - [ ] C.2.8.4: Central property management
    - [ ] C.2.8.5: Central personnel management
    - [ ] C.2.8.6: Taxation management
    - [ ] C.2.8.7: Central records and statistics management
    - [ ] C.2.8.8: Income information
    - C.2.8.9: Personal identity and authentication information
    - [ ] C.2.8.10: Entitlement event information
    - [ ] C.2.8.11: Representative payee information
    - [ ] C.2.8.12: General information
- C.3: Government resource management: Resource management functions are the back office support activities that enable the government to operate effectively. Security objectives and impacts for resource management functions are determined by the direct service missions and constituencies ultimately being supported. It is likely that all Federal government information systems store, process, and operate under the control of IT infrastructure maintenance information (e.g., password files and file and network access settings). A basic set of security controls will apply to this information and processes to combat potential corruption, misuse, or abuse of system information and processes.
  - [ ] C.3.1: Administrative management: Administrative Management involves the day-to-day management and maintenance of the internal infrastructure. Administrative information is usually routine and is relatively low impact. However, some administrative management information is either very sensitive (e.g., logistics management for nuclear or other hazardous materials, security management information, and security clearance management information) or critical (e.g., inventory control and logistics management information needed to support time-critical operations). National security information is outside the scope of this guideline. [See Appendix A, Glossary of Terms, for a definition of national security information/systems.] Routine administrative management information systems that do not process classified information are not usually designated national security systems, even if they are critical to the direct fulfillment of military or intelligence missions.
    - [ ] C.3.1.1: Facilities, fleet, and equipment management
    - [ ] C.3.1.2: Help desk services
    - [ ] C.3.1.3: Security management
    - [ ] C.3.1.4: Travel
    - [ ] C.3.1.5: Workplace policy development and management
  - [ ] C.3.2: Financial management: Financial management involves the aggregate set of accounting practices and procedures that allow for the accurate and effective handling of all government revenues, funding, and expenditures. Confidentiality impacts associated with financial management information are generally associated with the sensitivity of the existence of specific projects, programs, and/or technologies that might be revealed by unauthorized disclosure of information. For integrity, temporary successful frauds can affect agency image, and corrective actions are often disruptive to agency operations. Permanent loss/unavailability of financial management information can cripple agency operations.
    - [ ] C.3.2.1: Assets and liability management
    - [ ] C.3.2.2: Reporting and information
    - [ ] C.3.2.3: Funds control
    - [ ] C.3.2.4: Accounting
    - [ ] C.3.2.5: Payments
    - [ ] C.3.2.6: Collections and receivables
    - [ ] C.3.2.7: Cost accounting / performance measurement
  - [ ] C.3.3: Human resource management: Human resource management activities involve all activities associated with the recruitment and management of personnel.
  - [ ] C.3.3.1: HR strategy
    - [ ] C.3.3.2: Staff acquisition
    - [ ] C.3.3.3: Organization and position management
    - [ ] C.3.3.4: Compensation management
    - [ ] C.3.3.5: Benefits management
    - [ ] C.3.3.6: Employee performance management
    - [ ] C.3.3.7: Employee relations
    - [ ] C.3.3.8: Labor relations
    - [ ] C.3.3.9: Separation management
    - [ ] C.3.3.10: Human resources development
  - C.3.4: Supply chain management: Supply chain management involves the purchasing, tracking, and overall management of goods and services.
    - [ ] C.3.4.1: Goods acquisition
    - C.3.4.2: Inventory control
    - C.3.4.3: Logistics management
    - C.3.4.4: Services acquisition
  - [ ] C.3.5: Information and technology management: IT management involves the coordination of IT resources and systems required to support or enable a citizen service. Impacts to information associated with the operation of IT systems generally need to be considered even when all mission-related information processed by the system is intended to be available to the general public. The relevant issues may be different for integrity and availability than for confidentiality. Information that has been made public, by definition, requires no confidentiality protection. In contrast, integrity and availability protection cannot be maintained for copies of information that have been distributed to the public. Integrity and availability assurance can only be maintained by maintaining copies of information in organization-controlled information systems.
    - [ ] C.3.5.1: System development
    - C.3.5.2: Lifecycle / change management
    - [ ] C.3.5.3: System maintenance
    - [ ] C.3.5.4: IT infrastructure maintenance
    - C.3.5.5: Information security
    - C.3.5.6: Record retention
    - C.3.5.7: Information management
    - [ ] C.3.5.8: System and network monitoring
    - C.3.5.9: Information sharing
- [ ] D: Mission-based: In general, individual agencies should identify the mission information types processed by their systems. This Appendix identifies some information types that might be processed by Federal government organizations. The material includes mission information and potential impacts of unauthorized disclosure, modification, or unavailability of mission information. The primary purpose for Federal government information systems is to support provision of basic services to U.S. citizens and residents. This section addresses information types associated with both services provided by the Federal government to citizens and mechanisms used to achieve the purposes of government or deliver services for citizens. Delivery mechanisms include financial vehicles, direct government delivery, and indirect government delivery. Federal government missions or delivery mechanisms distributed among 26 mission areas and modes of delivery are identified in Table D-1. Each mission area and delivery mode corresponds to a Services to Citizens or Mode of Delivery business area as defined in the BRM described in the FEA Consolidated Reference Model Document Version 2.3. There is not a one- to-one mapping of services and delivery modes to government departments and agencies. Some departments and agencies focus on a single mission. Others support multiple missions within a mission area. Still others provide services associated with several different mission areas. An information type is associated with each Federal government mission and delivery mode. The identity of each information type is defined by the mission with which it is associated. Some of the management and support functions executed to support delivery of services or manage government resources are also executed by some agencies in delivering services to citizens. (See especially the 'General Government' functions in Section C.2.8. of Appendix C) Most of these information types could be included in Appendix D as mission-based information types. Because the BRM categorizes them as services delivery support functions, they are included in Volume I, Section 4.1.2 and Appendix C and are not repeated in Appendix D. The common impact determination factors described in Volume I, Section 4.2.3 and 4.4, also apply to mission-based information.
  - [ ] D.1: Defense and national security: Defense and national security operations protect and advance U.S. National Security interests and, if deterrence fails, decisively defeat threats to those interests. Defense and national security activities include military operations, border protection, and intelligence gathering. Defense operations are subdivided into the following sub-elements: Impacts to information and many information systems associated with defense and national security missions may affect the security of a broad range of critical infrastructures and key national assets. Systems that, involve command and control of military forces, weapons control29, involve equipment that is an integral part of a weapon or weapons system, are critical to the direct fulfillment of military missions or are otherwise employed in strictly military operations30 are defined under Public Law as national security systems. National security information and national security systems are outside the scope of this guideline. Information assurance responsibilities are delegated to the Department of Defense for systems that are operated by the Department of Defense, or another entity on behalf of the Department of Defense31. Security objectives and impact levels associated with these systems are determined by the Department of Defense.
  - [ ] D.2: Homeland security: Homeland Security involves protecting the nation against terrorist attacks. This includes analyzing threats and intelligence, guarding borders and airports, protecting critical infrastructure, and coordinating the response emergencies. The Homeland Security Line of Business is defined by the President's Strategy on Homeland Security. Note: Some of the Critical Mission Areas from the President's strategy are included in other information classes and categories.
    - [ ] D.2.1: Border and transportation security
    - [ ] D.2.2: Key asset and critical infrastructure protection
    - [ ] D.2.3: Catastrophic defense
    - [ ] D.2.4: Executive functions of the Executive Office of the President (EOP)
  - [ ] D.3: Intelligence operations: Intelligence operations involve the development and management of accurate, comprehensive, and timely foreign intelligence on national security topics. Information systems, the function, operation, or use of, which involve intelligence activities or are critical to the direct fulfillment of intelligence missions are defined under Public Law as national security systems. National security information and national security systems are outside the scope of this guideline. Security objectives and impact levels associated with national security systems are determined by the head of each agency exercising control of the system.
    - [ ] D.3.1: Intelligence planning
    - [ ] D.3.2: Intelligence collection
    - [ ] D.3.3: Intelligence analysis and production
    - [ ] D.3.4: Intelligence dissemination
    - [ ] D.3.5: Intelligence processing
  - [ ] D.4: Disaster management: Disaster management involves the activities required to prepare for, mitigate, respond to, and repair the effects of all physical and humanitarian disasters whether natural or man-made. Compromise of much information associated with any of the missions within the disaster management mission area may seriously impact the security of a broad range of critical infrastructures and key national assets.
    - [ ] D.4.1: Disaster monitoring and prediction
    - [ ] D.4.2: Disaster preparedness and planning
    - [ ] D.4.3: Disaster repair and restoration
    - [ ] D.4.4: Emergency response
  - [ ] D.5: International affairs and commerce: International Affairs and Commerce involves the non-military activities that promote U.S. policies and interests beyond our national borders, including the negotiation of conflict resolution, treaties, and agreements. In addition, this function includes: foreign economic development and social/political development; diplomatic relations with other Nations; humanitarian, technical and other developmental assistance to key Nations; and global trade. Information that is protected by procedures established and authorized under criteria specified in an Executive Order or an Act of Congress to be kept classified in the interests of foreign policy are national security related. Security objectives and impact levels associated with such national security information are determined by the head of each agency exercising control of the system and are outside the scope of this guideline.
    - [ ] D.5.1: Foreign affairs
    - [ ] D.5.2: International development and humanitarian aid
    - [ ] D.5.3: Global trade
  - [ ] D.6: Natural resources: The Natural Resources mission area includes all activities involved in conservation planning, land management, and national park/monument tourism that affect the nation's natural and recreational resources, both private and federal. Note: Energy-related natural resources are covered in the Energy Management mission area.
    - [ ] D.6.1: Water resource management
    - [ ] D.6.2: Conservation, marine, and land management
    - [ ] D.6.3: Recreational resource management and tourism
    - [ ] D.6.4: Agricultural innovation and services
  - [ ] D.7: Energy: Energy refers to all actions performed by the government to ensure the procurement and management of energy resources, including the production, sale and distribution of energy, as well as the management of spent fuel resources. Energy management includes all types of mass- produced energy (e.g., hydroelectric, nuclear, wind, solar, or fossil fuels). Also included in this mission area is the oversight of private industry.
    - [ ] D.7.1: Energy supply
    - [ ] D.7.2: Energy conservation and preparedness
    - [ ] D.7.3: Energy resource management
    - [ ] D.7.4: Energy production
  - [ ] D.8: Environmental management: Environmental management includes all functions required to determine proper environmental standards and ensure their compliance.
    - [ ] D.8.1: Environmental monitoring and forecasting
    - [ ] D.8.2: Environmental remediation
    - [ ] D.8.3: Pollution prevention and control
  - [ ] D.9: Economic development: Economic Development includes the activities required to promote commercial/industrial development and to regulate the American financial industry to protect investors. It also includes the management and control of the domestic economy and the money supply, and the protection of intellectual property and innovation. Note: The promotion of U.S. business overseas is captured in the function, \"International Affairs and Commerce.\""
    - [ ] D.9.1: Business and industry development
    - [ ] D.9.2: Intellectual property protection
    - [ ] D.9.3: Financial sector oversight
    - [ ] D.9.4: Industry sector income stabilization
  - [ ] D.10: Community and social services: Community and Social Services includes all activities aimed at creating, expanding, or improving community and social development, social relationships, and social services in the United States. This includes all activities aimed at locality-specific or nationwide social development and general social services and general community development and social services programs, as well as earned and unearned benefit programs that promote these objectives.
    - [ ] D.10.1: Homeownership promotion
    - [ ] D.10.2: Community and regional development
    - [ ] D.10.3: Social services
    - [ ] D.10.4: Postal services
  - [ ] D.11: Transportation: Transportation involves all federally supported activities related to the safe passage, conveyance, or transportation of goods and/or people. Note that impacts to some information and many information systems associated with transportation activities may affect the security of, not only the transportation infrastructure, but also to a broad range of other critical infrastructures and key national assets.
    - [ ] D.11.1: Ground transportation
    - [ ] D.11.2: Water transportation
    - [ ] D.11.3: Air transportation
    - [ ] D.11.4: Space operations
  - [ ] D.12: Education: Education refers to those activities that impart knowledge or understanding of a particular subject to the public. Education can take place at a formal school, college, university or other training program. This mission area includes all government programs that promote the education of the public, including both earned and unearned benefit programs.
    - [ ] D.12.1: Elementary, secondary, and vocational education
    - [ ] D.12.2: Higher education
    - [ ] D.12.3: Cultural and historic preservation
    - [ ] D.12.4: Cultural and historic exhibition
  - [ ] D.13: Workforce management: Workforce Management includes those activities that promote the welfare and effectiveness of the Nation's workforce by improving their proficiency, working conditions, advancing opportunities for profitable employment, and strengthening free collective bargaining.
    - [ ] D.13.1: Training and employment
    - [ ] D.13.2: Labor rights management
    - [ ] D.13.3: Worker safety
  - [ ] D.14: Health: Public Health involves Federal programs and activities charged with ensuring and providing for the health and well being of the public. This includes the direct provision of health care services and immunizations as well as the monitoring and tracking of public health indicators for the detection of trends and identification of widespread illnesses/diseases. It also includes both earned and unearned health care benefit programs. Note that impacts to some public health information and information systems may affect the security of critical elements of the public health infrastructure.
    - [ ] D.14.1: Access to care
    - [ ] D.14.2: Population health management and consumer safety
    - [ ] D.14.3: Health care administration
    - [ ] D.14.4: Health care delivery services
    - [ ] D.14.5: Health care research and practitioner education
  - [ ] D.15: Income security: Income Security includes activities designed to ensure that members of the public are provided with the necessary means - both financial and otherwise - to sustain an adequate level of existence. This includes all benefit programs, both earned and unearned, that promote these goals for members of the public.
    - [ ] D.15.1: General retirement and disability
    - [ ] D.15.2: Unemployment compensation
    - [ ] D.15.3: Housing assistance
    - [ ] D.15.4: Food and nutrition assistance
    - [ ] D.15.5: Survivor compensation
  - [ ] D.16: Law enforcement: Law enforcement involves the protection of people, places, and things from criminal activity resulting from non-compliance with U.S. laws. This includes patrols, undercover operations, response to emergency calls, as well as arrests, raids, and seizures of property. Impacts to some information and information systems associated with law enforcement missions may affect the security of a broad range of critical infrastructures and key national assets. Some information associated with Federal law enforcement is categorized as national security information. Rules governing establishment of impact levels and controls associated with national security information are governed by a separate set of policies and are outside the scope of this guideline. Confidentiality and integrity impacts are often determined by statutory and regulatory requirements that vary by violation.
    - [ ] D.16.1: Criminal apprehension
    - [ ] D.16.2: Criminal investigation and surveillance
    - [ ] D.16.3: Citizen protection
    - [ ] D.16.4: Leadership protection
    - [ ] D.16.5: Property protection
    - [ ] D.16.6: Substance control
    - [ ] D.16.7: Crime prevention
    - [ ] D.16.8: Trade law enforcement
  - [ ] D.17: Litigation and judicial services: Litigation and judicial activities involve all activities necessary for the development and oversight of Federal programs.
    - [ ] D.17.1: Judicial hearings
    - [ ] D.17.2: Legal defense
    - [ ] D.17.3: Legal investigation
    - [ ] D.17.4: Legal prosecution and litigation
    - [ ] D.17.5: Resolution facilitation
  - [ ] D.18: Federal correctional activities: Correctional Activities involves all Federal activities that ensure the effective incarceration and rehabilitation of convicted criminals.
    - [ ] D.18.1: Criminal incarceration
    - [ ] D.18.2: Criminal rehabilitation
  - D.19: General sciences and innovation: General Science and Innovation includes all Federal activities to meet the national need to advance knowledge in this area. This includes general research and technology programs, space exploration activities, and other research and technology programs that have diverse goals and cannot be readily classified into another mission area or information type.
    - D.19.1: Scientific and technological research and innovation
    - [ ] D.19.2: Space exploration and innovation
  - D.20: Knowledge creation and management: Knowledge Creation and Management involves the programs and activities in which the Federal Government creates or develops a body or set of knowledge, the manipulation and analysis of which can provide inherent benefits for both the Federal and private sector.
    - D.20.1: Research and development
    - [ ] D.20.2: General purpose data and statistics
    - [ ] D.20.3: Advising and consulting
    - D.20.4: Knowledge dissemination
  - [ ] D.21: Regulatory compliance and enforcement: Regulatory Compliance and Enforcement involves the direct monitoring and oversight of a specific individual, group, industry, or community participating in a regulated activity via market mechanisms, command and control features, or other means to control or govern conduct or behavior.
    - [ ] D.21.1: Inspections and auditing
    - [ ] D.21.2: Standards setting / reporting guideline development
    - [ ] D.21.3: Permits and licensing
  - [ ] D.22: Public goods creation and management: The construction, manufacturing, administration, and/or management of goods, structures, facilities, common resources, etc. used for the general well being of the American public or society at large.
    - [ ] D.22.1: Manufacturing
    - [ ] D.22.2: Construction
    - [ ] D.22.3: Public resources, facility, and infrastructure management
    - [ ] D.22.4: Information infrastructure management
  - [ ] D.23: Federal financial assistance: Federal Financial Assistance is the provision of earned and unearned financial or monetary-like benefits to individuals, groups, or corporations.
    - [ ] D.23.1: Federal grants (non-state)
    - [ ] D.23.2: Direct transfers to individuals
    - [ ] D.23.3: Subsidies
    - [ ] D.23.4: Tax credits
  - [ ] D.24: Credit and insurance: Credit and Insurance involves the use of government funds to cover the subsidy cost of a direct loan or loan guarantee or to protect/indemnify members of the public from financial losses.
    - [ ] D.24.1: Direct loans
    - [ ] D.24.2: Loan guarantees
    - [ ] D.24.3: General insurance
  - [ ] D.25: Transfers to state/local governments: Transfers to States and Local Governments involve the transfer of funds or financial assistance from the Federal government to State and Local governments and Indian tribes.
    - [ ] D.25.1: Formula grants
    - [ ] D.25.2: Project / competitive grants
    - [ ] D.25.3: Earmarked grants
    - [ ] D.25.4: State loans
  - [ ] D.26: Direct services for citizens: Direct Services for Citizens refers to the delivery of a good or service to (or on behalf of) the citizenry by the federal government with no other intervening persons, conditions, or organizations.
    - [ ] D.26.1: Military operations
    - [ ] D.26.2: Civilian operations
</details>

## Security and Privacy Requirements

The BloSS@M Team relies on guidance from the Risk Management Framework, [NIST IR-8011 series](https://csrc.nist.gov/publications/detail/nistir/8011/vol-1/final), and [our threat model](../threat_model/index.md) to define and prioritize system security and privacy requirements.

Below are the initial requirements for this pilot. Per NIST IR-8011, these requirements are categorized within [the framework of the DHS CISA Continuous Diagnostics and Mitigation Capabilities](https://www.cisa.gov/cdm). These are for initial system design and early implementation, so they may not be authoritative for the whole lifecycle of the project. The authoritative point of reference for planned, ongoing, and completed work for these requirements is the [the project GitHub board](https://github.com/usnistgov/blossom). Requirements we document here at this time may cross-reference initial requirements design and implementation linked to issues in the board.

### Hardware Asset Management Capability (HWAW)

**NOTE**: The BloSS@M pilot is intended for design, implementation, and deployment only in a cloud-native environment. This choice means we do not directly control hardware. Some capabilities and sub-capabilities will be dependent upon our cloud service provider and will be accordingly design, implemented, and documented in components and system security plan. Others are still relevant for the management of "hardware-like" assets in our cloud environment(s).

- HWAM-C00: Prevent unauthorized devices
- HWAM-C01: Reduce number of devices without assigned device manager
- HWAM-C02: Reduce exploitation of decommissioned or deprovisioned systems
- HWAM-C03: Reduce insider threat of unauthorized device
- HWAM-C04: Reduce unauthorized device sub-components
- HWAM-C05: Verify ongoing business need for device
- HWAM-C06: Ensure required device data is collected

### Software Asset Management Capability (SWAM)

- SWAM-C01: Prevent unauthorized software executables
- SWAM-C02: Prevent unauthorized software installers
- SWAM-C03: Prevent or reduce software execution from unauthorized locations
- SWAM-C04: Ensure or increase trust of system software at startup
- SWAM-C05: Ensure completeness of device-level software asset management reporting
- SWAM-C06: Ensure completeness of defect-level check reporting for software asset management defects
- SWAM-C07: Increase overall reporting
- SWAM-C08: Ensure overall reporting timeliness
- SWAM-C09: Ensure or increase integrity of software authorizers
- SWAM-C10: Prevent or reduce malicious software approval
- SWAM-C11: Promptly determine and address needed installation and de-installation of software
- SWAM-C12: Prevent or reduce exploitation of software on devices moving in or out of protective boundaries
- SWAM-C13: Enable rollback and recovery
- SWAM-C14: Prevent or reduce software defects
- SWAM-C15: Verify ongoing business need for software
- SWAM-C16: Prevent or reduce unused software products
- SWAM-C17: Ensure device-software-item level accountability
- SWAM-C18: Ensure that software complies with license agreements
- SWAM-C19: Required software is present
- SWAM-C20: Ensure that software is managed
- SWAM-C21: Increase software integrity and maintainability
- SWAM-C22: Prevent or reduce malware 
### Configuration Settings Management Capability (CSM)

- CSM-C01: Prevent unauthorized configuration changes
- CSM-C02: Prevent unauthorized access to sensitive configurations
- CSM-C03: Ensure a documented review process occurs for configuration changes is followed
- CSM-C03: Prevent or reduce risk around errant or malicious configuration changes to system
- CSM-C04: Prevent or reduce the use of unauthorized configuration changes
- CMS-C05: Ensure completeness of reporting of configuration state and changes for individual sub-systems
- CSM-C06: Ensure completeness of system-wide reporting on configuration state and configuration changes
- CSM-C07: Increase overall reporting

### Vulnerability Management Capability (VULN)

- VULN-C01: Ensure all sub-systems are monitored for vulnerabilities
- VULN-C02: Ensure sub-system vulnerabilities detected by monitoring are classified by impact based between sub-system interactions and overall system impact
- VULN-C03: Ensure that all identified vulnerabilities are managed
- VULN-C04: Increase overall reporting of vulnerabilities triaged

### Management of Trusted Persons Granted Access Capability (TRUST)

- TRUST-C01: Ensure all trusted users and their trust level are identified.
- TRUST-C02: Ensure all trusted users have their trust level periodically reviewed to be authorized and/or revoked with reporting records.
- TRUST-C03: Ensure anomalous user activity outside trust level limits are monitored and reviewed with periodic reporting.
- TRUST-C04: Increase overall reporting of trusted users as trained, provisioned, and deprovisioned

### Management of Behavioral Expectations Capability (BEHAVE)

- BEHAVE-C01: Ensure all users are trained for system usage
- BEHAVE-C02: Ensure all users have agreed to rules of behavior and demonstrate knowledge from training educating users on the rules of behavior
- BEHAVE-C04: Monitor trusted users behavior for compliant and non-complaint usage of the system
- BEHAVE-C05: Ensure users are notified of non-compliant behavior and receive reminders with guidance on compliant user behavior
- BEHAVE-C05: Minimize the number sum of all non-compliant activities
- BEHAVE-C06: Increase overall reporting on all user activity in the system, complaint or non-compliant with established rules of behavior in training

### Management of Credentials and Authentication Capability (CRED)

- CRED-C01: Ensure all users authenticate with the system with strong credential types
- CRED-C02: Monitor all users for attempts to authenticate with weak credential types
- CRED-C03: Ensure all approved credential types for users are securely stored, used, and transmitted
- CRED-CO4: Ensure all approved credential types are refreshed at relevant intervals, as applicable
- CRED-C05: Monitor all users for attempts of credential reuse and/or credential recycling
- CRED-CO6: Increase reporting on the use and misuse of all credential types for all users

### Management of Privileges and Accounts Capability (PRIV)

- PRIV-C01: Ensure all new users are enrolled by the enrollment process to become trusted users
- PRIV-C02: Ensure all system trusted users are properly identified when accessing system
- PRIV-C03: Monitor trusted users for authorized operations and detect anomalies
- PRIV-C04: Monitor deprovisioned users and revoking their access to system information
- PRIV-C05: Increase overall reporting of trusted users enrolled, operating within, and deprovisioned from the system

### Management of Physical Boundaries Capability (BOUND-P)

TBD

### Management of Network Boundaries Capability (BOUND-N)

TBD

### Management of Other Boundaries Capability (BOUND-O)

TBD

### Preparation for Events, Incidents, and Contingencies (PREP)

TBD

### Management of Anomalous Events (DETECT)

TBD

### Management of Anomalous Event Response and Recovery (RESPOND)

TBD