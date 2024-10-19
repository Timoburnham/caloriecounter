from tkinter import *


main_window= Tk()
main_window.geometry("500x500")
main_window.title("Calorie Counter")

label = Label(main_window, text="Meeting your physique goals is easy with this calorie tracker.", font=('arial', 10, 'bold'))
label.pack()

main_window.mainloop()