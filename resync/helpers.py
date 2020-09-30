import os


def list_file(path):
    # r=root, d=directories, f = files
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            path = os.path.join(r, file)
            files.append([path, os.path.getmtime(path)])
    return files