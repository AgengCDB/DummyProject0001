import os
os.system("title Hello")

import tkinter as tk
from tkinter import ttk, filedialog
import tkinter.scrolledtext as tkscrolled

from tkinterdnd2 import DND_FILES

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import random
from datetime import datetime

# My script
from renewal import getRenewal
import excel_to_csv

#############################################################################################################################################

# Text
E_NO_DIR = "INPUT DIRECTORY FIRST!!!\n" # show this if no directory inserted
ABOUT_TEXT = """Hello World 
Since 2024 May 24
"""

# COLOR
COL_GREEN = "#7DC343"
COL_DARK_GREEN = "#4C7B24"
COL_ORANGE = "#EC722E"
COL_DARK_ORANGE = "#B34C1C"
COL_BLUE = "#64A2D8"
COL_DARK_BLUE = "#3D6DAB"
COL_YELLOW = "#EED842"
COL_DARK_YELLOW = "#B7AD2D"

## random
colors = ["#7DC343", "#4C7B24", "#EC722E", "#B34C1C", "#64A2D8", "#3D6DAB", "#EED842", "#B7AD2D"]
colors_all = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue","blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk","crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey", "darkkhaki","darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue","darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey","dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod","gray", "green", "greenyellow", "grey", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender","lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow","lightgray", "lightgreen", "lightgrey", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray","lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine","mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise","mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab","orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff","peru", "pink", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown","seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen","steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"]
random_color = random.choice(colors)

# TK
TK_BUTTON_BORDERWIDTH = 3
TK_BUTTON_BACKGROUND = COL_GREEN
TK_BUTTON_ACTIVEBACKGROUND = COL_DARK_GREEN

# Scrolled Text
SCROLLED_TEXT_WIDTH = 60

#############################################################################################################################################

# Renewal    
def select_input_folder():
    input_folder_path = filedialog.askdirectory()
    input_text.config(state=tk.NORMAL)  # Enable editing
    input_text.delete(1.0, tk.END)  # Clear previous content
    input_text.insert(tk.END, input_folder_path)  # Insert new content
    input_text.config(state=tk.DISABLED)
    
def process_folder():
    input_folder = input_text.get("1.0", tk.END).strip()
    if input_folder == "":
        result_text.config(state=tk.NORMAL)  # Enable editing
        result_text.delete(1.0, tk.END)  # Clear previous content
        result_text.insert(tk.END, E_NO_DIR)
        result_text.config(state=tk.DISABLED)
    else:
        result_text.config(state=tk.NORMAL)  # Enable editing
        result_text.delete(1.0, tk.END)  # Clear previous content
        result_file_path = getRenewal(input_folder=input_folder, is_moveConverted=is_moveConverted, is_fileName=is_fileName)
        result_text.insert(tk.END, result_file_path)
        result_text.config(state=tk.DISABLED)

def open_folder():
    excel_dir = result_text.get("1.0", tk.END).strip()
    if os.path.exists(excel_dir):
        os.startfile(os.path.dirname(excel_dir))
    else:
        result_text.config(state=tk.NORMAL)  # Enable editing
        result_text.delete(1.0, tk.END)  # Clear previous content
        result_text.insert(tk.END, "Sorry, but u have nothing to open")
        result_text.config(state=tk.DISABLED)

# Modify
def mod_input_excel():
    excel_folder_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    
    input_text2.config(state=tk.NORMAL)  # Enable editing
    input_text2.delete(1.0, tk.END)  # Clear previous content
    input_text2.insert(tk.END, excel_folder_path)  # Insert new content
    input_text2.config(state=tk.DISABLED)
    
def command_button_get_csv():
    excel_dir = input_text2.get("1.0", tk.END).strip()
    
    if os.path.exists(excel_dir):
        output_dir = os.path.dirname(excel_dir)
        result_file_path = excel_to_csv.main(excel_dir, output_dir)
        
        result_text2.config(state=tk.NORMAL)  # Enable editing
        result_text2.delete(1.0, tk.END)  # Clear previous content
        result_text2.insert(tk.END, result_file_path)
        result_text2.config(state=tk.DISABLED)
    else:
        result_text2.config(state=tk.NORMAL)  # Enable editing
        result_text2.delete(1.0, tk.END)  # Clear previous content
        result_text2.insert(tk.END, "Input excel first!")
        result_text2.config(state=tk.DISABLED)

