"""Define the future causal model for corrections to relative pose increments.

Inputs: past and current Mighty pose, IMU, and tracking signals only.
Outputs: corrections to Mighty's relative pose increments, without using
future samples or arm measurements.
"""
