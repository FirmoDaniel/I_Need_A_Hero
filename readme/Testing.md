# Testing : I Need A Hero 


## Users

### Registration
User (Testing) can register via register.html using 'password' as their password. They are redirected to profile.html
![registration-success](readme/testing/registration-successful.jpg)
The registered user is added to db ![registration-success-mongo](readme/testing/registration-successful-mongo.jpg)
Once logged in the registered user -who is not admin- has access to 'Characters', 'Profile', and 'Create' in the navbar 
while 'log in' and 'register' have been removed. The 'session' is also active.![user-not-admin](readme/testing/user-not-admin.jpg)

### Profile page
* A button/link labelled 'view charcaters' is available on Testing's profile page to navigate user to (info.html/Characters)
![user-not-admin-characters-page](readme/testing/user-not-admin-charcters-page.jpg)
* A button/link labelled 'create' is available on Testing's profile page to navigate user to create_from_profile.html
as noted in the url address. This allows the user to be redirected back to their profile page after character creation, whereas
creating a character form the create.html, or from info.htm/Characters page both send users back to info.html/Characters. 
![create-from-profile](readme/testing/create-from-profile.jpg)
* The role category is access via select options and the input elements are validated with min and max lenght where applicable.
* The cancel button redirects user to their profile.
![create-a-character](readme/testing/create-a-character.jpg)
* The create button redirects user to their profile with a flash message as confirmation and their newly created character showing.
It also provides options to 'Edit' or 'Delete' existing characters. A new 'create' button is placed at the top of their list for easy access.
![create-from-profile-success](readme/testing/create-from-profile-success.jpg)
* Choosing to Edit a Character brings the user to edit_info_from_profile.html so they can be sent back to their profile upon completion.
The page displays the selected Characters information for editing.
![edit-info-from-profile](readme/testing/edit-from-profile.jpg)
A 'Cancel' button returns the user to their profile. The 'Edit Character' button implements any changes made and also rediects to profile.html 
For example we have changed character description from witch to warlock.
![character-edited-from-profile](readme/testing/character-edited-from-profile.jpg)
* Deleting a character from the profile page. Upon selecting 'Delete' in the intended character's dropdown
a modal appears advise user that all deletions are permenant. The modal's cancel option returns user to their profile page.
![delete-from-profile-modal](readme/testing/delete-from-profile-modal.jpg)
The modal's 'proceed to delete' option dismisses the modal, hides the original 'Delete' button which calle dthe modal, and unhides
two further buttons. 'No! Cancel' giving the user a further chance to rethink their decision, and 'Yes! Delete forever' which removes the
character and returns the user to their profile with a flash message for confirmation.
![delete-from-profile-success](readme/testing/delete-from-profile-success.jpg)
if the user navigates away the delete forever button is re-hidden and they must initiate the process again following the steps laid out above.

### Characters page
* Here a self updating list of serachable terms is provided : roles(hero/heroine) or descriptions (Werewolf/Necromancer). 
Only the Admin can update Character Roles, though users are free to add descriptions of their choice to newly created characters. 
* There is also a serach function where users can utilise the list provided to search by role or description or both.
![search-function](readme/testing/search-function.jpg)
* serach results display all matches to 'hero' and 'werewolf'
![search-function-hero-and-werewolf](readme/testing/search-function-hero-and-werewolf.jpg)
### logout



