#H1
#Kert-Andero Põldmaa
import tkinter as tk

def main():
    aken = tk.Tk()
    aken.title("Tkinderi ülesanded")
    aken.geometry("400x400")
    aken.resizable(True, False)

    label = tk.Label(aken, text="Tere, maailm!").pack()
    button = tk.Button(aken, text="Tere maailm", command=aken.destroy).pack()

    aken.mainloop()

if __name__ == "__main__":
    main()