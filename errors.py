""" This program is a password-checker - it tries to validate a password and
then "creates an account," which for our purposes just returns a tuple
containing both the username and password."""

class InvalidPasswordError(ValueError):
    pass

INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)
def validate_password(username, password):
    if password == username:
        raise InvalidPasswordError('Passord cannot be the same as your username.')
    if password in INVALID_PASSWORDS:
        raise InvalidPasswordError('Password cannot be that simple.')
    


def create_account(username, password):
    return (username, password)


def main(username, password):
    try:
        print(f'username: {username!r}, password: {password!r}')
        validate_password(username, password)
    except InvalidPasswordError as err:
        print (err)
    else:
        account = create_account(username, password)
        print("Validated password against username and simple passwords")
        
    

if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')
    main('guest', 'guest')