def ex1(arr):
    for num in arr:
        if num in arr and -num not in arr:
            return num

print(ex1([1, -1, 2, -2, -3, 3, -52]))

my_list = [1, -1, 2, -2, -3, 3, -52]
my_list[3] =5
my_dict = {"h":1, "p":2}
my_dict.update({"h":2, "p":8})
print(my_dict)
my_set = {1,2,3,4,5}
my_set.discard(8)
my_list = [x**2 for x in range(1,11) ]
print(my_list)