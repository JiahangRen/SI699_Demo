import sys, os



def univ_import(mylib):

    sys.path.insert(0, os.path.join(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib'))

    import mylib

    del sys.path[0], sys, os