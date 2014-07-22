jirahelper
==========

Example of a Jira Groups Management tool I discussed in a Janestreet interview.

Features:
Request Group Access From Group Admin.  Specify access level you are requesting(read or read/write) and what your reason for access is(short string).
Basic database manages admin priveledges, in an actual implementation you could replace this with the Jira API.

Goals: 
- Provide an intuitive, easy, and clean system to allow management of access rights to specific Confluence spaces.  
- Value simplicity and quickness over complexity and specific cases.  A general intuitive tool is required here, not a complex one. 

Specific Functions
- Quick way for users to request access to a particular space.
- Quick way for admins to manage access requests.
