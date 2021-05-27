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

-    ## Administrator Goals
        * I should be able to edit / delete any character.
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
    * Full and mobile Index page [here](readme/index_wireframes.pdf)
    * Full and mobile Characters page [here](readme/characters_wireframes.pdf)
    * Full and mobile Roles page [here](readme/roles_wireframes.pdf)

## Features
-   Responsive on all devices with:
    *   CSS Media Queries for showing/hiding elements on scaling.
    *   Collaspible Header with side nav for mobile devices.
-   Contains interactive elements such as:
    *   Serachable database.
    *   User authentication via register/log in/ log out.
    *   Loops hide/show various navigation options depending on user status.
    *   Contact form linked with Emailjs.
    *   C.R.U.D. functionality scaled with user status.(user/ unregistered / admin).

## Technologies Used
### Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [PYthon 3](https://www.python.org/)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries & Programs Used
- [Email.JS](https://www.emailjs.com/) - for contact form.
- [GitHub](https://github.com)
- [Jquery](https://jquery.com/) - For hide/ show of elements.
- [GitPod](https://www.gitpod.io/) - IDE.
- [Materialize (including JQuery)](https://materializecss.com/) -Utilized for responsiveness via columns, buttons and navbars.
- [Google Fonts](https://fonts.google.com) - User for header and body fonts throughout.
- [Font Awesome](https://fontawesome.com/)  - For icons.
- Google Chrome's Responsive Viewer found [here](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb)
- Google Chrome's lighthouse function.
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - For template engine.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/) - For creating views and methods.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) - For password hashing.
- [MongoDB](https://www.mongodb.com/) - Database.
- [Heroku](https://www.heroku.com/) - For hosting.

## Testing
-   Using [W3C validator](https://validator.w3.org/) both HTML and CSS were checked by direct input. Issues arising were promptly corrected. 
<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>
<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>

-   [JsHINT](https://jshint.com)- Used for Java Script validation. Warnings relating to the use of 'let' to declare variables.
    The script was not amended to address these.


### Testing User Stories from User Experience (UX) section.
### First Time Visitor Goals :

*  I want easily understand the site's purpose.
    1.  The index page utilises eye-cathcing colours, fonts and clean lines with an upfront description
        of the sites aim.
    2.  Users are immediately granted access to the site's database via clickable images.
    3.  Users are made aware of the site's policy, and the added benefits to registering.
     
* I want to navigate the site's content.
    1.  A static, collaspible header contains all the nav elemnets available to new users. Although 
        registration/login is rerquired to access more functions, the main database is available to read.
        As is the contact, register and Log In page.

* I want to understand how to create my own characters.
    1.  Users are informed how to create characters on both the index page and the Characters page.
        New users can register a username and password which instantly grants them create, update and delete
        functionality for their characters. Upon registration, new users are brought to their profile page
        which, in time, will display all their characters, on first visit they are offered a chance to create
        their first character.
    2.  On clicking 'create' a form is rendered where the user can populate the required fields. The character's role
        must come from an existing list via a dropdown. All users are free to populate the other fields as they wish.
    3.  Upon completeion, the user is redirected to the characters page with a flash messsage for confirmation,
        and their new character is added to the database. The new character is also viewable from their profile page. 

### Returning / Registered User Goals :

*  I want to see characters I have created.
    1.  A returning user can log in, afterwhich they are brought to their profile page which displays any 
        previously created characters listed from newest addition to oldest. The profile page is always available 
        in the nav bar for logged in users.
     
* I want to edit or delete my characters. 
    1.  Only characters created by a user can be edited or deleted by that user. Characters can be deleted or edit 
        from the user's personal profile page or from the main characters page.
    2.  Characters eligible for edit or delete will have the available buttons displayed in their drop down.
    3.  To Edit : clicking the edit button renders a form populated with the selected character's information.
        The user can make their intended changes and click 'Save Changes', or cancel the request altogether. Both
        options return the user to the characters page with a flash confirming edits or a reload characters' page
        in the case of a cancel. 
    4.  To Delete : clicking the delete button calls a modal to warn the user all deletions are permenant. 
        The user can cancel the process at the modal, or proceed to final confirmation by accepting the warning.
        Upon accepting the modal warning a 'delete forever' button is displayed which when clicked deletes the
        selected character from the database with a flash message to confirm.

* I want to contact the site admin.
    1.  All users can navigate to the contact page in the nav bar. There is a simple form available to contact
        the site's admin. First name, email and a message is all that is required. Links to social media accounts
        are also available in the footer.  



### Administrator Goals :

* I should be able to edit / delete any character.
    1.  Upon log in, an administrator is brought to their profile page which lists all their characters.
        The characters page which lists all charcaters is also available but unlike standard users, the admin
        has the ability to edit or delete all characters in the database. 
    2.  To Edit : clicking the edit button renders a form populated with the selected character's information.
        The admin can make their intended changes and click 'Save Changes', or cancel the request altogether. Both
        options return the admin to the characters page with a flash confirming edits or a reload characters' page
        in the case of a cancel. 
    3.  To Delete : clicking the delete button calls a modal to warn the admin all deletions are permenant. 
        The admin can cancel the process at the modal, or proceed to final confirmation by accepting the warning.
        Upon accepting the modal warning a 'delete forever' button is displayed which when clicked deletes the
        selected character from the database with a flash message to confirm.  

* I want to add, edit or delete new character roles.
    1.  When logged in as admin, the roles page becomes available. The page lists all roles currently live on the site
        from which users can choose for their characters. Roles are listed in alphabetical order. 
    2.  To Add : a 'Add Role' button is prominently displayed at the top of the roles page. Clicking the button brings
        the admin to add_role.html which contains a single row form the admin can populate. Here they can cancel the operation,
        or proceed with their addition. Adding a role diverts the admin back to the roles page with a flash message as confirmation. 
    3.  To Edit : a 'Edit / Delete' button is available to the admin for each populated role. Upon clicking the admin is brought to
        edit_role.html which pre-populates the single row form with the current role selected for edit or delete. The admin can
        cancel the request, or proceed with editing. A usccessful edit returns the admin to the roles page with flash message for   
        confirmation.

Click [here](Testing.md) for full testing based on user stories.


### Further Testing 
    login, user, see roles etc


# Deployment 

# Credits   
## contents 
## Media