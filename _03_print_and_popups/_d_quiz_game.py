from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score=0
    # ASK A QUESTION AND CHECK THE ANSWER
    y=simpledialog.askstring(title= "quiz show" , prompt="what is 15x divide by 3x^2")
    #      // 2.  Ask the user a question 

    #      // 3.  Use an if statement to check if their answer is correct
    if y=="5x^3":
        messagebox.showinfo(message='you were correct congratulations')
        score=score+1
    else:
        messagebox.showerror(message= 'you suck get a life and lose a point')
        score=score-1
    x=simpledialog.askstring(title= "quiz show" , prompt= "Are zebra white with black stripes or black with white stripes")
    if x=="black with white stripes":
        messagebox.showinfo(message="good job you smort")
        score=score+1
    else:
        messagebox.showerror(message="L bozo you need to get smarter")
        score=score-1
    z=simpledialog.askstring(title="quiz show" , prompt= "you see a boat filled with people. It has not sunk, but when you look again you don't see a single person on the boat. Why?")
    if z=="they are all couples":
        messagebox.showinfo(message="good job idiot")
        score=score+1
    else:
        messagebox.showerror(message="your a dumbass no wonder you are single")
        score=score-1

        #      // 4.  if the user's answer was correct, add one to their score

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(message="your score="+ str(score))
    # Run the window's .mainloop() method
    window.mainloop()
pass
