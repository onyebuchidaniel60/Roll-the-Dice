#dice rolling game. This game simulates dice rolling
import tkinter
from random import*
from tkinter.messagebox import*

#GUI version of the dice game
comments=["6, you killed it", "6, higest score ever", " oops try again sir", "you scored low very low",
 " you tried, keep going to increase your score further", "that's moderate", "you rock", "repeat after me, 'you are a winner'"]

top= tkinter.Tk()
top.geometry('600x400')

    
inputval=tkinter.StringVar()
message="you have not entered a number "
errorMessage="please enter a valid number"
def useinput():
    try:
        
            yourinput=inputval.get()
            stat=randint(1,int(yourinput))
            if stat>6:
                randint(1,6)
            if stat>4:
                showinfo("score",comments[4])
            elif stat<=2:
                showinfo("score",comments[3])
            elif stat>=2:
                showinfo("score",comments[randint(4,5)])
            elif stat>=5:
                showinfo("score",comments[7])
            elif stat==6:
                showinfo("score",comments[random(0,1)])
            
    except:
        errortext=tkinter.Text(top, height=1,fg="red")
        errortext.pack()
        errortext.insert(tkinter.END,errorMessage)
        errortext['state']="disabled"
game=tkinter.Label(top,text="Dice Rolling Game")
game.pack()

instruction=tkinter.Text(top,height=3)
instruction.pack()
instruction.insert(tkinter.END,"This is game that simulates Dice rolling. In orderto play you need to enter a number which could be of any value, just not an alphabet")
instruction['state']="disabled"

inputfield=tkinter.Entry(top,textvariable=inputval)
inputfield.pack()

button=tkinter.Button(top,text="play",bg="blue",fg="white",command=useinput)
button.pack()
        
top.mainloop()

#button object should take an event handler function/commandoption that calls a function when the user presses the button.
#this function should take the value of the input from the entry field/input text field and call a random function that does something with this input value
#and outputs the user's score to the screen with comments

#command line version of the dicegame
try:
    rolldice=input("please enter play to roll dice")
    while rolldice.lower()!="play".lower():
        print("please enter play to roll dice")
except:
    print("something went wrong")

score=random.randint(1,6)
if score>4:
    print(comments[4])
elif score<=2:
    print(comments[3])
elif stat>=2:
    print(comments[randint(4,5)])
elif stat>=5:
    print(comments[7])
elif stat==6:
    print(comments[random(0,1)])
