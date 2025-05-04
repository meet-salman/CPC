def process_string(str):
    temp = []

    for char in str:
        if char == "#":
            if temp:
                temp.pop()
        else:
            temp.append(char)
    
    return ''.join(temp)


a = "1#122#a#34#4"
b = "1a$####11#bc##23444##"

if process_string(a) == process_string(b):
    print(True)
else:
    print(False)