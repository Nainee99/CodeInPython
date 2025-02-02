# -------------------------------
# Problem 3: File Extensions
# -------------------------------
# File extensions help computers determine the type of a file, while web browsers use media types
# (formerly known as MIME types) to handle files from the web. This program will identify the 
# media type based on the file extension.
#
# Task:
# - Prompt the user for the name of a file.
# - Determine the media type of the file based on its extension.
# - Output the media type if the file’s name ends (case-insensitively) with one of these extensions:
#   - .gif → image/gif
#   - .jpg → image/jpeg
#   - .jpeg → image/jpeg
#   - .png → image/png
#   - .pdf → application/pdf
#   - .txt → text/plain
#   - .zip → application/zip
# - If the file’s name has an unrecognized extension or no extension, output: application/octet-stream
#
# Requirements:
# - Handle file extensions case-insensitively (e.g., .JPG and .jpg are treated the same).
# - Ignore leading or trailing whitespace in the user's input.
#
# Example:
# Input: image.jpeg
# Output: image/jpeg
#
# Input: document.pdf
# Output: application/pdf
#
# Input: unknownfile.xyz
# Output: application/octet-stream
#
# -------------------------------

# Your code starts here:
def get_media_type(filename):
    # Remove leading and trailing whitespace from the filename
    filename = filename.strip()

    # Get the file extension
    extension = filename.split('.')[-1].lower()

    # Determine the media type based on the file extension
    if extension == 'gif':
        return 'image/gif'
    elif extension in ['jpg', 'jpeg']:
        return 'image/jpeg'
    elif extension == 'png':
        return 'image/png'
    elif extension == 'pdf':
        return 'application/pdf'
    elif extension == 'txt':
        return 'text/plain'
    elif extension == 'zip':
        return 'application/zip'
    else:
        return 'application/octet-stream'

# Prompt the user for the name of a file
filename = input('Enter the name of a file: ')
print(get_media_type(filename))
