import click
import subprocess
import mpremote
import mpremote.commands


import os
import shutil
import time


def delete_folder_by_name(root_dir, folder_name):
    """
    Recursively deletes folders matching the given name within the root directory.

    Args:
        root_dir (str): The root directory to start the search from.
        folder_name (str): The name of the folder to delete.
    """
    for item in os.listdir(root_dir):
        # Skip .venv, there is tons of cached stuff in there
        if item == ".venv":
            continue
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            if item == folder_name:
                try:
                    shutil.rmtree(item_path)
                    print(f"Deleted folder: {item_path}")
                except OSError as e:
                    print(f"Error deleting {item_path}: {e}")
            else:
                delete_folder_by_name(item_path, folder_name)


@click.command()
@click.option("--clean", is_flag=False, help="Delete all files from device and load")
# @click.option("--reset", is_flag=False, help="Reset after load")
def main(clean: bool):
    # Make the source code ready for mpremote (remove __pycache__ folders)
    delete_folder_by_name(".", "__pycache__")

    if clean:
        print("Cleaning...")
        subprocess.run("py -m mpremote bootloader")
        subprocess.run("py -m esptool erase_flash")
        subprocess.run(
            "py -m esptool --baud 460800 write_flash 0 .\\bin\\ESP32_GENERIC_S3-20241129-v1.24.1.bin "
        )
        time.sleep(2)

    subprocess.run("py -m mpremote fs cp ./boot.py :")
    subprocess.run("py -m mpremote fs cp ./config.py :")
    subprocess.run("py -m mpremote fs cp ./config.json :")
    subprocess.run("py -m mpremote fs cp ./main.py :")
    subprocess.run("py -m mpremote fs cp -r ./src : ")
    subprocess.run("py -m mpremote fs cp -r ./public :")

    # if reset:
    #     print("Resetting...")
    subprocess.run("py -m mpremote reset")

    print("Load successful!")


if __name__ == "__main__":
    main()
