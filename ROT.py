import codecs

print("Welcome to the Encoder! It is so good to see you using our site!")
print("Thank you for giving us the opportunity to serve you!!")

clear_text = input("Please type the first word that you want the computer to encode.........").lower()

str1 = clear_text

print("Your encrypted text is...........", codecs.encode(clear_text, 'rot_13'))

print("Thank you very much for utilizing our site!")