import numpy as np
import matplotlib.pyplot as plt
import cv2

# Loading the picture and switching its color format from BGR to RGB
rgb_picture = cv2.cvtColor(cv2.imread('1st_img.jpeg'), cv2.COLOR_BGR2RGB)

# Setting up a figure area for multiple images
figure_layout = plt.figure(figsize=(15, 5))

# Showcasing the untouched picture
plt.subplot(1, 4, 1)
plt.imshow(rgb_picture)
plt.title('Base Image')

# Modifying the structure of the picture to a matrix of RGB color codes
color_matrix = rgb_picture.reshape((-1, 3))

# Adjusting the type of matrix elements for the algorithm
color_matrix_float = np.float32(color_matrix)

# Establishing the algorithm's stopping rules
kmeans_parameters = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)

# Selecting a set of cluster counts to examine
cluster_options = [3, 10, 20]

# Applying the algorithm with various cluster counts
for panel_index, cluster_number in enumerate(cluster_options, start=2):
    # Clustering the color data
    _, cluster_labels, cluster_centers = cv2.kmeans(color_matrix_float, cluster_number, None, kmeans_parameters, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Recasting cluster centers for image reconstruction
    redefined_centers = np.uint8(cluster_centers)
    recolored_matrix = redefined_centers[cluster_labels.flatten()]

    # Rebuilding the picture with the clustered colors
    clustered_picture = recolored_matrix.reshape((rgb_picture.shape))

    # Displaying the newly colored picture
    plt.subplot(1, 4, panel_index)
    plt.imshow(clustered_picture)
    plt.title(f'Clusters: {cluster_number}')

# Rendering the complete figure with all pictures
plt.show()
