from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open('data.txt', 'a') as data:
        web_data = web_entry.get()
        email = email_entry.get()
        password = passwrd_entry.get()
        data.write(f"{web_data} | {email} | {password} \n")
    web_entry.delete(0, END)
    passwrd_entry.delete(0, END)
    web_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manger")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website = Label(text='Website')
website.grid(column=0, row=1)

web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1)

user_name = Label(text='Email/Username: ')
user_name.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.insert(0, 'example@.com')
email_entry.grid(column=1,row=2)

password_word = Label(text="Password")
password_word.grid(column=0, row=3)

passwrd_entry = Entry(width=35)
passwrd_entry.grid(column=1, row=3)

generate_password = Button(text='Generate Password')
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4,)



window.mainloop()