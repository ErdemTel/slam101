"""Compare raw and corrected trajectories.

Inputs: raw Mighty trajectories, corrected trajectories from ``infer``, and,
where available, reference poses with uncertainty.
Outputs: trajectory error comparisons, including independent tests after the
camera is removed from the arm.
"""
