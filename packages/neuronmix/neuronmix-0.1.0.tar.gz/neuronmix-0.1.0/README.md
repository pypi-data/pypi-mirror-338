# NeuronMix 🧠

NeuronMix is a lightweight PyTorch module for applying **neuron-level mixed activations** automatically.

## Features
- Mix ReLU, GELU, Swish across channel groups
- Plug-and-play with any CNN layer
- Great for adversarial robustness and experimentation

## Installation

Clone or install via pip:

```bash
pip install .
```

## Usage

```python
from neuronmix import AutoMixedActivation

act = AutoMixedActivation()
out = act(input_tensor)  # Tensor shape: (B, C, H, W)
```

## License
MIT © Muhammad Adeel Javaid
