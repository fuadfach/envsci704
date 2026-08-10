"""
Verification script for Python environment setup
University of Auckland - ENVSCI 704
"""

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

print("=" * 50)
print("Python Environment Verification")
print("=" * 50)

# Check Python version
print(f"\n✅ Python version: {sys.version.split()[0]}")

# Check package versions
print(f"✅ numpy version: {np.__version__}")
print(f"✅ pandas version: {pd.__version__}")
print(f"✅ scipy version: {scipy.__version__}")
print(f"✅ matplotlib version: {plt.matplotlib.__version__}")

# Test pandas and numpy functionality
print("\n" + "=" * 50)
print("Testing pandas and numpy...")
print("=" * 50)

# Create a sample DataFrame with three New Zealand cities
cities = pd.DataFrame({
    'city': ['Auckland', 'Wellington', 'Christchurch'],
    'population': [1657200, 215100, 381500],
    'mean_temp_c': [15.2, 12.8, 12.1]
})

print(cities)

# A taste of the modelling to come: 5% decay per day for 10 days
decay = 100 * (1 - 0.05) ** np.arange(11)
print(f"\nTracer after 10 days of 5% daily decay: {decay[-1]:.1f} mg/L")

print("\n✅ All tests passed! Your modelling environment is ready.")
print("\n" + "=" * 50)