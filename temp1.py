import os, zipfile, sys
from threading import Lock
dir_ = 'D:\My_Folder_Parent\Study\Programming\Python_files'
if dir_ in os.getcwd():
    print("You tried to zip the contents of zipped files as well creating a infinite loop\nForced exit to prevent memory use")
    sys.exit()
def zip_file(zipf, folder, file_path, lock):
    """Helper function to write a single file to the zip archive."""
    with lock:
        zipf.write(file_path, os.path.relpath(file_path, folder))
lock = Lock()
zip1 = zipfile.ZipFile('zipped.zip', 'w')
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=None) as executor:
    for i,j,k in os.walk(dir_):
        for file in k:    
            dir_name = os.path.join(i, file)
            executor.submit(zip_file, zip1, dir_, dir_name, lock)
print("\n\n-------------Successful---------------\n\n") 