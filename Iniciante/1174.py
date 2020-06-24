values = []

for i in range(100):
    n = float(input())
    if (n <= 10):
        val = {"i": i,"value": n}
        values.append(val)

for item in values:
    print ("A[{}] = {}".format(item["i"],item["value"]))
