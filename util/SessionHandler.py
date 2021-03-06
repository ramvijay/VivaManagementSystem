"""
Handles all things related to the Sessions
"""
from enum import Enum
from datetime import datetime
from util.configuration import ConfigurationManager


class SessionVariableKeys(Enum):
    """
    Stores the keys used in the session storage
    """
    USER_ID = 'user_id',
    USER_ROLE = 'user_role',
    IS_LOGGED_IN = 'is_logged_in',
    LAST_ACTIVE = 'last_active'


class SessionHandler:
    """
    Handles all session related activites
    """
    # Variable that stores the session object of the current request
    __session_obj = None
    # Validity time for the session
    __SESSION_VALID_TIME = 60 * 15

    @staticmethod
    def set_session_obj(session_obj):
        """
        Method for setting the session object which is getting attached to the request.
        :param session_obj: Request's session obj
        :return: None
        """
        SessionHandler.__session_obj = session_obj
        # Now update the session
        SessionHandler.update_active_session()

    @staticmethod
    def login_user(user_obj):
        """
        Method for logging in the user by setting the required  session variables
        :param user_obj: Details about the authenticated user
        :return: None
        """
        SessionHandler.__set_session_var(SessionVariableKeys.IS_LOGGED_IN, True)
        SessionHandler.__set_session_var(SessionVariableKeys.LAST_ACTIVE, datetime.now())
        SessionHandler.__set_session_var(SessionVariableKeys.USER_ID, user_obj.user_id_id)
        SessionHandler.__set_session_var(SessionVariableKeys.USER_ROLE, user_obj.user_role)

       # print(user_obj[0].user_id)
        # SessionHandler.__session_obj['is_logged_in'] = True
        # SessionHandler.__session_obj['last_active'] = datetime.now()
        # SessionHandler.__session_obj['user_id'] = user_obj.user_id

    @staticmethod
    def is_user_logged_in():
        """
        Method for checking if the user is logged in or not
        :return: True if the user is logged in. False otherwise.
        """
        try:
            return SessionHandler.__get_session_var(SessionVariableKeys.IS_LOGGED_IN)
            # return SessionHandler.__session_obj['is_logged_in']
        except KeyError:
            return False

    @staticmethod
    def update_active_session():
        """
        Method for updating the current sessions's timestamp
        :return: None
        """
        ConfigurationManager.get_instance()
        if not SessionHandler.__session_obj.has_key(SessionVariableKeys.IS_LOGGED_IN):
            # Set them to the defaults and return
            SessionHandler.__set_session_var(SessionVariableKeys.IS_LOGGED_IN, False)
            SessionHandler.__set_session_var(SessionVariableKeys.LAST_ACTIVE, datetime.now())
            SessionHandler.__set_session_var(SessionVariableKeys.USER_ID, None)
            # SessionHandler.__session_obj['is_logged_in'] = False
            # SessionHandler.__session_obj['last_active'] = datetime.now()
            # SessionHandler.__session_obj['user_id'] = None
            return
        if SessionHandler.__get_session_var(SessionVariableKeys.IS_LOGGED_IN):
            now_time = datetime.now()
            time_diff = now_time - SessionHandler.__get_session_var(SessionVariableKeys.LAST_ACTIVE)
            if time_diff.seconds > SessionHandler.__SESSION_VALID_TIME:
                # Invalidate the session since it has been inactive for too long.
                SessionHandler.__set_session_var(SessionVariableKeys.IS_LOGGED_IN, False)
        SessionHandler.__set_session_var(SessionVariableKeys.LAST_ACTIVE, datetime.now())

    @staticmethod
    def get_user_role():
        """
        Method for getting the type of the logged in user.
        :return: Type of the user logged in.
        """
        return SessionHandler.__get_session_var(SessionVariableKeys.USER_ROLE)
    @staticmethod
    def get_user_id():
        """
        Returns the user_id from the stored session.
        :return: ID of the logged in user
        """
        return SessionHandler.__get_session_var(SessionVariableKeys.USER_ID)

    @staticmethod
    def logout_user():
        """
        Method for destroying the session
        :return: None
        """
        # SessionHandler.__session_obj['is_logged_in'] = False
        # SessionHandler.__session_obj['user_id'] = None
        SessionHandler.__set_session_var(SessionVariableKeys.IS_LOGGED_IN, False)
        SessionHandler.__set_session_var(SessionVariableKeys.USER_ID, None)

    @staticmethod
    def __get_session_var(var_key):
        """
        Method to get a session variable
        :param var_key: Variable key that is to be obtained from the Session
        :return: Value of the variable
        """
        try:
            return SessionHandler.__session_obj[var_key]
        except KeyError:
            return None

    @staticmethod
    def __set_session_var(var_key, var_value):
        """
        Sets the value of a particular session variable
        :param var_key: Variable to set
        :param var_value: Value of variable to set
        :return: None
        """
        SessionHandler.__session_obj[var_key] = var_value

