import os


def get_download_directory():
    if os.name == 'nt':  # For Windows
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:  # For macOS and Linux
        return os.path.join(os.path.expanduser('~'), 'Downloads')
