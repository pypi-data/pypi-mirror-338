import sys
import argparse
import uuid
import subprocess

from importlib.metadata import version
from ngm_remove import lib
from ngm_remove import db

def main():
    
    parser = argparse.ArgumentParser(description="Remove files/folders")
    parser.add_argument("--version", action="store_true", help="Show version and exit")
    parser.add_argument("--input", help="file with list of items to remove", type=str, default="")
    parser.add_argument("--cmd", help="command to get list of items to remove", type=str, default="")
    parser.add_argument("--url", help="http/https url to get list of items to remove", type=str, default="")
    # parser.add_argument("--option", help="some option", type=str, default="default_value")
    parser.add_argument("paths", nargs="*", help="Files/Folders to Remove")

    args = parser.parse_args()

    if args.version:
        print(version("ngm-remove"))
        exit(0)
    
    sessionid = uuid.uuid4()
    dbi = db.DB(sessionid)

    if args.cmd:
        try:
            process = subprocess.run(
                args.cmd,
                shell=True,
                capture_output=True,
                text=True,  # Capture output as text (strings)
                check=True,  # Raise CalledProcessError for non-zero exit codes
            )
            lines = process.stdout.strip().splitlines()
            print(lines)
            for item in lines:
                lib.remove(item.strip(), dbi)

        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            print(f"Stderr: {e.stderr}") #print the standard error
            exit(1)

        except FileNotFoundError:
            print("Command not found.")
            exit(1)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            exit(1)
        
        finally:
            print("exiting")
            exit(0)

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
