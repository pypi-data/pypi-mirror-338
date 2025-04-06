from collections.abc import Iterable, Sequence
from itertools import chain, repeat

from toolz.itertoolz import sliding_window


def iter_to_grams[T](
    _iter: Iterable[T],
    *,
    n: int,
    pad: T | None = None,
) -> Iterable[Sequence[T]]:
    if pad is not None:
        _iter = chain(
            repeat(pad, n - 1),
            _iter,
            repeat(pad, n - 1),
        )

    return sliding_window(n, _iter)
