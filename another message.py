largest_number = -99999999
counter = 0

number = int(input("5"))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("6"))

if counter:
    print("the largest number is", largest_number)
else:
    print("you haven't entered any number")





# using whie loop to creat a program and ask to enter a word, and chupacabra the secret exit word 
while True:
    word = input("Enter a word")
    if word == "Chupacabra":
        print("you've successfully left the loop")
        break    
