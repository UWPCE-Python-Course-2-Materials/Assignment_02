'''
main driver for a simple social network project
'''
import csv
import logging
import pathlib
import users
import user_status


def init_user_collection():
    '''
    Creates and returns a new instance of UserCollection
    '''
    user_instance = users.UserCollection()
    # print(instance.database)
    return user_instance


def init_status_collection():
    '''
    Creates and returns a new instance of UserStatusCollection
    '''
    status_instance = user_status.UserStatusCollection()
    return status_instance


def load_users(filename, user_collection:users.UserCollection):
    '''
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    '''
    valid = True
    if not pathlib.Path(filename).resolve().is_file():
        valid = False
        logging.warning("false file path given. Valid returning false.")
        print('invalid file. Please try again.')
    if valid is True:
        with open(filename, 'r',encoding='utf-8') as file:
            file_read = csv.reader(file)
            file_list = list(file_read)
            for row in file_list[1:]:
                if '' in row:
                    logging.warning("invalid empty fields. exiting function and returning false.")
                    return valid is False
                check_user_exists = search_user(row[0],user_collection)
                if check_user_exists.user_id is None:
                    user_collection.add_user(*row)
        logging.info("file path valid. Returning true")
    return valid


def check_path_valid(file):
    '''
    checks if the called file format works for writing to csv
    '''
    logging.info("entered check_path_valid for save_users. ")
    valid = False
    restricted_chars = ['/','?', '|', '\\',]
    if not file.endswith(".csv"):
        logging.error("incorrect file type. returning false")
        print("Incorrect file type. Please input a path to a .csv file.")
    # elif file.
    else:
        valid = True
    for item in restricted_chars:
        if item in file:
            valid = False
            break
    print('in check path valid test', valid)
    return valid


def save_users(filename, user_collection: users.UserCollection):
    '''
    Saves all users in user_collection into
    a CSV file

    Requirements:
    - If there is an existing file, it will
    overwrite it.
    - Returns False if there are any errors
    (such as an invalid filename).
    - Otherwise, it returns True.
    '''
    valid = check_path_valid(filename)
    logging.info("check file validity returned %s", valid)
    if valid is True:
        with open(filename, 'w',newline='',encoding='utf-8') as saved_users:
            write_csv = csv.writer(saved_users)
            write_csv.writerow(["USER_ID","EMAIL","NAME","LASTNAME"])
            for item in user_collection.database.values():
                write_csv.writerow([item.user_id,item.email,item.user_name,item.user_last_name])
    logging.info("users successfully saved into csv")
    return valid

def load_status_updates(filename, status_collection:user_status.UserStatusCollection):
    '''
    Opens a CSV file with status data and adds it to an existing
    instance of UserStatusCollection

    Requirements:
    - If a status_id already exists, it will ignore it and continue to
      the next.
    - Returns False if there are any errors(such as empty fields in the
      source CSV file)
    - Otherwise, it returns True.
    '''
    valid=True
    if not pathlib.Path(filename).resolve().is_file():
        logging.error("file does not exist. returning false")
        valid = False
    if valid is True:
        with open(filename, 'r', encoding='utf-8') as file:
            file_read = csv.reader(file)
            file_list = list(file_read)
            for row in file_list[1:]:
                if '' in row:
                    valid = False
                    break
                check_status_exists = search_status(row[0], status_collection)
                if check_status_exists.status_id is None:
                    status_collection.add_status(*row)
    logging.info("status successfully loaded")
    return valid


def save_status_updates(filename, status_collection:user_status.UserStatusCollection):
    '''
    Saves all statuses in status_collection into a CSV file

    Requirements:
    - If there is an existing file, it will overwrite it.
    - Returns False if there are any errors(such an invalid filename).
    - Otherwise, it returns True.
    '''
    valid = check_path_valid(filename)
    print("right after check path valid test",valid)
    if valid is True:
        with open(filename, 'w',newline='',encoding='utf-8') as saved_users:
            write_csv = csv.writer(saved_users)
            write_csv.writerow(["STATUS_ID","USER_ID","STATUS_TEXT"])
            for item in status_collection.database.values():
                write_csv.writerow([item.status_id,item.user_id,item.status_text])
        print('what is this',write_csv)
    print(valid)
    return valid



def add_user(user_id, email, user_name, user_last_name, user_collection: users.UserCollection):
    '''
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_user() returns False).
    - Otherwise, it returns True.
    '''
    return user_collection.add_user(user_id, email, user_name, user_last_name)


def update_user(user_id, email, user_name, user_last_name, user_collection: users.UserCollection):
    '''
    Updates the values of an existing user

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    # '''
    # print("here is user_collection",user_collection.database)
    return user_collection.modify_user(user_id,email,user_name,user_last_name)


def delete_user(user_id, user_collection:users.UserCollection):
    '''
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    '''
    return user_collection.delete_user(user_id)


def search_user(user_id, user_collection:users.UserCollection):
    '''
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    '''
    return user_collection.search_user(user_id)


def add_status(user_id, status_id, status_text, status_collection:user_status.UserStatusCollection):
    '''
    Creates a new instance of UserStatus and stores it in
    user_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    '''
    return status_collection.add_status(user_id,status_id,status_text)


def update_status(status_id, user_id, status_text,
                  status_collection:user_status.UserStatusCollection):
    '''
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    return status_collection.modify_status(status_id, user_id, status_text)


def delete_status(status_id, status_collection:user_status.UserStatusCollection):
    '''
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    '''
    return status_collection.delete_status(status_id)


def search_status(status_id, status_collection: user_status.UserStatusCollection):
    '''
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    '''
    return status_collection.search_status(status_id)

# if __name__ == "__main__":
#     instance = init_user_collection()
#     loaded_status = load_users('test_file_good.csv', instance)
#     returned_instance = delete_user('testuser',instance)
#     # returned_instance = save_users('abc123.csv', instance)
#     print("after delete_user",instance.database)
