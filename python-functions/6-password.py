def validate_password(password):

    if len(password) >= 8:

        lowerCase = False
        upperCase = False
        num = False
        Special = False

        for i in password:
            if(i.isdigit()):
                num = True
            if(i.isupper()):
                upperCase = True
            if(i.islower()):
                lowerCase = True
            if(not i.isalnum()):
                Special = True
                 
        return lowerCase and upperCase and num and Special
    
    else:
        return False
hi = validate_password("password")
print(hi)