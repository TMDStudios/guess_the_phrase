answer = 'this is the secret phrase'

my_answer_dictionary = {}
my_answer = ''
for i in range(len(answer)):
    if answer[i] == ' ':
        my_answer_dictionary.update({i: ' '})
        my_answer += ' '
    else:
        my_answer_dictionary.update({i: '*'})
        my_answer += '*'

guessed_letters = ''
count = 0
multiple_letters = False

print('Can you decipher the text?')
print(my_answer)

while count < 10:
    my_answer = ''
    if not multiple_letters:
        guess_answer = input("Guess the full text: ")
        if guess_answer == answer:
            print("You win!")
            break
        else:
            print("Incorrect guess")
    multiple_letters = False
    guess = input("Guess a letter: ")
    if len(guess) == 1:
        for i in range(len(answer)):
            if answer[i] == guess:
                my_answer_dictionary.update({i: guess})
        for i in my_answer_dictionary:
            my_answer += my_answer_dictionary[i]

        if my_answer == answer:
            print(my_answer)
            print("You win!")
            break

        if len(guessed_letters) == 0:
            guessed_letters += guess
        else:
            guessed_letters += ', ' + guess

        print(my_answer)
        print(f'Guessed letters: {guessed_letters}')

        count += 1
        if count < 10:
            print(f'{10 - count} guesses remaining')

    else:
        print('Please enter only one letter.')
        multiple_letters = True

print('Game Over')
