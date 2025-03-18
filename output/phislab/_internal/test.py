def check_email(email: str) -> bool:
    if "@" in email and "." in email:
        if email.index("@") != 0 and email.index("@") <= len(email) - 3 and email.index(".") > email.index("@"):
            return True
    return False

def new_check_mail(email: str) -> bool:
    if "@" in email and "." in email and " " not in email:
        dog, dot = email.index("@"), email.index(".")
        if dog != 0 and dog <= len(email) - 3 and dot > dog:
            if not email[dot + 1].isdigit(): 
                if dot - dog > 1:
                    return True
    return False
# print(check_email("2@.u"))
print(new_check_mail(input()))