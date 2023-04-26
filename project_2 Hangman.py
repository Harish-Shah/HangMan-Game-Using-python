import random
movies = ["housefull four","bala","chichore","titinic","ujada chaman","The joya factor"]
name=input("Enter name: ")
print()
print("Welcome",name)
print()
totalturns=7
print("so let's get started")
print()
print("following are the rules of the game")
print()
print("you will be given "  +str(totalturns)+ " chances to get movie correctly")
print()
print("if u have guessed wrong character your turns will be deducted by 1 each time")
print()
print("OK...LET'S PLAY")
print()
print("type exit if not want to play")
print()
q="y"

while True:
    choosenletters = []
    random.shuffle(movies)
    movie = orgmovie = random.choice(movies).lower()
    #choice replace with shuffle due to repetation
    if q == "y" or q == "yes":
        turns = totalturns
        for i in movie :
            if i not in "aeiou " :
                movie = movie.replace(i, "-")
        print("Guess movie :",movie)
        while (turns>=1):
            guess = input("guess character :")
            guess=guess.lower()
            if(guess == "exit"):
                exit(0)
            if guess in orgmovie:
                for x in range(0,len(movie)):
                    if orgmovie[x] == guess:
                        guessmovie = list(movie)
                        guessmovie[x] = guess
                        movie = "".join(guessmovie)
                        print("you chosen correct character")
                        
            else:
                if guess in choosenletters:
                    print("This letter alredy choosen. try another one.")
                    continue
                choosenletters.append(guess)
                turns -= 1
                print("You have entered wrong word now your turn chance remains : " + str(turns))
            print(movie)
            if(movie==orgmovie):
                print("You won!!!!")
                break
        if(turns==0):
            print("Better luck next time!!!")
            print("correct word is: " + orgmovie.upper())
    q=input("wanna play hangman again?")
    q=q.lower()
    if(q!="y" and q!="yes"):
        break
                        



                
                
            


