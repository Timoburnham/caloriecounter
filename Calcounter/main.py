
import customtkinter

#app logic

class Food:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

food_list = [
    Food("Apple", 95, 0.5, 25, 0.3),
    Food("Chicken Breast", 165, 31, 0, 3.6),
    Food("Brown Rice", 215, 5, 45, 1.5),
]

















#create window

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("test")



food_entry = customtkinter.CTkEntry(root, width=200, placeholder_text="Enter food item")
food_entry.pack(pady=10)








root.mainloop()