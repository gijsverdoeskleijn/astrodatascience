#Obtained from ChatGPT4 at https://chat.openai.com/share/f323b186-4439-448f-9fd6-f064cbdc1efe
import matplotlib.pyplot as plt
import numpy as np

# Define the catalogs and their sizes
catalogs = ['Hipparchus', 'Ptolemy', 'Tycho Brahe', 'John Flamsteed', 'Henry Draper',
            'Hipparcos', 'Tycho-2', 'Gaia DR1', 'Gaia DR2', 'Gaia DR3']
star_counts = [1000, 1022, 1000, 3000, 225000, 118218, 2539913, 1e9, 1.7e9, 1.8e9]

# Convert counts to a logarithmic scale to better visualize changes
log_star_counts = np.log10(star_counts)

# Plotting
plt.figure(figsize=(10, 5))  # Set the figure size
plt.bar(catalogs, log_star_counts, color='skyblue')
plt.xlabel('Catalog')
plt.ylabel('Log of Star Count')
plt.title('Increase in Size of Stellar Catalogs Over Time')
plt.xticks(rotation=45)  # Rotate x labels for better readability
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()  # Adjust layout to not cut off labels

# Show the plot
plt.show()
