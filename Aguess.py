print("Welcome to my Geography Quiz!")

playing = input("Do yo want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Each correct answer is 1 point. There is a total of 7 questions. Be Prepared!")
score = 0

answer = input("What is an example of a Mid-Oceanic Ridge? ")
if answer.lower() == "the azores in north atlantic ocean":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

answer = input("What is an example of a Rift Valley? ")
if answer.lower() == "east african rift valley":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

answer = input("What is an example of a Oceanic Trench? ")
if answer.lower() == "mariana islands":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

answer = input("What is an example of a Fold Mountain? ")
if answer.lower() == "mount everest in the himalayas":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

hard = input("Now comes the harder questions, Ready? ")
if playing.lower() != "yes":
    quit()

answer = input("What is an example of an Earthquake incident in Japan? ")
if answer.lower() == "the great hanshin earthquake in kobe":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

answer = input("What is an example of a Erupted Volcano? ")
if answer.lower() == "the eyjafjallajokull volcano":
    print('Correct!')
    score += 1
else:
    print('Wrong!')

answer = input("What are the 3 effects that can be done to accelerates the process of Slab-Pull Force ? ")
if answer.lower() == "weight, gravity and momentum":
    print('Correct!')
    score += 1
else:
    print('Wrong!')



print("You got " + str(score) + " Questions Correct!")
print("You got " + str((score / 7) * 100) + "%.")


