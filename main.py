import os
import subprocess

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

root = Tk()
root.title("RunPy")
root.configure(bg="#323846")
root.attributes("-fullscreen", True)

# app settings

window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

# code input

code_input = Text(root, font=("arial", 18))
code_input.place(x=150, y=0, width=window_width - 550, height=window_height)

# code output

code_output = Text(root, font=("arial", 18), bg="#323846", fg="lightgreen")
code_output.place(x=window_width - 550, y=0, width=window_width -
                  (window_width - 550), height=window_height)

# buttons

open_btn = PhotoImage(file="./assets/open.png")
save_btn = PhotoImage(file="./assets/save.png")
run_btn = PhotoImage(file="./assets/run.png")
exit_btn = PhotoImage(file="./assets/exit.png")

# function

file_path = ""

def set_file_path(path):
    global file_path
    file_path = path

def open_file():
    path = askopenfilename(filetypes=[("Python Files", "*.py")])

    with open(path, "r") as file:
        code = file.read()
        code_input.delete("1.0", END)
        code_input.insert("1.0", code)

        set_file_path(path)

def save_file():
    if file_path == "":
        path = asksaveasfilename(filetypes=[("Python Files", "*.py")])

    else:
        path = file_path

    with open(path, "w") as file:
        code = code_input.get("1.0", END)
        file.write(code)

        set_file_path(path)


def run_file():
    if file_path=="":
        messagebox.showerror("RunPy", "Save your code")
        return

    cmds = f"py {file_path}"
    process= subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, err = process.communicate()
    code_output.delete("1.0", END)
    code_output.insert("1.0", output)
    code_output.insert("1.0", err)

Button(root, image=open_btn, bg="#323846", bd=0,
       command=open_file).place(x=15, y=50)
Button(root, image=save_btn, bg="#323846", bd=0,
       command=save_file).place(x=15, y=200)
Button(root, image=run_btn, bg="#323846", bd=0,
       command=run_file).place(x=15, y=350)
Button(root, image=exit_btn, bg="#323846", bd=0,
       command=exit).place(x=15, y=500)

mainloop()
