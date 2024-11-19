import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
import matplotlib.pyplot as plt

historical_data = []

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            result_label.config(fg="blue")
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            result_label.config(fg="green")
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            result_label.config(fg="orange")
        else:
            category = "Obese"
            result_label.config(fg="red")

        historical_data.append(bmi)
        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height")

def plot_graph():
    if len(historical_data) > 1:
        plt.figure(figsize=(6, 4))
        plt.plot(historical_data, marker='o', linestyle='-', color='b')
        plt.title('BMI Trend Over Time', fontsize=14)
        plt.xlabel('Data Points', fontsize=12)
        plt.ylabel('BMI', fontsize=12)
        plt.grid(True)
        plt.show()

def show_graph():
    if len(historical_data) == 0:
        messagebox.showinfo("No data", "No BMI data available to plot. Please calculate at least one BMI first.")
    else:
        plot_graph()

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x250")
root.configure(bg="#f0f0f5")

title_font = font.Font(family="Helvetica", size=18, weight="bold")
label_font = font.Font(family="Arial", size=12)
result_font = font.Font(family="Arial", size=14, weight="bold")

title_label = tk.Label(root, text="BMI Calculator", font=title_font, bg="#f0f0f5", fg="#333")
title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="w", padx=10)

tk.Label(root, text="Enter weight (kg):", font=label_font, bg="#f0f0f5").grid(row=1, column=0, pady=5, padx=10, sticky="w")
weight_entry = tk.Entry(root, width=15, font=label_font)
weight_entry.grid(row=1, column=1, pady=5, padx=10)

tk.Label(root, text="Enter height (m):", font=label_font, bg="#f0f0f5").grid(row=2, column=0, pady=5, padx=10, sticky="w")
height_entry = tk.Entry(root, width=15, font=label_font)
height_entry.grid(row=2, column=1, pady=5, padx=10)

button_frame = tk.Frame(root, bg="#f0f0f5")
button_frame.grid(row=3, column=0, columnspan=2, pady=15, sticky="w", padx=10)

calculate_button = tk.Button(button_frame, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), padx=10)
calculate_button.grid(row=0, column=0, pady=5, padx=10)

show_graph_button = tk.Button(button_frame, text="Show Graph", command=show_graph, bg="#2196F3", fg="white", font=("Arial", 12, "bold"), padx=10)
show_graph_button.grid(row=0, column=1, pady=5, padx=10)

result_label = tk.Label(root, text="", font=result_font, bg="#f0f0f5")
result_label.grid(row=4, column=0, columnspan=2, pady=10, sticky="w", padx=10)

root.mainloop()