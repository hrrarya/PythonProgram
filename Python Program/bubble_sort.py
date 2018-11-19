def  bubble_sort(list):

	#sorting item using swap

	for iter_num in range(len(list)-1,0,-1):
		for idx in range(iter_num):
			if list[idx]>list[idx+1]:
				temp = list[idx]
				list[idx] = list[idx+1]
				list[idx+1] = temp




list = [34,12,4,45,23,46,6,7,8]


bubble_sort(list)
print(list)