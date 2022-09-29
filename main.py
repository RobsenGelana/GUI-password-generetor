from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
from types import new_class
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    passwrd_entry.insert(0, password)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open('data.json', 'r') as data_file:
            webs_data = web_entry.get()
            data = json.load(data_file)
            if str(webs_data) in data.keys():
                files = data[f'{webs_data}']
                email = files['email']
                password = files['password']
                messagebox.showinfo(title='Your info', message=f"email: {email} \n password: {password}")
            else:
                messagebox.showinfo(title='ohh', message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showerror(title='Opps', message="No Data File Found")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_data = web_entry.get()
    email = email_entry.get()
    password = passwrd_entry.get()
    new_data = {
        web_data:{
            'email': email,
            'password': password
        }
    }
    if len(web_data) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Dont leave the filed's empty")
    else:
        try:
            with open('data.json', 'r') as data:
                data_file = json.load(data)
                data_file.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as data:
                json.dump(new_data, data, indent=4)
        else:
            with open('data.json', 'w') as data:
                json.dump(data_file, data, indent=4)
        finally:
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

search_button = Button(text='Search', command=find_password)
search_button.grid(column=2, row=1)

user_name = Label(text='Email/Username: ')
user_name.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.insert(0, 'example@.com')
email_entry.grid(column=1,row=2)

password_word = Label(text="Password")
password_word.grid(column=0, row=3)

passwrd_entry = Entry(width=35)
passwrd_entry.grid(column=1, row=3)

generate_password = Button(text='Generate Password', command=generate_password)
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4,)



window.mainloop()