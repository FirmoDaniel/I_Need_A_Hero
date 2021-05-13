# Project Name: I Need A Hero

## Project aim
The site's aim is to provide a place for users to share characters 
they no longer need, or to find character ideas from those uploaded from other users.
The site targets fantasy writers firstly but the character lists can be utilised by role-players
or anyone with an idea they like to share.

Firstly the site to benefit the user community, and secondly to grow a user database and run competitions
via the monthly newletter with user-submitted short-stories and awards for best uploads.


## UX
#### Strategy & Scope planes
The website targets writers in need of or, in posession of: 
* New character idea's
* Uneeded characters they don;t wnat to waste
* General reserach to see if their idea is already out there.

In terms of scope the site is kept concise and utilises the same colours throughout for a smooth
tranistion from page to page.
* #8e24aa (Deep Purple) - Nav and footer.
* #00e676 (Green), #ff1744 (Red), #2979ff (Blue), #ffea00 (Yellow) for buttons.
* Standard whitesmoke for body background.
* font-family:'Montserrat' for body font, and font-family:'Permanent Marker' for headers.
Both from [Google Fonts](https://fonts.google.com).

## User Experiances
* [New User](#new-user)
* [Returning / Registered User](#returning-user)
* [Administrator](#Administrator)

## New User
### Question: 
"I need a character idea for a story I'm working on." 

### Answer: 
New users arrive at the home/index page to a brief description of the site's intentions.
They are advised to keep uploads family friendly and provided links to view site's characters.
![Index](readme/screenshots/new-user-index.jpg)

A New User can:
* see only certain navbar links (home, contact, characters, register or [log in](readme/screenshots/login.jpg)).
* choose to [register](readme/screenshots/register.jpg) from the home page.
* choose to [contact](readme/screenshots/contact.jpg) the site from the home page.
* click on any of the three card images which all navigate to the characters page
![characters page/ (info.html)](readme/screenshots/new-user-characters.jpg) where they are advised to 
register if they'd like to upload a character, and if not the  
search functionality is explained and accompanied by a list of current, and self-updating, 
active serach terms. In addition to the search function New Users can scroll through the
existing list of characters and further advised to utilise the dropdown carret for more
information. ![dropdown](readme/screenshots/new-user-characters-dropdown.jpg)


## Returning / Registered User
### Question: 
"I have a character I've' previously shared, but now I want to edit them" 

### Answer: 
A returning / registered user arrives at the home/index page where they can navigate to [log in](readme/screenshots/login.jpg)).
Upon successful login, they are brought to their own profile page which displays only the characters they have created.
![profile](readme/screenshots/registered-user-profile.jpg) (Note:registered user have access to more nav bar options such as
"Profile" and "Create" ). On their profile page they also have access to edit or delete only charcaters THEY have created. 
characters![profile](readme/screenshots/registered-user-profile-edit-delete.jpg). Upon selecting 'edit' they are presented with
the selcted characters information displayed on a new 'Edit character from profile' page[edit_profile](readme/screenshots/registered-user-profile-edit.jpg).
Once the character information has been updated the user is returned to their profile page and flash message confirms their changes.
![edit character from profile success](readme/screenshots/registered-user-profile-edit-success.jpg)

## Administrator
### Question: 
"I need to delete an inappropriate/nonsensical upload" 

### Answer: 
Upon login the admin is brought to their profile page but can navigate to the characters page to find the offending enrty. Once located, 
via serach function, or scrolling, the admin can expand any uploaded character to find options for 'edit' or 'delete'.
![Admin delete non-sensical upload](readme/screenshots/admin-delete-nonsensical.jpg)
After selecting 'delete' a customized modal appears warning the admin that all deleteions are permenant. When the admin confirms their
understanding and  closes the modal two new buttons appear. "No! Cancel" giving the admin a second chance to rethink their decision, and
"Yes! Delete Forever" which will permenatly remove the upload from the site. Upon permenant deletion the admin's choice is confirmed 
via flash message displayed at the top of the screen. ![admin character deleted](readme/screenshots/admin-character-deleted.jpg)