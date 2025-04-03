import torch

import penn


###############################################################################
# Voiced/unvoiced
###############################################################################


def interpolate(pitch, periodicity, value):
    """Fill unvoiced regions via linear interpolation"""
    # Threshold periodicity
    voiced = threshold(periodicity, value)

    # Handle no voiced frames
    if not voiced.any():
        return pitch

    # Pitch is linear in base-2 log-space
    pitch = torch.log2(pitch)

    # Anchor endpoints
    pitch[..., 0] = pitch[voiced][..., 0]
    pitch[..., -1] = pitch[voiced][..., -1]
    voiced[..., 0] = True
    voiced[..., -1] = True

    # Interpolate
    pitch[~voiced] = penn.interpolate(
        torch.where(~voiced[0])[0][None],
        torch.where(voiced[0])[0][None],
        pitch[voiced][None])

    return 2 ** pitch


def threshold(periodicity, value):
    """Threshold periodicity to produce voiced/unvoiced classifications"""
    return periodicity > value
