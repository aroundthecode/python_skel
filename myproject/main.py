import logging
import sys

log = logging.getLogger("main")
log_format = "%(asctime)s | %(levelname)9s | %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO)


def hello():
    return "Hello"


def main():
    print(hello())
    sys.exit(0)


if __name__ == '__main__':
    main()
