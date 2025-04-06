from __future__ import annotations

from typing import TYPE_CHECKING

from .markdown import iter_images

if TYPE_CHECKING:
    from collections.abc import Iterator

    from nbstore.store import Store

    from .image import Image


def convert(markdown: str, store: Store) -> Iterator[str | Image]:
    for image in iter_images(markdown):
        if isinstance(image, str):
            yield image
        else:
            yield from convert_image(image, store)


def convert_image(image: Image, store: Store) -> Iterator[str | Image]:
    if "source" in image.classes:
        image.classes.remove("source")
        yield from get_source(image, store)

    try:
        content_suffix = store.get_content(image.src, image.identifier)
    except Exception:  # noqa: BLE001
        yield image.markdown
    else:
        if not content_suffix:
            yield image.markdown
        else:
            image.set_content(*content_suffix)
            yield image


def get_source(image: Image, store: Store) -> Iterator[str]:
    if source := store.get_source(image.src, image.identifier):
        language = store.get_language(image.src)
        yield f"```{language}\n{source}\n```\n\n"
