from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def ann_model(input_dim=64):
    model = Sequential([
        Dense(32, activation='relu', input_dim=input_dim),
        Dense(1, activation='sigmoid')
    ])
    return model
