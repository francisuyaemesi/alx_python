def validate_password(password):

    if len(password) > 8:

        lowerCase = False
        upperCase = False
        num = False
        space = True

        for i in password:
            if(i.isdigit()):
                num = True
            if(i.isupper()):
                upperCase = True
            if(i.islower()):
                lowerCase = True
            if(i.isspace()):
                space = False
                 
        return lowerCase and upperCase and num and space
    
    else:
        return False
    
