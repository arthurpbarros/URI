k = int(input())
res = "Top "
if (k <= 1):
    res += "1"
elif (k <= 3):
    res += "3"
elif (k <= 5):
    res += "5"
elif (k <= 10):
    res += "10"
elif (k <= 25):
    res += "25"
elif (k <= 50):
    res += "50"
elif (k <= 100):
    res += "100"

if (len(res) > 4):
    print (res)
