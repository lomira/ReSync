import os


class FileClass:
    def __init__(self, path, filename, timestamp):
        self.path = path
        self.filename = filename
        self.timestam = timestamp

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.filename == other.filename and self.timestam == other.timestam
        else:
            return False

    def __hash__(self):
        return hash([self.filename, self.timestam])


def list_file(path):
    # r=root, d=directories, f = files
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if not file.startswith("~$"):
                path = os.path.join(r, file)
                files.append(FileClass(path, file, os.path.getmtime(path)))
    return files
