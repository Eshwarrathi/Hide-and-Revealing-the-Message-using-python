from stegano import lsb

# Use the correct path
image_path = "C:/Users/RathiSoft Innovation/Desktop/image.png"
output_path = "C:/Users/RathiSoft Innovation/Desktop/secret_image.png"

# Hide the secret message in the image
try:
    secret_image = lsb.hide(image_path, "Your secret message")
    secret_image.save(output_path)
    print(f"Secret image saved as {output_path}")


except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
