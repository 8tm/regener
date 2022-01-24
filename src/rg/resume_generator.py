import json
from pathlib import Path

from rg.classes.pdf import PDF  # type: ignore
from rg.menu import parse_arguments  # type: ignore


def generate_pdf(content: dict, path: Path):
    pdf = PDF(
        orientation=content['metadata'].get('orientation') or 'portrait',
        unit=content['metadata'].get('units') or 'mm',
        format=content['metadata'].get('format') or 'A4',
    )
    pdf.add_page()
    pdf.load_from_json(content)
    pdf.install_font(content, path)
    pdf.load_layouts(content, path)
    pdf.load_items(content)
    return pdf


def select_output_path(argument_output: Path, argument_path: Path, content_path) -> str:
    if not argument_output:
        if not content_path:
            return 'cv.pdf'
        else:
            return str(argument_path / content_path)
    else:
        output_path = argument_output

        if argument_output.is_dir():
            output_path = argument_output / 'cv.pdf'

        return str(output_path)


def main():
    arguments = parse_arguments()
    json_file_path = Path(arguments.path) / 'cv.json'

    with open(json_file_path, 'r') as json_file:
        content = json.load(json_file)

    pdf_content = generate_pdf(content, arguments.path)
    pdf_content.output(select_output_path(arguments.output, arguments.path, content.get('output')))


if __name__ == '__main__':
    main()
