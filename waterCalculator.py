import tkinter as tk

def calculate_water_usage():
    showers_per_week = int(showers_entry.get())
    bathroom_visits_per_day = int(bathroom_entry.get())
    laundry_loads_per_month = int(laundry_entry.get())
    water_efficient_toilets = toilet_var.get()
    water_efficient_sinks = sink_var.get()

    SHOWER_USAGE = 2.5
    TOILET_USAGE = 1.6
    CLOTHES_USAGE = 41

    total_water_usage = (showers_per_week * 52 * SHOWER_USAGE) + (bathroom_visits_per_day * 365 * TOILET_USAGE) + (laundry_loads_per_month * CLOTHES_USAGE)

    if water_efficient_toilets:
        total_water_usage *= 0.75

    if water_efficient_sinks:
        total_water_usage *= 0.9

    average_daily_usage = total_water_usage / 365
    result_label.config(text=f"Your average daily water usage is {average_daily_usage:.2f} gallons.")

# Create the main window
root = tk.Tk()
root.title("Water Usage Calculator")

# Labels and Entries
tk.Label(root, text="Showers per week:").grid(row=0, column=0)
showers_entry = tk.Entry(root)
showers_entry.grid(row=0, column=1)

tk.Label(root, text="Bathroom visits per day:").grid(row=1, column=0)
bathroom_entry = tk.Entry(root)
bathroom_entry.grid(row=1, column=1)

tk.Label(root, text="Laundry loads per month:").grid(row=2, column=0)
laundry_entry = tk.Entry(root)
laundry_entry.grid(row=2, column=1)

toilet_var = tk.BooleanVar()
tk.Checkbutton(root, text="Water-efficient toilets", variable=toilet_var).grid(row=3, column=0)

sink_var = tk.BooleanVar()
tk.Checkbutton(root, text="Water-efficient sinks", variable=sink_var).grid(row=4, column=0)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_water_usage)
calculate_button.grid(row=5, column=0, columnspan=2)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2)

root.mainloop()
