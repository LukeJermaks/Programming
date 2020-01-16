#Arrays v2

names = ["Rebecca", "Victoria", "David", "Jenny"]
score = [16, 23, 35, 41, 59, 68, 71, 83, 97]

print(score[1])

print(score[3:5]) #the : cuts the middle numbers out... but you already know that...

print(score[:5])  #yes... begining numbers until place 5 in the list.

print(score[4:])  #yes... end numbers from place 4 in the list.

score[0] = 12 #changes the code 

print(score[0])#prints it


TopPerformingPupils = score[5:]
print(TopPerformingPupils)

print(names[2], TopPerformingPupils[2])
