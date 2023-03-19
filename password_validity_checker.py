'''
  class: SSP
    assignment - basic password validity checker program
'''

import re
from typing import Union, List

class PasswordValidityChecker:
  '''
    Password validity checker checks password is valid or not based on following criteria: 

      Password should not contain any space.
      Password should contain at least one digit(0-9).
      Password length should be between 8 to 15 characters.
      Password should contain at least one lowercase letter(a-z).
      Password should contain at least one uppercase letter(A-Z).
      Password should contain at least one special character ( @, #, %, &, !, $, etc…).

  '''

  @staticmethod
  def is_valid_password(password: str) -> Union[bool, List[str]]:
    """
      Static method (is_valid_password) called directly on the class Object

      @param password: password to verify
      @return: bool | List[str] - indicating whether password meets all the criterias OR list of Unmatched criterias

    """

    # list to keep track of failed criteria
    unmatched_criteria = []

    try:
      if password:
        if len(password) < 8 or len(password) > 15:
          unmatched_criteria.append("Password length should be between 8 to 15 characters.")
        if ' ' in password:
          unmatched_criteria.append("Password should not contain any space.")
        if not re.search(r'\d', password):
          unmatched_criteria.append("Password should contain at least one digit(0-9).")
        if not re.search(r'[a-z]', password):
          unmatched_criteria.append("Password should contain at least one lowercase letter(a-z).")
        if not re.search(r'[A-Z]', password):
          unmatched_criteria.append("Password should contain at least one uppercase letter(A-Z).")
        if not re.search(r'[@_!#$%^&*()<>?/\|}{~:]', password):
          unmatched_criteria.append("Password should contain at least one special character ( @, #, %, &, !, $, etc…).")

      if unmatched_criteria: return unmatched_criteria
      else: return True

    except Exception as e:
      print(f"Error validating password: {str(e)}")


def main():
  user_password = input("Please enter password to verify: ")

  if not user_password.strip():
    print('No password entered, please enter a valid password to be verified.')
    print(
        """
        Password must meet the following requirements:
          - Should not contain any space.
          - Should contain at least one digit (0-9).
          - Length should be between 8 to 15 characters.
          - Should contain at least one lowercase letter (a-z).
          - Should contain at least one uppercase letter (A-Z).
          - Should contain at least one special character (@, #, %, &, !, $, etc.).
        """
    )

  else:
    result = PasswordValidityChecker.is_valid_password(user_password)

    if result:
      if isinstance(result, bool):
        print("\t '{password}' is a valid password!".format(password = user_password))
      elif isinstance(result, list):
        print("Sorry '{password}' is an invalid password!\n".format(password = user_password))
        print("The following criteria were not met:")
        for criteria in result:
          print("\t-> {}".format(criteria))
    else:
      print("Sorry '{password}' is an invalid password!".format(password = user_password))


if __name__ == '__main__':
  main()
