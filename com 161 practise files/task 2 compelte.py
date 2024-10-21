#full discoloure im going to have a brain anuyrism becasue of this
eyecolor = []
age = []
def main():
    file = open('eye.txt', 'r')
    read = file.readlines()
 
#splits the list sepereateed by the commas 
#each side of the txt file is appeneded into 
#a differnt list
    for i in read:
       split_list = i.split(",")
       age.append(split_list[1].rstrip('\n'))
       eyecolor.append(split_list[0].rstrip('\n'))
#holy shit just delete the first entry into the list 
#i cant figure out how to just not read a line 
    del age[0]
    del eyecolor[0]
    
#convert str to int so i can move on with my life
#why was this so hard    
    truage = list(map(int, age))
    total = sum(truage)
    lenght = len(age)
    average_age = float(total/lenght)
    formatted = format(average_age, '.1f')

    print(formatted)

#working out the second part of the question i misread it and wasted an hour :(
    countblue = eyecolor.count('blue')
    blueper = (countblue/lenght)
    print(blueper)

    counthazel = eyecolor.count('hazel')
    hazelper = (counthazel/lenght)
    print(hazelper)

    countbrown = eyecolor.count('brown')
    brownper = (countbrown/lenght)
    print(brownper)
    
    countgreen = eyecolor.count('green')
    greenper = (countgreen/lenght)
    print(greenper)
    
main()



