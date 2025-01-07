import random

MAX_LEN = 5
TRIES = 3

def jumble_word(word):
    res = ""
    for i in range(len(word)):
        r = random.randrange(0, len(word))
        res += word[r]
        word = word[:r] + word[r+1:]

    return res

def select_difficulty():
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    global MAX_LEN
    global TRIES
    while True:
        ans = input("Select difficulty: ")
        if ans=="1":
            MAX_LEN = 5
            TRIES = 3
            break
        elif ans=="2":
            MAX_LEN = 7
            TRIES = 3
            break
        elif ans == "3":
            MAX_LEN = 10
            TRIES = 5
            break
        else:
            print("Select correct index!!")
    

def check_correctness(word, ans):
    res = ""
    for i in range(len(word)):
        if word[i]==ans[i]:
            res+=word[i]
        else:
            res+="_"

    return res

def filt(x, m):
    if len(x)==m:
        return True
    else:
        return False


with open("wordlist.txt") as f:
    select_difficulty()
    wordlist = f.readlines()
    wordlist = [word.strip() for word in wordlist]
    wordlist = list(filter(lambda x: filt(x, MAX_LEN), wordlist))
    # print(wordlist)
    l = len(wordlist)

while True:
    rand_word = wordlist[random.randrange(0, l)]
    jumbled = jumble_word(rand_word)

    print(jumbled)
    for i in range(3):
        ans = input("Enter your answer: ")
        if ans==rand_word:
            print("Correct!")
            break
        else:
            print(check_correctness(ans, rand_word))
    else:
        print("Game Over!")
    
    again = input("Do you want to play again??(y/n)")
    if again =="y":
        continue
    else:
        break
