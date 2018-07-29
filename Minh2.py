items = ["T-shirt","Sweater"]
n = input("Welcome to our shop, what do you want (C, R, U, D)?")
if n == "R":
    text = "{0} {1}, {2}".format("Our items:" , *items,sep = ',')
    print(text)
elif n == "C":
    c = input("Enter new item: ")
    items.append(c)
    text = "{0} {1}, {2}, {3}".format("Our items:" , *items,sep = ',')
    print(text)
elif n == "U":
    u = int(input("Update position?"))
    new = input("New item?")
    items[u] = new
    text = "{0} {1}, {2}".format("Our items:" , *items,sep = ',')
    print(text)
elif n == "D":
    d = int(input("Delete position? "))
    del items[d]
    text = "{0} {1}".format("Our items:" , *items,sep = ',')
    print(text)


