from stegano import lsb

# Path to the image with the hidden message
secret_image_path = "C:/Users/RathiSoft Innovation/Desktop/secret_image.png"

# Reveal the message
try:
    revealed_message = lsb.reveal(secret_image_path)
    print(f"Revealed Message: {revealed_message}")

except FileNotFoundError:
    print(f"Error: The file '{secret_image_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