def command_button_open_csv():
    temp_dir = result_text2.get("1.0", tk.END).strip()
    if os.path.exists(temp_dir):
        os.startfile(os.path.dirname(temp_dir))
    else:
        result_text2.config(state=tk.NORMAL)  # Enable editing
        result_text2.delete(1.0, tk.END)  # Clear previous content
        result_text2.insert(tk.END, "File not found or it's just empty")
        result_text2.config(state=tk.DISABLED)

#############################################################################################################################################

root = tk.Tk() 
root.title("HelloWorld")

root.configure(bg=random_color)
# root.resizable(False, False)
root.iconbitmap("C:/xampp/htdocs/SmartDashboard/Renewal/HelloWorld.ico")

tabControl = ttk.Notebook(root)
tabControl.pack(padx=20, pady=20)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Renewal (PDF to Excel)') 
tabControl.add(tab2, text ='Modify (Excel to CSV)') 
tabControl.add(tab3, text ='About') 

tabControl.pack(expand = 1, fill ="both")

# Renewal (PDF to Excel) ###################################################################################################################################################################

## frame Result
f_result = ttk.Frame(tab1)
f_result.pack(side=tk.LEFT)

### Label input dir
label1 = tk.Label(f_result, text="Input directory :")
label1.pack(pady=(10, 0))

### Input text
input_text = tkscrolled.ScrolledText(f_result, 
                                     bg="lightgray", 
                                     fg="black", 
                                     wrap=tk.WORD, 
                                     height=5,
                                     width=SCROLLED_TEXT_WIDTH)
input_text.pack(padx=20, pady=(0, 20), fill='both')
input_text.config(state=tk.DISABLED)

label2 = tk.Label(f_result, text="Result :")
label2.pack()

result_text = tkscrolled.ScrolledText(f_result, bg="lightgray", fg="black", wrap=tk.WORD, height=5,
                                      width=SCROLLED_TEXT_WIDTH)
result_text.pack(padx=20, pady=(0, 20), fill='both')
result_text.config(state=tk.DISABLED) 

## frame Checkbox
f_checkBox = ttk.Frame(tab1)
f_checkBox.pack(side=tk.RIGHT, expand=True)

is_fileName = tk.IntVar()
is_moveConverted = tk.IntVar()

checkbox1 = tk.Checkbutton(f_checkBox, text="Add fileName column", variable=is_fileName)
checkbox2 = tk.Checkbutton(f_checkBox, text="Move converted PDF to another folder", variable=is_moveConverted)
checkbox1.pack(anchor="w", padx=(0, 20))
checkbox2.pack(anchor="w", padx=(0, 20))

### Input button
input_folder_button = tk.Button(f_checkBox, text="Input Folder", 
                                command=select_input_folder, 
                                borderwidth=TK_BUTTON_BORDERWIDTH,
                                background=COL_BLUE,
                                activebackground=COL_DARK_BLUE)
input_folder_button.pack(padx=(0, 20), pady=(20, 10), fill=tk.BOTH)

### Process button
process_button = tk.Button(f_checkBox, text="Process Folder", 
                           command=process_folder,
                           borderwidth=TK_BUTTON_BORDERWIDTH,
                           background=COL_BLUE,
                           activebackground=COL_DARK_BLUE)
process_button.pack(padx=(0, 20), pady=(0, 10), fill=tk.BOTH)

### Open Folder
button_open_folder = tk.Button(f_checkBox, text="Open excel location", 
                           command=open_folder,
                           borderwidth=TK_BUTTON_BORDERWIDTH,
                           background=TK_BUTTON_BACKGROUND,
                           activebackground=TK_BUTTON_ACTIVEBACKGROUND)
button_open_folder.pack(padx=(0, 20), pady=(0, 0), fill=tk.BOTH)

# Modify (text to csv) ###############################################################################################################################################################################################################################################################################################################################################################

## Results
f_result2 = ttk.Frame(tab2)
f_result2.pack(side=tk.LEFT)

### Label input dir
label3 = tk.Label(f_result2, text="Excel directory :")
label3.pack(pady=(10, 0))

### Input text
input_text2 = tkscrolled.ScrolledText(f_result2, bg="lightgray", fg="black", wrap=tk.WORD, height=5,
                                      width=SCROLLED_TEXT_WIDTH)
