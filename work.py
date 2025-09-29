def pyramid_height(blocks):
    height = 0
    layer_blocks = 1
    
    while blocks >= layer_blocks:
        blocks -= layer_blocks
        height += 1 
        layer_blocks += 1 
num_blocks = 6 
print("the height of the pyramid is:", pyramid_height)



  
for i in range(1, 11):
    if i % 2 == 0:
        i //= 2
    else:
        i = 3 * i + 1
    print(i)   


var= 16 
var_right = var >> 1
var_left =  var << 3
print(var, var_right, var_left)

number = [10, 5, 7, 2, 1]
print(number)


number[0] = 111
print(number)

number[1] = number[4]
print(number)

print(len(number)) 