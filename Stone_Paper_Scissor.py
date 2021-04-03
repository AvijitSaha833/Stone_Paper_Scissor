import random as rnd

class game():
    def __init__(self,comp,plr):
        self.comp=comp
        self.plr=plr
    def result(self):
        if self.comp==self.plr:
            return None
        elif self.comp==1:
            if self.plr==2:
                return True
            else:
                return False
        elif self.comp==2:
            if self.plr==3:
                return True
            else:
                return False
        elif self.comp==3:
            if self.plr==1:
                return True
            else:
                return False


def result():
    res=game(comp,plr)
    if res.result()==None:
        print("The game is tie!")
    elif res.result()==True:
        print("YOU WIN!!")
    else:
        print("COMPUTER WINS!!")

if __name__ == '__main__':
    print("Computers Turn : Stone(1),Paper(2),Scissor(3)\n")
    comp=rnd.choice([1,2,3])   # we can aslo use rnd.randint(1,3)
    plr=int(input("Your Turn : Stone(1),Paper(2),Scissor(3)\n"))
    l=["Stone","Paper","Scissor"]
    print(f"Copmuter Chose: {l[comp-1]}")
    print(f"You Chose: {l[plr - 1]}")
    result()
