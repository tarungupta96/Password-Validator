from Rules import ValidateLength, ValidateCasing, ValidateNumericCharacter, ValidateSpecialCharacters, ValidateExcludedCharacters

class PasswordValidator(object):
    
    """
    To set custom rules for the password strength and later to validate the given password as per the rules.
    """
    ruleList = []
    def __init__(self, minLength = False, maxLength = False, hasUpperCase = False, hasLowerCase = False, hasNumeric = False, specialCharacters = "", excludedCharacters = ""):

        (minLength or maxLength) and self.ruleList.append(ValidateLength(minLength = minLength, maxLength = maxLength))
        (hasUpperCase or hasLowerCase) and self.ruleList.append(ValidateCasing(hasUpperCase = hasUpperCase, hasLowerCase = hasLowerCase))
        (hasNumeric) and self.ruleList.append(ValidateNumericCharacter(hasNumeric = hasNumeric))
        (len(specialCharacters) > 0) and self.ruleList.append(ValidateSpecialCharacters(specialCharacters = specialCharacters))
        (len(excludedCharacters) > 0) and self.ruleList.append(ValidateExcludedCharacters(excludedCharacters = excludedCharacters))

    def validate(self, password):
        for x in self.ruleList:
            result, message = x.validate(password)
            if (result is False):
                return password + " Failure " + message

        return password + " Success"
