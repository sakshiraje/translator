from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

# Initialize the main window
root = Tk()
root.title("Google Translator")
root.geometry("1080x400")
root.resizable(False, False)
root.configure(background="#e6f7ff")  # Light Blue background

# Function to update labels every second
def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

# Function to perform translation
def translate_now():
    text_ = text1.get(1.0, END)
    if not text_:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return
    
    t1 = Translator()
    try:
        # Translate the text
        trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
        trans_text = trans_text.text
        text2.delete(1.0, END)
        text2.insert(END, trans_text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation Error: {str(e)}")

# Function to clear the input and output text boxes
def clear_text():
    text1.delete(1.0, END)
    text2.delete(1.0, END)

# Add an icon for the window (replace with your own image file path)
try:
    image_icon = PhotoImage(file="google.png")
    root.iconphoto(False, image_icon)
except:
    pass

# Add an arrow image (replace with your own image file path)
try:
    arrow_image = PhotoImage(file="arrow.png")
    image_label = Label(root, image=arrow_image, width=150)
    image_label.place(x=450, y=30)
except:
    pass

# Get the list of available languages from googletrans
language = googletrans.LANGUAGES
languageV = list(language.values())

# Input language selection
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("english")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="#e6f7ff", fg="#333333", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

# Input text area
f = Frame(root, bg="#333333", bd=5)  # Dark gray frame
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Output language selection
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="#e6f7ff", fg="#333333", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

# Output text area
f1 = Frame(root, bg="#333333", bd=5)  # Dark gray frame
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(
    root,
    text="Translate",
    font=("Roboto", 15),
    activebackground="#45a049",  # Green when active
    cursor="hand2",
    bd=1,
    width=10,
    height=2,
    bg="#4CAF50",  # Green background
    fg="white",
    command=translate_now,
)
translate.place(x=480, y=250)

# Clear button with more space from the Translate button
clear = Button(
    root,
    text="Clear",
    font=("Roboto", 15),
    activebackground="#FF4500",  # Orange-red when active
    cursor="hand2",
    bd=1,
    width=10,
    height=2,
    bg="#FF6347",  # Tomato red
    fg="white",
    command=clear_text,
)
clear.place(x=480, y=310)  # Increased y value to create space between buttons


# Continuously update the labels with selected languages
label_change()

root.configure(bg="#e6f7ff")  # Light Blue background for the window
root.mainloop()
