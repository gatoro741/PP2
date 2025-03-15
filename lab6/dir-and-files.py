import os

#1
path = r'C:\Users\sofya\OneDrive\Рабочий стол'
print("Directories:")
for dirs in os.listdir(path):
    if os.path.isdir(os.path.join(path, dirs)):
        print(dirs)

print("\nFiles:")
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)

print("\nAll Directories and Files:")
for tdir, dirs, files in os.walk(path):
    for dir in dirs:
        print(os.path.join(tdir, dir))
    for file in files:
        print(os.path.join(tdir, file))


#2
path = r'C:\Users\sofya\OneDrive\Рабочий стол'
print("Existence: ", os.access(path, os.F_OK))
print("Readable: ", os.access(path, os.R_OK))
print("Writable: ", os.access(path, os.W_OK))
print("Executable: ", os.access(path, os.X_OK))


#3
