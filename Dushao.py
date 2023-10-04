import json
import random 


class Dushao:
    def __init__(self) -> None:
        self.words = json.load(open('data/words.json'))
        

    def start(self):
        # 
        print("please select a game mode")
        print("(1) words: eng -> chin")
        print("(2) words: chin -> eng")
        print("(3) phrases: eng -> chin")
        print("(4) phrases: chin -> eng\n")
        mode_selection = input("enter choice : ")

        match mode_selection:
            case "1":
                self.words_eng_chin()
            case "2":
                self.words_chin_eng()
            case "3":
                self.phrases_eng_chin()               
            case "4":
                self.phrases_chin_eng() 

    def words_eng_chin(self):
        # method for words: eng->chin
        rounds = int(input("\n\nhow many words would you like to practice? : "))
        selections = self.req(rounds, len(self.words))

        for i in range(1, rounds):
            word = self.words[str(selections[i])]
            print(word.word)
            guess = input(" : ")
            if guess == word["chararacter"]:
                print("correct")
            else:
                print("wrong")

    def req(self, n, m):
        if n == 0 or m == 0 or n > m + 1:
            return []
        
        r = []
        while len(r) < n:
            nm = random.randint(0, m)
            while nm in r:
                nm = random.randint(0,m)
            r.append(nm)
            
        return list(r)
    

def main():
    ds = Dushao()
    ds.start()

if __name__ == "__main__":
    main()