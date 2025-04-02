import sys
import argparse
import uuid

from importlib.metadata import version
from ngm_remove import lib
from ngm_remove import db

def main():
    
    parser = argparse.ArgumentParser(description="Remove files/folders")
    parser.add_argument("--version", action="store_true", help="Show version and exit")
    parser.add_argument("--input", help="file with list of items to remove", type=str, default="")
    # parser.add_argument("--option", help="some option", type=str, default="default_value")
    parser.add_argument("paths", nargs="*", help="Files/Folders to Remove")

    args = parser.parse_args()

    if args.version:
        print(version("ngm-remove"))
        exit(0)
    
    sessionid = uuid.uuid4()
    dbi = db.DB(sessionid)

    if args.input:
        print(args.input)
        # check for file exitence
        # use try/except
        with open(args.input, "r", encoding="utf-8") as file:
            lines = file.readlines()
            print(lines)
            for item in lines:
                lib.remove(item.strip(), dbi)
    
        exit(0)
    
    # args = sys.argv[1:]
    # # print(f"Args: {args}")

    argscount = len(args.paths)

    if argscount == 0:
        print("Usage: remove <path>")
        sys.exit(1)
    
    for item in args.paths:
        lib.remove(item, dbi)
