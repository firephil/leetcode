def isAnagramAll(s: str, t: str) -> bool:
    
    return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy')

if __name__ == "__main__" :
    print(isAnagramAll("abc", "cba"))