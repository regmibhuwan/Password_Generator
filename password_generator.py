import random
import string 

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation    #Concatenation
    password = ''.join(random.choice(characters) for _ in range (length)) #list comprehension 
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    password = generate_password(password_length)
    print("Generated Password:", password)



