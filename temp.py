import os, zipfile
dir_ = 'D:\My_Folder_Parent\Study\Programming\Python_files\My_Repositories'

if dir_ in os.getcwd():
    print("You tried to zip the contents of zipped files as well creating a infinite loop\nForced exit to prevent memory use")

zip1 = zipfile.ZipFile('zipped.zip', 'w')
for i,j,k in os.walk(dir_):
    for file in k:    
        dir_name = os.path.join(i, file)
        zip1.write(dir_name)
print("\n\n-------------Successful---------------\n\n")