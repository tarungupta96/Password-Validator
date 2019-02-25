# Password Validator

Password Validator is a module for specifing custom rules and handling the security of user supplied passwords.

## Usage

### Instructions to run

1. Clone this repository.
    
2. Update `Test Passwords.txt` with list of comma seperated passwords to be validated.

2. Goto the src directory:

        $ cd ./src

3. Run main.py:

        $ python main.py


## Customizing Rules

``` python
from PasswordValidator import PasswordValidator

# Initialize Password Validator with required properties
passwordValidator = PasswordValidator(minLength = 6, maxLength = 12, hasLowerCase = True, hasUpperCase = True, hasNumeric = True, specialCharacters = "*$_#=@" excludedCharacters = "[%!)(]")

# Validate password strings
passwordValidator.validate("Hello24@*") # Success

passwordValidator.validate("helloz") # Failure Password must contain at least one letter from A-Z

passwordValidator.validate("HELLOINDIA") # Failure Password must contain at least one letter from a-z.

passwordValidator.validate("lkdf") # Failure Password must be at least 6 characters long.

passwordValidator.validate("Skjdfldjldfjfdklj") # Failure Password must be at max 12 characters long.

passwordValidator.validate("Hello234") # Failure Password must contain at least one letter from *$_#=@.

passwordValidator.validate("dljfd5dfSF$%") # Failure Password cannot contain [%!)(].

```

### Rules supported as of now

|     Rules      |               Descriptions                               |
|:--------------------------|:----------------------------------------------|
|**minLength**              | minimum length of password                    |
|**maxLength**              | maximum length of password                    |
|**hasLowerCase**           | password must include lowercase letters       |
|**hasUpperCase**           | password must include uppercase letters       |
|**hasNumeric**             | password must include digits                  |
|**specialCharacters**      | must include specific special characters      |
|**excludedCharacters**     | must not contain specific characters          |
