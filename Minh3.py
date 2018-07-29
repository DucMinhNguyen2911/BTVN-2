sizes = [5,7,300,90,24,50,75]
print("Hello, my name is Minh and here are my sheep sizes")
print(sizes)
biggest = max(sizes)
print("Now my biggest sheep has size",biggest,"let's shear it")
print("After shearing,here is my flock")
sii= sizes.index(biggest)
sizes[sii] = 8
print(sizes)
s = 0
si = 0
siz = 0
print("Month",1,":")
for i in range(7):
    sizes[s] +=50
    s +=1
biggest = max(sizes)
print("One month has passes,now here is my flock")
print(sizes)
print("Now my biggest sheep has size",biggest,"let's shear it")
print("After shearing,here is my flock")
sii= sizes.index(biggest)
sizes[sii] = 8
print(sizes)
print("Month",2,":")
for i in range(7):
    sizes[si] +=50
    si +=1
biggest = max(sizes)
print("One month has passes,now here is my flock")
print(sizes)
print("Now my biggest sheep has size",biggest,"let's shear it")
print("After shearing,here is my flock")
sii= sizes.index(biggest)
sizes[sii] = 8
print(sizes)
print("Month",3,":")
for i in range(7):
    sizes[siz] +=50
    siz +=1
print("One month has passes,now here is my flock")
print(sizes)
total = sizes[0]+sizes[1]+sizes[2]+sizes[3]+sizes[4]+sizes[5]+sizes[6]
print("My flock has size in total:",total)
money = total *2
print("I would get",total,"*2$:",money,"$")


