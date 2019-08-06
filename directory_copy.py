import os
from uuid import uuid4
import shutil
import inotify.adapters


def main():
    """

    :return:
    """
    base_dir = os.path.join(
        os.getcwd(),
        "data"
    )
    write_path = os.path.join(
        os.getcwd(),
        "nocopy"
    )

    if not os.path.isdir(write_path):
        os.mkdir(write_path)
    print(write_path)

    to_copy = [
        os.path.join(base_dir, f)
        for f in os.listdir(base_dir)
    ]

    i = inotify.adapters.Inotify()
    i.add_watch(write_path)
    shutil.rmtree(write_path)
    for c in to_copy:
        print(c)
        print(write_path)
        write_file = f"{write_path}/{c.split('/')[-1]}"

        shutil.move(c, write_path)

    RES = []

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        print(event)
        for typ in type_names:
            if "CLOSE" in typ:
                RES.append(typ)
                break
        print(len(RES))
        if len(RES) == len(to_copy):
            break

    print(f"""
    
    FINISHED WITH RESULTS
    
    """)


if __name__ == "__main__":
    """
    
    """
    main()