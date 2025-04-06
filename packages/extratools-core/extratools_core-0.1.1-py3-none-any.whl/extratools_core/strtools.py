from collections.abc import Iterable

from .iter import iter_to_grams


def str_to_grams(
    s: str,
    *,
    n: int,
    pad: str = '',
) -> Iterable[str]:
    if len(pad) > 1:
        raise ValueError

    for c in iter_to_grams(s, n=n, pad=pad or None):
        yield ''.join(c)
