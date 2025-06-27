from tkinter import*
def buttonpress(num):
    global text1  #it will varible which is outside the function if we didnot put global there python will treat it as new local varible for function\
    text1+=str(num) #appending the argument to text1=""
    equation1.set(text1)#this update the stringVar() to new value 
def equalto():
    try:
        global text1
        result=str(eval(text1))
        equation1.set(result)
    except ZeroDivisionError:
        equation1.set("you divide with zero")                #error handling
        text1=""
    except SyntaxError:
        equation1.set("enter correctky")
        text1=""
def clear():
    global text1
    global equation1
    equation1.set("")
    text1="" #if we not change text1 it will show the previous stored string when type new open future we add backspace too lazy now
window=Tk()
window.title("calculator")
window.geometry("600x600")
text1=""    #created a empty string so it can hold number when which numberbutton is pressed
equation1=StringVar() #Tkinter class used to create a variable that holds a string //Store a string value //Be traced for changes
label=Label(window,textvariable=equation1,bg="white",width=90,height=5,font=('Arial,50,bold'),fg="black")
label.pack() #label is the area where widgets can hold there texts and images within window
frame=Frame(window) #we need frames to hold widgets like buttons images and etc
frame.pack()
button1=Button(frame,text="1",width=10,height=5,command=lambda:buttonpress(1))
button1.grid(row=0,column=0)
button2=Button(frame,text="2",width=10,height=5,command=lambda:buttonpress(2))
button2.grid(row=0,column=1)
button3=Button(frame,text="3",width=10,height=5,command=lambda:buttonpress(3))
button3.grid(row=0,column=2)
button4=Button(frame,text="4",width=10,height=5,command=lambda:buttonpress(4))
button4.grid(row=2,column=0)
button5=Button(frame,text="5",width=10,height=5,command=lambda:buttonpress(5))
button5.grid(row=2,column=1)
button6=Button(frame,text="6",width=10,height=5,command=lambda:buttonpress(6))
button6.grid(row=2,column=2)
button7=Button(frame,text="7",width=10,height=5,command=lambda:buttonpress(7))
button7.grid(row=3,column=0)
button8=Button(frame,text="8",width=10,height=5,command=lambda:buttonpress(8))
button8.grid(row=3,column=1)
button9=Button(frame,text="9",width=10,height=5,command=lambda:buttonpress(9))
button9.grid(row=3,column=2)
button0=Button(frame,text="0",width=10,height=5,command=lambda:buttonpress(0))
button0.grid(row=4,column=1)
buttonplus=Button(frame,text="+",width=10,height=5,command=lambda:buttonpress("+"))
buttonplus.grid(row=0,column=4)
buttonmin=Button(frame,text="-",width=10,height=5,command=lambda:buttonpress("-"))
buttonmin.grid(row=4,column=4)
buttondiv=Button(frame,text="/",width=10,height=5,command=lambda:buttonpress("/"))
buttondiv.grid(row=2,column=4)
buttonmul=Button(frame,text="*",width=10,height=5,command=lambda:buttonpress("*"))
buttonmul.grid(row=3,column=4)
buttonequal=Button(frame,text="=",width=10,height=5,command=lambda:equalto())
buttonequal.grid(row=4,column=2)
buttonclear=Button(frame,text="C",width=10,height=5,command=lambda:clear())
buttonclear.grid(row=4,column=0)
window.mainloop()
#what i learned
#error handling , collision of grid and pack
#updates:-backspace ,make more complex,try add button as array using for loops(work on this logic)