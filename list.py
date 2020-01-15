print("type:")
print("a: append")
print("i: insert")
print("r: remove")
stuff = []
while True:
    v = input("so, what do you want? ")
    if v == '':
        break
    elif v == 'a':
        stuff.append(input("value: "))
    elif v == 'i':
        stuff.insert(int(input("index: ")), input("value: "))
    elif v == 'r':
        r = input("value: ")
        if r in stuff:
            stuff.remove(r)
        else:
            print("value not found")

for index, value in enumerate(stuff):
    print("index " + str(index) + " with value > " + value)