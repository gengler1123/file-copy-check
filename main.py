import argparse
import os
from uuid import uuid4
import shutil
import inotify.adapters
from time import time


def check_file(fname: str,
               write_dir: str,
               src: str,
               dst: str):
    """

    :param filename:
    :return:
    """
    i = inotify.adapters.Inotify()
    i.add_watch(write_dir)

    shutil.copyfile(
        src,
        dst
    )
    for event in i.event_gen(yield_nones=False,
                             timeout_s=0.1):
        (_, type_names, path, filename) = event
        if filename == fname:
            if "IN_CLOSE_WRITE" in type_names:
                print("Copied")
                break


def main():
    """

    :return:
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--write_directory",
        type=str,
        default="write_directory"
    )

    args = parser.parse_args()

    for d in dir(args):
        if d[0] != "_":
            print(d)

    if not os.path.isdir(args.write_directory):
        os.mkdir(args.write_directory)

    path = os.path.join(
        os.getcwd(),
        "data"
    )
    Data = [
        os.path.join(path, f) for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    ]

    for data in Data:
        fname = f"{uuid4()}.{data.split('.')[-1]}"
        write_path = f"{os.getcwd()}/{args.write_directory}/{fname}"
        check_file(
            fname=fname,
            write_dir=f"{os.getcwd()}/{args.write_directory}",
            src=data,
            dst=write_path
        )


if __name__ == "__main__":
    main()
