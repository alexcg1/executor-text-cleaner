from typing import Any, Dict, Optional, Sequence
from jina import Executor, DocumentArray, requests
import re


class TextCleaner(Executor):
    """
    @param rm_newlines: Remove all instances of "\r" and "\n"
    @param rm_multiple_spaces: Remove any instance of more than one space at a time, e.g. "  ", "   ". Retains single spaces
    @param rm_hyphen spaces: Words often break across lines and are hyphenated with "- ". This merges the two parts into one word
    @param convert_quotes: Convert curly quotes into standard quotes. needs more testing
    @param access_paths: Default traversal paths
    """

    def __init__(
        self,
        rm_newlines: bool = True,
        rm_multiple_spaces: bool = True,
        rm_hyphen_spaces: bool = True,
        convert_quotes: bool = True,
        access_paths: str = "@r",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.rm_newlines = rm_newlines
        self.rm_hyphen_spaces = rm_hyphen_spaces
        self.rm_multiple_spaces = rm_multiple_spaces
        self.convert_quotes = convert_quotes
        self.access_paths = access_paths

    @requests
    def clean_text(self, docs: DocumentArray, parameters: Dict[str, Any],  **kwargs):
        access_paths = parameters.get("access_paths", self.access_paths)
        for doc in docs[access_paths]:
            if self.rm_newlines:
                self._rm_newlines(doc)

            if self.convert_quotes:
                self._convert_quotes(doc)

            if self.rm_multiple_spaces:
                self._rm_multiple_spaces(doc)

            if self.rm_hyphen_spaces:
                self._rm_hyphen_spaces(doc)

    def _rm_newlines(self, doc):
        newlines = ["\n", "\r"]
        for char in newlines:
            doc.text = doc.text.replace(char, "")

    def _convert_quotes(self, doc):
        double_quotes = ["“", "”"]
        single_quotes = ["‘"]

        for char in double_quotes:
            doc.text = doc.text.replace(char, '"')

        for char in single_quotes:
            doc.text = doc.text.replace(char, "'")

    def _rm_multiple_spaces(self, doc):
        doc.text = re.sub(" +", " ", doc.text)

    def _rm_hyphen_spaces(self, doc):
        hyphen_spaces = ["- "]
        for char in hyphen_spaces:
            doc.text = doc.text.replace(char, "")
