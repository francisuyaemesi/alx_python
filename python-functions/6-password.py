def validate_password(password):
    if len(password) < 8:
        return False
    else:
        for i in password:
            print(i)
            if i.isupper():
                continue
            elif i.islower():
                continue
            elif i.isdigit():
                continue
            elif i.isspace == False:
                continue
            else:
                return False
        return True
