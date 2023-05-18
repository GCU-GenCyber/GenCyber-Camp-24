## Threat Modeling and Incident Response
Threat Modeling is the process of reviewing, improving, and testing the security protocols in place. There are several different cyber threat modeling methodologies. They are all used to help companies improve their cybersecurity and threat intelligence practices. We will go over the STRIDE and PASTA methodologies. There are four main principles in Threat Modeing. 
+ Preparation
+ Identification
+ Mitigation
+ Review

However, if the particular incident is a complex process, then there are different principles. Those are: 
+ Threat Intelligence
+ Asset Identification
+ Mitigation Capabilities
+ Risk Assessment

### STRIDE: Used to Identifying Computer Security Threats 
+ Spoofing Identity
    + Requires authentication of requests and users accessing a system
    + Involves a malicious party impersonating another user
    + Access keys (API keys) or signatures via encryption helps remidate
+ Tampering with data
    + Anti-tampering measures on a system or application help provide integrity to data (like seals on food products)
+ Repudiation threats
    + dictates the use of services such as logging of activity for a system or application to track
+ Information Disclosure
    + same principle as of least privilege; don't disclose more than necessary
+ Denial of Service 
     + Applications use system resources, so there should be measures taken so that the app isn't bringing the whole system down
+ Elevation of privileges
    + Worst case scenario

<p align="center">
    <img src="https://github.com/GCU-GenCyber/GenCyber-Camp-23/blob/main/Principles%20of%20Security/img/STRIDE.png" />
</p>


### PASTA: Process for Attack Simulation and Threat Analysis
PASTA is used to simulate attacks, analyze threats, how they started, what their risks are, and how to mitigate those risks. The model is used to Identify the Threats, Enumerate them, and Assign a Score. 

<p align="center">
  <img src="https://github.com/GCU-GenCyber/GenCyber-Camp-23/blob/main/Principles%20of%20Security/img/PASTA.png" />
</p>

**A Breach of Security is Known as an Incident**
    - Hence the Term Incident Response
    - Incidents are classified by Urgency and Impact
    
<p align="center">
  <img src="https://github.com/GCU-GenCyber/GenCyber-Camp-23/blob/main/Principles%20of%20Security/img/Threat.png" />
</p>

**Companies Should Have a CSIRT: Computer Security Incident Response Team**
- Their a Group of IT Professionals that Respond to Incidents and Help Prevent Cybersecurity Emergencies. 
- Their Main Goal is to Respond to Incidents Quickly and Efficiently which will Minimize Damage on a system and Regain Control of it. 
- There are 6 Phases of to Resolve an Incident
    - Preparation
    - Identification
    - Containment
    - Eradication
    - Recovery
    - Lessons Learned

CSIRTs Have Many Responsibilities Such As: 
+ Create and update incident response plans
+ Maintain and communicate information to internal and external entities
+ Identify, assess and analyze incidents
+ Coordinate and communicate response efforts
+ Remediate incidents
+ Report on incidents
+ Manage audits
+ Review security policies
+ Recommend changes to prevent future incidents

Donegan, K., &amp; Sullivan, P. (2023, February 13). What is a computer security incident response team (CSIRT)?: Definition from TechTarget. WhatIs.com. https://www.techtarget.com/whatis/definition/Computer-Security-Incident-Response-Team-CSIRT 
