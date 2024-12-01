import pandas as pd
import numpy as np

def generate_mock_data():
    # Simulate heart rate and glucose level data for testing.
    np.random.seed(42)
    data = pd.DataFrame({
        'heart_rate': np.random.randint(50, 150, 100),  # Random heart rate
        'glucose_level': np.random.randint(60, 200, 100)  # Random glucose level
    })
    return data
