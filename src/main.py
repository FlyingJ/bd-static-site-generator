from sysutils import copy_directory_contents
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive

SOURCE = 'static'
DESTINATION = 'public'

def main():
    if not copy_directory_contents(SOURCE, DESTINATION):
        raise Exception(f'Error: copy_directory_contents failed for {SOURCE} -> {DESTINATION}')

    from_path = './content'
    template_path = 'template.html'
    dest_path = './public'
    if not generate_pages_recursive(from_path, template_path, dest_path):
        raise Exception(f'Error: generate_pages_recursive failed for {from_path}')

if __name__ == "__main__":
    main()
