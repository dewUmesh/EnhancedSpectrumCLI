import argparse

def main():

        parser = argparse.ArgumentParser(description='Parse input string')
        parser.add_argument("-c", "--command", help='Input String', nargs='+')
        parser.add_argument("-s", "--server", help='Input String', nargs='+')
        args = parser.parse_args()

        arg_str = args.command + args.server
        print(arg_str)


if __name__ == '__main__':
    main()