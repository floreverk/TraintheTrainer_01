from tkinter import *
from PIL import ImageTk, Image
from tkinter import font

def start():
    choice = [var1.get(), var2.get(), var3.get()]
    if tuple(choice) == ('postcard1', '', ''):
        #create postcard1
    elif tuple(choice) == ('', 'postcard2', ''):
        #create postcard2
    elif tuple(choice) == ('', '', 'postcard3'):
        #create postcard3
    else:
        error = Label(text="Please select only one postcard", bg="#fffedd")
        error.grid(row=13, column=1)


postcardmaker = Tk()
postcardmaker.configure(bg="#fffedd")
postcardmaker.iconbitmap(r"C:\Users\Verkesfl\PycharmProjects\pythonProject\HvApostcards\hva.ico")
postcardmaker.title("Huis van Alijn: Postcardmaker")
postcardfont = font.Font(family = "Comic sans MS", name="postcardmakerfont", size = 10, weight = 'bold')

first_step = Label(text="Please Select your Card: ", font=postcardfont, fg="#583b2a", bg="#fffedd")
first_step.grid(row=0, column=0)

second_step = Label(text="Please provide details of recipient:", font=postcardfont, fg="#583b2a", bg="#fffedd")
second_step.grid(row=3, column=0)

third_step = Label(text="Write your message: ", font=postcardfont, fg="#583b2a", bg="#fffedd")
third_step.grid(row=10, column=0)

first_postcard = ImageTk.PhotoImage(Image.open(r"C:\Users\Verkesfl\PycharmProjects\pythonProject\HvApostcards\postcard1.jpg"))
first_pstcrd = Label(image=first_postcard, bg="#fffedd")
first_pstcrd.grid(row=1, column=0)

second_postcard = ImageTk.PhotoImage(Image.open(r"C:\Users\Verkesfl\PycharmProjects\pythonProject\HvApostcards\postcard2.jpg"))
second_pstcrd = Label(image=second_postcard, bg="#fffedd")
second_pstcrd.grid(row=1, column=1)

third_postcard = ImageTk.PhotoImage(Image.open(r"C:\Users\Verkesfl\PycharmProjects\pythonProject\HvApostcards\postcard3.jpg"))
third_pstcrd = Label(image=third_postcard, bg="#fffedd")
third_pstcrd.grid(row=1, column=2)

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

first_card = Checkbutton(postcardmaker, text="", variable=var1, onvalue="postcard1", offvalue="", bg="#fffedd")
second_card = Checkbutton(postcardmaker, text="", variable=var2, onvalue="postcard2", offvalue="", bg="#fffedd")
third_card = Checkbutton(postcardmaker, text="", variable=var3, onvalue="postcard3", offvalue="", bg="#fffedd")

first_card.grid(row=2, column=0)
second_card.grid(row=2, column=1)
third_card.grid(row=2, column=2)


recipient_name = Label(text="Name:", fg="#583b2a", bg="#fffedd")
recipient_name.grid(row=4, column=0)
name = Entry(postcardmaker)
name.grid(row=4, column=1)

recipient_street = Label(text="Street:", fg="#583b2a", bg="#fffedd")
recipient_street.grid(row=5, column=0)
street = Entry(postcardmaker)
street.grid(row=5, column=1)

recipient_streetnumber = Label(text="Streetnumber:", fg="#583b2a", bg="#fffedd")
recipient_streetnumber.grid(row=6, column=0)
number = Entry(postcardmaker)
number.grid(row=6, column=1)

recipient_city = Label(text="City:", fg="#583b2a", bg="#fffedd")
recipient_city.grid(row=7, column=0)
city = Entry(postcardmaker)
city.grid(row=7, column=1)

recipient_postalcode = Label(postcardmaker, text="Postalcode:", fg="#583b2a", bg="#fffedd")
recipient_postalcode.grid(row=8, column=0)
postalcode = Entry(postcardmaker)
postalcode.grid(row=8, column=1)

recipient_country = Label(postcardmaker, text="Country:", fg="#583b2a", bg="#fffedd")
recipient_country.grid(row=9, column=0)
landenlijst = StringVar(postcardmaker)
landenlijst.set('Choose country')
menu = OptionMenu(postcardmaker, landenlijst, "Belgium", "France", "Germany")
menu.grid(row=9, column=1)

message = Text(postcardmaker, height=10)
message.grid(row=11, column=0, columnspan=3)

create_postcard = Button(text="Create Postcard", padx=10, command=start)
create_postcard.grid(row=12, column=1)

postcardmaker.mainloop()
