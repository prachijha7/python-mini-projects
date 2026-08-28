import random
print(r'''  _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
      ''')

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list =[
"apple","banana","camel","dog","elephant","forest","garden","house","island","jungle",
"kite","lemon","mountain","notebook","ocean","pencil","queen","river","sun","tree",
"umbrella","village","water","xylophone","yacht","zebra","air","ball","cat","door",
"egg","fish","goat","hat","ice","juice","king","lion","moon","nest",
"orange","parrot","quiet","rain","snake","tiger","unit","van","wolf","yak",
"ant","bread","chair","desk","earth","feather","glass","hill","iron","jar",
"key","lamp","milk","night","oil","paper","question","road","stone","table",
"user","voice","window","box","yellow","zero","actor","beach","cloud","dance",
"energy","fire","gold","heart","idea","jewel","knife","light","magic","noise",
"order","plant","quick","rock","salt","time","use","value","wind","zone",
"angle","brush","circle","dream","event","field","group","horse","image","joke",
"knife","level","model","north","offer","point","quote","range","shape","track",
"unity","visit","world","youth","zone","author","bridge","camera","design","engine",
"family","growth","health","input","judge","knowledge","leader","market","nature","object",
"power","result","system","travel","update","vision","wealth","year","zone","artist",
"battle","center","detail","effect","future","ground","honor","impact","journey","lesson",
"memory","number","option","people","quality","reason","school","theory","union","victory",
"winner","yesterday","zoo","adventure","balance","culture","decision","effort","freedom","goal",
"habit","income","justice","kindness","language","moment","network","opinion","purpose","respect",
"skill","talent","understand","value","wisdom","youthful","zeal"
]
chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(f"Word to guess: {placeholder}")

game_over = False
correct_letters =[]
lives = 6
while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display =""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        print(f"****************************{lives}/6 LIVES LEFT****************************")
        if lives == 0:
            game_over = True
            print(stages[0])
            print(f"****************************IT WAS {chosen_word}! YOU LOSE****************************")
    else:
        print(stages[lives])
        
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
