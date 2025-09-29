largest_number = -99999999
counter = 0

while True:
    number = int(input(55))
    if number ==-1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

    if counter != 0: 
        print("The largest number is", largest_number)
    else:
        print("you haven't enter any number.")


# programe a vowel eater using the for and in with continue
user_word = input("Gregory:")
user_word = user_word.upper()
for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)

    word = "python"
for letter in word:
    print(letter, end="*")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)