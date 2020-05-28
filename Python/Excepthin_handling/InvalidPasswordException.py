'''a = input("Enter a password: ").strip()
try:
     assert len(a)>8,"InvalidPasswordException"
except AssertionError:
     print("Create a password with minimum of 8 characters")
else:
     print("Password: "+a)
'''
class InvalidePasswordException(Exception):
    def __init__(self, msg):
        self.msg = msg


def password(pwd):
    if len(pwd) >= 8:
        print("Strong password.")
    else:
        raise InvalidePasswordException("Password should be at least 8 character long.")


try:
    print("Enter password of minimum length 8 characters.")
    pwd1 = input("Enter password: ")
    password(pwd1)
except InvalidePasswordException:
        print("Password should be at least 8 character long.")

