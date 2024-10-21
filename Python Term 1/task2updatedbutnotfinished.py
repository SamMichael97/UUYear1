def task2():
    eyecolour = []
    age = []


    file = open('optometry.txt', 'r')
    read = file.readlines()

    for things in read:
        splitlist = things.split(",")
        eyecolour.append(splitlist[0].rstrip('\n'))
        age.append(splitlist[1].rstrip('\n'))

    del eyecolour[0]
    del age[0]
    intage = list(map(int, age))
    # the tuple created is immutable so if i need to do
    #shit with it i need to change it
    tup = [(eyecolour[i], intage[i]) for i in range(0, len(eyecolour))]
    hazelper = (eyecolour.count('hazel')/len(eyecolour))*100
    blueper = (eyecolour.count('blue')/len(eyecolour))*100
    greenper = (eyecolour.count('green')/len(eyecolour))*100
    brownper = (eyecolour.count('brown')/len(eyecolour))*100

    htotal = 0

    for thing in tup:
        if tup[0] == 'hazel':
            htotal += tup[1]

        
    print(htotal)









    #die = dict(zip(eyecolour, intage))
    #print(die)





task2()

