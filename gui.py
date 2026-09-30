from tkinter import *

from emoji_project import Emoji_Database

db = Emoji_Database("emoji.json")

window = Tk()

def search():
    user_input = entry.get()
    print("you have clicked the button ")
    print(f"you have searched for: {user_input}")
    
    result_box.delete(0,END)
    
    matching_emojis = db.partial_search(user_input)
    for item in matching_emojis:
        result_box.insert(END,item.emoji)
    
photo = PhotoImage(file = '/home/useer456/Downloads/skull.png')

label = Label(window,
              text = "GLOBAL EMOJI BAR",
              font = ('Arial',40,'bold'),
              fg = "#00FF00",
              bg = "black",
              relief = RAISED,
              bd = 10,
              padx = 20,
              pady = 20,
              image = photo,
              compound = 'bottom')
label.pack()

entry = Entry(window,
              font = ("Arial",50),
              fg ="#E6D00F",
              bg = 'cyan',
              )
entry.pack()

button = Button(window,
                text = "clk to search",
                command = search,
                font = ("Comic Sand",30),
                fg = "#00FF00",
                bg = "black",
                activeforeground = "#00FF00",
                activebackground = "black",
                state = ACTIVE,
                compound = 'top')
button.pack()

result_box = Listbox(window,
                     font = ("Arial",24),
                     width = 20,
                     height = 6,
                     bg = "black",
                     fg = "#00FF00",
                     selectbackground = "cyan",
                     selectmode = SINGLE)
result_box.pack(pady = 10)

window.mainloop()