"""
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""

def filter_list(l):
    ret_list = []
    for i in range(len(l)):
        elem_string = l[i]
        if(not isinstance(l[i], str)):
            ret_list.append(l[i])
    'return a new list with the strings filtered out'
    return ret_list

ex_list = [1, 2, 'str1', 'a', 1340]

""" print(range(len(ex_list)))

for i in range(len(ex_list)):
    print(isinstance(ex_list[i],str)) """

result_list = filter_list(ex_list)

print(result_list)