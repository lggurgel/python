pack = []

while True:
    beer = input("beer name: ")
    if beer == '':
        break
    pack.append(beer)


for index, item in enumerate(pack):
    print("Index " + str(index) + "in pack is: " + item)