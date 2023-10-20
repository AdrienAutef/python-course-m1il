try:
 with open('../data/file.txt') as f:
    file = f.read()
except FileNotFoundError:
 file = None
print(file)