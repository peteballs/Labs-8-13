print("Welcome to the Encoder! It is so good to see you using our site!")
print("Thank you for giving us the opportunity to serve you!!")
clear_text = input("Please type the first word that you want the computer to encode.........").lower()
number = int(input("Please input the rotation number for the encription..............."))
str1 = clear_text
abc = "abcdefghijklmnopqrstuvwxyz"
rot_13 = lambda x: "".join([abc[(abc.find(c)+number)%26] for c in x])
encrypted_text = rot_13(str1)
print('Your encrypted text: ' + encrypted_text)
decrypted_text = rot_13(encrypted_text)
print('Your decrypted text: ' + decrypted_text)
print("Thank you very much for utilizing our site!")