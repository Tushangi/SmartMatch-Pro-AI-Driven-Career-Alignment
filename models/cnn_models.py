from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense

def cnn_model(vocab_size=5000):
    model = Sequential([
        Embedding(vocab_size, 128),
        Conv1D(64, 5, activation='relu'),
        GlobalMaxPooling1D(),
        Dense(64, activation='relu')
    ])
    return model
