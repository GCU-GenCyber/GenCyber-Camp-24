## CIA Triad
***This is one of the most valuable items to someone wanting to learn about Cybersecurity. It is one of the foundations of cyber.***
<p align="center">
  <img src="https://github.com/GCU-GenCyber/GenCyber-Camp-23/blob/main/Principles%20of%20Security/img/Triad.png" />
</p>


The CIA Triad is a model that is used to form security systems. It is used to find vulnerabilities and ways to create solutions. When all three standards have been met, the security profile of the organization is stronger and better equipped to handle threat incidents.
There are Three parts to the CIA Triad (Hence the name Triad): 
+ Confidentiality
+ Integrity
+ Availability


### Confidentiality
+ Refers to the protection of data from unauthorized access and misuse
+ This could include employee records, accounting documents, etc. 
+ The goal is to make sure that data is kept private/secret. 
+ Access to information MUST be controlled to prevent the unauthorized access, misuse, or sharing of data
+ Organizations and Companies MUST make sure that people without proper authorization are prevented from accessing assets important to their business
+ However, those who need to have access must have the necessary privileges.
+ This is where ***Availability*** comes in. 
+ Ways to meet Confidentiality include:
  + Classifying and Labeling Restricted Data
  + Enabling Access Control Policies
  + Encrypting Data
  + Using Multi-Factor Authentication (MFA)
  + Employee Awareness and Trainging

### Integrity
+ Involves making sure your data is trustworthy and free from tampering
+ Data is authentic, accurate, and reliable.
+ Information should be kept consistent and correct unless authorized changes have been made.
+ Access Control and Authentication HELP A LOT
+ Ways to Ensure Integrity Include:
  + Hashing
  + Encryption
  + Digital Signatures

### Availability 
+ Refers to the concept of data being available and accessible by the user when AUTHORIZED
+ A system should be available when necessary to prevent damage to reputation of a company or loss of finances
+ Ensuring Confidentiality and Integrity is useless if employees are unable to access the data they need to serve their customers
+ Systems, Networks, and Applications should be up and working when they should and as they should. 
+ It should not take an immense amount of time to access data. 
+ Disasters such as natural or power outages can affect Availability.
+ This is why Disaster Recovery Plans (DRPs) are put into place my most if not all companies. 
+ Ways to Ensure Availability Include:
  + Usage of Redundant Networks, Servers, or Applications
  + Consistently Upgrading or Updating Software


## Principles of Privileges
Principles of Privileges refer to what level of access employee have. There are various types of principles, but levels of access are always determined by 2 factors:
+ The Individual's Position within a Company/Organization
+ The Sensitivity of the Information Being Stored

1. Privileged Identity Management (PIM)
+ This is used to translate a user's roles within an organization into an access role on the system
+ It is a service in Azure Active Directory (Azure AD) that enables a person to manage, control, and monitor access to important resources in one's company/organization. 
+ Companies want to lessen the number of people who have access to secure information or resources.  
+ This is because it reduces the chance of: 
  + an authorized user inadvertently impacting a sensitive resource
  + A threat actor getting access. Examples of Threat Actors Include: 
    + Hackers : Typical people trying to hack your infrastructure
    + Hacktivists : Those who promote their cause their cause through hacking
    + Script Kiddies : Can't hack so they grab known scripts; premade attacks
    + Insiders : An employee, someone who has access to the place
    + Competitors : They try to break in and get business info
    + Shadow IT : Any form of IT infrastructure that is being put in an unofficial or potential illegal way. This could be another department within the company installing an access point without permission. 
    + Criminal Syndicates : These are paid people who will Hack, DoS, ransomware, etc. for money. 
    + State Actors : Russians, Chinese, French, state-sponsored long-term threat actors
    + Advanced Persistent Threat (APT) : long-term hacking of something in order to get information over time; could be an organization or person
    + Basically anyone or anything with motive and resources to attack another's IT infrastructure

Privileged Identity Management provides time-based and approval-based role activation to mitigate the risks of excessive, unnecessary, or misused access permissions on resources that a company cares about. Examples of key features of Privileged Identity Management:
+ Provides users temporary permissions to perform privileged tasks and access to Azure AD and Azure resources
+ Assign a role where a user can use the role or have access to materials only within start and end dates
+ Require approval to activate privileged roles
+ Enforce multi-factor authentication to activate any role
+ Get notifications when privileged roles are activated
+ Conduct access reviews to ensure users still need roles

