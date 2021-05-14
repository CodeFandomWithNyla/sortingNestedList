# Reversing the Foods and calories list
def Sort(sub_li): # this sorts the list according to 2nd elemnt of sublst
	l = len(sub_li)
	for i in range(0, l):
		for j in range(0, l-i-1):
			if (sub_li[j][1] < sub_li[j + 1][1]): # ascending order
				sub_li[j],sub_li[j + 1] = sub_li[j + 1], sub_li[j]

	return sub_li
# Main program
n = int(input("Enter the number of items you want to add in the menu\t"))
l=[]
for i in range(n): # taking menu items from user
    item1 = input("Food Item \t")
    calri = input("Calories \t")
    item = item1+","+calri
    m = list(item.split(","))
    l.append(m)
print(l)
l_asc = Sort(l) # using Sort function if user puts value randomly then it sorts it in ascending order
l_copy1 = l_asc[:] # making a copy so that original list remains original
# Inbuilt Method
l_dsc = l_copy1.reverse()
print("Using inbuilt method food item list is : ", l_dsc)
# Using string slicing trick
l_copy2 = l_asc[:] # making a copy so that original list remains original
l_dsc = l_copy2[::-1]
print("Using string slicing trick : ", l_dsc)
# Using swapping method
l_copy3 = l_asc[:] # making a copy so that original list remains original
l = len(l_copy3)
for i in range(0, l):
    for j in range(0, l - i - 1):
        if (l_copy3[j][1] > l_copy3[j + 1][1]):  # descending order
            l_copy3[j], l_copy3[j + 1] = l_copy3[j + 1], l_copy3[j]

print("Using Swapping method : ",l_copy3)