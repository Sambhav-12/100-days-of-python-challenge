from tkinter import *
from tkinter import messagebox
from random import randint, choice , shuffle
import pyperclip 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_nums = [choice(symbols) for _ in range(randint(2, 4))]
    passworrd_list = password_letters + password_symbols + password_nums
    shuffle(passworrd_list)

    password = "".join(passworrd_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS!", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Day-29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)


# Entries
website_entry = Entry(width=41)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=41)
email_entry.grid(column=1 , row=2, columnspan=2 )
email_entry.insert(0, "XYZ@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)


# Buttons
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)



window.mainloop()
