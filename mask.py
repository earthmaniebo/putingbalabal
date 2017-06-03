import sys


def run(params):
    # loop into user input
    # we start with index 1 since 0 is the file name
    for i in range(1, len(params)):
        email = params[i].split('@')
        username = email[0]
        username_len = len(username)
        try:
            extension = email[1]
            if '.' not in extension:
                raise IndexError
        except IndexError:
            print params[i] + ' is not a valid email address.'
            return

        # create a list of None equal to the length of username
        masked_username = [None] * username_len

        # assign the first and last char of username to the new list
        masked_username[0] = username[0]
        masked_username[username_len - 1] = username[username_len - 1]

        # loop into username
        # ignore first and last char
        for i in range(1, username_len - 1):
            '''
            String is immutable in Python. So instead of just doing:
                username[i] = '*'
            We need to create another list with values of None and assign the
            result to the current
            '''
            if username[i] == '.':
                masked_username[i] = '.'
            else:
                masked_username[i] = '*'

        masked_email = ''.join(masked_username) + '@' + extension
        print masked_email


def main():
    run(sys.argv)


if __name__ == '__main__':
    main()
