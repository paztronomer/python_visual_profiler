'''
guppy3 is quite simple to use. At some point in your code, you have to write the following:

https://stackoverflow.com/questions/110259/which-python-memory-profiler-is-recommended
'''
from guppy import hpy
h = hpy()
print(h.heap())