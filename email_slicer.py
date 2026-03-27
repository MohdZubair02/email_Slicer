def email_slicer(email):
    # Split the email into username and domain
    username = email[:email.index('@')]
    domain = email[email.index('@') + 1:]
    
    return username, domain

if __name__ == "__main__":
    email = input("Enter your email address: ")
    username, domain = email_slicer(email)
    
    print(f"Username: {username}")
    print(f"Domain: {domain}")
