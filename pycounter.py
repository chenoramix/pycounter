import sys
import os


def recursivewalk(path, endswith):
    counter = 0;

    for root, dirs, files in os.walk(path):
        for name in files:
            if ".venv" in root:
                continue
            if name.endswith(endswith):
                fullname = os.path.join(root, name)
                with open(fullname, "r") as f:
                    lines = len(f.readlines())
                    counter += lines
    print("I counted", counter, "lines")


def main():
    if len(sys.argv) != 3:
        print("Pycounter v1.0\n")
        print("Usage:")
        print("python pycounter.py path endswith")
        sys.exit(0)

    path = sys.argv[1]
    endswith = sys.argv[2]

    recursivewalk(path, endswith)


if __name__ == "__main__":
    main()