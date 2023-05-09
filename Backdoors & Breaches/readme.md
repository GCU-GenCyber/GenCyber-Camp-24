All the instructions and information you need to play backdoors & breaches right at your fingertips!

To read: Change the format at the top from preview to code

Original Link: https://mygcuedu6961-my.sharepoint.com/:o:/g/personal/aurbaszews_my_gcu_edu/Eg7lPGa4sXRGsvIAORkwLEEBZMNg5K3cpyebp-DatCzC6w?e=4k4kcx

Attack Cards

Password Spray- Access internal network by spraying common passwords against the organization
	• Spraying tool kit- set of python scripts/utilities to make password spraying quicker
	• FireProx- leverages the AWS API gateway to create pass-through proxies that rotate the source IP address with every request
	• Hydra- password brute force
	• Mailsniper- pen test tool for searching through email in a microsoft exchange environment for specific terms
	• Bruteloops- library providing logic for efficient password brute force attacks against authentication interfaces
	• MSOL Spray- for microsoft online accounts; the script logs if a user cred is valid; MFA is enabled on the account; if a tenant doesn’t exist; if user doesn’t exist; if the account is locked or disabled

Credential Stuffing- take advantage of third-party breaches to identify and use ID’s and passwords against your organization
	• Burpsuite- used for pen testing of web apps
	• Hydra- see password spray
	• Users registering for services with their work emails

Exploitable External Service- take advantage of misconfiguration or publicly available exploit to pivot to internal resources
	• Metasploit- provides info about security vulnerabilities and pentesting 
	• Failed patching process
	• Unauthorized system stood up by employee

Web Server Compromise- take over external; pivot to internal network
	• Zed attack proxy- used to detect vulnerabilities present on any web server and try to remove them
	• Sqlmap- detect and exploit database vulnerabilities and inject malicious codes
	• Burp proxy- intercept, inspect, and modify traffic both ways; between browser and target apps

Phish- malicious email targeting users
	• Modalishka- automates phishing of one time passcodes
	• Evilginx- man in the middle framework for phishing login credentials to bypass 2-factor authentication protection
	• Gophish- run authorized phishing simulations

Social Engineering- trick a user into running malware
	• Phones, peoples trust

External Cloud Access- access cloud resources then pivot
	• Spraying toolkit- see password spray
	• Trufflehog- open source secret scanning engine that helps resolve exposed secrets across your company’s entire tech stack
	• Fireprox- see password spray

Insider Threat- an internal user exfiltrates information from your network
	• Lots of time

Bring Your Own Exploited Device- attackers use these devices to compromise your organization
	• Do not allow workers to bring their own computers and such

Trusted Relationship- third party who has access to your network is compromised then pivot to internal resources
	• Only trust certain people

Pivot and Escalate Cards

Local Priviledge Escalation- attackers use a vulnerability in local software to gain administrative access
	• Powersploit's Power up- modules designed for offensive security operations; quick checks against a machine
	• Meterpreter Post-Exploitation Scripts- any actions after an open session, which is an open shell from a successfule exploit or bruteforce attack

Broadcast/Multicast Protocol Poisoning- LLMNR lets a host ask for name resolution from any system on the same network; performs poisoning on the active directory network
	• Responder attacks LLMNR, NBT-NS, mDNS
	• https://Github.com/lgandx/Responder

New Service Creation- attackers create and load their malware using a service with system privileges or create a new service 
	• Metasploit getsystem- elevates current privileges to system

Kerberoasting- attackers use a "feature" of SPN's to extract and crack service passwords
	• GetUserSPNs.py from Impacket- can be used to obtain a password hash for user accounts that have an SPN (service principal name)
	• Hashcat for Cracking- password recovery tool

Weaponizing Active Directory- attackers map trust relationships and user/group privileges in your active directory network
	• Bloodhound- continuously maps and quantifies active directory attack paths
	• DeathStar- python script that uses empires restful API to automate gaining domain admin rights in active directory environments
	• CrackMapExec- developed in python and designed for pentesting against networks

Credential Stuffing- attackers use valid active directory credentials that were on open shares and files
	• ADExplorer.exe- viewer and editor for active directory uses
	• Invoke-Sharefinder- finds non-standard shares on hosts in the local domain
	• Invoke-Filefinder- finds potentially sensitive files on hosts in the local domain
	• Find-Interestingfile- searches for files on the given path that match a series of specified criteria
	• Mailsniper- pentesting tool for searching through email in a ms exchange environment for specific terms

Internal Password Spray- attackers start a password spray against the rest of the organization from a compromised system
	• Domain password spray- tool written in powershell to perform a password spray attack against users of a domain

Persistence Cards

Malicious Service- attackers add a service that starts every time the system starts
	• Meterpreter persistence modules- meterpreter is a listener, persistent keeps it going, module uploads it 
	• Msconfig.exe- system utility to troubleshoot the microsoft windows startup process; can disable or re-enable software, device drivers and windows services that run at startup, or change boot parameters
	• SILENTTRINITY- open source remote administration and post-exploitation framework primarily written in Python that includes stagers written in Powershell, C, and Boo.
	• Sysinternals- website that offers technical resources and utilities to manage, diagnose, troubleshoot, and monitor a microsoft windows environment
	• Autoruns.exe- shows you all the programs that run during startup and disables unnecessary and malicious ones

Malicious Driver- loaded into the operating system
	• Pasam- creates a backdoor through which remote attackers can upload files
	• Wingbird- surveillance tool to gather credentials, files, docs, recording data, gaining access to webcams and mics
	• SeaDuke- trojan malware written in python; used against high value targets
	• ROCKBOOT- bootkit that establishes persistence
	• Alureon- trojan and rootkit created to steal data by intercepting a system's network traffic and searching through the data

