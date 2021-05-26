# Project Name: I Need A Hero

## Project aim
The site's aim is to provide a place for users to share characters 
they no longer need, or to find character ideas from those uploaded from other users.
The site targets fantasy writers firstly but the character lists can be utilised by role-players
or anyone with an idea they like to share.

Firstly the site to benefit the user community, and secondly to grow a user database and run competitions
via the monthly newletter with user-submitted short-stories and awards for best uploads.

[View Live Version here]()

## User Experiance (UX)

### User stories
-    ## First Time Visitor Goals
        * I want easily understand the site's purpose. 
        * I want to navigate the site's content.
        * I want to understand how to create my own characters.

-    ##   Returning / Registered User Goals
        * I want to see characters I have created.
        * I want to edit or delete my characters. 
        * I want to contact the site admin.

-    ## Administrator
        * I should be able to edit / delete all characters.
        * I want to edit or add new character roles.

### Design
-    ### Colour Scheme
        * #8e24aa (Deep Purple) - Nav, forms and footer.
        * #00e676 (Green), #ff1744 (Red), #2979ff (Blue), #ffea00 (Yellow) for buttons.
        * Standard whitesmoke for body background.
            
-    ### Typography
        * font-family:'Montserrat' for body font, and font-family:'Permanent Marker' for headers and some flash messages.
        Both from [Google Fonts](https://fonts.google.com). Sans Serif is used a fallback. 

-    ### Imagery
        * Three card images on the index page 
            * [Blue sky](https://static.wikia.nocookie.net/god-of-slaughter/images/3/3a/Thunder2.jpg)
            * [Red Sky](https://media.freestocktextures.com/cache/4b/b4/4bb46fda2948c0d26699661ac01f212c.jpg)
            * [Grey Sky](https://sewitall.com/wp-content/uploads/2020/01/Lightning-Grey-cut-piece-scaled.jpg)            


*   ### Wireframes
    * Full and mobile Index page - [veiw](readme/index_wireframes.pdf)


ADD IN WIREFRAMES


## Features
### The Surface Plane
Overall the site is responsive and scales with user screen size.

### Existing Features
* Header : Navigation collapses depending on screen size, while also adding/removing options depending on users are logged in or not.
* Index : Is kept concise by design, offers options for registration, contact and login in the body. Media queries
and jquery adjust the display cards
accordingly as screen size changes.  
* Contact : A simple form with an area for messages from users. It is not intended for any other purpose.
* Characters: Contains an active list of queriable terms for the serach function. Also houses a complete list of all uploaded 
characters.
* Roles: Available only to ADMIN, the roles pages allows full C.R.U.D. functionality for the admin. Also provides defensive 
programming against duplicate role creations.
* Profile: Allows creation for registered users and ADMIN, as well as displaying characters uploaded by only that user. 
Edit and Delete functions also accessible 
* Create: Available to registered users and ADMIN only, allows creation of new characters which are added to the main characters page
and the users' profile page.
* Log in: verifies username with stored password before granting access.
* Register: checks current user list against entry to deny duplicate user names.
* Log out: Returns user to login page with reduced navbar options, treating them as brand new users. 
* Footer : Links provided to fictional social medias.
* Other: Modals and hide/show functions to interupt accidental deletions.

### Features left to implement 
* Link contact form using python. When email.js was applied and functional, it interfered with the flash messages on submit. Had to use jquery for confirmation message instead. 

## Technologies used
* HTML-For basic structure.
* CSS-For styling and required Media Query outside of Bootstrap.
* JavaScriprt 
* [Email.JS](https://www.emailjs.com/)
* [Jquery](https://jquery.com/)
* [W3C validator](https://validator.w3.org/) - Used in testing HTML and CSS.
* [JsHINT](https://jshint.com)- Used for Java Script validation.
* [GitHub](https://github.com)
* [GitPod](https://www.gitpod.io/) - IDE.
* [Materialize (including JQuery)](https://materializecss.com/) -Utilized for responsiveness via columns, buttons and navbars.
* [Google Fonts](https://fonts.google.com) - User for header and body fonts throughout.
* [Font Awesome](https://fontawesome.com/)  - For icons.
* Google Chrome's Responsive Viewer found [here](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb)
* Google Chrome's lighthouse function.
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - For template engine.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
* [Pthon 3](https://www.python.org/) - For creating views and methods.
* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
* [MongoDB](https://www.mongodb.com/) - Database.
* [Heroku](https://www.heroku.com/) - For hosting.
* Others such as FLASK can be found in the app.py and requirements folders.

# Testing
Click [here](Testing.md) for full testing based on user stories.
## Responsiveness 
## Lighthouse

# Code Validation
## jshint and others 

# Deployment 

# Credits   
## contents 
## Media