from __future__ import annotations
import re
from pathlib import Path
from typing import TYPE_CHECKING

from mkdocs.config import Config, config_options
from mkdocs.plugins import BasePlugin, get_plugin_logger


if TYPE_CHECKING:
    from typing import Any

    from mkdocs.config.defaults import MkDocsConfig
    from mkdocs.structure.pages import Page as MkDocsPage



class NbstoreConfig(Config):
    """Configuration for Nbstore plugin."""

    notebooks_dir = config_options.Type(str, default=".")


logger = get_plugin_logger("mkdocs-nbstore")


class NbstorePlugin(BasePlugin[NbstoreConfig]):
    store: Store
    filters: list[Filter]

    def on_config(self, config: MkDocsConfig, **kwargs: Any) -> MkDocsConfig:
        path = Path(config.docs_dir) / self.config.notebooks_dir
        self.store = Store([path.resolve()])
        return config

    def on_page_markdown(
        self,
        markdown: str,
        page: MkDocsPage,
        config: MkDocsConfig,
        **kwargs: Any,
    ) -> str:
        if ".ipynb){#" not in markdown:
            return markdown

        doc: Doc = pf.convert_text(markdown, standalone=True)  # type: ignore

        set_output_format(doc, "markdown")

        for filter_ in self.filters:
            doc = filter_.run(doc)

        delete_output_format(doc)

        m = pf.convert_text(doc, input_format="panflute", output_format="markdown")  # type: ignore
        print(m)
        return m


def convert(markdown: str, store: Store) -> str: