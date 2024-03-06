from tkinter import *

def display_text():
    lbl_sample.configure(text=ent_text.get(),fg="Green")

root = Tk()
root.geometry("500x220")
root.title("J1T-midLA1")
root.config(background="#d1d1e9")

lbl_name = Label(root,text ="Renzo Emmanuel V. Ramos",font = "courier",background="#d1d1e9")
lbl_name.pack(pady="5")
lbl_input_text = Label(root,text ="Input Text Here",font = "courier")
lbl_input_text.pack(pady=5)
ent_text = Entry(root,width=50,justify="center")
ent_text.pack(pady=5)
btn_display_text = Button(root,text="Display Text",width = 20,height = 1,pady=10,command= display_text,font=("Arial",10,"italic"))
btn_display_text.pack(pady = 5)
lbl_sample = Label(text="Text Appear Here!",font=("Arial",15,"bold"),background="#d1d1e9")
lbl_sample.pack()
root.mainloop()