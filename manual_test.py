from time import sleep
from edm.core import Owner


def main():
    owner = Owner("dummy")
    owner.start(False)

    sleep(5)
    owner.stop()


if __name__ == '__main__':
    main()
