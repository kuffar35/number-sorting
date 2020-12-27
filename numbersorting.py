def window1():
    print("click -1 for finish")
    numbers=0
    liste = []
    while numbers!=-1:
     numbers = int(input("please enter your number"))
     if numbers != -1:
      liste.append(numbers)

    liste2=[]

    max = 0
    print(liste)
    while len(liste) > 0:
     for i in range(0,len(liste)):
        if(liste[i]>max):
             max=liste[i]
             index=i
     liste2.append(max)
     liste.pop(index)

     index=0
     max=0
    print(liste2)
window1()
