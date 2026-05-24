# list for invalid chars can't you type in email
invalid_email_chars = [
    # spaces and brackets
    ' ', '(', ')', '[', ']', '{', '}', '<', '>',

    # invalid chars
    ',', ';', ':', '\\', '"', '/', '*', '!', '#', 
    '$', '%', '^', '&', '?', '~', '`', '|', '=', '+'
]

def search(em):
    try:
        mail = str(em)
        m1, m2 = mail.split("@")
        contains_invalid = any(char in em for char in invalid_email_chars)
        if contains_invalid == False:
                mm1 , mm2 = m2.split(".")
        else: 
            return False
    except ValueError: 
        return False
    else:
        return True

def emailcheck(email):
    count = str(email)
    if count.count("@") or count.count(".") == 1 :
        if search(email) :
            return True
        else:
            return False
    else: 
        return False