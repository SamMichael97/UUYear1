def task2():
    eyecolour = []
    age = []
    haage = 0
    blage = 0
    brage = 0
    grage = 0
    hacount = 0
    blcount = 0
    brcount = 0
    grcount = 0


    file = open('optometry.txt', 'r')
    read = file.readlines()

    for things in read:
        splitlist = things.split(",")
        eyecolour.append(splitlist[0].rstrip('\n'))
        age.append(splitlist[1].rstrip('\n'))
        if splitlist[0] == 'green':
            grage += int(splitlist[1])
            grcount += 1
        elif splitlist[0] == 'blue':
            blage += int(splitlist[1])
            blcount += 1
        elif splitlist[0] == 'brown':
            brage += int(splitlist[1])
            brcount += 1
        elif splitlist[0] == 'hazel':
            haage += int(splitlist[1])
            hacount += 1

    del eyecolour[0]
    del age[0]
    intage = list(map(int, age))
    # the tuple created is immutable so if i need to do
    # shit with it i need to change it
    tup = [(eyecolour[i], intage[i]) for i in range(0, len(eyecolour))]
    hazelper = (eyecolour.count('hazel') / len(eyecolour)) * 100
    blueper = (eyecolour.count('blue') / len(eyecolour)) * 100
    greenper = (eyecolour.count('green') / len(eyecolour)) * 100
    brownper = (eyecolour.count('brown') / len(eyecolour)) * 100

    totalaverageage = sum(intage)/len(intage)
    print(grage/grcount, haage/hacount, brage/brcount, blage/blcount)
    print(hazelper, blueper, greenper, brownper)
    print(totalaverageage)



task2()