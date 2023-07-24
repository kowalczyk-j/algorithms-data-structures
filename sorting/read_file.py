import re

def read_file(path):
    with open(path) as handle:
        data = handle.read()

    data = re.sub(r"\W", " ", data)
    data = re.sub(r" +", " ", data)
    data = data.lower().split(" ")
    return data
