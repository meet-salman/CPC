n = int(input())

for _ in range(n):
    word = input()
    
    if len(word) > 10:
    
        fIdx = word[0]
        lIdx = word[len(word)-1]
        length = str(len(word)-2)
        
        print(fIdx + length + lIdx)
    else:
        print(word)