import os
import secrets

def generate_secret_key(length=24):
    # Generate a random URL-safe text string, in this case 24 characters long
    return secrets.token_urlsafe(length)

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print("Your generated secret key is:", secret_key)
