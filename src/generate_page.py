from pathlib import Path

from extract_title import extract_title
from markdown_to_htmlnode import markdown_to_htmlnode

def generate_page(basepath, from_path, template_path, dest_path):
    # create Path objects from our provided bits and pieces
    from_obj = Path(from_path)
    template_obj = Path(template_path)
    dest_obj = Path(dest_path)
    # ensure paths exist and are appropriate file types
    for file in (from_obj, template_obj):
        if not file.is_file():
            raise Exception(f'Error: {file} not a file')

    # greeting message
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    markdown = from_obj.read_text()
    html = template_obj.read_text()
    content = markdown_to_htmlnode(markdown).to_html()
    title = extract_title(markdown)

    html = html.replace('{{ Title }}', title)
    html = html.replace('{{ Content }}', content)
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')

    dest_obj.parent.mkdir(parents=True, exist_ok=True)
    dest_obj.write_text(html)
    return True
