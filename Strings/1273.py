rows = int(input())
vez = True
while (rows != 0):
    read = max_len = 0
    names = []
    while (read != rows):
        name = input()
        names.append(name)
        max_len = len(name) if len(name) > max_len else max_len
        read += 1
    read = 0
    if (vez):
        vez = False;
    else:
        print ()
    while (read != rows):
        for name in names:
            print ((max_len-len(name))*" "+name)
            read+=1
    rows = int(input())
    
