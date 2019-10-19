import string

print("Welcome to the Encoder! It is so good to see you using our site!")
print("Thank you for giving us the opportunity to serve you!!")

while True:
    
    clear_text = input("Please type the first word that you want the computer to encode between PARENTHESIS.........").lower()
    str1 = clear_text

    number = int(input("Please indicate the rotation desired.........."))

    abc = "abcdefghijklmnopqrstuvwxyz"
    rot_13 = lambda x: "".join([abc[(abc.find(c)+number)%26] for c in x])
    encrypted_text = rot_13(str1)
    print('Your encrypted text: ' + encrypted_text)
    decrypted_text = rot_13(encrypted_text)
    print('Your decrypted text: ' + decrypted_text)
    proceed = input("Do you want to continue?.....(yes or no)......").lower()

    if proceed == "no":
        print("Thank you very much for utilizing our site!")
        break