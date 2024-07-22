import cv2

def convert_4_to_3_channel(image_path, output_path):
    # Read the 4-channel image
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    # Check if the image has 4 channels
    if image.shape[2] == 4:
        # Convert the image from RGBA to RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        
        # Save the converted image
        cv2.imwrite(output_path, rgb_image)
        print(f"Image converted and saved to {output_path}")
    else:
        print("The image does not have 4 channels.")

# Example usage
convert_4_to_3_channel('raw.png', 'output.png')
