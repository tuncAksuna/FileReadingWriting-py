import os

path = 'C:/Users/netadmin/Desktop/TEST/ndu-platform'

def walk_through(path, extension):
    for (dirpath, dirname, filenames) in os.walk(path):
        for filename in filenames:
            for ext in extension:
                if filename.endswith(ext) and "/node_modules/" not in dirpath and \
                        "/esm" not in dirpath and "/target/" not in dirpath and "/ui-ngx/" not in dirpath:
                    yield os.path.join(dirpath, filename)


with open("all-codes.txt", "a", encoding='utf-8') as writefile:
    for fileName in walk_through(path, [".java"]):
        print(fileName)
        with open(fileName, "r", encoding="ISO-8859-1") as f:
            text = f.read()
        writefile.write(text)
