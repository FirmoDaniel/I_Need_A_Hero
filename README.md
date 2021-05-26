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
        functionality for their characters.

### Returning / Registered User Goals :

*  I want to see characters I have created.
    1.  The 
    2.  Users 
    3.  Users 
     
* I want to edit or delete my characters. 
    1.  A static

* I want to contact the site admin.
    1.  Users 




Click [here](Testing.md) for full testing based on user stories.


### Further Testing 
    login, user, see roles etc


# Deployment 

# Credits   
## contents 
## Media