import os

from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TIT2


def title_to_filename(folder_path):
    try:
        # List all files in the given folder
        for filename in os.listdir(folder_path):
            if filename.lower().endswith('.mp3'):
                # Split the filename into name and extension
                name, extension = os.path.splitext(filename)
                # Form the full file path
                file_path = os.path.join(folder_path, filename)

                # Load the MP3 file
                try:
                    audio = EasyID3(file_path)
                except Exception:
                    audio = ID3(file_path)

                # Set the title tag to the filename (without extension)
                audio['title'] = name
                # Save the changes
                audio.save()
                print(f'Updated title for: {file_path}')

    except Exception as e:
        print(f'Error: {e}')