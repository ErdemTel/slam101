"""Train the correction model using reference motion.

Inputs: synchronized Mighty recordings paired with reference poses and their
uncertainty from ``reference``.
Outputs: trained model checkpoints. Data is split by complete trajectories
and sessions, never by individual samples, to avoid leakage.
"""
