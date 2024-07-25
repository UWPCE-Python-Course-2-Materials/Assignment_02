'''
Classes for user information for the social network project
'''
# pylint: disable=R0903
import logging

class Users():
    '''
    Contains user information
    '''

    def __init__(self, user_id, email, user_name, user_last_name):
        logging.info("user class set up.")
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        self.user_last_name = user_last_name


class UserCollection():
    '''
    Contains a collection of Users objects
    '''

    def __init__(self):
        logging.info("initiating class instance database")
        self.database = {}

    def add_user(self, user_id, email, user_name, user_last_name):
        '''
        Adds a new user to the collection
        '''
        logging.info("add_user run")
        if user_id in self.database:
            logging.error("user_id already in data base. not added to collection.")
            return False
        if user_id == "" or email == "" or user_name == "" or user_last_name == "":
            logging.error("inputs cannot be empty. not added to collection.")
            return False
        new_user = Users(user_id, email, user_name, user_last_name)
        self.database[user_id] = new_user
        logging.info("new instance created. New user profile is %s", user_id)
        return True

    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
        Modifies an existing user
        '''
        logging.info("entering modify_user function")
        if user_id not in self.database:
            logging.error("%s not in user database", user_id)
            return False
        self.database[user_id].email = email
        self.database[user_id].user_name = user_name
        self.database[user_id].user_last_name = user_last_name
        logging.info("user information updated successfully for %s.", user_id)
        return True

    def delete_user(self, user_id):
        '''
        Deletes an existing user
        '''
        logging.info("entering delete_user function")
        if user_id not in self.database:
            logging.error("user is not in database. returning false.")
            return False
        del self.database[user_id]
        logging.info("user %s successfully deleted.", user_id)
        return True

    def search_user(self, user_id):
        '''
        Searches for user data
        '''
        logging.info("entering delete_user function")
        if user_id not in self.database:
            logging.error("user not in database. returning empty instance")
            return Users(None, None, None, None)
        logging.info("user information searched successfully for %s.", user_id)
        return self.database[user_id]
