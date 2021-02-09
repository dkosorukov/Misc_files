""" This program is a password-checker - it tries to validate a password and
then "creates an account," which for our purposes just returns a tuple
containing both the username and password."""

INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)

class InvalidPasswordError(Exception):
    pass
    

def validate_password(username, password):
    flag = password != username and password not in INVALID_PASSWORDS
    if flag:
        return flag
    else:
        raise InvalidPasswordError()


def create_account(username, password):
    return (username, password)


def main(username, password):
    try:
        valid = validate_password(username, password)
    except InvalidPasswordError:
        print ('Bad password')
    else:
        account = create_account(username, password)
        print(f'username: {username!r}, password: {password!r}')
    

if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')
    main('guest', 'guest')