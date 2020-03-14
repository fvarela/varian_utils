from simple_salesforce import Salesforce, SalesforceAuthenticationFailed, SalesforceMalformedRequest
import sys
import os
#from varian_utils import my_logging
from varian_utils.mystyle import mystyle
from varian_utils.my_logging import logger
import pdb

user = None

def sf_login(development):
    global user
    sf = None
    if development:
        user_var = 'SFQA3_USER'
        user_pass = 'SFQA3_PASS'
        user_token = 'SFQA3_TOKEN'
    else: 
        user_var = 'SF_USER'
        user_pass = 'SF_PASS'
        user_token = 'SF_TOKEN'
    def get_variables():
        user = os.environ.get(user_var)
        password = os.environ.get(user_pass)
        token = os.environ.get(user_token)
        return user, password, token
    user, password, token = get_variables()
    missing_variable = False
    print()
    for key,value in {user_var:user, user_pass:password, user_token:token}.items():
        if not value:
            logger.info(f"Variable {mystyle.bad}{key}{mystyle.done} not found on OS!\n")
            missing_variable = True
        else:
            logger.info(f"Variable {mystyle.bright}{key}{mystyle.done} found on OS\n")
    print()
    if missing_variable:
        logger.error(f"{mystyle.bad}Some variables were missing!{mystyle.done}\n\n"
                     f"Please make sure to add {mystyle.bright}{user_var}{mystyle.done}, {mystyle.bright}{user_pass}{mystyle.done} and {mystyle.bright}{user_token}{mystyle.done} "
                     "variables to your Operating System and try again.\n\n")
        input("Press enter to exit")
        sys.exit()
    try:
        if development:
            sf = Salesforce(username = user, password = password, security_token = token, domain='test')
        else:
            sf = Salesforce(username = user, password = password, security_token = token)
        if sf:
            logger.info(f'Successfully {mystyle.good}logged in{mystyle.done} on Salesforce!\n')               
            input("... Press Enter to continue\n")
            return sf
    except SalesforceAuthenticationFailed as e:
        logger.info(f'{mystyle.bad}Login unsuccessful!{mystyle.done}, check your Salesforce credentials on this computer and try again\n')
        input("Press enter to exit\n")
        sys.exit()
