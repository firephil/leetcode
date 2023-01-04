# Based on Hack method from LeetCode,  fastest method in Python

# https://www.w3schools.com/python/ref_func_all.asp

# https://docs.python.org/3/library/functions.html#all

def isAnagram(s :str, t: str) -> bool:

    return all(s.count(x) == t.count(x) for x in tmp)

if __name__ == "__main__" :
    print(isAnagram("abc", "cba"))