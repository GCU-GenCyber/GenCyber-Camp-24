
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

### Privileged Identity Management (PIM)
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



### Privileged Access Management



<p align="center">
  <img src="https://github.com/GCU-GenCyber/GenCyber-Camp-23/blob/main/Principles%20of%20Security/img/pim-vs-pam.png" />
</p>
