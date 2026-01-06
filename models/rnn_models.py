from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dense

def rnn_model(vocab_size=5000):
    model = Sequential([
        Embedding(vocab_size, 128),
        LSTM(64),
        Dense(64, activation='relu')
    ])
    return model
