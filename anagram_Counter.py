from collections import Counter

def isAnagramAll(s: str, t: str) -> bool:
    
    return Counter(s) == Counter(t)

if __name__ == "__main__" :

    print(isAnagramAll("abc", "cba"))