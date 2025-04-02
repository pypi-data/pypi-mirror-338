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
        splits = torch.chunk(x, n, dim=1)  # Handles uneven splits
        activated = [act(split) for act, split in zip(self.activations, splits)]
        return torch.cat(activated, dim=1)
