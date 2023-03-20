import datetime

# Assignment: Mini program testing user qualification for access:

# default argument
# python inputs are set to string by default
def compute_current_user_age(dob = "10-03-2000"):
  # input validation
  user_input = dob.split('-')
  
  # if user mistype or submit wrong format 
  if len(user_input) < 3: 
    return False
  
  try:
    current_date  = datetime.date.today()
    parsed_dob  = datetime.datetime.strptime(dob, "%d-%m-%Y").date()
    user_dob  = (current_date.year - parsed_dob.year) - ((current_date.month, current_date.day) < (parsed_dob.month, parsed_dob.day))
    return user_dob  
  except Exception as e:
    return None


def get_age():
  try:
    user_dob_input = input("Please enter your date of birth in the format 'dd-mm-yyyy': ")
    age = compute_current_user_age(user_dob_input)

    if not age:
      print("Invalid ({user_dob_input}) date of birth provided")
      return False

    return age
  except Exception as e:
    return None


# User's security Clearance Level= High (give the user 3 options:- High, Medium, Low)
def get_clearance_level():
  try:
    print("Please enter your security clearance level with the corresponding number: ")
    print("1. High")
    print("2. Medium")
    print("3. Low")
    user_security_clearance_level = input()

    return user_security_clearance_level
  except Exception as e:
    return None


# User's Qualification/Degree
def get_qualification():
  try:
    print("Please enter your Qualification/Degree with the corresponding number: ")
    print("1. Bachelors")
    print("2. Masters")
    print("3. Doctoral")
    user_qualification = input()

    return user_qualification
  except Exception as e:
    return None

''' User's prior experience in security domain in years >= 5 '''
def get_industry_experience():
  try:
    print("Please enter your experience in security domain (in years): ")
    user_industry_experience = int(input())

    return user_industry_experience
  except Exception as e:
    return None


# User's Position Levels
def get_position_level():
  try:
    print("Please enter your position with the corresponding number: ")
    print("1. Partner")
    print("2. Sr Manager")
    print("3. Manager")
    print("4. Deputy Manager")
    print("5. Associate")
    print("6. Analyst")
    print("7. Assistant")
    user_position_level = input()

    return user_position_level
  except Exception as e:
    return None


# Here we check if all the above conditions are satisfied before granting access.
# isUserAuthorized function returns a boolean value
def is_user_authorized(age: int, security_level: str, qualification: str, experience: int, position_level: str) -> bool:
  return (
    age >= 18
    and security_level == "1"
    and (qualification == "2" or qualification == "3")
    and experience >= 5
    and (position_level == "1" or position_level == "2" or position_level == "3")
  )


def user_access_verification_system():
  age = get_age()

  if age is False:
    print("Please provide a valid (D-O-B) {pdob} in the format provided".format(pdob = 'dd-mm-yyyy'))
    return

  security_level = get_clearance_level()
  qualification = get_qualification()
  experience = get_industry_experience()
  positionLevel = get_position_level()

  if is_user_authorized(age, security_level, qualification, experience, positionLevel):
    print('Access Granted')
  else:
    print("Access Denied")


if __name__ == "__main__":
  user_access_verification_system()


'''

Improvement:
  Could use proper error handling
  Proper Input validation

'''