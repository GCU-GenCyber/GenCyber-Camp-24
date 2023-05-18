## Threat Modeling and Incident Response
- Process of reviewing, improving, and testing the security protocols in place
- 4 main principles
    - preparation
    - identification
    - mitigation
    - review
- But, if its a complex process
    - threat intelligence
    - asset identification
    - mitigation capabilities
    - risk assessment
- STRIDE
    - Spoofing Identity
        
        - requires authentication of requests and users accessing a system
        - involves a malicious party impersonating another user
        - Access keys (API keys) or signatures via encryption helps remidate
    - Tampering with data
        
        - anti-tampering measures on a system or application help provide integrity to data
        - like seals on food products
    - Repudiation threats
        
        - dictates the use of services such as logging of activity for a system or application to track
    - Information Disclosure
        
        - same principle as of least privilege; don't disclose more than necessary
    - Denial of Service
        
        - apps use system resources, there should be measures taken so that the app isn't bringing the whole system down
    - Elevation of privileges
        
        - worst case scenario
- PASTA
    - Process for Attack Simulation and Threat Analysis
- Breach of security is known as an incident
    - hence incident response
    - they're classified by urgency and impact
    
<p align="center">
  <img src="https://github.com/GCU-GenCyber/GenCyber-Camp-23/edit/main/Principles%20of%20Security/img/Threats.png">
</p>

- CSIRT: Computer Security Incident Response Team
- 6 Phases of to resolve and incident
    - Preparation
    - Identification
    - Containment
    - Eradication
    - Recovery
    - Lessons Learned
