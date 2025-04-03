"""
Compressor.

This module contains classes that implement compressors used in JaxILI.
"""

from typing import Any, Callable
from jaxtyping import Array

import flax.linen as nn


class Identity(nn.Module):
    """Identity transformation."""

    @nn.compact
    def __call__(self, x):
        """
        Forward pass of the identity transformation.

        Parameters
        ----------
        x : jnp.Array
            Input data.

        Returns
        -------
        jnp.Array
            Output data.
        """
        return x


class Standardizer(nn.Module):
    """Standardizer transformation."""

    mean: Array
    std: Array

    @nn.compact
    def __call__(self, x):
        """
        Forward pass of the standardizer transformation. The standardization uses the z-score.

        Parameters
        ----------
        x : jnp.Array
            Input data.

        Returns
        -------
        jnp.Array
            Standardized data.
        """
        return (x - self.mean) / self.std


class MLPCompressor(nn.Module):
    """
    Base class of a MLP Compressor.

    Defines a MLP compressor to send the summary statistic to the same dimension than the parameters.

    Parameters
    ----------
    hidden_size : list
        List with the size of the hidden layers.
    activation : Callable
        Activation function. Preferably from `jax.nn` or `jax.nn.activation`.
    output_size : int
        Size of the output layer.
    """

    hidden_size: list
    activation: Callable
    output_size: int

    @nn.compact
    def __call__(self, x):
        """
        Forward pass of the MLP Compressor.

        Parameters
        ----------
        x : jnp.array
            Input data.

        Returns
        -------
        jnp.array
            Compressed data.
        """
        for size in self.hidden_size:
            x = nn.Dense(size)(x)
            x = self.activation(x)
        x = nn.Dense(self.output_size)(x)
        return x


class CNN2DCompressor(nn.Module):
    """
    Base class of a CNN2D Compressor.

    Defines a 2 dimensional Convolutional Neural Network to compress the data to the same dimension as the parameters.

    Parameters
    ----------
    output_size : int
        Size of the output layer
    activation : Callable
        Activation function. Preferably from `jax.nn` or `jax.nn.activation`.
    """

    output_size: int
    activation: Callable

    @nn.compact
    def __call__(self, inputs):
        """
        Forward pass of the CNN2D Compressor.

        Parameters
        ----------
        inputs : jnp.array
            Input data.

        Returns
        -------
        jnp.array
            Compressed data.
        """
        net_x = nn.Conv(32, 3, 2)(inputs)
        net_x = self.activation(net_x)
        net_x = nn.Conv(64, 3, 2)(net_x)
        net_x = self.activation(net_x)
        net_x = nn.Conv(128, 3, 2)(net_x)
        net_x = self.activation(net_x)
        net_x = nn.avg_pool(net_x, (16, 16), (8, 8), padding="SAME")
        # Flatten the tensor
        net_x = net_x.reshape((net_x.shape[0], -1))
        net_x = nn.Dense(64)(net_x)
        net_x = self.activation(net_x)
        net_x = nn.Dense(self.output_size)(net_x)
        return net_x.squeeze()
