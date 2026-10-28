"""Synchronize measurements and calculate calibrated reference poses.

Inputs: recorded Mighty streams and arm encoder readings, calibrated forward
kinematics, and the wrist-to-camera transform.
Outputs: time-aligned reference poses expressed in the same body frame as
Mighty, with uncertainty; a calibrated reference, not exact ground truth.
Training and evaluation only; never used at deployment.
"""
