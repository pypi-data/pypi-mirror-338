from collections.abc import Iterable

from ..typing import Comparable
from .common import iter_to_seq  # noqa: F401


def sorted_by_rank[T](
    data: Iterable[T],
    ranks: Iterable[Comparable],
    *,
    _reverse: bool = False,
) -> list[T]:
    return [
        v
        for v, _ in sorted(
            zip(data, ranks, strict=True),
            key=lambda x: x[1],
            reverse=_reverse,
        )
    ]
