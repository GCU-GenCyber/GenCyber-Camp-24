
## Principles of Privileges
Almost every organization uses identity and access management (IAM) strategies or tools as part of its security practices. IAM is the encompassing term to describe how companies manage user identities, authenticate users, and control access to company resources. Privileged identity management (PIM) and privileged access management (PAM) are subgroups of IAM.

PIM and PAM lets companies manage who can access a company’s most critical resources, like servers, databases, and applications. They operate under the ***Principle of least Privilege** to limit who and how many users can access secure systems and the sensitive data stored within.  

There are various types of principles, but levels of access are always determined by 2 factors:
+ The Individual's Position within a Company/Organization
+ The Sensitivity of the Information Being Stored

### Principle of Least Privilege
+ The principle that users should be given the minimum amount of privileges. 
+ Only those absolutely necessary should have access to certain content. 
+ It is defined as "the practice of restricting account creation and permission levels to only the resources a user requires to perform an authorized activity."
+ It is widely considered to be a cybersecurity best practice and it is a foundational step in protecting privileged access to critical data and assets.

Benefits of Least Privilege
+ Minimizes Attack Surface (the number of all possible attack vectors where the system can be accessed and data can be extracted.)
+ Reduces Spread of Malware
+ Protects Against Human Error

<p align="center">
  <img src="https://github.com/GCU-GenCyber/GenCyber-Camp-23/blob/main/Principles%20of%20Security/img/PoLP.png"
</p>
  
### Privileged Identity Management (PIM)
This is the process companies use to manage which privileged users, including human users and machine users, have access to which resources. These policies focus on ontrolling users with elevated permissions to change settings, provision or deprovision access, and make other significant changes without formal oversight. Some companies use PIM solutions to monitor user behavior and distributed access to prevent admins from having too many permissions.
  
Companies want to lessen the number of people who have access to secure information or resources  because it reduces the chance of: 
  + an authorized user inadvertently impacting a sensitive resource
  + A ***Threat Actor*** getting access.  
<sub>Definition of TAs Down Below</sub> 

  
Examples of key features of Privileged Identity Management:
+ Provides users temporary permissions to perform privileged tasks and access to Azure AD and Azure resources
+ Assign a role where a user can use the role or have access to materials only within start and end dates
+ Require approval to activate privileged roles
+ Enforce multi-factor authentication to activate any role
+ Get notifications when privileged roles are activated
+ Conduct access reviews to ensure users still need roles

<p align="center">
  <img src="https://github.com/GCU-GenCyber/GenCyber-Camp-23/blob/main/Principles%20of%20Security/img/Denied.png" />
</p>

### Privileged Access Management
This is the process of controlling and monitoring access to critical company resources, often using identity and access management technologies. Companies use PAM solutions to manage credentials and authenticate users when they tries to access a company resource. They also provide access to users that don't normally have access to certain materials for a certain amount of time. 

PAM strategies are used for the following: 
+ Enforcing ***Principle of Least Privilege***
+ Restricting Account Creation and Permissions
+ Providing Security Teams with Detailed Authorities over Sensitive Systems
+ Letting Those Teams Monitor How Privileged Resources are Being Used
+ Preventing ***Threat Actors*** from Accessing Privileged Resources
+ Prevents Catastrophic Error
+ Improves Company Policy Compliance
<sub>Definition of TAs Down Below</sub> 

<p align="center">
  <img src="https://github.com/GCU-GenCyber/GenCyber-Camp-23/blob/main/Principles%20of%20Security/img/pim-vs-pam.png" />
</p>

***The main difference between PIM and PAM is that PIM addresses what access a user is already granted, while PAM addresses how to monitor and control access whenever a user requests access to a resource.***

### Examples of Threat Actors Include: 
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


