# NeuronMix 🧠

[![PyPI version](https://img.shields.io/pypi/v/neuronmix.svg)](https://pypi.org/project/neuronmix/)
[![Python](https://img.shields.io/pypi/pyversions/neuronmix.svg)](https://pypi.org/project/neuronmix/)
[![License](https://img.shields.io/github/license/ajaviaad/neuronmix)](https://github.com/ajaviaad/neuronmix/blob/main/LICENSE)

NeuronMix is a lightweight PyTorch module for applying **neuron-level mixed activations** automatically.  
It splits input tensors along channels and applies different activation functions like ReLU, GELU, and Swish — enabling better feature diversity and adversarial robustness.

---

## 🚀 Features

- ✅ Drop-in activation layer for PyTorch
- 🧠 Mixes ReLU, GELU, and Swish across channels
- 🔁 Works with CNNs, ResNet, and custom models
- 🔒 Designed for adversarial robustness

---

## 📦 Installation

Install directly from PyPI:

```bash
pip install neuronmix
