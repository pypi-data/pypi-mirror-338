"""
Utils.

This module contains utility functions used in the JaxILI package.
Some functions are used to format the input data for the training.
Other functions allow to check the validity of the input data.
"""

from typing import Any, Callable, Sequence, Union

import jax.numpy as jnp
import jax_dataloader as jdl
import numpy as np


def create_data_loader(
    *datasets: Sequence[jdl.DataLoader],
    train: Union[bool, Sequence[bool]] = True,
    batch_size: int = 128,
):
    """
    Create data loaders from a set of datasets.

    Parameters
    ----------
    datasets : Datasets for which data loaders are created.
    train : Sequence indicating which datasets are used for training and which not.
    If single bool, the same value is used for all datasets.
    batch_size : Batch size to use in the data loaders.

    Returns
    -------
    list[jdl.DataLoader]
        List of data loaders.
    """
    loaders = []
    if not isinstance(train, (list, tuple)):
        train = [train for _ in datasets]
    for dataset, is_train in zip(datasets, train):
        loader = jdl.DataLoader(
            dataset,
            "jax",
            batch_size=batch_size,
            shuffle=is_train,
            drop_last=is_train,
        )
        loaders.append(loader)
    return loaders


def check_density_estimator(estimator_arg: str):
    """
    Check density estimator argument to see if it belongs to the authorized network.

    Parameters
    ----------
    estimator_arg : str
        Density estimator argument to check.
    """
    if estimator_arg not in ["maf", "mdn", "realnvp"]:
        raise ValueError(
            f"Invalid density estimator argument: {estimator_arg}. Options are 'maf', 'mdn' and 'realnvp'."
        )


def validate_theta_x(theta: Any, x: Any):
    r"""
    Check if the passed $(\theta, x)$ pair is valid.

    We check that:
    - $\theta$ and $x$ are jax arrays
    - $\theta$ and $x$ have the same number of samples.
    - $\theta$ and $x$ have dtype=float32.

    Raises
    ------
        AssertionError if $\theta$ and $x$ are not jax arrays, do not have the same batch size or are not dtype==np.float32.

    Parameters
    ----------
    theta : Any
        Parameters of the simulations.
    x : Any
        Simulation outputs.
    """
    assert isinstance(theta, jnp.ndarray) or isinstance(
        theta, np.ndarray
    ), "theta should be a jax array."
    assert isinstance(x, jnp.ndarray) or isinstance(
        x, np.ndarray
    ), "x should be a jax array."
    assert (
        theta.shape[0] == x.shape[0]
    ), f"Number of parameter sets ({theta.shape[0]}) and number of simulation outputs ({x.shape[0]}) should be the same."

    assert theta.dtype == jnp.float32, "theta should have dtype float32."
    assert x.dtype == jnp.float32, "x should have dtype float32."

    batch_size = theta.shape[0]

    return theta, x, batch_size


def check_hparams_maf(hparams: dict):
    """
    Check the hyperparameters of the Masked Autoregressive Flow.

    Parameters
    ----------
    hparams : dict
        Dictionary with the hyperparameters of the MAF.
    """
    assert "n_layers" in hparams, "n_layers not found in hyperparameters."
    assert "layers" in hparams, "layers not found in hyperparameters."
    assert "activation" in hparams, "activation not found in hyperparameters."
    assert "use_reverse" in hparams, "use_reverse not found in hyperparameters."

    assert isinstance(hparams["n_layers"], int), "n_layers should be an int."
    assert isinstance(hparams["layers"], list), "layers should be a list of int."
    assert callable(hparams["activation"]), "activation should be a callable."
    assert isinstance(hparams["use_reverse"], bool), "use_reverse should be a boolean."


def check_hparams_realnvp(hparams: dict):
    """
    Check the hyperparameters of the RealNVP.

    Parameters
    ----------
    hparams : dict
        Dictionary with the hyperparameters of the RealNVP.
    """
    assert "n_layers" in hparams, "n_layers not found in hyperparameters."
    assert "layers" in hparams, "layers not found in hyperparameters."
    assert "activation" in hparams, "activation not found in hyperparameters."

    assert isinstance(hparams["n_layers"], int), "n_layers should be an int."
    assert isinstance(hparams["layers"], list), "layers should be a list of int."
    assert callable(hparams["activation"]), "activation should be a callable."


def check_hparams_mdn(hparams: dict):
    """
    Check the hyperparameters of the Mixture Density Network.

    Parameters
    ----------
    hparams : dict
        Dictionary with the hyperparameters of the MDN.
    """
    assert "n_components" in hparams, "n_components not found in hyperparameters."
    assert "layers" in hparams, "layers not found in hyperparameters."
    assert "activation" in hparams, "activation not found in hyperparameters."

    assert isinstance(hparams["n_components"], int), "n_components should be an int."
    assert isinstance(hparams["layers"], list), "layers should be a list of int."
    assert callable(hparams["activation"]), "activation should be a callable."


def handle_non_serializable(obj):
    """
    Replace or transform objects into something serializable to save metadata from training.

    Custom handler for non-serializable objects.

    Parameters
    ----------
    obj : Any
        Object to handle.
    """
    return str(obj)  # Default behavior is to convert to string
