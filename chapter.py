bicycle = ("mulk", "redline", "maddox")

message = f"my first bicycle was {bicycle[2].title()}"
print(message)
i = 0 
while i < 100:
    i += 1
 

 
for i in range(2, 8, 3):
    print("the value  of i is currently", i)


    power = 1
for expo in range(16):
    print("2 to the power of", expo)
    power *= 2 

  print("the break instruction")
for i in range(1, 6):
    if i ==3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")
   

print("\nThe continue instruction")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")   