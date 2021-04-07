import numpy as np
from scipy.ndimage import convolve


def loaddata(path):
    """ Load bayerdata from file

    Args:
        Path of the .npy file
    Returns:
        Bayer data as numpy array (H,W)
    """

    return np.load(path)


def separatechannels(bayerdata):
    """ Separate bayer data into RGB channels so that
    each color channel retains only the respective
    values given by the bayer pattern and missing values
    are filled with zero

    Args:
        Numpy array containing bayer data (H,W)
    Returns:
        red, green, and blue channel as numpy array (H,W)
    """

    r_mask = np.zeros(bayerdata.shape)
    r_mask[0::2, 1::2] = 1
    r = bayerdata * r_mask
    
    g_mask = np.zeros(bayerdata.shape)
    g_mask[0::2, 0::2] = 1
    g_mask[1::2, 1::2] = 1
    g = bayerdata * g_mask

    b_mask = np.zeros(bayerdata.shape)
    b_mask[1::2, 0::2] = 1
    b = bayerdata * b_mask

    return r, g, b


def assembleimage(r, g, b):
    """ Assemble separate channels into image

    Args:
        red, green, blue color channels as numpy array (H,W)
    Returns:
        Image as numpy array (H,W,3)
    """

    img = np.stack((r, g, b), axis=-1)
    return img


def interpolate(r, g, b):
    """ Interpolate missing values in the bayer pattern
    by using bilinear interpolation

    Args:
        red, green, blue color channels as numpy array (H,W)
    Returns:
        Interpolated image as numpy array (H,W,3)
    """

    rb_filter = np.array([[1/4, 1/2, 1/4], [1/2, 1, 1/2], [1/4, 1/2, 1/4]])
    g_filter = np.array([[0, 1/4, 0], [1/4, 1, 1/4], [0, 1/4, 0]])

    ch_r = convolve(r, rb_filter, mode='mirror')
    ch_g = convolve(g, g_filter, mode='mirror')
    ch_b = convolve(b, rb_filter, mode='mirror')

    img = np.stack((ch_r, ch_g, ch_b), axis=-1)

    return img