class board_matrix:
    def __init__(self):
        self.dict1 = {(1,1):"",(1,2):"",(1,3):"",(2,1):"",(2,2):"",(2,3):"",(3,1):"",(3,2):"",(3,3):""}     #Initializes this dictionary every time a new class instance is run
    def play(self):
        turn = 2
        while True:
            if turn%2 == 0:
                val = "O"
            else:
                val = "X"
            turn += 1  #uses the turn variable to toggle between X & O as it varries between odd and even
            print("Turn of:", val)
            key = input()
            self.update(key,val)    #updates the dict1 class variable to change the build
            self.build()
            if self.win() == True:
                print(val, "wins")
                return 0;
    def build(self):
        a = self.dict1[(1,1)]
        b = self.dict1[(1,2)]
        c = self.dict1[(1, 3)]
        d = self.dict1[(2, 1)]
        e = self.dict1[(2, 2)]
        f = self.dict1[(2, 3)]
        g = self.dict1[(3, 1)]
        h = self.dict1[(3, 2)]
        i = self.dict1[(3, 3)]
        print(a,"|",b,"|",c,"\n",d,"|",e,"|",f,"\n",g,"|",h,"|",i)
    def update(self,key,val):
        self.dict1.update({key:val})
    def win(self):
        for i in range(1,4):
            if self.dict1[i,1] == self.dict1[i,2] == self.dict1[i,3] != "":
                return True
            elif self.dict1[1,i] == self.dict1[2,i] == self.dict1[3,i] != "":
                return True
            elif self.dict1[1,1] == self.dict1[2,2] == self.dict1[3,3] != "":
                return True
            elif self.dict1[3,1] == self.dict1[2,2] == self.dict1[1,3] != "":
                return True

b = board_matrix()
b.play()





