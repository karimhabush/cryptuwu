import argparse
from modules.rand.main import randgen
from modules.hash.main import sha224, sha256, sha512, md2, md5

def main():
    parser = argparse.ArgumentParser(description='add, modify and delete upstream nodes')
    parser.add_argument(
        'mod', choices=['rand', 'sym', 'asym','hash','encode'], help='Choose a command to execute.')
    parser.add_argument(
        '-H', '--hash', choices=['sha224', 'sha256', 'sha512','md2','md5'], help='select the type of encoding')
    parser.add_argument(
        '-e', '--encode', choices=['base64', 'hex'], help='select the type of encoding')
    parser.add_argument(
        '-s', '--size', type=int, help='select the size of encoding')
    parser.add_argument(
        '-i', '--input', type=str, help='Choose an input file')
    args = parser.parse_args()

    if args.mod == "rand":
        print(randgen(args.size,args.encode))

    elif args.mod == "hash":
        if args.hash == 'sha224':
            sha224(args.input)
        elif args.hash == 'sha256':
            sha256(args.input)
        elif args.hash == 'sha512':
            sha512(args.input)
        elif args.hash == 'md2':
            md2(args.input)
        elif args.hash == 'md5':
            md5(args.input)
    
    elif args.mod == ""

if __name__ == "__main__":
    main()