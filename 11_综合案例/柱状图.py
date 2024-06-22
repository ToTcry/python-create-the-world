


#排序，基于带名函数
def choose_sort_key(element):
return element[1]
my_list.sort(key=choose_sort_key,reverse=True)
print(my_list)