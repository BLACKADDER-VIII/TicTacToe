from kivy.app import App
from kivy.uix.widget import Widget



class myApp(App):
    def build(self):
        return mygridlayout()
class mygridlayout(Widget):
    turn = 2
    def add_signaa(self):
        if self.turn%2 == 0:
            val = "O"
            self.ids.aa.text = "O"
            self.turn += 1
        else:
            val = "X"
            self.ids.aa.text = "X"
            self.turn += 1
        if self.has_won() == True:
            statement = "Victory for:" + val
            self.ids.main_disp.text = statement

    def add_signab(self):
        if self.turn%2 == 0:
            val = "O"
            self.ids.ab.text = "O"
            self.turn += 1
        else:
            val = "X"
            self.ids.ab.text = "X"
            self.turn += 1
        if self.has_won() == True:
            statement = "Victory for:" + val
            self.ids.main_disp.text = statement
    def add_signac(self):
        if self.turn%2 == 0:
            val = "O"
            self.ids.ac.text = "O"
            self.turn += 1
        else:
            val = "X"
            self.ids.ac.text = "X"
            self.turn += 1
        if self.has_won() == True:
            statement = "Victory for:" + val
            self.ids.main_disp.text = statement
    def add_signba(self):
        if self.turn%2 == 0:
            val = "O"
            self.ids.ba.text = "O"
            self.turn += 1
        else:
            val = "X"
            self.ids.ba.text = "X"
            self.turn += 1
        if self.has_won() == True:
            statement = "Victory for:" + val
            self.ids.main_disp.text = statement
    def add_signbb(self):
        if self.turn%2 == 0:
            val = "O"
            self.ids.bb.text = "O"
            self.turn += 1
        else:
            val = "X"
            self.ids.bb.text = "X"
            self.turn += 1
        if self.has_won() == True:
            statement = "Victory for:" + val
            self.ids.main_disp.text = statement
    def add_signbc(self):
        if self.turn%2 == 0:
            val = "O"
            self.ids.bc.text = "O"
            self.turn += 1
        else:
            val = "X"
            self.ids.bc.text = "X"
            self.turn += 1
        if self.has_won() == True:
            statement = "Victory for:" + val
            self.ids.main_disp.text = statement
    def add_signca(self):
        if self.turn%2 == 0:
            val = "O"
            self.ids.ca.text = "O"
            self.turn += 1
        else:
            val = "X"
            self.ids.ca.text = "X"
            self.turn += 1
        if self.has_won() == True:
            statement = "Victory for:" + val
            self.ids.main_disp.text = statement
    def add_signcb(self):
        if self.turn%2 == 0:
            val = "O"
            self.ids.cb.text = "O"
            self.turn += 1
        else:
            val = "X"
            self.ids.cb.text = "X"
            self.turn += 1
        if self.has_won() == True:
            statement = "Victory for:" + val
            self.ids.main_disp.text = statement
    def add_signcc(self):
        if self.turn%2 == 0:
            val = "O"
            self.ids.cc.text = "O"
            self.turn += 1
        else:
            val = "X"
            self.ids.cc.text = "X"
            self.turn += 1
        if self.has_won() == True:
            statement = "Victory for:" + val
            self.ids.main_disp.text = statement

    def has_won(self):
        count = 0
        if self.ids.aa.text == self.ids.ab.text == self.ids.ac.text != "":
            count += 1
        if self.ids.ba.text == self.ids.bb.text == self.ids.bc.text != "":
            count += 1
        if self.ids.ca.text == self.ids.cb.text == self.ids.cc.text != "":
            count += 1
        if self.ids.aa.text == self.ids.ba.text == self.ids.ca.text != "":
            count += 1
        if self.ids.ab.text == self.ids.bb.text == self.ids.cb.text != "":
            count += 1
        if self.ids.ac.text == self.ids.bc.text == self.ids.cc.text != "":
            count += 1
        if self.ids.aa.text == self.ids.bb.text == self.ids.cc.text != "":
            count += 1
        if self.ids.ac.text == self.ids.bb.text == self.ids.ca.text != "":
            count += 1
        if count == 1:
            return True


myApp().run()


