from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

warning_font = ("Verdana", 8, "bold")


def click_button():
    user_weight = my_entry_1.get()
    user_height = my_entry_2.get()
    if user_weight == "":
        my_label_3.config(text="You didn't enter your weight", font=warning_font, fg="red")
        return
    elif user_height == "":
        my_label_3.config(text="You didn't enter your height", font=warning_font, fg="red")
        return
    elif user_weight <= "0":
        my_label_3.config(text="Your weight must be more then 0", font=warning_font, fg="red")
        return
    elif user_height <= "0":
        my_label_3.config(text="Your height must be more then 0", font=warning_font, fg="red")
        return
    try:
        user_weight = float(user_weight)
        user_height = float(user_height) / 100
    except ValueError:
        my_label_3.config(text="Please enter valid numbers", font=warning_font, fg="red")
        return

    bmi = round(float(user_weight) / user_height ** 2, 2)

    if bmi < 18.5:
        my_label_3.config(text=f"Your BMI score is {bmi}. You are Underweight", fg="black")
    elif 18.5 <= bmi < 25:
        my_label_3.config(text=f"Your BMI score is {bmi}. You are Normal Weight", fg="black")
    elif 25 <= bmi < 30:
        my_label_3.config(text=f"Your BMI score is {bmi}. You are Overweight", fg="black")
    elif 30 <= bmi < 35:
        my_label_3.config(text=f"Your BMI score is {bmi}. You are Class I Obesity", fg="black")
    elif 35 <= bmi < 40:
        my_label_3.config(text=f"Your BMI score is {bmi}. You are Class II Obesity", fg="black")
    elif bmi >= 40:
        my_label_3.config(text=f"Your BMI score is {bmi}. You are Class III Obesity", fg="black")


my_label_1 = Label(text="Enter Your Weight (kg)")
my_label_1.config(padx=10, pady=10)
my_label_1.pack()

my_entry_1 = Entry(width=15)
my_entry_1.focus()
my_entry_1.pack()

my_label_2 = Label(text="Enter Your Height (cm")
my_label_2.config(padx=10, pady=10)
my_label_2.pack()

my_entry_2 = Entry(width=15)
my_entry_2.pack()

my_button = Button(text="Calculate", command=click_button)
my_button.config(width=10)
my_button.pack()

my_label_3 = Label(text="")
my_label_3.config(padx=10, pady=10)
my_label_3.pack()

window.mainloop()


