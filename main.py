def main():
    email = input('Enter your email: ')

    result = True

    if email[0].isalpha():
        result = True
    
    elif len(email) <= 5 or len(email) >= 30:
        result = False
    
    elif '@' not in email:
        result = False
    
    else:
        at_index = email.find('@')
        if '.' not in email[at_index:]:
            result = False
        else:
            result = True
    
    print(result)
    


    ########################################
    # Do not delete the return statement
    ########################################
    return result

if __name__ == '__main__':
    main()
