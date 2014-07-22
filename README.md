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

Temporary DB Structure.
This DB allows for prototyping of implementation, without a Confluence API environment.

  Users
    id
    user_name
    email_address

  Spaces
    id - Auto incrementing id.
    Name - Name of space
  
  Access
    user_name - FK pointing to users
    space_id - FK pointing to Spaces table.
    access_type - string "admin" "read" "write"
   
  Pending - Contains pending requests
    user_name - FK pointing to users
    space_id - FK pointing to spaces
    access_type_requested - access_type string
    explanation_string - String of user inputed explanation.

TODO:
Implement edit button for management.  This button would prompt a popup where you can edit or delete access rights. 
In general alot of the input could stand to have more error checking. 
