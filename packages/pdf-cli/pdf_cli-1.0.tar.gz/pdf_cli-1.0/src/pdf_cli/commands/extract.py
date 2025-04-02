from __future__ import annotations

from typing import Any

import click
from pypdf import PdfReader, PdfWriter

from pdf_cli.main import main
from pdf_cli.utils import Console, Range


@main.command()
@click.argument("input_file", type=click.File("rb"))
@click.option("-p", "--pages", default=None, type=Range, help="starting page to extract")
@click.option("-o", "--output", type=click.File("wb"), required=True)
@click.option("-v", "--verbosity", type=int, default=0)
def extract(input_file: click.File, output: click.File, pages: list[int] | None, verbosity: int, **kwargs: Any) -> None:  # noqa: ARG001
    """extract one or multiple pages and build a new document."""
    source = PdfReader(input_file)  # type: ignore[arg-type]
    console = Console(verbosity)

    if pages is None:
        pages = Range(f"1-{len(source.pages)}", None)

    selection = []
    for page_num in pages:
        real_page = page_num - 1
        console.echo(".", f"Extracting page {page_num}")
        selection.append(source.pages[real_page])

    output_pdf = PdfWriter()
    for page in selection:
        output_pdf.add_page(page)
    console.info(f"Writing {output.name}")
    output_pdf.write(output)  # type: ignore[arg-type]
