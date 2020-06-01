from Tkinter import *
import tkFileDialog

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkFileDialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

button = Button(root, text="Save", command=saveas)
button.grid()

root = Tk(className="glowEdit")

text = Text(root)
text.grid()

root.mainloop()
