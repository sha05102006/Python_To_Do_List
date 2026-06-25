from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title('WriteUp - To Do List!')
root.iconbitmap(r"C:\Users\shash\code_section\Python_ToDoList\images.ico")
root.geometry("500x500")

# Define our Font
my_font = Font(
    family="Bookman Old Style",
    size=20,
    weight="bold")

#Create a frame
my_frame = Frame(root)
my_frame.pack(pady=10)

#Create a listbox
my_list = Listbox(my_frame,
                  font=my_font,
                  width=25,
                  height=8,
                  bg="SystemButtonFace",
                  bd=0,
                  fg="#464646",
                  highlightthickness=0,
                  selectbackground="#a6a6a6",
                  activestyle="none")

#Create a dummy list
#stuff=["Walk the dog","Learnt python tkinter","Buy groceries for the house"]
#Add the dummy list to list box
#for item in stuff:
    #my_list.insert(END, item)

#Add scrollbar
side_scrollbar = Scrollbar(my_frame, orient=VERTICAL)
side_scrollbar.pack(side=RIGHT, fill=Y)
bottom_scrollbar = Scrollbar(my_frame, orient=HORIZONTAL)
bottom_scrollbar.pack(side=BOTTOM,fill=X)
#Add scrollbar
my_list.config(yscrollcommand=side_scrollbar.set)
side_scrollbar.config(command=my_list.yview)
my_list.config(xscrollcommand=bottom_scrollbar.set)
bottom_scrollbar.config(command=my_list.xview)

#Expand to fit the Scroll bar
my_list.pack(side=LEFT, fill=BOTH, expand=True)

#Create an entry box to add items to the list
my_entry = Entry(root, font=("Helvetica", 24), width=26)
my_entry.pack(pady=20)
#Create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#Functions
def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def cross_off_item():
    #Cross of item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    #Get rid of selection bar
    my_list.selection_clear(0 ,END)

def uncross_item():
    # Cross of item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")
    # Get rid of selection bar
    my_list.selection_clear(0, END)

def delete_crossed_item():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))

        else:
            count += 1

def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/Users/shash/code_section/Python_ToDoList/data",
        title="Save File",
        filetypes=(("Dat Files", "*.dat"),
                   ("All Files", "*.*"))
    )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

        #Delete crossed of items before saving
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))

            else:
                count += 1

        #Grab all the stuff from the list
        stuff = my_list.get(0, END)
        #Open the file
        output_file = open(file_name, 'wb')
        #Actually add the stuff to the file
        pickle.dump(stuff, output_file)

def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="C:/Users/shash/code_section/Python_ToDoList/data",
        title="Open File",
        filetypes=(("Dat Files", "*.dat"),
                   ("All Files", "*.*"))
    )
    if file_name:
        #Delete currently open list
        my_list.delete(0, END)
        #Open the file
        input_file = open(file_name, 'rb')
        #Load the data from the file
        stuff = pickle.load(input_file)
        #Output stuff to the screen
        for item in stuff:
            my_list.insert(END, item)

def clear_list():
    my_list.delete(0, END)

#Create menu
my_menu = Menu(root)
root.config(menu=my_menu)
#Add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
#Add dropdown items
file_menu.add_command(label="Save list", command=save_list)
file_menu.add_command(label="Open list", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear list", command=clear_list)

#Add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="List Handling", menu=file_menu)
#Add dropdown items
file_menu.add_command(label="Cross Off Item", command=cross_off_item)
file_menu.add_command(label="Uncross Item", command=uncross_item)
file_menu.add_separator()
file_menu.add_command(label="Delete Crossed Item", command=delete_crossed_item)

#Add some buttons
add_button = Button(button_frame, text="Add Item", command=add_item)
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
#cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item)
#uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)
#delete_crossed_button = Button(button_frame, text="Delete Crossed Item", command=delete_crossed_item)

add_button.grid(row=0, column=0)
delete_button.grid(row=0, column=1, padx=20)
#cross_off_button.grid(row=0, column=2)
#uncross_button.grid(row=0, column=3, padx=20)
#delete_crossed_button.grid(row=0, column=4)

root.mainloop()