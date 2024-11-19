import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
from collections import Counter

# Initialize data storage

patients = []

def add_patient():

    """Add patient details to the list."""

    name = name_entry.get()
    age = int(age_entry.get())
    category = age_category.get()
    file = file_path.get()

    if not name or not category or not file:
        messagebox.showwarning("Missing Information", "Please fill all the fields.")
        return

    patients.append({"Name": name, "Age": age, "Category": category, "File": file})
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    file_path.set("")
    list_patients()
    messagebox.showinfo("Success", "Patient added successfully!")

def list_patients():

    """List all patient details."""

    patient_list.delete(0, tk.END)
    for patient in patients:
        patient_list.insert(tk.END, f"{patient['Name']} - {patient['Category']}")

def browse_file():

    """Open file dialog to select a file."""

    file = filedialog.askopenfilename()
    if file:
        file_path.set(file)

def show_graph():

    """Generate and display a bar graph of patient categories."""

    categories = [patient['Category'] for patient in patients]
    count = Counter(categories)
    labels = list(count.keys())
    values = list(count.values())

    # Plot the bar graph
    plt.figure(figsize=(8, 6))
    plt.bar(labels, values, color=['blue', 'green', 'orange', 'red'])
    plt.xlabel("Age Categories")
    plt.ylabel("Number of Patients")
    plt.title("Patients by Age Category")
    plt.show()

# Main application
root = tk.Tk()
root.title("Healthcare Dashboard")
root.geometry("600x500")


# Widgets
tk.Label(root, text="Healthcare Dashboard", font=("Arial", 16)).pack(pady=10)


# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)


tk.Label(input_frame, text="Name: ").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)


tk.Label(input_frame, text="Age: ").grid(row=1, column=0, padx=5, pady=5, sticky="e")
age_entry = tk.Entry(input_frame, width=30)
age_entry.grid(row=1, column=1, padx=5, pady=5)


tk.Label(input_frame, text="Age Category: ").grid(row=2, column=0, padx=5, pady=5, sticky="e")
age_category = ttk.Combobox(input_frame, values=["Children", "Youth", "Adult", "Senior"], width=28)
age_category.grid(row=2, column=1, padx=5, pady=5)


tk.Label(input_frame, text="File: ").grid(row=3, column=0, padx=5, pady=5, sticky="e")
file_path = tk.StringVar()
file_entry = tk.Entry(input_frame, textvariable=file_path, width=30, state="readonly")
file_entry.grid(row=3, column=1, padx=5, pady=5)
tk.Button(input_frame, text="Browse", command=browse_file).grid(row=3, column=2, padx=5, pady=5)


tk.Button(input_frame, text="Add Patient", command=add_patient, bg="green", fg="white").grid(row=4, columnspan=3, pady=10)


# Patient List
tk.Label(root, text="Patients:").pack()
patient_list = tk.Listbox(root, width=60, height=10)
patient_list.pack(pady=10)

# Show Graph Button
tk.Button(root, text="Show Graph", command=show_graph, bg="blue", fg="white").pack(pady=10)

# Run the application
root.mainloop()
