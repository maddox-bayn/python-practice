guest_list = ["Albert Einstian", "Elon Musk", "jeff Besiuse"]

print(f"Hello {guest_list[0]}. you are invited for dinner.")
print(f"Hello {guest_list[1]}. you are invited for dinner.")
print(f"Hello {guest_list[2]}. you are invited for dinner.")

print(f"{guest_list[1]} can not make it unforturnatly")

guest_list[1] = "Thomos Edison"

print(f"Hello {guest_list[0]}. you are invited for dinner.")
print(f"Hello {guest_list[1]}. you are invited for dinner.")
print(f"Hello {guest_list[2]}. you are invited for dinner.")


print("we have found bigger dinnner table ") 

guest_list.insert(0, "Maddox Bayn")
guest_list.insert(2, "Mega Elite")
guest_list.append("King joe")

print(guest_list)

print(f"Hello {guest_list[0]}. you are invited for dinner.")
print(f"Hello {guest_list[1]}. you are invited for dinner.")
print(f"Hello {guest_list[2]}. you are invited for dinner.")
print(f"Hello {guest_list[3]}. you are invited for dinner.")
print(f"Hello {guest_list[4]}. you are invited for dinner.")
print(f"Hello {guest_list[5]}. you are invited for dinner.") 
 
print("we can only invite 2 people for dinner")

uninvited_guest = guest_list.pop()
print(f"Hello {uninvited_guest}. unfortunatly we have to uninvite you")
uninvited_guest = guest_list.pop()
print(f"Hello {uninvited_guest}. unfortunatly we have to uninvite you")
uninvited_guest = guest_list.pop()
print(f"Hello {uninvited_guest}. unfortunatly we have to uninvite you")
uninvited_guest = guest_list.pop()
print(f"Hello {uninvited_guest}. unfortunatly we have to uninvite you")

print(f"Hello {guest_list[0]}. you are invited for dinner.")
print(f"Hello {guest_list[1]}. you are invited for dinner.")

del guest_list[1]
del guest_list[0] 

print(guest_list)
