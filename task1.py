import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("flipkart_products_20250405.csv")

# Set Seaborn style and context
sns.set(style="darkgrid", context="talk")

# Create the histogram plot
plt.figure(figsize=(12, 7))
hist = sns.histplot(
    df["Price (₹)"],
    bins=40,
    kde=True,
    color="#33f6ff",           
    edgecolor="black",         # Bar border color
    linewidth=1.2              # Border width
)

# Add title and axis labels
hist.set_title("📦 Price Distribution of Flipkart Products", fontsize=20, fontweight='bold', pad=20)
hist.set_xlabel("Price in ₹", fontsize=14)
hist.set_ylabel("Number of Products", fontsize=14)

# Customize grid
plt.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout
plt.tight_layout()