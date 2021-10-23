import random

from hangman_art import stages
from hangman_words import word_list
from hangman_art import logo

print(logo)

chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

word_length = len(chosen_word)
display = []
game_over = True

lives = 6

for n in range(word_length):    # listeye kelime uzunluğu kadar "_" ekler.
    display.append("_")

while game_over == True:

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length): # Bu for döngüsü tahmin edilen harfle, seçilen kelimenin her harfini kontrol eder. 
        letter = chosen_word[position]  # Eşleşen "_" ler harfe dönüşür.
        if letter == guess:           
            display[position] = guess

    if "_" not in display:
        game_over = False   # Hiç "_" kalmadığında tüm harfleri bilmiş olur ve kazanır.
        print("You Won")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:          # her yanlış tahmin yaptığında 1 canı gider ve 0 olunca ölür.
            game_over = False
            print("You Lose")

    print(stages[lives])    # 

    print(display)