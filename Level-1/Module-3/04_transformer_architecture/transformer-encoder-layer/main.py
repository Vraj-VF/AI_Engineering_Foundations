import torch
from torch import nn


class EncoderLayer(nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = nn.MultiheadAttention(16, 4, batch_first=True)
        self.feed_forward = nn.Sequential(
            nn.Linear(16, 32), nn.ReLU(), nn.Linear(32, 16)
        )
        self.norm = nn.LayerNorm(16)

    def forward(self, values):
        attended = self.attention(values, values, values)[0]
        values = self.norm(values + attended)
        return self.norm(values + self.feed_forward(values))


layer = EncoderLayer()
print(layer(torch.randn(2, 6, 16)).shape)
