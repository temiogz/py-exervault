'''

  class: SSP
    -> Simple website blocker program per instruction

'''


class SimpleWebsiteBlocker:
  def __init__(self, blocked_websites):
    self.blocked_websites = blocked_websites

  def is_verified(self, website):
    is_allowed = True

    for blocked_website in self.blocked_websites:
      if blocked_website in website:
        is_allowed = False
        break

    return is_allowed
  

blocked_websites = [
    "www.youtube.com", 
    "youtube.com", 
    "www.facebook.com", 
    "facebook.com", 
    "www.twitter.com", 
    "twitter.com", 
    "www.gmail.com", 
    "gmail.com", 
    "www.linkedin.com", 
    "linkedin.com", 
    "www.amazon.com", 
    "amazon.com", 
    "www.addictinggames.com", 
    "www.espn.com"
  ]

# instance of the class (SimpleWebsiteBlocker)
website_blocker = SimpleWebsiteBlocker(blocked_websites)

user_prompt_website_url = input("Please enter website you want to visit (in the format www.website.com): ")
allowed = website_blocker.is_verified(user_prompt_website_url)

if allowed:
  print("{user_webssite} : Website Allowed".format(user_webssite = user_prompt_website_url))
else:
  print("Sorry, {entered_url} -> Website access not allowed".format(entered_url = user_prompt_website_url))

