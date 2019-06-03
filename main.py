import argparse
import os
from glob import glob
from pathlib import Path

import pyperclip


def print_file(filename):
    home = Path.home()

    main_dir = home / ".texpander"

    if not main_dir.exists():
        raise ValueError(
            f"{main_dir} does not exist.\n"
            "Please create a .texpander directory in your home folder."
        )
    os.chdir(main_dir)

    file = sorted(glob(filename + '*'))[0]

    with open(file) as f:
        read_data = f.read()
    read_data = read_data.rstrip()
    backup_old_clipboard = pyperclip.paste()
    pyperclip.copy(read_data)
    print(backup_old_clipboard)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Print the file of the give name'
    )
    parser.add_argument('filename', type=str, help='a filename')
    args = parser.parse_args()

    print_file(args.filename)
