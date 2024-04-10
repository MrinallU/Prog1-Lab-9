def encode_password(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password



def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            encoded_password = input("Please enter the encoded password: ")
            decoded_password = ""
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif option == "3":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
