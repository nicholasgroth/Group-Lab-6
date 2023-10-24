#Hector Cruz
def encode(password):
    encoded = ""
    for digit in password:
        new = int(digit)
        new += 3
        encoded += str(new)
    return encoded

#Nicholas Groth
def decode(encoded):
    decoded = ""
    for digit in encoded:
        new = int(digit)
        new -= 3
        decoded += str(new)
    return decoded

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        menu_opt = int(input("Please enter an option: "))
        if menu_opt == 1:
            ini_pass = input("Please enter your password to encode: ")
            encoded_pass = encode(ini_pass)
            print("Your password has been encoded and stored! ")
            print()
        if menu_opt = 2:
            print(f"The encoded password is {encode(ini_pass)}, and the original password is {decode(encoded_pass)}.")
        if menu_opt == 3:
            break

if __name__ == '__main__':
    main()
