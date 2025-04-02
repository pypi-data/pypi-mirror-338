import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("arcjetcv_calibration_2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Chessboard pattern size (columns, rows) of inner corners
pattern_size = (9, 6)

# Find corners
ret, corners = cv2.findChessboardCorners(
    gray,
    pattern_size,
    flags=cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE,
)

if not ret:
    print("❌ Chessboard pattern not found.")
    exit()

# Refine corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

# Prepare object points (real-world coords)
objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0 : pattern_size[0], 0 : pattern_size[1]].T.reshape(-1, 2)

# Calibrate
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
    [objp], [corners], gray.shape, None, None
)

# Show calibration metrics
print("\n=== 📐 Calibration Results ===")
print("Focal Length (fx, fy):", mtx[0, 0], mtx[1, 1])
print("Principal Point (cx, cy):", mtx[0, 2], mtx[1, 2])
print("Distortion Coefficients:", dist.ravel().tolist())

# Undistort
undistorted = cv2.undistort(img, mtx, dist)

# Show result
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(undistorted, cv2.COLOR_BGR2RGB))
plt.title("Undistorted")
plt.axis("off")
plt.tight_layout()
plt.show()
