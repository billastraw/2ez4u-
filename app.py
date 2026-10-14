from frontend.ui import buat_tampilan
import tkinter as tk


def main():
    root = tk.Tk()
    root.title("2EZ4U APP")
    root.geometry("1200x750")
    root.minsize(1000, 650)

    buat_tampilan(root)

    root.mainloop()


if __name__ == "__main__":
    main()