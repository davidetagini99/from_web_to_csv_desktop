import tkinter
import customtkinter
from csv_generator import generate_csv as generate_csv_function
import tkinter.messagebox as messagebox

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("From Web to CSV")

# Function to center the window on the screen
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Create a frame to hold the form objects
form_frame = customtkinter.CTkFrame(app)
form_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def generate_csv():
    link = link_entry.get()
    classname = classname_entry.get()

    success = generate_csv_function(link, classname)

    if success:
        print("CSV generated successfully")
        messagebox.showinfo("CSV generated successfully")
        link_entry.delete(0, 'end')
        classname_entry.delete(0, 'end')
    else:
        print("Failed to generate the CSV")

link_label = customtkinter.CTkLabel(form_frame, text="Website Link")
link_label.grid(row=0, column=0, padx=10, pady=15)

link_entry = customtkinter.CTkEntry(form_frame, width=180)
link_entry.grid(row=0, column=1, padx=10, pady=10)

classname_label = customtkinter.CTkLabel(form_frame, text="Class Name")
classname_label.grid(row=1, column=0, padx=10, pady=5)

classname_entry = customtkinter.CTkEntry(form_frame, width=180)
classname_entry.grid(row=1, column=1, padx=10, pady=10)

makecsv_button = customtkinter.CTkButton(form_frame, text="Generate CSV", command=generate_csv, width=200, height=32)
makecsv_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

center_window(app)
app.mainloop()