Malicious Browser Plugins- install plugins, can be used as part of C2 and persistence; the browser is the new endpoint
	• Grammarly is a keylogger
	• Graniet/chromebackdoor- PoC of pentest tool; after launch runs a malicious extension or script on browsers

Logon Scripts- attackers install a script that triggers when a user logs on
	• Meterpreter persistence- see malicious service

Application Shimming- use app compatibility toolkit to trick apps into not seeing the ports, directories, files, and services the attackers want to hide
	• Windows assessment and deployment kit (ADK)- assess the quality and performance of systems or components

New User Added- attackers add a new user to the local computer
	• Metasploit- provides info about security vulnerabilities and aids in pentesting and IDS signature development
	• Cobalt Strike- assesses security of networks and systems; commercial pentesting tool

Accessibility Features- attackers hijack features
	• Bash Bunny- multi vector usb atacks
	• USB Rubber Ducky- wifi injector

DLL Attacks- hijack the order in which dynamic link libraries are loaded; through insecure directory/file permissions
	• DLLHIjack Test- looks for the same name in multiple locations to perform an analysis
	• Powersploit: Powerup- collection of ms powershell modules that can aid pentesters during assessments

Evil Firmware- attackers update network firmware of cards, video cards, BIOS, or UEFI; very difficult to detect and update
	• UEFI RootKit- allows someone to maintain command and control over a computer without the user knowing
	• BadBIOS- rootkit that infects a systems basic input output system
	• Trickbot- bankng trojan that can steal financial details, account credentials, and personally identifiable information; can spread within a network and drop ransomware

C2 and Exfil Cards

DNS as C2- attackers use DNS as a C2 channel
	• Dnscat2- create an encrypted command and control channel over the DNS protocol, which tunnels out of almost every netwrok

Domain Fronting as C2- attackers use domain fronting to bounce their traffic off of legitimate systems
	• Cobalt Strike- assess the security of networks and systems and to identify and exploit potential vulnerabilities and weaknesses

Gmail, Tumblr, Salesforce, Twitter as C2- attackers route traffic through third-party services
	• Gcat- google cybersecurity action team
	• Sneaky creeper- open source project that allows security professionals to import modules

HTTP as Exfil- attackers use HTTP
	• Metasploit Reverse HTTP Payloads- creates a connection from the target machine back to the metasploit server over HTTP
	• VSAgent- uses the ViewState parameter in a well-formed HTML page to communicate commands and their results between the C2 server and client
	• Prismatica- automatically collects and analyzes data patterns to assess project health and systemic behaviors in agile activities

HTTPS as Exfil- attackers use HTTPS
	• Metasploit Reverse HTTPS Payloads- it is a pentesting tool that can control responses in the systems
	• SILENTTRINITY- open source remote administration and post-exploitation framework primarily written in Python that includes stagers written in Powershell, C, and Boo

Windows Background Intelligent Transfer Service (BITS)- attackers use BITS, which is often ignored
	• Netflow- collects ip network traffic as it enters or exits an interface
	• Zeek/bro- targets high-perfomance networks and is used operationally at a variety of large sites
	• RITA Analysis- real intelligence threat analytics is an open source framework for detecting command and control communication through network traffic analysis

Injects- Place any notes here! 

Procedures

Netflow, Zeek/Bro, RITA Analysis- capture and review network traffic
	• RITA- real intelligence threat analytics is an open source framework for detecting command and control communication through network traffic analysis
	• Security Onion- threat hunting, network security monitoring, and log management
	• AI-Hunter- continuously threat hunts your network to identify which of your systems have been compromised

Isolation- isolate infected systems to prevent further harm
	• Switch and Router commands- look up a good cheat sheet

User and Entity Behavior Analytics (UEBA)- looks for multiple concurrent logins, impossible logins based on geography, unusual file access, password sprays and more
	• Logontracer- investigates malicious logon by visualizing and analyzing windows active directory event logs

Firewall Log Review- analyze and understand logs; regularly emulate attack scenarios and verify procedures
	• SOF-ELK- appliance like virtual machine that is preconfigured to ingest and parse several hundred different types of log entries and netflow data

Endpoint Security Protection Analysis- get alerts and logs, review them. 
	• Check with vendor

Server Analysis- baseline a system and verify that its operating in a normal state
	• DeepBlueCLI- powershell module for threat hunting via windows event logs
	• SANS Analysis Cheat Sheets- find a link

Endpoint Analysis- defenders use SANS IR cheat sheets to detect attacks on workstations
	• DeepBlueCLI- powershell module for threat hunting via windows event logs
	• SANS IR Cheat Sheets- find a link

Internal Segmentation- turn on host based firewalls, segment different organizational units, treat the internal network as hostile
	• Netsh advfirewall- controls firewall behavior and rules
	• Windows Defender Firewall- helps prevent hackers or malicious software from gaining access to a PC through the internet or network
	• Iptables- user space utility program that allows a system administrator to configure the IP packet filter rules of the Linux firewall

Crisis Management- legal and management teams have procedures for effectively and ethically notifying impacted victims of compromises
	• This rarely happens so good notifications are ideal

Security Information and Event Management (SIEM) Log Analysis- logging the right things and emulate attack scenarios to see if you can detect them
	• SOF-ELK- appliance like virtual machine that is preconfigured to ingest and parse several hundred different types of log entries and netflow data
	• JPCert Tools Analysis- results for each tool are in table format; logs are recorded and examined


