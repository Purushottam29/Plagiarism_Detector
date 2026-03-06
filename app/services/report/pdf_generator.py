from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os


def generate_pdf(file_id, plagiarism_percentage, highlighted_text):

    env = Environment(loader=FileSystemLoader("app/templates"))
    template = env.get_template("report_template.html")

    html_content = template.render(
        file_id=file_id,
        percentage=round(plagiarism_percentage, 2),
        content=highlighted_text
    )
    stem = Path(file_id).stem
    output_path = f"reports/{stem}_report.pdf"

    HTML(string=html_content).write_pdf(output_path)

    return output_path
