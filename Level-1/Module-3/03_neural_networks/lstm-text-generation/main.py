import torch
from torch import nn


class LSTMGenerator(nn.Module):
    def __init__(self, vocabulary):
        super().__init__()
        self.embedding = nn.Embedding(vocabulary, 16)
        self.lstm = nn.LSTM(16, 32, batch_first=True)
        self.output = nn.Linear(32, vocabulary)

    def forward(self, tokens):
        return self.output(self.lstm(self.embedding(tokens))[0])


model = LSTMGenerator(20)
print(model(torch.randint(0, 20, (2, 10))).shape)
