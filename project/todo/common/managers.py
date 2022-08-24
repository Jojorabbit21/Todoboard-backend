from django.contrib.auth.models import BaseUserManager

# https://axce.tistory.com/99?category=991890 참고해서 제작중

class UserManager(BaseUserManager):
  
  # All User
  def create_user(self, username, email, password=None, **extra_fields):
    if username is None:
      raise TypeError("Username invalid")
    if email is None:
      raise TypeError("Email invalid")
    if password is None:
      raise TypeError("Password Invalid")