from  tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter import messagebox
root = Tk()
root.title("HASH-PAS 2.0")
root.geometry("1200x688")

global open_status_name
open_status_name =False

global selected
selected=False

#Create NEW_FILE functions.
def New_File():
    my_text.delete("1.0",END)
    root.title("New File - HASH-PAD")
    status_bar.config(text="New File      ")
    global open_status_name
    open_status_name =False

#Create OPEN_FILE functions. 
def Open_File():
    #Delete PREVIOUS_TEXT.
    my_text.delete("1.0", END)

    #Grab FILENAME
    text_file = filedialog.askopenfilename(initialdir="C:/Users/pc/Desktop/", title="OPEN FILE", filetypes=(("Text Files", "*.txt"), ("Html Files", "*.html"), ("Css File", "*.css"), ("Js File", "*.js"), ("All files", "*.*")))
    if text_file:
        global open_status_name
        open_status_name = text_file
    #Update STATUS_BAR.
    name = text_file
    status_bar.config(text=f'{name}        ')
    name = name.replace("C:/Users/pc/Desktop/", "")
    root.title(f"{name} - HASH-PAD")

    #OPEN FILE.
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    #ADD FILE TO TEXT BOX.
    my_text.insert(END, stuff)
    text_file.close()

#Create SAVE_AS_FILE functions.
def Save_As_File():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/Users/pc/Desktop/", title="Save File", filetypes=(("Text Files", "*.txt"),("Html Files", "*.html"),("Css Files", "*.css"),("All Files", "*.*")))
    if text_file:
        name=text_file
        name=name.replace("C:/Users/pc/Desktop/", "")
        root.title(f'{name} - HASH-PAD')

        #Save the file
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

#Create SAVE_FILE functions. 
def Save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        status_bar.config(text="File Saved.      ")
    else:
        Save_As_File()

#Create CUT-TEXT functions.
def cut_text(e):
    global selected
    if e:
        selected=root.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)

#Create COPY-TEXT functions.
def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()


    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


#Create COPY-TEXT functions.
def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else: 
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)
            root.clipboard_clear()
            root.clipboard_append(selected)

def bold_it():
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    #Configure A tag
    my_text.tag_configure("bold", font=bold_font)
    #Def Current tag
    current_tags = my_text.tag_names("sel.first")

    #If statement to see if tag has been used or not
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")

def italic_it():
    italic_font = font.Font(my_text, my_text.cget("font"))
    italic_font.configure(slant="italic")

    #Configure A tag
    my_text.tag_configure("italic", font=italic_font)
    #Def Current tag
    current_tags = my_text.tag_names("sel.first")

    #If statement to see if tag has been used or not
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")

def color_Text():


    my_color= colorchooser.askcolor()[1]
    status_bar.config(text=my_color)
    if my_color:
        
        color_font = font.Font(my_text, my_text.cget("font"))

        #Configure A tag
        my_text.tag_configure("colored", font=color_font, foreground=my_color)
        #Def Current tag
        current_tags = my_text.tag_names("sel.first")

        #If statement to see if tag has been used or not
        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")
        else:
            my_text.tag_add("colored", "sel.first", "sel.last")

def color_text_all():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)

def color_Background():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color) 

def clearFunc():
    my_text.delete("1.0", END)

def font_change(num):
    my_text.configure(font=("Helvetica", num))

def AboutFunc():
    messagebox.showinfo("About", "This Program Made By YGH2007, You can Edit the source in github :)")

# Create Frame.
my_frame = Frame(root)
my_frame.pack(pady=5)

#Create SCROLLBAR.
textscroll = Scrollbar(my_frame)
textscroll.pack(side=RIGHT, fill=Y)

hor_scroll = Scrollbar(my_frame, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)
#Create TEXTBOX.
my_text = Text(my_frame, width=97, height=27, font=("Helvetica", 16), selectbackground='blue', selectforeground="white", undo=True, yscrollcommand= textscroll.set, wrap="none",xscrollcommand=hor_scroll.set)
my_text.pack()

#Config SCROLLBAR.
textscroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)
# Create Menu
my_menu  = Menu(root)
root.config(menu=my_menu)

#Add FILE MENU.
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
#Add FILE_ITEMS.
file_menu.add_command(label="New", command=New_File)
file_menu.add_command(label="Open", command=Open_File)
file_menu.add_command(label="Save", command=Save_file)
file_menu.add_command(label="Save As", command=Save_As_File)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#Add EDIT_MENU.
edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Edit", menu=edit_menu)
#Add EDIT_ITEMS.
edit_menu.add_command(label="Copy",command=lambda: copy_text(False), accelerator="(Ctrl+C)")
edit_menu.add_command(label="Cut", command=lambda: cut_text(False), accelerator="(Ctrl+X)")
edit_menu.add_command(label="Paste", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(Ctrl+Z)")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="(Ctrl+Y)")

#Add FORMAT MENU.
format_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Format", menu=format_menu)
font_weight_menu = Menu(format_menu, tearoff=0)
text_color_menu = Menu(format_menu, tearoff=0)
format_menu.add_cascade(label="Font Weight", menu=font_weight_menu) 
format_menu.add_cascade(label="Color... ", menu=text_color_menu)
font_weight_menu.add_command(label="Italic", command=italic_it)
font_weight_menu.add_command(label="Bold", command=bold_it)
text_color_menu.add_command(label="Background", command=color_Background)
text_color_menu.add_command(label="Text", command=color_Text)
text_color_menu.add_command(label="Text All", command=color_text_all)

#Add CONFIG MENU.
config_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Config", menu=config_menu)
config_menu.add_command(label="Clear Text", command=clearFunc)
font_size_menu = Menu(config_menu, tearoff=0)
config_menu.add_cascade(label="Font Size... ", menu=font_size_menu)
font_size_menu.add_command(label="10", command=lambda: font_change(10))
font_size_menu.add_command(label="12", command=lambda: font_change(12))
font_size_menu.add_command(label="14", command=lambda: font_change(14))
font_size_menu.add_command(label="19", command=lambda: font_change(19))
font_size_menu.add_command(label="21", command=lambda: font_change(21))
font_size_menu.add_command(label="26", command=lambda: font_change(26))
font_size_menu.add_command(label="32", command=lambda: font_change(32))
font_size_menu.add_command(label="46", command=lambda: font_change(46))
font_size_menu.add_command(label="52", command=lambda: font_change(52))
font_size_menu.add_command(label="72", command=lambda: font_change(72))
config_menu.add_command(label="About HASHPAD", command=AboutFunc)


#Add STATUS BAR.
status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM)

#Bind Editing
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)


root.mainloop()