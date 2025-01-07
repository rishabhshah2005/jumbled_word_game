import random

def jumble_word(word):
    res = ""
    for i in range(len(word)):
        r = random.randrange(0, len(word))
        res += word[r]
        word = word[:r] + word[r+1:]

    return res

def check_correctness(word, ans):
    res = ""
    for i in range(len(word)):
        if word[i]==ans[i]:
            res+=word[i]
        else:
            res+="_"

    return res

def filt(x):
    if len(x)<=5:
        return True
    else:
        return False

with open("wordlist.txt") as f:
    wordlist = f.readlines()
    wordlist = [word.strip() for word in wordlist]
    wordlist = list(filter(filt, wordlist))
    l = len(wordlist)

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
