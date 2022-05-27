class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.is_lenght_valid(value) and self.contains_number(value) and self.contains_upercase(value):
            self.password = value
            return
        else:
            raise ValueError("")
    def is_lenght_valid(self, password):
        return len(password) >= 8

    def contains_upercase(self, password):
        upper_letters = [char for char in password if char.isupper()]
        return True if upper_letters else False

    def contains_number(self, password):
        nums = [char for char in password if char.isdigit()]
        return True if nums else False
# short_name = Profile("asd", "pass")
# print(short_name.username)

#Да се довърши!!!