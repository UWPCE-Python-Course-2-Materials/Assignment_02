# Findings #

* ERR: KeyError - user_section does not recognize letter case by itself, so menu_options[user_selection]() gives a KeyError
    * SOLN:menu_options[user_selection.upper()]()
* ERR: load_users() needs an instance input parameter, not the user_selection:  main.load_users(filename, user_selection)
    * SOLN: replace user_selection with user_collection which is the actual instance
* ERR: menu add_users() function logic does not truly check if inputs are valid
    * SOLN: 

*ERR: search_user function. While trying to add user,  runs through result.name. "name" is not an attribute of search_user.
    * SOLN: replaced "name" with "user_id" 

* ERR: menu update_users() function logic does not truly check if inputs are valid
    * SOLN: 