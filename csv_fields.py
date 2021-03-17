from tkinter import *
from tkinter import filedialog
import csv

root = Tk()
root.title('GUI File Reader')
root.geometry("800x800")
root.filename = filedialog.askopenfilename()

# csv file name
filename = "fields.csv"

# initializing the titles and rows list
fields = []
rows = []
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

        # get total number of rows
    print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
#  printing first 3 rows
print('\nFirst 3 rows are:\n')
for row in rows[:3]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col),
    print('\n')


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
    fields.insert(END, stuff)  # new open file widget
    text_file.close()


# Save Txt File Method
def save_txt():
    # Save Txt File
    text_file = filedialog.askopenfilename(title="Open Text File", filetypes=(("Text Files", "*.*"),))
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))


my_frame = Frame(root)
my_frame.pack(pady=10)

# Create Scroll Bar
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box Frame
my_text = Text(my_frame, width=60, height=10, font=("Helvetica", 16),
               selectforeground="black", yscrollcommand=text_scroll.set)

fields = Text(my_frame, width=60, height=10, font=("Helvetica", 16))
fields.pack()
my_text.pack()

# Configure our scrollbar
text_scroll.config(command=my_text.yview)

# Open and Save Image and Text Buttons
open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=10)

save_button = Button(root, text="Save File", command=save_txt)
save_button.pack(pady=10)

root.mainloop()
