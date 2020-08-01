def do_twice(f):
    f()
    f()
def do_four(f):
    do_twice(f)
    do_twice(f)

def plus():
    print('+', end = ' ')
def less():
    print('-', end = ' ')
def space():
    print(' ', end = ' ')
def bar():
    print('|', end = ' ')
def print_end():
    print()

def line():
    plus()
    do_four(less)
def columns():
    bar()
    do_four(space)
    
def line_end():
    do_four(line)
    plus()
    print_end()
def column_end():
    do_four(columns)
    bar()
    print_end()
def grid():
    line_end()
    do_four(column_end)
def grid_end():
    do_four(grid)
    line_end()
grid_end()

