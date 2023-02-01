## if you want, you can change the secret word!
secret = "movies"
already_typed = []
mistakes = 0

def draw(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

while True:
    letter = input("Type a letter: ")
    if len(letter) > 1:
        print("ERROR! Just one letter, try again!")
        continue
    already_typed.append(letter)
    word_so_far = ''
    for secret_letter in secret:
        if secret_letter in already_typed:
            word_so_far += secret_letter
        else:
          word_so_far += ' _ '
    if word_so_far == secret:
        print("Congrats, you won :)")
        break
    else:
        print("The secret word so far: ", word_so_far)
    if letter not in secret:
        mistakes += 1 
        draw(mistakes)
    if mistakes >= 7:
        print("You lost :(")
        print("The word was: ",secret)
        break
