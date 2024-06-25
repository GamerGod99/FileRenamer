import os

from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TIT2, TRCK


def get_track_index(file_path):
    try:
        audio_data = EasyID3(file_path)  # Load the MP3 file
        track_number = audio_data.get('tracknumber', None)  # Get the track number

        if track_number:
            return int(track_number[0])
        else:
            return "No track number found."

    except Exception as e:
        return f'Error: {e}'


def enum_files(folder_path):
    try:
        for filename in os.listdir(folder_path):  # List all files in the given folder
            original_file = os.path.join(folder_path, filename)  # Form the full original and new file paths
            index = get_track_index(original_file)
            new_filename = f'{'0' + str(index) if index < 10 else str(index)} {filename}'  # Slices the string, excluding the extension

            new_file = os.path.join(folder_path, new_filename)  # Renames the file
            os.rename(original_file, new_file)
            print(f'Renamed: {original_file} -> {new_file}')

    except Exception as e:
        print(f'Error: {e}')


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
