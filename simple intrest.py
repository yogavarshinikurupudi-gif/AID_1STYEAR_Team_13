from tkinter import *   # Step 1: Import everything from Tkinter

# Step 2: Create the main window (called 'root')
root = Tk()
root.title("Simple Interest Calculator")   # Title of the window
root.geometry("350x300")                   # Set size of the window
root.config(bg="lightyellow")              # Set background color

# Step 3: Define a function to calculate simple interest
def calculate_interest():
    # Get values from the input boxes
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())

    # Calculate simple interest
    interest = (principal * rate * time) / 100

    # Display the result
    result_label.config(text=f"Simple Interest = ₹{interest:.2f}")

# Step 4: Create and place labels, entry boxes, and buttons
heading = Label(root, text="Simple Interest Calculator", font=("Arial", 14, "bold"), bg="lightyellow")
heading.pack(pady=10)

# Principal
principal_label = Label(root, text="Principal (₹):", bg="lightyellow")
principal_label.pack()
principal_entry = Entry(root)
principal_entry.pack()

# Rate
rate_label = Label(root, text="Rate of Interest (%):", bg="lightyellow")
rate_label.pack()
rate_entry = Entry(root)
rate_entry.pack()

# Time
time_label = Label(root, text="Time (in years):", bg="lightyellow")
time_label.pack()
time_entry = Entry(root)
time_entry.pack()

# Calculate button
calculate_button = Button(root, text="Calculate", bg="lightgreen", command=calculate_interest)
calculate_button.pack(pady=10)

# Result label
result_label = Label(root, text="Simple Interest = ₹0.00", font=("Arial", 12, "bold"), bg="lightyellow")
result_label.pack(pady=5)

# Step 5: Run the Tkinter main loop
root.mainloop()
