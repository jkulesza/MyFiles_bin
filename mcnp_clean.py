#!/usr/bin/env python

import __main__ as main
if(__name__ == '__main__' and hasattr(main, '__file__')):

    import os
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if(f.startswith('out') and len(f) == 4):
            os.remove(f)
        elif(f.startswith('runtp') and len(f) == 6):
            os.remove(f)
        elif(f.startswith('comou') and len(f) == 6):
            os.remove(f)
        elif(f.startswith('srct') and len(f) == 5):
            os.remove(f)
        elif(f.startswith('meshta') and len(f) == 7):
            os.remove(f)
        elif(f.startswith('mcta') and len(f) == 5):
            os.remove(f)
        elif(f.startswith('ptra') and len(f) == 5):
            os.remove(f)

