import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample Sales Data
data = {
    "Month": ["January", "February", "March", "April", "May", "June"],
    "Sales": [5000, 7000, 4500, 8000, 6000, 7500]
}

# Create a DataFrame
df = pd.DataFrame(data)

# 1. Calculate Total Sales
total_sales = np.sum(df["Sales"])

# 2. Calculate Average Sales
average_sales = np.mean(df["Sales"])

# 3. Create a Bar Chart to Visualize Sales Data
plt.figure(figsize=(8, 5))
plt.bar(df["Month"], df["Sales"], color="skyblue")
plt.title("Sales Data Visualization")
plt.xlabel("Month")
plt.ylabel("Sales (in units)")
plt.show()

# Display Results
print("Sales Data Analysis:")
print(df)
print(f"\nTotal Sales: ₹{total_sales}")
print(f"Average Sales: ₹{average_sales:.2f}")
