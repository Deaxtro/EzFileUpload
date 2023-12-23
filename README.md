EzFile

This Django project consists of several endpoints for managing files and user authentication.

Used in built django groups to seperate users for achieving view restriction 

based on whether the user is Ops user or not and by default all the logged in user are treated as clients.

Also customized filefield to restrict the filetype being uploaded(only pptx, docs, xlsx)

while also making it flexible enough to add/remove restrictions as per the need.

Endpoints
1. List Files
Path: /ezFile/
Function: views.ez_FileList
Description: Displays a list of files.
2. Upload File
Path: /ezFile/upload
Function: views.ez_File_upload
Description: Allows users to upload files.
3. User Login
Path: /ezFile/login
Function: views.login_user
Description: Handles user login functionality.
4. User Logout
Path: /ezFile/logout
Function: views.logout_user
Description: Handles user logout functionality.
5. User Signup
Path: /ezFile/signup
Function: views.signup
Description: Allows new users to sign up.
