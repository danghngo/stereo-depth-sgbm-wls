# stereo-depth-sgbm-wls
Stereo depth pipeline using OpenCV SGBM + WLS. Geometric systems study of baseline scaling and depth uncertainty.

# Stereo Depth Estimation Pipeline  
OpenCV SGBM + WLS Filtering  
Author: Dang Ngo  
MS Applied Mathematics  

---

## 1. Project Overview

This project implements a stereo depth estimation pipeline using:

- OpenCV Semi-Global Block Matching (SGBM)
- Weighted Least Squares (WLS) disparity refinement
- Geometric depth reconstruction via triangulation

Dataset:
- Aloe stereo pair (OpenCV sample dataset)

The purpose of this project is not only to compute disparity maps,
but to study geometric depth behavior as a systems problem.

---

## 2. Stereo Geometry

Depth is computed via standard pinhole stereo triangulation:

Z = fB / d

Where:
- Z = depth
- f = focal length
- B = baseline
- d = disparity

---

## 3. Uncertainty Propagation

Using first-order error propagation:

σ_Z = (Z² / fB) σ_d

This reveals:

- Depth uncertainty increases quadratically with distance
- Depth uncertainty decreases linearly with baseline
- Disparity noise is the fundamental stability bottleneck

This equation forms the theoretical basis for the systems study.

---

## 4. Pipeline Architecture

1. Load rectified stereo pair
2. Compute disparity using StereoSGBM
3. Apply WLS filtering for noise suppression
4. Convert disparity to depth map
5. Analyze depth behavior

---

## 5. Parameter Study

### Optimal numDisparities

Empirically determined:

numDisparities ≈ 80

This value balances:

- Sufficient disparity range
- Matching robustness
- Noise suppression
- Computational cost

---

## 6. Geometric Systems Study (In Progress)

The following structured experiments are planned:

### A. Baseline Scaling
Study depth variance as a function of baseline length.

Prediction:
σ_Z ∝ 1 / B

---

### B. Disparity Range vs Robustness
Evaluate how increasing disparity search window impacts:

- Error rate
- Invalid pixels
- False matches
- Runtime

---

### C. Long-Range Failure Threshold

From:

Z_max = fB / σ_d

Determine the theoretical range limit where
depth uncertainty equals measured depth.

---

## 7. Files

main.py
- Full stereo pipeline implementation

requirements.txt
- Python dependencies

sample_images/
- Aloe stereo pair

results/
- Generated disparity and depth maps

---

## 8. Motivation

This project is part of a broader investigation into:

- Geometric robustness in stereo systems
- Depth stability under noise
- Baseline optimization strategies
- Long-range sensing limitations

Applications include:
- Satellite stereo imaging
- Aerial mapping
- 3D reconstruction
- Robotic vision

---

## 9. Future Work

- Covariance matrix propagation
- Subpixel disparity modeling
- Baseline optimization curves
- Long-range degradation simulation
- Extension to multi-view stereo

---


