"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""

def array_diff(l1, l2):
    result_list = l1.copy()

    for i in range(len(l2)):
        for j in range(len(l1)):
            if l1[j] == l2[i] and l1[j] in result_list:
                result_list.remove(l1[j])
    return result_list

l1 = [-11, 4]
l2 = [16, -19, 16, -18, 15, 17, 1, 8, 14, -6, 16, 4, -19, -15, 4, 9, 13, 2, 5]

res = array_diff(l1, l2)

print(res)