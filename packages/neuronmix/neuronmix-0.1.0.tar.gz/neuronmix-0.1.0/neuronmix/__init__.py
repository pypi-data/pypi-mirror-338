import torch
import torch.nn as nn
import torch.nn.functional as F

class AutoMixedActivation(nn.Module):
    """
    Automatically applies mixed activations at the neuron (channel) level.
    Splits input tensor along the channel dimension and applies different 
    activation functions to each split automatically.
    """

    def __init__(self, activations=None):
        super().__init__()
        self.activations = activations or [
            lambda x: F.relu(x),
            lambda x: F.gelu(x),
            lambda x: x * torch.sigmoid(x)  # Swish
        ]

    def forward(self, x):
        B, C, H, W = x.shape
        n = len(self.activations)
        if C % n != 0:
            raise ValueError(f"Channels ({C}) must be divisible by number of activations ({n})")
        chunks = torch.chunk(x, n, dim=1)
        return torch.cat([act(c) for act, c in zip(self.activations, chunks)], dim=1)
