import os
import sys
import argparse

def main():
    
    print(f"current script path: {sys.argv[0]}")
    path1 = os.path.dirname(__file__)
    print(f"current script path: {path1}")
    path2 = os.path.abspath(__file__)

    print(f" python sys.prefix path: {sys.prefix}")
    print(f" python sys.exec_prefix path: {sys.exec_prefix}")
    
    gen_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    print(f" gen_path: {gen_path}")


     #解析参数
    parser = argparse.ArgumentParser()
    parser.description = 'please enter two parameters input and outputfile ...'
    parser.add_argument("-i", "--input", help="this is parameter dicom filename",
                        dest="dcmfile", type=str, default=None)
    parser.add_argument("-o", "--output", help="this is parameter labelMap filepath",
                        dest="labelmap", type=str, default=None)
    args = parser.parse_args()
    if args.dcmfile == None:
        print("please input dcm filename")
        exit()
    if args.labelmap == None:
        print("please input label filename")
        exit()

    return

if __name__ == '__main__':
    main()

