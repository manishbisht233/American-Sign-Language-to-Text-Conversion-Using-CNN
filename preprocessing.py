import cv2
import os
minValue = 70


# Function to apply filter to images in a directory
def apply_filter_to_images(input_dir, output_dir, filter_type):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get a list of all image files in the input directory
    image_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    
    # Apply filter to each image and save to the output directory
    for filename in image_files:
        # Read the image
        image_path = os.path.join(input_dir, filename)
        img = cv2.imread(image_path)
        
        # Apply the filter
        # filtered_img = cv2.GaussianBlur(img, (5, 5), 0)  # Example: Gaussian blur filter
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),2)

        th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
        ret, filtered_img = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
        # Save the filtered image
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, filtered_img)
        print(f"Saved filtered image: {output_path}")

# Input and output directories

# for i in range(97, 123):
    # input_directory = "dataset/testingData/"+chr(i)
    # output_directory = "dataset/test/"+chr(i)
    # apply_filter_to_images(input_directory, output_directory, filter_type= "gaussian_blur")

input_directory = "dataset/trainingData/0"
output_directory = "dataset/train/0"
# Apply filter to images in the input directory and save to the output directory
apply_filter_to_images(input_directory, output_directory, filter_type= "gaussian_blur")


