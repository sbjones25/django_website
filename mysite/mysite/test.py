import os

print '/'.join(os.path.realpath(__file__).split('/')[:-1])
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print BASE_DIR
