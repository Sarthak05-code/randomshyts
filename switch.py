import tkinter as tk
 

def set_dark_mode(frame, label, button):
    frame.config(bg="white")
    label.config(bg="white", fg="black")
    button.config(text="dark-mode", bg="white", fg="black",
                  command=lambda: set_light_mode(frame, label, button))

def set_light_mode(frame, label, button):
    frame.config(bg="black")
    label.config(bg="black", fg="white")
    button.config(text="light-mode", bg="black", fg="white",
                  command=lambda: set_dark_mode(frame, label, button))
def close(root, close):
    root.destroy()
def main():
    root = tk.Tk()
    root.title("Switch")
    root.geometry('720x540')

    frame = tk.Frame(root, bg="black")
    frame.pack(fill="both", expand=True)

    label = tk.Label(frame, text="Press for switch", font=("Roboto", 20), bg="black", fg="white")
    label.grid(row=0, column=1, columnspan=2, pady=10)

    button = tk.Button(frame, text="light-mode", font=("Arial", 15),
                       fg="white", bg="black",
                       command=lambda: set_dark_mode(frame, label, button))
    button.grid(row=1, column=1, columnspan=2, pady=10)
    close_btn = tk.Button(frame, text = "Close" , font = ("Arial",18), fg = "Yellow", bg="Cyan" , command= lambda: close(root, close_btn))
    close_btn.grid(row = 2 , column= 3 , columnspan=2 , pady=10)
    root.mainloop()

main()
