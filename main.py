from random_word import RandomWords
def print_word(r,gl):
    tmp_word=""
    for i in r:
        if i in gl:
            tmp_word+=i
        else:
            tmp_word+="*"
    return tmp_word
def __main__():
    rw = RandomWords().get_random_word()
    get_lst=[]
    attempts=len(set(rw))+3
    print("Welcome to Hangman!")
    while attempts>0 and print_word(rw,get_lst)!=rw:
        print("Your Word: {}　　Attempts Left: {}".format(print_word(rw,get_lst),attempts))
        if get_lst != []:
            print("Letters Guessed: {}".format(", ".join(get_lst)))
        attempts-=1
        guess=input("Guess a letter: ").lower()
        if guess in get_lst or len(guess)!=1 or not guess.isalpha():
            print("You already guessed that letter. Try again.")
            attempts+=1
        elif guess in rw:
            print("Good guess!")
            get_lst.append(guess)
        else:
            print("Wrong guess.")
            get_lst.append(guess)
    if print_word(rw,get_lst)==rw:
        print("Congratulations! You guessed the word: {}".format(rw))
    else:
        print("Game over! The word was: {}".format(rw))

if __name__ == "__main__":
    __main__()
