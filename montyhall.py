import random


switch = False
games =1000000

winningDoor = random.randint(0, 2)

wins = 0

for i in range(games):
	doorPick =random.randint(0,2)
	if(doorPick == winningDoor):
		wins +=1
	else:
		secondPick = doorPick
		if switch:
			while secondPick == doorPick:
				secondPick = random.randint(0,2)
		if secondPick == winningDoor:
			wins +=1

print 'Non switch wins : %s' % wins

switch = True

winningDoor = random.randint(0, 2)

wins = 0

for i in range(games):
	doorPick =random.randint(0,2)
	if(doorPick == winningDoor):
		wins +=1
	else:
		secondPick = doorPick
		if switch:
			while secondPick == doorPick:
				secondPick = random.randint(0,2)
		if secondPick == winningDoor:
			wins +=1

print 'Switch wins : %s' % wins