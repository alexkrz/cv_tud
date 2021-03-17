import os
import numpy as np
import matplotlib.pyplot as plt


def display_image(img):
    """ Show an image with matplotlib:

    Args:
        Image as numpy array (H,W,3)
    """

    plt.imshow(img)


def save_as_npy(path, img):
    """ Save the image array as a .npy file:

    Args:
        Image as numpy array (H,W,3)
    """

    np.save(os.path.join("data", path), img)


def load_npy(path):
    """ Load and return the .npy file:

    Args:
        Path of the .npy file
    Returns:
        Image as numpy array (H,W,3)
    """

    return np.load(os.path.join("data", path))


def mirror_horizontal(img):
    """ Create and return a horizontally mirrored image:

    Args:
        Loaded image as numpy array (H,W,3)

    Returns:
        A horizontally mirrored numpy array (H,W,3).
    """

    return np.flip(img, axis=1)


def display_images(img1, img2):
    """ display the normal and the mirrored image in one plot:

    Args:
        Two image numpy arrays
    """

    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(img1)
    axes[0].set_title("Original Image")
    axes[1].imshow(img2)
    axes[1].set_title("Flipped Image")
