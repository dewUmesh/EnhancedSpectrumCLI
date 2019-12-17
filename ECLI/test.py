import argparse
import traceback
import logging

def test():
    try:
            with open(file="") as f:
                f.readline()
    except Exception as e:
            print(traceback.print_exc())

    else:
            f.close()
            print("in else")
    finally:
            print("in final clause")


def main():

        # parser = argparse.ArgumentParser(description='Parse input string')
        # parser.add_argument("-c", "--command", help='Input String', nargs='+')
        # parser.add_argument("-s", "--server", help='Input String', nargs='+')
        # args = parser.parse_args()
        #
        # arg_str = args.command + args.server
        # print(arg_str)
        test()

if __name__ == '__main__':
    main()