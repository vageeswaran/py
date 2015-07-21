from Tkinter import *
class App:
    xyz=1
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()
        self.xyz=master
        self.button=Button(frame,text="Quit",fg="red",command=frame.quit)
        self.button.pack(side=LEFT)
        self.hithere=Button(frame,text="hello",command=self.say_hi)
        self.hithere.pack(side=LEFT)
    def say_hi(self):
        w=Label(self.xyz,text="hi there")
        w.pack()
root=Tk()
app=App(root)
root.mainloop()
root.destroy()


