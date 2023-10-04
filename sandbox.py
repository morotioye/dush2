import json
import random

words = json.load(open('data/words.json'))

def req(n, m):
        if n == 0 or m == 0 or n > m + 1:
            return []
        
        r = []
        while len(r) < n:
            nm = random.randint(0, m)
            while nm in r:
                nm = random.randint(0,m)
            r.append(nm)
            
        return list(r)

rounds = int(input("\n\nhow many words would you like to practice? : "))
selections = req(rounds, len(words))
print(len(selections))
score = 0
for i in range(0, rounds):
    word = words[str(selections[i])]
    print(word["word"])
    guess = input("guess : ")
    if guess == word["character"]:
        print("correct")
        score +=1
    else:
         print("incorrect")

print(f"score: {score}/{rounds}")
