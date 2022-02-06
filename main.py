from cryptography.fernet import Fernet

'''
def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:  # wb means write in bytes
        key_file.write(key)
# create_key()
'''


def load_key():
    file = open("key.key", "rb")  # rb means read in bytes
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master key?\n>>")
key = load_key() + master_pwd.encode() # converting master password to bytes
fer = Fernet(key)

def add():
    name = input("Username: ")
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:  # with will close the file after execution, "a" means append. w and r
        f.write(f'{name} | {str(fer.encrypt(pwd.encode()))}\n')

def view():
    with open('passwords.txt', 'r') as f:  # with will close the file after execution, "r" means read. w and a
        for line in f.readlines():
            data = line.rstrip()  # strips the extra new line
            user, password = data.split("|")  # assigns first element from list to user and second to password
            print(f'User: {user} | Password: {str(fer.decrypt(password.encode()))}')


while True:
    mode = input("(Add) a new password or (View) old password or (Q)uit?\n>> ").lower()

    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid Input!")
        continue