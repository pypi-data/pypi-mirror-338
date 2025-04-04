from asyncio import subprocess
from subprocess import Popen
import sys 
import pandas as pd 
import argparse
import os 
import re 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--document")
    parser.add_argument("--sheet")
    parser.add_argument("--command")
    parser.add_argument("--join-sheet", default=None)
    parser.add_argument("--join-primary", default=None)
    parser.add_argument("--join-foreign", default=None)
    parser.add_argument("--verbosity", type=int, default=0)
    parser.add_argument("--action", choices=["exec", "columns"], default="exec")

    args, _ = parser.parse_known_args(sys.argv)


    engines = {
        ".xlsx": "xlrd",
        ".ods": "odf"
    }
    doc_name, ext = os.path.splitext(args.document)
    if ext == ".csv":
        data = pd.read_csv(args.document)
    else:
        data: pd.DataFrame = pd.read_excel(args.document, engine=engines[ext], sheet_name=args.sheet)
    if args.join_sheet is not None:
        data2 = pd.read_excel(args.document, engine=engines[ext], sheet_name=args.join_sheet)
        data = data.join(data2.set_index(args.join_foreign), on=args.join_primary)


    if isinstance(data, dict):
        print("Please select sheet from: ")
        for sheet in data.keys():
            print(sheet)
        sys.exit(1)
    data = data.rename(columns=lambda x: x.strip())
    

    columns = data.columns 
    def executor(command, row):
        for column in columns:
            # command = command.replace(r"{{" +column+ r"}}", str(row[column]))
            command = re.sub(r"{{\s*" + column + r"\s*}}", str(row[column]), command)
        proc = Popen(command, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = proc.communicate()
        print(stdout.decode("utf-8"), end="")

    if args.verbosity > 0:
        print(data)

    if args.action == "exec":
        for i, x in data.iterrows():
            executor(args.command, x)
    elif args.action == "columns":
        for c in data.columns:
            print(c)

if __name__ == "__main__":
    main()