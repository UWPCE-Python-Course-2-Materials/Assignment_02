# Findings #

* ERR: KeyError - user_section does not recognize letter case by itself, so menu_options[user_selection]() gives a KeyError
    * SOLN:menu_options[user_selection.upper()]()

* ERR: load_users() needs an instance input parameter, not the user_selection:  main.load_users(filename, user_selection)
    * SOLN: replace user_selection with user_collection which is the actual instance

*ERR: search_user function. While trying to add user,  runs through result.name. "name" is not an attribute of search_user.
    * SOLN: replaced "name" with "user_id" 

* ERR: update_user() did not have required user_collection to call update_user() from main properly.
    * SOLN: added user_collection to update_user() parameters

* ERR: TypeError: if wrong csv file is opened, user gets type error.
    * SOLN: conditional statement added to give warning if csv file header does not fit required inputs

* WARN: empty strings can also be added as users.
    *SOLN: added and logged a conditional statement that looks for empty strings in user input

* ERR: main.add_status() called in update_status() in menu instead of main.update_status()
    *SOLN: replaced add_status with update_status. Changed order of parameters as well in order to return correct items to the base function.