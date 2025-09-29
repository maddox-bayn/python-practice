my_list = [8, 10, 6, 2, 4]
swapped = True
 
while swapped:
    swapped = False
    for i in range(len(my_list) -1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)  

    
my_list = []
swapped = True
num = int(input("how many element do u wan to sort"))
for i in range(num):
    val = float(input("enter a list element:"))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nsorted") 
print(my_list) 
_     

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(list_1)):
    found = list_1[i] == to_find
    if found:
        break

if found:
    print("element found at index")
else:
    print("absent")    


drawn = [5, 11, 9, 42, 3, 49,]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1
print(hits)