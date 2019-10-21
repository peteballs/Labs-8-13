def main():
    total = int(input('Please enter the total dollar amount in pennies: '))

    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    nQuarters = total // quarter
    quarter_remainder = total % quarter

    nDimes = quarter_remainder // dime
    dime_remainder = quarter_remainder % dime

    nNickels = dime_remainder // nickel
    nickel_remainder = dime_remainder % nickel

    nPennies = nickel_remainder // penny

    print(f'\nyou have {.25 * nQuarters + .10 * nDimes + 0.05 * nNickels + 0.01 * nPennies}')
    print(f'you have {nQuarters} quarters, {nDimes} dimes, {nNickels} nickels, and {nPennies} pennies\n')
    print(f"Thank you, it was great working with you, {user_name}!")

print("Welcome to the US Coin Changer Site!")
print(f"\nThis is a wonderful opportunity to test your basic mathematics skills and to learn how to make change in real life.")

print(f"\nThis is a great game for children and a wonderful manner to train employees who may be working with cash.")
print(f"\nThis is such a lost art in our culture these days! Let's do what we can to change it!!")

user_name = input(f"\nWhat is your name, by the way, before we get started? I did not mean to be so rude, Sincerely apologize, let's get started!......")
print(f"\nHello {user_name}, it is my pleasure to meet you!")

main()
