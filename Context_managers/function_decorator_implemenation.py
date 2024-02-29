from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()
        
with open_file('sample2.txt', 'w') as f:
    f.write('content of sample.txt')

print(f.closed)