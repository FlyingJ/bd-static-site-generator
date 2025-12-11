from sysutils import copy_directory_contents

SRC_DIR='static'
DST_DIR='public'

def main():
    if not copy_directory_contents(SRC_DIR, DST_DIR):
        raise Exception(f' - {__name__} failed to copy_directory_contents')

if __name__ == "__main__":
    main()
