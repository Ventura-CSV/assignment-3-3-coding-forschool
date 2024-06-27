def main():
    email = input('Enter your email: ')

    result = True

    if email[0].isalpha:
        return True
    elif len(email) <= 5 or len(email) >= 30:
        return False
    elif email.find('@'):
        result = False
    
    else:
        at_index = email.find('@')
        if email.find('.', at_index) == 1:
            result = False
            
    


    ########################################
    # Do not delete the return statement
    ########################################
    return result

if __name__ == '__main__':
    main()
