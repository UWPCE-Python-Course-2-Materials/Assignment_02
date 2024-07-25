'''
classes to manage the user status messages
'''
import logging
# pylint: disable=R0903


class UserStatus():
    '''
    class to hold status message data
    '''
    def __init__(self, status_id, user_id, status_text):
        self.status_id = status_id
        self.user_id = user_id
        self.status_text = status_text


class UserStatusCollection():
    '''
    Collection of UserStatus messages
    '''

    def __init__(self):
        self.database = {}

    def add_status(self, status_id, user_id, status_text):
        '''
        add a new status message to the collection
        '''
        logging.info("running add_status")
        if status_id in self.database:
            # Rejects new status if status_id already exists
            logging.error("error in add_status. status_id already exists.")
            return False
        new_status = UserStatus(status_id, user_id, status_text)
        self.database[status_id] = new_status
        logging.info("finished add_status successfully")
        return True

    def modify_status(self, status_id, user_id, status_text):
        '''
        Modifies a status message

        The new user_id and status_text are assigned to the existing message
        '''
        logging.info("entered modify_status function")
        if status_id not in self.database:
            # Rejects update is the status_id does not exist
            logging.error("status_id does not exist. returning false.")
            return False
        self.database[status_id].user_id = user_id
        self.database[status_id].status_text = status_text
        logging.info("finished changing status successfully. %s", status_text)
        return True

    def delete_status(self, status_id):
        '''
        deletes the status message with id, status_id
        '''
        logging.info("entering delete_status function")
        if status_id not in self.database:
            # Fails if status does not exist
            logging.error("status does not exist. returning false.")
            return False
        del self.database[status_id]
        logging.info("deleted status successfully. %s returning true.", status_id)
        return True

    def search_status(self, status_id):
        '''
        Find and return a status message by its status_id

        Returns an empty UserStatus object if status_id does not exist
        '''
        logging.info("entering search_status function")
        if status_id not in self.database:
            # Fails if the status does not exist
            logging.error("status does not exist. returning None.")
            return UserStatus(None, None, None)
        logging.info("successfully ran search_status. returning status_id")
        return self.database[status_id]
