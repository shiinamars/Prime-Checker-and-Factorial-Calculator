# Techinical Assessment - Dulce, Marcella Grace F.

import tkinter as tk
from math import sqrt, log10
from threading import Thread

# Function to check if a number is prime using the optimized algorithm called the "Sieve of Eratosthenes"
def is_prime(n):
    if n < 2:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

# Function to find the factorial of a number using an iterative approach
def factorial(n):
    if n < 0:
        return "Invalid input. Please enter a positive number."

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

# Function to handle button click for prime checking
def check_prime():
    try:
        number = int(entry_1.get())

        def check_prime_task():
            if is_prime(number):
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"{number} is a prime number.")
            else:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"{number} is not a prime number.")

        Thread(target=check_prime_task).start()
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Invalid input. Please enter a valid number.")

# Function to handle button click for factorial calculation
def calculate_factorial():
    try:
        number = int(entry_1.get())

        def calculate_factorial_task():
            result = factorial(number)

            if isinstance(result, str):
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, result)
            else:
                exponent = int(log10(result))
                mantissa = result / (10 ** exponent)
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, f"The factorial of {number} is {mantissa:.10f} x 10^{exponent}.")

        Thread(target=calculate_factorial_task).start()
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Invalid input. Please enter a valid number.")

# Create the GUI window
window = tk.Tk()
window.title("Prime Checker & Factorial Calculator")
window.geometry("800x500")
window.resizable(False,False)

# Create a frame
gradient_frame = tk.Frame(window, bg="#043045")
gradient_frame.place(relwidth=1, relheight=1)

# Create an image label for the background
bg_image = tk.PhotoImage(file=r"Image-2.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=30, y=28, width=740, height=440)

# Create the title header
title_label = tk.Label(bg_label, text="Prime Checker and Factorial Calculator", font=("Montserrat ExtraBold", 18), bg="#4094AF", fg="white")
title_label.place(x=115, y=10)

# Create horizontal lines for the title header
line1 = tk.Frame(bg_label, bg="white", width=893, height=5)
line1.place(x=-1, y=-1)

line2 = tk.Frame(bg_label, bg="white", width=893, height=5)
line2.place(x=-1, y=55)

# Create the "Enter a number" label
number_label = tk.Label(bg_label, text="Enter a number:", font=("Montserrat Bold", 12), bg="#4094AF", fg="white")
number_label.place(x=300, y=65)

# Create textbox for entry_1
entry_1 = tk.Entry(bg_label, bd=0, bg="white", fg="black", font=("Montserrat Regular", 12), highlightthickness=0)
entry_1.place(x=200, y=100, width=350, height=25)

# Create buttons for prime checking and factorial calculation
button_1 = tk.Button(bg_label, text="Check Prime", font=("Montserrat Semibold", 10), bg="#80CED7", fg="white", activebackground="#80CED7", activeforeground="white", bd=0, command=check_prime)
button_1.place(x=300, y=140, width=140, height=30)

button_2 = tk.Button(bg_label, text="Calculate Factorial", font=("Montserrat Semibold", 10), bg="#80CED7", fg="white", activebackground="#80CED7", activeforeground="white", bd=0, command=calculate_factorial)
button_2.place(x=300, y=180,width=140, height=30)

# Create a scrollbar for the result_text
scrollbar = tk.Scrollbar(bg_label)
scrollbar.place(x=550, y=230, height=110)

# Create a Text for displaying results
result_text = tk.Text(bg_label, width=50, height=5,font=("Montserrat SemiBold", 12), bg="white", fg="black", wrap="word", yscrollcommand=scrollbar.set)
result_text.place(x=200, y=230, width=350, height=110)

# Configure the scrollbar to scroll the result_text
scrollbar.config(command=result_text.yview)

# Start the GUI event loop
window.mainloop()