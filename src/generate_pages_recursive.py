from pathlib import Path

from generate_page import generate_page

def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    content = Path(dir_path_content)
    if not content.is_dir():
        raise Exception(f'Error: content source {content} is not a directory')

    template = Path(template_path)
    if not template.is_file():
        raise Exception(f'Error: template file {template} is not a file')

    # if destination does not exist
    #   create it
    destination = Path(dest_dir_path)
    if not destination.is_dir():
        print(f'- generate_pages_recursive: creating destination {destination}')
        destination.mkdir(parents=True, exist_ok=True)

    for file in content.iterdir():
        if file.is_file() and file.name.endswith('.md'):
            if not generate_page(basepath, (content / file.name).resolve(), template.resolve(), (destination / file.name.replace('.md', '.html')).resolve()):
                raise Exception(f'Error: generate_page failed for ${file.resolve()}')
        elif file.is_dir():
            if not generate_pages_recursive(basepath, (content / file.name).resolve(), template.resolve(), (destination / file.name).resolve()):
                raise Exception(f'Error: generate_pages_recursive failed for ${file.resolve()}')

    return True
