from PasswordValidator import PasswordValidator

if __name__ == "__main__":

    # Reading comma separated passwords for the validation
    file = open("../Test Passwords.txt", "r")
    input_passwords = file.read().split(",")

    # Configure the rules for Password Validation
    passwordValidator = PasswordValidator(minLength = 6, maxLength = 12, hasLowerCase = True, hasUpperCase = True, hasNumeric = True, specialCharacters = "*$_#=@", excludedCharacters = "%!)(")

    for x in input_passwords:
    	print(passwordValidator.validate(x))
