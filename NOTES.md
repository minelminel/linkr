# LINKR Development Notes
---
# TODO
- Robust timeout decorator that handles TimeoutError raised
-
-

# Decisions
- Application framework?
  - Django
- Single-page app or structured?
- Front-end framework: css/html, react or angular, etc?
- Backend database
- How to handle database queries for joined rows?

# Database Schema
```python
__table__ = "users"
columns = {
    "id" : "int primary key autogenerate",
    "created_at" : "timestamp autogenerate",
    "modified_at" : "timestamp autogenerate",
    "username" : "charfield",
    "email" : "charfield",
    "settings" : "text as json",
    "active_account" : "boolean",
}

__table__ = "bucket"
columns = {
    "id" : "int primary key",
    "created_at" : "timestamp autogenerate",
    "modified_at" : "timestamp autogenerate",
    "username" : "int FROM users.id",
    "children" : "int list OF member links",
    "sharekey" : "charfield HASH",
}

__table__ = "link"
columns = {
    "id" : "int primary key autogenerate",
    "created_at" : "timestamp autogenerate",
    "modified_at" : "timestamp autogenerate",
    "username" : "int FROM users.id",
    "bucket" : "int FROM bucket.id",
    "notes" : "text",
    "sharekey" : "charfield HASH",
}
```

# Sitemap
- Home
  - Login
  - Signup
  - Demo
- Login
  - Form & Submit
  - Link to Signup
- Signup
  - Form and Submit
  - Link to Login
- Dashboard
  - My Buckets
  - My Links
  - New Bucket
  - New Link
  - Settings
  - Share
- Settings
  - etc
  - etc
  - Delete Account

# Use Cases

Signup
```
the user navigates to the sites homepage
the user is shown a clear button to create an account or login
the user selects create new account
the user fills out the form and the data is validated
the new user account is committed to the database
the user is redirected to the login page
```

Login
```
the user navigates to the homepage
the user clicks the button to login
the user fills out the login form
the form is validated and submitted
if the login is successful the user is redirected to the dashboard
```

Creating bucket
```
the user navigates to the dashboard
the user selects a button to create a bucket
the user enters a name for the bucket
the bucket is created and displayed to the user
```

Adding a link to new bucket
```
the user copies a link to the clipboard
the user navigates to the site and creates a new bucket
the user creates a new link within the bucket
the user pastes the link within the creation window
the user can add notes in a text area
the user saves the link and is redirected to the bucket detail view and focused on the new link
a preview is displayed in a preview pane
```

Interacting with saved link
```
the user navigates to the site and selects a bucket
the user scrolls through the saved links
the user selects a link for detailed view
the user is presented with 3 buttons in the detailed view:
  open in current window
  open in new window
  copy link to clipboard
the user clicks in the notes area and can immediately edit or copy the text
the text from the form is automatically committed to the database WHEN THE USER DESELECTS THE FIELD
the user clicks one of the main buttons and the appropriate action is performed
```

Sorting assets
```
the user navigates to the dashboard
the user selects a method of sorting buckets
the user selects a method of sorting links
the display is modified accordingly
```

Searching assets
```
the user navigates to the dashboard
the user enters a query in the search box
a hovering dropdown displays results of searching the users Links and Buckets by name or by notes
the user clicks an option is is shown the relevant asset view
```

Sharing a link
```
the user navigates to a link detail view
the user selects a button the share the link
the user is presented with different actions for different platforms
the user selects an option and the appropriate action is performed
```

Sharing a bucket
```
the user navigates to a bucket
the user selects an option to share the bucket
the user is presented with several options for sharing on different platforms
the user selects an option and the appropriate action is performed
```

Creating a new bucket from existing link
```
the user navigates to a detail link view
the user is presented a button to clone the link to a different bucket,
   or to start a new bucket with that link
the user selects the option to create a new bucket with that link
the user is prompted for a bucket name and types it into a form
the bucket is created with that link present
```

Deleting a link
```
the user navigates to a link detail view
the user decides to delete the link
the user is able to quickly and elegantly delete the link
```

Deleting a bucket
```
the user navigates to a bucket
the user decides to delete the bucket
the user is able to quickly and elegantly delete the bucket
```

Settings
```
the user navigates to a settings page
the user modifies some of their settings
the user clicks a save button
the settings are committed to the database
the user is redirected to the dashboard view
```

Deleting account
```
the user wants to delete their account
the user navigates to the settings page
the user selects the delete account button
the user is prompted with a modal window asking for confirmation
the user selects NO and no changes are made, OR,
the user has the "ACCOUNT_IS_ACTIVE" column of the user database set to False
```

# Display routine
<!-- Let's reduce our database load by fetching live resources every time the user requests a preview. Only minimal data should be saved persistently--id corresponding to the username of the creator, and string of the url address. The dispatcher's job is to query the __link__ database with the username_id and the link_id of the url string. If the requestor is the author && the requested element exists, return the  -->

[0] Request is created either from an interaction with the UI

[1] Target link is passed as an argument to the dispatcher

[2] GET request is created and sent

[3] Request is returned to dispatcher and parsed

[4] Schema is created and populated

[5] next::schema is fed to a display template





<!--  -->
