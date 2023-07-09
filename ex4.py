"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, 
containing distinct letters - each taken only once - coming from s1 or s2.

EXAMPLES:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

"""

def longest(a1, a2):
    compare_str = "abcdefghijklmnopqrstuvwxyz"
    result_str = ""

    for i in range(len(compare_str)):
        cond = False
        for j in range(len(a1)):
            if a1[j] == compare_str[i]:
                result_str = result_str + compare_str[i]
                cond = True
                break
        if cond == False:
            for k in range(len(a2)):
                if a2[k] == compare_str[i]:
                    result_str = result_str + compare_str[i]
                    break
            
    return result_str


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

expected_str = "abcdefklmopqwxy"
result_str = longest(a, b)

if(result_str == expected_str):
    print("GOOD JOB! The result and expected strings match!")
else:
    print("ERROR! The result and expected string do not match!")

