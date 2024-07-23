def encode(password):
    encoded = ''.join(str(int(char) + 3) for char in password)
    return encoded
def decode(password):
    decoded = ''.join(str(int(char) - 3) for char in password)
    return decoded
def main():
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("\nPlease enter an option: ")

        if option == '1':
            password = input("Please enter the password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == '2':
            if 'encoded_password' in locals():
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            else:
                print("No password has been encoded yet!")

        elif option == '3':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()