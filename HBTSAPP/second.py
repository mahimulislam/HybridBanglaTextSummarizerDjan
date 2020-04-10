import sys

def do_something(val):
    # do something
    val="SSos"
    print("SSSJAJA")
    # return something
    return val

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    return_val = do_something(arg)