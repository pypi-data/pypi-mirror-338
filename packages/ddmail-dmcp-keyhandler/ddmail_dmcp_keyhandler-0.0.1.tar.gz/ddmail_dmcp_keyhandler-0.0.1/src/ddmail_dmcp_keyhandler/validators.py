import re

# Validate password. Passwords will be base64 encoded. Only allow the following chars: A-Z, a-z, 0-9 and +/=
def is_password_allowed(password):
    pattern = re.compile(r"[a-zA-Z0-9\+\/\=]")

    for char in password:
        if not re.match(pattern, char):
            return False

    return True

# Validate domain names. Only allow the following chars: a-z, 0-9 and .-
def is_domain_allowed(domain):
    if not len(domain) > 3:
        return False

    if domain.startswith('.') or domain.startswith('-'):
        return False
    if domain.endswith('.') or domain.endswith('-'):
        return False
    if '--' in domain:
        return False
    if '..' in domain:
        return False

    if domain.find(".") == -1:
        return False

    pattern = re.compile(r"[a-z0-9.-]")
    for char in domain:
        if not re.match(pattern, char):
            return False

    return True

# Validate email address. Only allow the following chars: a-z, 0-9 and @.-
def is_email_allowed(email):
    if not len(email) > 6:
        return False

    if email.count('@') != 1:
        return False
    if email.startswith('.') or email.startswith('@') or email.startswith('-'):
        return False
    if email.endswith('.') or email.endswith('@') or email.endswith('-'):
        return False

    # Validate email part of email.
    splitted_email = email.split('@')
    if splitted_email[0].startswith('.') or splitted_email[0].startswith('-'):
        return False
    if splitted_email[0].endswith('.') or splitted_email[0].endswith('-'):
        return False
    if '--' in splitted_email[0]:
        return False
    if '..' in splitted_email[0]:
        return False

    # Validate Domain part of email.
    if is_domain_allowed(splitted_email[1]) != True:
        return False

    pattern = re.compile(r"[a-z0-9@.-]")
    for char in email:
        if not re.match(pattern, char):
            return False

    return True
