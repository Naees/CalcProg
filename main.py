from tkinter import *

smallFont = ("Constantia",16, )
bigFont = ("Constantia",40, "bold")
bannerColor = "#2b2b2b"
totalExpressionBg = "#404040"
currentExpressionBg ="#3d3d3d"
frameBg = "#383838"
btnBg = "#454545"

class Calculator:
    def __init__(self):
        self.calcWin = Tk()
        self.calcWin.geometry("500x500")
        self.calcWin.resizable(0,0)
        self.calcWin.title("Naees's Simple Calculator Programming Challenge")
        
        self.ttlExpression = ""
        self.currentExpression = ""
        self.displayFrame = self.create_display_frame()
        
        self.ttlLbl, self.lbl = self.create_display_lbl()
        
        
        self.digits={
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            0:(4,1), '.':(4,2)
            
        }
        
        self.operators = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        
                
        self.btnFrame = self.create_display_frame()
        
        self.btnFrame.rowconfigure(0, weight=1)
        
        # size the btnFrame properly
        for x in range (1,5):
            self.btnFrame.rowconfigure(x,weight=1)
            self.btnFrame.columnconfigure(x,weight=1)
        
        # self.operators = {
        #     '+': (1, 4), '-': (2, 4),
        #     '*': (3, 4), '/': (4, 4),
        #     'C': (1, 5), '<': (2, 5),
        #     '%': (3, 5), '√': (4, 5),
        #     'x²': (1, 6), 'π': (2, 6),
        #     '%' : (4,3)
        # }
        
        # create btn        
        
        self.create_value_btns()
        self.create_operator_btns()
        
        self.clearBtn()
        self.equalsBtn()
        
        self.openBracketBtn()
        self.closeBracketBtn()
        
        self.ModulusDivideBtn()
        self.PiBtn()
        self.RootBtn()
        self.SquareBtn()
        # self.percentageBtn()
        self.clearEntryBtn()
        self.bindKeys()
        
    # display frame creation
    def create_display_frame(self):
        frame = Frame(self.calcWin, height=222, bg=frameBg)
        frame.pack(expand=True, fill="both")
        return frame
    
    def bindKeys(self):
        self.calcWin.bind("<Return>", lambda event: self.equals())
        self.calcWin.bind("<KP_Enter>", lambda event: self.equals())
        print()
        for key in self.digits:
            self.calcWin.bind(str(key), lambda event,digit=key: self.add_to_expressions(digit))
            
        for key in self.operators:
            self.calcWin.bind(key, lambda event, operator=key: self.inputOperator(operator))
            
        self.calcWin.bind("<KP_Decimal>", lambda event: self.add_to_expressions('.'))
        self.calcWin.bind("<KP_0>", lambda event: self.add_to_expressions('0'))
        self.calcWin.bind("<KP_1>", lambda event: self.add_to_expressions('1'))
        self.calcWin.bind("<KP_2>", lambda event: self.add_to_expressions('2'))
        self.calcWin.bind("<KP_3>", lambda event: self.add_to_expressions('3'))
        self.calcWin.bind("<KP_4>", lambda event: self.add_to_expressions('4'))
        self.calcWin.bind("<KP_5>", lambda event: self.add_to_expressions('5'))
        self.calcWin.bind("<KP_6>", lambda event: self.add_to_expressions('6'))
        self.calcWin.bind("<KP_7>", lambda event: self.add_to_expressions('7'))
        self.calcWin.bind("<KP_8>", lambda event: self.add_to_expressions('8'))
        self.calcWin.bind("<KP_9>", lambda event: self.add_to_expressions('9'))
            
    # display label creation
    def create_display_lbl(self):
        ttlLbl = Label(self.displayFrame, text=self.ttlExpression, anchor=E, bg=totalExpressionBg, fg="#d3d8da", font=smallFont)    
        ttlLbl.pack(expand=True, fill="both")
        
        lbl = Label(self.displayFrame, text=self.currentExpression, anchor=E, bg=currentExpressionBg, fg="#d3d8da", font=bigFont)    
        lbl.pack(expand=True, fill="both")
        
        return ttlLbl, lbl
    
    def add_to_expressions(self, value):
        self.currentExpression += str(value)
        self.update_current_Lbl()
        
    
    # Number button creation
    def create_value_btns(self):
        for digits,grid_value in self.digits.items():
            valueBtns = Button(self.btnFrame, text=str(digits), bg=btnBg, fg="white", font=smallFont, borderwidth=0, highlightthickness=0, command=lambda x=digits: self.add_to_expressions(x))
            valueBtns.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)
    
    def inputOperator(self, operator):
        self.currentExpression += operator
        self.ttlExpression += self.currentExpression
        self.currentExpression = ""
        self.update_ttl_Lbl()
        self.update_current_Lbl()
    
    # Number button frame creation
    def create_buttons_frame(self):
        frame = Frame(self.calcWin)
        frame.pack(expand=True, fill="both")
        return frame
    
    def update_ttl_Lbl(self):
        # Change operator symbols to more readable symbols
        expression = self.ttlExpression
        for ops, sym in self.operators.items():
            expression = expression.replace(ops, f' {sym} ')
        self.ttlLbl.config(text=expression)
        
        # change the text of the lbl
        self.ttlLbl.config(text=expression)
    
    def update_current_Lbl(self):
        # change the text of the lbl
        self.lbl.config(text=self.currentExpression[:11]) # limits the length due to overrun
    
    # Operator button creation
    def create_operator_btns(self):
        i = 0
        for operator, symbol in self.operators.items():
            btn = Button(self.btnFrame, text=symbol, bg=btnBg, fg="#dce3e2", font=smallFont, borderwidth=0, highlightthickness=0, command= lambda x=operator:self.inputOperator(x) )
            btn.grid(row=i, column=4, sticky=NSEW)
            i+=1
    
    # Clear button creation (C)
    def clear(self):
        self.currentExpression = ""
        self.ttlExpression = ""
        self.update_current_Lbl()
        self.update_ttl_Lbl()
    
    def clearBtn(self):
        btn = Button(self.btnFrame, text="C", bg="#f04b51", fg="#dce3e2", font=smallFont, borderwidth=0, highlightthickness=0, command=self.clear)
        btn.grid(row=0, column=1, sticky=NSEW)
        
    def clearEntry(self):
        self.currentExpression = ""
        self.update_current_Lbl()
        
    def clearEntryBtn(self):
        btn = Button(self.btnFrame, text="CE", bg=btnBg, fg="#dce3e2", font=smallFont, borderwidth=0, highlightthickness=0, command=self.clearEntry)
        btn.grid(row=0, column=2, sticky=NSEW)

        
    def equals(self):
        self.ttlExpression += self.currentExpression
        self.update_ttl_Lbl()
        
        try: # Exception handling
            self.currentExpression = str(eval(self.ttlExpression))
            self.ttlExpression = ""
        except Exception as e:
            if str("(") in self.ttlExpression:
                self.ttlExpression += str(")")
                self.clearEntry()
                self.update_ttl_Lbl()
                self.equals()
            else:
                
                self.currentExpression = "Invalid"
        finally:
            self.update_current_Lbl()
    
    # Equals button creation (=)
    def equalsBtn(self):
        btn = Button(self.btnFrame, text="=", bg="#6db442", fg="#dce3e2", font=smallFont, borderwidth=0, highlightthickness=0, command=self.equals)
        btn.grid(row=3, column=5, rowspan=2, stick=NSEW)
    
    # Brackets button creation
    def openBracket(self):
        self.currentExpression += str("(")
        self.update_current_Lbl()
    def openBracketBtn(self):
        btn = Button(self.btnFrame, text="(", bg=btnBg, fg="#dce3e2", font=smallFont, borderwidth=0, highlightthickness=0, command=self.openBracket)
        btn.grid(row=4, column=3, stick=NSEW)   
        
    def closeBracket(self):
        self.currentExpression += str(")")
        self.update_current_Lbl() 
    def closeBracketBtn(self):
        btn = Button(self.btnFrame, text=")", bg=btnBg, fg="white", font=smallFont, borderwidth=0, highlightthickness=0, command=self.closeBracket)
        btn.grid(row=4, column=4,stick=NSEW)

    # Special Functions button creation
    def ModulusDivideBtn(self):
        btn = Button(self.btnFrame, text="MOD", bg=btnBg, fg="white", font=smallFont, borderwidth=0,highlightthickness=0)
        btn.grid(row=0, column=3,stick=NSEW)
    def PiBtn(self):
        btn = Button(self.btnFrame, text="π", bg=btnBg, fg="white", font=smallFont, borderwidth=0, highlightthickness=0)
        btn.grid(row=0, column=5,stick=NSEW)
        
    def Root(self):
        self.currentExpression = str(eval(f"{self.currentExpression}**0.5"))
        self.update_current_Lbl()
        
    def RootBtn(self):
        btn = Button(self.btnFrame, text="√", bg=btnBg, fg="white", font=smallFont, borderwidth=0, highlightthickness=0, command=self.Root)
        btn.grid(row=1, column=5,stick=NSEW)
    
    def square(self):
        self.currentExpression = str(eval(f"{self.currentExpression}**2"))
        self.update_current_Lbl()
    
    def SquareBtn(self): # unicode for square is "x\u00b2"
        btn = Button(self.btnFrame, text="x²", bg=btnBg, fg="white", font=smallFont, borderwidth=0, highlightthickness=0, command=self.square)
        btn.grid(row=2, column=5,stick=NSEW)
    
    # Percentage button creation (%)
    # def percentageBtn(self):
    #     btn = Button(self.btnFrame, text="%", bg=btnBg, fg="white", font=smallFont, borderwidth=0, highlightthickness=0)
    #     btn.grid(row=4, column=3,stick=NSEW)
    
    # run the program
    def run(self):
        self.calcWin.mainloop()
    
    # additional functions for brainstorming
    def onPress(self, input):
        pass
    def Backspace(self, ):
        pass


# run in terminal
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
