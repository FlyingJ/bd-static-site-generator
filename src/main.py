from sysutils import copy_directory_contents
from generate_page import generate_page

SOURCE = 'static'
DESTINATION = 'public'

def main():
    if not copy_directory_contents(SOURCE, DESTINATION):
        raise Exception(f' - {__name__} failed to copy_directory_contents')

    from_path = 'content/index.md'
    template_path = 'template.html'
    dest_path = 'public/index.html'

    generate_page(from_path, template_path, dest_path)


if __name__ == "__main__":
    main()
