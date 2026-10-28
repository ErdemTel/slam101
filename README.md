# slam101

Learned correction of visual–inertial odometry (VIO) for the Mighty Camera.

## Objective

An SO-101 arm moves a wrist-mounted Mighty Camera. Synchronized encoder
measurements, calibrated forward kinematics, and a wrist-to-camera transform
provide reference motion for training a temporal model that corrects Mighty's
VIO. The correction must keep working after the camera is removed from the arm.

## Status

Early development: architecture scaffold only. Nothing is implemented and there
are no measured results.

## Training vs. deployment

- **Training and evaluation** use arm encoders and kinematics as a calibrated
  reference with uncertainty, not exact ground truth.
- **Deployment** uses only Mighty's pose, IMU, and tracking signals. Encoder
  data is never a deployment input.

Reference and training dependencies are kept separate from inference
(`reference` and `train` extras in `pyproject.toml`).

## Layout

```
src/mighty_vio/
  capture.py    record Mighty streams and optional arm measurements
  reference.py  synchronize and compute calibrated reference poses
  model.py      causal model for relative pose-increment corrections
  train.py      training with trajectory- and session-level splits
  infer.py      Mighty-only correction (host computer first)
  evaluate.py   raw vs. corrected trajectories, including off-arm tests
```
