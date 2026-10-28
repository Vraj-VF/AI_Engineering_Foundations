import math
import torch


def positional_encoding(length, dimensions):
    result = torch.zeros(length, dimensions)
    positions = torch.arange(length).unsqueeze(1)
    scale = torch.exp(torch.arange(0, dimensions, 2) * (-math.log(10000) / dimensions))
    result[:, 0::2] = torch.sin(positions * scale)
    result[:, 1::2] = torch.cos(positions * scale)
    return result


values = torch.randn(5, 8)
enriched = values + positional_encoding(5, 8)
print(enriched.shape)
