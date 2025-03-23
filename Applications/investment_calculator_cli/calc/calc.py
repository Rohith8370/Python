"""
    calc.py

    This module perfoms basic Calculations
    1. add
    2. sub
    3. mul
    4. div
    5. mod

    usage:
        * python calc.py add 10 5
            15
        * python calc.py sub 10 5
            5
        * python calc.py mul 10 5
            50
        * python calc.py div 10 5
            2
        * python calc.py mod 10 5
            0
        
"""

import argparse

def create_parser():
    """This method creates a parser 

    """
    parser = argparse.ArgumentParser(
        prog="calculation",
        description= "This is used for the basic calculations",)
    parser.add_argument(
        "args.operations",
        choices= ["add","sub","mul","div","mod"],
        help= "Operation to perform: add, sub, mul, div, mod",
    )
    parser.add_argument("value1", type=int, help="First number")
    parser.add_argument("value2", type=int, help="Second number")
    return parser

def operate(args):
    """This function Operates on the args

    """
    if args.operation == "add":
        print(args.value1 + args.value2)
    elif args.operation == "sub":
        print(args.value1 - args.value2)
    elif args.operation == "mul":
        print(args.value1 * args.value2)
    elif args.operation == "div":
        print(args.value1 // args.value2)
    elif args.operation == "mod":
        print(args.value1 % args.value2)

def main():
    """This function creates a parser and performs operations

    """
    # This Creates parser
    parser = create_parser()
    # This process arguments
    args = parser.parse_args()
    # This perform the operations
    operate(args)


if __name__ == "__main__":
    main()
