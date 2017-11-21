from __future__ import print_function
import sys

# print 'Number of arguments: ', len(sys.argv), 'arguments.'
# print 'Argumentlist: ', str(sys.argv)
# print 'Last two arguments: ', sys.argv[len(sys.argv) - 2], sys.argv[len(sys.argv) - 1], '.'

if len(sys.argv) > 1:
    del sys.argv[0]
    print(sys.argv[len(sys.argv) - 2] + " " + sys.argv[len(sys.argv) - 1]) if len(sys.argv) > 1 else print(
        sys.argv[len(sys.argv) - 1])
else:
    print("No arguments...")
