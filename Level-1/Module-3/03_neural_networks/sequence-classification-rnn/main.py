import torch
from torch import nn


class SequenceClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.rnn = nn.RNN(4, 12, batch_first=True)
        self.output = nn.Linear(12, 2)

    def forward(self, values):
        return self.output(self.rnn(values)[0][:, -1])


model = SequenceClassifier()
print(model(torch.randn(3, 6, 4)).shape)
