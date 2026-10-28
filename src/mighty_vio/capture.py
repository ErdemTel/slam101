"""Record timestamped Mighty streams and optional arm measurements.

Inputs: live Mighty pose, IMU, and tracking streams; optionally SO-101 joint
encoder readings when the camera is mounted on the arm.
Outputs: per-session recordings with each stream's native timestamps preserved.
"""
