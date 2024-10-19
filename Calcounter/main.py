from tkinter import *


main_window= Tk()
main_window.geometry("1000x1000")
main_window.title("Calorie Counter")

label = Label(main_window, text="Meeting your physique goals is easy with this calorie tracker.",
 font=('arial', 10, 'bold'),
 fg='#FFFFFF',
 bg='black',
 relief=RAISED,
 bd=5,
 padx=15
 )
label.pack()

main_window.mainloop()