import tkinter
import customtkinter
from csv_generator import generate_csv as generate_csv_function

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue") # objects color

app = customtkinter.CTk() # new window instance

# window attributes start 

app.title("from web to csv") # application title
app.geometry("500x500") # starting resolution

# window attributes end

def generate_csv():
    link = link_entry.get()
    classname = classname_entry.get()

    success = generate_csv_function(link, classname) # recalling the backend

    if success:
        print("csv generated successfully")
    else:
        print("failed to generate the csv")

# front end form

link_label = customtkinter.CTkLabel(app, text="website link")
link_label.place(x=17, y=25)

link_entry = customtkinter.CTkEntry(app)
link_entry.place(x=100, y=25)

classname_label = customtkinter.CTkLabel(app, text="class name")
classname_label.place(x=17, y=68)

classname_entry = customtkinter.CTkEntry(app)
classname_entry.place(x=100, y=68)

makecsv_button = customtkinter.CTkButton(app, text="generate csv", command=generate_csv) # injecting the backend on the button click
makecsv_button.place(x=17, y=120)

app.mainloop()