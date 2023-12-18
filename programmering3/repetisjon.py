#for-løkke 1
for tall in range(11):
    print(tall)

#for-løkke 2
y = 0
for x in range(101):
    y+=x

print(y)

#while løkker
o = 2
while o < 31:
    print(o)
    o += 2

#Funksjoner
def kul(a, b):
    print(a+b)
kul(a=5, b=7)


#Funksjoner 2
def gjennomsnitt():
    ting=[24, 873, 34, 4356, 12904, 35, 134, 21]
    result = sum(ting) /len(ting)
    print (result)
gjennomsnitt()



#Edgardo
def pizza():
    mel = 400
    vann = 450
    olje = 35
    egg=1
    tomat = 4
    ost = 350
    ingredienser=[mel, vann, olje, egg, tomat, ost]
    result = sum(ingredienser)
    print(result)
pizza()