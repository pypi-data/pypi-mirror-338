import torch
import torch.nn as nn
import torch.nn.functional as F

class AutoMixedActivation(nn.Module):
    """
    Automatically applies mixed activations at the neuron/channel level.
    Compatible with both image tensors (4D: B,C,H,W) and transformer tensors (3D: B,T,D).
    """

    def __init__(self, activations=None):
        super().__init__()
        self.activations = activations or [
            lambda x: F.relu(x),
            lambda x: F.gelu(x),
            lambda x: x * torch.sigmoid(x)  # Swish
        ]

    def forward(self, x):
        n = len(self.activations)

        if x.dim() == 4:
            # CNN-style input (B, C, H, W)
            splits = torch.chunk(x, n, dim=1)
        elif x.dim() == 3:
            # Transformer-style input (B, T, D)
            splits = torch.chunk(x, n, dim=2)
        else:
            raise ValueError("Unsupported input shape: expected 3D or 4D tensor")

        activated = [act(split) for act, split in zip(self.activations, splits)]
        return torch.cat(activated, dim=2 if x.dim() == 3 else 1)
