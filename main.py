import cv2
import numpy as np
import matplotlib.pyplot as plt

LEFT_PATH  = "images/aloel.jpg"
RIGHT_PATH = "images/aloer.jpg"

left = cv2.imread(LEFT_PATH, cv2.IMREAD_GRAYSCALE)
right = cv2.imread(RIGHT_PATH, cv2.IMREAD_GRAYSCALE)

if left is None or right is None:
    raise FileNotFoundError("Could not load stereo images.")
if left.shape != right.shape:
    raise ValueError(f"Image sizes differ: {left.shape} vs {right.shape}")

print("Image shape:", left.shape)

# Slight blur to stabilize matching
left_blur = cv2.GaussianBlur(left, (3, 3), 0)
right_blur = cv2.GaussianBlur(right, (3, 3), 0)

min_disp = 0
num_disp = 64   # Aloe needs a wider search range
block = 7

left_matcher = cv2.StereoSGBM_create(
    minDisparity=min_disp,
    numDisparities=num_disp,
    blockSize=block,
    P1=8 * block**2,
    P2=32 * block**2,
    uniquenessRatio=10,
    speckleWindowSize=100,
    speckleRange=32,
    disp12MaxDiff=1,
    mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
)

# Right matcher for WLS
right_matcher = cv2.ximgproc.createRightMatcher(left_matcher)

disp_left = left_matcher.compute(left_blur, right_blur).astype(np.int16)
disp_right = right_matcher.compute(right_blur, left_blur).astype(np.int16)

# WLS filter
wls = cv2.ximgproc.createDisparityWLSFilter(left_matcher)
wls.setLambda(8000)
wls.setSigmaColor(1.5)

disp = wls.filter(disp_left, left_blur, None, disp_right).astype(np.float32) / 16.0

# Visualization
disp_vis = disp.copy()
disp_vis[disp_vis <= 0] = np.nan

vmin = np.nanpercentile(disp_vis, 5)
vmax = np.nanpercentile(disp_vis, 95)

plt.figure(figsize=(10,5))
plt.imshow(disp_vis, cmap="plasma", vmin=vmin, vmax=vmax)
plt.colorbar()
plt.title("Aloe Stereo Disparity (SGBM + WLS)")
plt.tight_layout()
plt.show()

valid_pct = 100.0 * np.mean(~np.isnan(disp_vis))
print(f"Valid disparity pixels: {valid_pct:.1f}%")
