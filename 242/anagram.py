def isAnagram (s1, s2):
    return sorted(s1) == sorted(s2)

if __name__ == "__main__" :
   print(isAnagram("abc", "cba"))