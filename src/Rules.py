import re
import sys 

class ValidateLength(object):
    """
    Rule to validate the Password length as per the configuration
    """
    
    def __init__(self, minLength=-1, maxLength=sys.maxsize):
        self.minLength = minLength
        self.maxLength = maxLength

    def validate(self, password):
        length = len(password)
        if (length < self.minLength):
            return False, "Password must be at least " + str(self.minLength) +" characters long."
        elif (length > self.maxLength):
            return False, "Password must be at max " + str(self.maxLength) + " characters long."
        
        return True, ""


class ValidateCasing(object):
    """
    Rule to validate the inclusion of Upper and Lower case character
    """

    def __init__(self, hasUpperCase = False, hasLowerCase = False):
        self.hasUpperCase = hasUpperCase
        self.hasLowerCase = hasLowerCase

    def validate(self, password):
        if (self.hasLowerCase and not re.search('[a-z]', password)):
            return False, "Password must contain at least one letter from a-z."
        elif (self.hasUpperCase and not re.search("[A-Z]",password)):
            return False, "Password must contain at least one letter from A-Z."
        
        return True, ""


class ValidateNumericCharacter(object):
    """
    Rule to validate the inclusion of Upper and Lower case character
    """

    def __init__(self, hasNumeric):
        self.hasNumeric = hasNumeric

    def validate(self, password):
        if (self.hasNumeric and not re.search('[0-9]', password)):
            return False, "Password must contain at least one letter from 0-9."

        return True, ""

class ValidateSpecialCharacters(object):
    """
    Rule to validate the inclusion of special character
    """

    def __init__(self, specialCharacters):
        self.specialCharacters = specialCharacters

    def validate(self, password):
        if any(char in password for char in self.specialCharacters):
            return True, ""
        
        return False, "Password must contain at least one letter from {}.".format(self.specialCharacters)


class ValidateExcludedCharacters(object):
    """
    Rule to validate the exclusion of unwanted character
    """
    
    def __init__(self, excludedCharacters):
        self.excludedCharacters = excludedCharacters

    def validate(self, password):
        if any(char in password for char in self.excludedCharacters):
            return False, "Password cannot contain {}.".format(self.excludedCharacters)
        
        return True, ""