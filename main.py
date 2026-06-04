#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================================
# MIT License
#
# Copyright (c) 2026 Snowy Collie
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================

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
