import array

numbers = array.array('h',[-2,-1,0,1,2])
memv = memoryview(numbers)

print(len(memv))
memv_oct = memv.cast('B')
print(memv_oct.tolist())
print(memv_oct, memv_oct[5])
memv_oct[5] = 128
print(memv_oct.tolist())
print(numbers)
# memv_oct[6] = 2
# memv_oct[1] = 255
# memv_oct[0] = 0
# print(memv_oct.tolist())
# print(numbers)