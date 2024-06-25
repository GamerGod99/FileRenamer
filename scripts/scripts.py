import os


def cut_single(str, pos):
    if len(pos) == 1:
        pos = list(pos)
        pos.append(None)
    str, ext = os.path.splitext(str)
    return str[pos[0]:pos[1]] + ext


def cut_names(folder_path, pos):
    try:
        for filename in os.listdir(folder_path):  # List all files in the given folder
            original_file = os.path.join(folder_path, filename)  # Form the full original and new file paths

            new_filename = cut_single(filename, pos)  # Slices the string, excluding the extension

            new_file = os.path.join(folder_path, new_filename)  # Renames the file
            os.rename(original_file, new_file)
            print(f'Renamed: {original_file} -> {new_file}')

    except Exception as e:
        print(f'Error: {e}')
