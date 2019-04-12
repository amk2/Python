
import os

def find(path='.'):
    for item in os.listdir(path):
        fn = os.path.normpath(os.path.join(path, item))
        if os.path.isdir(fn):
            for f in find(fn):
                yield f
        else:
            yield fn

for fn in find('/home/temp'):
    print fn