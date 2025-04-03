import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import List

import mammoth
import pymupdf4llm
from markdownify import markdownify
from pptx2md import convert

from duowen_agent.rag.extractor.html_parser import MainContentExtractor
from duowen_agent.rag.extractor.xls_extractor import XlsExtractor
from duowen_agent.rag.extractor.xlsx_extractor import XlsxExtractor


def word2md(file_path: str) -> str:
    def convert_image(image):
        return {"src": ""}

    with open(file_path, "rb") as docx_file:
        return markdownify(
            mammoth.convert_to_html(
                fileobj=docx_file,
                convert_image=mammoth.images.img_element(convert_image),
            ).value
        )


def pdf2md(file_path: str) -> str:
    md_text = pymupdf4llm.to_markdown(file_path)
    return md_text


def ppt2md(file_path: str) -> str:
    with NamedTemporaryFile(
            "w+t",
            suffix=".md",
    ) as temp_file:
        output_path = temp_file.name

        if not os.path.exists(output_path):
            open(output_path, "w").close()

        run_args = dict(
            pptx_path=Path(file_path),
            output=Path(output_path),
            disable_notes=True,
            disable_image=True,
        )
        convert(**run_args)

        with open(output_path, "r") as f:
            text = f.read()
            return text


def html2md(content: str) -> str:
    return MainContentExtractor.extract(content, output_format="markdown")


def excel_parser(file_path: str) -> List[str]:
    match _suffix := Path(file_path).suffix.lower():
        case ".xlsx":
            return XlsxExtractor(file_path).extract()
        case ".xls":
            return XlsExtractor(file_path).extract()
        case _:
            raise ValueError(f"无法识别的excel格式:{_suffix}")
