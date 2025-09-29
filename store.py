# the while loop and the else branchise
i = 1 
while i > 5:
    print(i)
    i += 1
else:
    print("else:", i)

# the for loop and the else branch
i = 11
for i in range(2, 1):
    print(i)
else:
    print("else", i)  

beateles = []
print("step 1:", beateles)

beateles.append("John Lennon")
beateles.append("Paul Mccartney")
beateles.append("George Harrison")
print("step 2:", beateles)

for member in ["Stu Sutcliffe" "Pete Best"]:
    new_member = (f"Add {member} to the band:")
    beateles.append(new_member)
print("step 3:", beateles) 

del beateles [-2:]
print("step 4:", beateles)

beateles.insert(0, "Ringo starr")
print("step 5:", beateles)  

my_list = [8, 10, 6, 2, 4]

for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i -1], my_list[i]


 my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for number in my_list:
    if number not in  new_list:
        new_list.append(number)
print("original list:", my_list)
print("list with no duplication:", new_list)             
# 1 american mile = 1609.344 meter
# 1 american gallon = 3.785411784 liter
def liter_100km_to_mile_gallons(litre):
    gallon = litre / 3.785411784
    mile = 100 * 1000 / 1609.344
    return mile / gallon
def mile_gallon_to_liter_100km(mile):
    km100 = mile * 1609.344 / 1000 / 100
    litre = 3.785411784
    return litre / km100
print(liter_100km_to_mile_gallons(3.9))
print(liter_100km_to_mile_gallons(7.57))
print(liter_100km_to_mile_gallons(10))
print(mile_gallon_to_liter_100km(60.3))
print(mile_gallon_to_liter_100km(31.4))
print(mile_gallon_to_liter_100km(23.5))
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)