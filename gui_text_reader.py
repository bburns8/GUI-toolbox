# very first GUI created which opens txt files

from tkinter import *
from tkinter import filedialog
from tkhtmlview import HTMLLabel
from PIL import ImageTk, Image

root = Tk()
root.title('GUI Image/Text Reader')
root.geometry("800x800")
root.filename = filedialog.askopenfilename()


# Read only 'r'
# Read and write 'r+' (beginning of file)
# Write only 'w' (over-written)
# Write and read 'w+' (over-written)
# Append Only 'a' (end of file)
# Append and read 'a+' (end of file)


def open_txt():
    # Open Txt file
    text_file = filedialog.askopenfilename(title="Open Text File", filetypes=(("Text Files", "*.*"),))
    text_file = open(text_file, 'r')
    stuff = text_file.read()

    my_text.insert(END, stuff)
    text_file.close()


# Save Txt File Method
def save_txt():
    # Save Txt File
    text_file = filedialog.askopenfilename(title="Open Text File", filetypes=(("Text Files", "*.*"),))
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))


# Add Image Method
def add_image():
    # Add image
    global image_file
    image_file = filedialog.askopenfilename(initialdir="/Users/blake/Desktop/PNG", title="Open Image File",
                                            filetypes=(("PNG Files", "*.*"),))
    position = my_text.index(INSERT)
    Label(root, text=image_file).pack()
    my_image = ImageTk.PhotoImage(Image.open(image_file))
    Label(image=my_image).pack()
    image_file = open(image_file, encoding='utf-8')
    open_image = image_file.read()
    my_text.image_create(position, open_image)
    image_file.close()


my_frame = Frame(root)
my_frame.pack(pady=10)

# Create Scroll Bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box Frame
my_text = Text(my_frame, width=60, height=20, font=("Helvetica", 16), selectbackground="yellow",
               selectforeground="black", yscrollcommand=text_scroll.set)
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)

# Open and Save Image and Text Buttons
open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=20)

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=20)

image_button = Button(root, text="Open Image File", command=add_image)
image_button.pack(pady=5)

root.mainloop()
