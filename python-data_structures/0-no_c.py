def no_c(my_string):
    updated_string = ""
    for char in my_string:
        if  char != "c" and char != "C":
            updated_string  += char
    return updated_string