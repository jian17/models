import os

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..\\images\\")
print(path)

counter = 1
for f in os.listdir(path):
    suffix = f.split('.')[-1]
    if suffix == 'jpg' or suffix == 'png':
        new = '{}.{}'.format(str(counter), suffix)
        os.rename(path + f, path + new)
        counter = int(counter) + 1