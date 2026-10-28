import torch
from torch import nn


class ModifiedCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 16, 3),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, 3),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.classifier = nn.Linear(32 * 5 * 5, 10)

    def forward(self, image):
        return self.classifier(self.features(image).flatten(1))


model = ModifiedCNN()
print(model(torch.randn(4, 1, 28, 28)).shape)