input_text2.pack(padx=20, pady=(0, 20))
input_text2.config(state=tk.DISABLED)

### Label
label4 = tk.Label(f_result2, text="CSV directory :")
label4.pack()

result_text2 = tkscrolled.ScrolledText(f_result2, bg="lightgray", fg="black", wrap=tk.WORD, height=5,
                                       width=SCROLLED_TEXT_WIDTH)
result_text2.pack(padx=20, pady=(0, 20))
result_text2.config(state=tk.DISABLED) 

## Button
f_button = ttk.Frame(tab2)
f_button.pack(padx=10, pady=10, side=tk.RIGHT, expand=True, fill="x")

button_get_excel = tk.Button(f_button, text="Input excel", 
                        command=mod_input_excel,
                        borderwidth=TK_BUTTON_BORDERWIDTH,
                        background=TK_BUTTON_BACKGROUND,
                        activebackground=TK_BUTTON_ACTIVEBACKGROUND)
button_get_excel.pack(pady=10, padx=(0, 20), fill=tk.BOTH)

button_get_csv = tk.Button(f_button, text="Get csv", 
                        command=command_button_get_csv,
                        borderwidth=TK_BUTTON_BORDERWIDTH,
                        background=COL_ORANGE,
                        activebackground=COL_DARK_ORANGE)
button_get_csv.pack(pady=(0, 10), padx=(0, 20), fill=tk.BOTH)

button_open_csv = tk.Button(f_button, text="Open csv", 
                        command=command_button_open_csv,
                        borderwidth=TK_BUTTON_BORDERWIDTH,
                        background=COL_YELLOW,
                        activebackground=COL_DARK_YELLOW)
button_open_csv.pack(pady=(0, 10), padx=(0, 20), fill=tk.BOTH)

# About ###############################################################################################################################################################################################################################################################################################################################################################
def cmd_button_check():
    button_check.config(bg=random.choice(colors))
    button_scroll_to_bottom.config(bg=random.choice(colors_all),
                                   fg=random.choice(colors_all))
    root.configure(bg=random.choice(colors))
    text_about.configure(fg=random.choice(colors_all),
                         bg=random.choice(colors_all))
    
    text_about.config(state=tk.NORMAL)  # Enable editing
    text_about.insert(tk.END, datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")+"\n")
    text_about.config(state=tk.DISABLED) 

text_about = tkscrolled.ScrolledText(tab3, height=10, width=40)
text_about.pack(padx=10, pady=10, fill=tk.BOTH)
text_about.insert(tk.END, ABOUT_TEXT)
text_about.config(state=tk.DISABLED) 

## Button
f_about_button = ttk.Frame(tab3)
f_about_button.pack(side=tk.BOTTOM, expand=True)

button_check = tk.Button(f_about_button, text="Hello World", 
                        command=cmd_button_check,
                        borderwidth=TK_BUTTON_BORDERWIDTH,
                        background=random_color,
                        activebackground=random_color)
button_check.pack(padx=10, pady=20, side=tk.LEFT)

def scroll_to_bottom():
    text_about.yview_moveto(1.0)
    
button_scroll_to_bottom = tk.Button(f_about_button, text="Scroll to Bottom", command=scroll_to_bottom,
                        borderwidth=TK_BUTTON_BORDERWIDTH,
                        background=random_color,
                        activebackground=random_color)
button_scroll_to_bottom.pack(padx=10, pady=20, side=tk.RIGHT)

# Style
DEFAULT_BG_COLOR = "#F0F0F0"
style = ttk.Style()
style.theme_create('yummy', settings={"TNotebook.Tab": {"configure": {"padding": [5, 1], 
                                                                      "background": "grey"},
                                                        "map": {"background": [("selected", DEFAULT_BG_COLOR)],
                                                                "expand": [("selected", [1, 1, 1, 0])]} },
                                      "TFrame": {"configure": {"background": DEFAULT_BG_COLOR} },
                                      "TButton": {"configure": {"foreground": "white",
                                                                "background": DEFAULT_BG_COLOR,
                                                                "relief": "groove",
                                                                "padding": 10,
                                                                "borderwidth": 2,
                                                                "focuscolor": "#80CBC4"} } 
                                      } )
style.theme_use("yummy")

root.mainloop()