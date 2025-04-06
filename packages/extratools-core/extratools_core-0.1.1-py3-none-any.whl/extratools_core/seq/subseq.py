from collections.abc import Callable, Iterable, Sequence
from functools import cache
from itertools import chain

from . import iter_to_seq


def best_subseq[T](
    a: Iterable[T],
    score_func: Callable[[Iterable[T]], float],
) -> Sequence[T]:
    s: Sequence = iter_to_seq(a)

    return max(
        chain([[]], (
            s[i:j]
            for i in range(len(s))
            for j in range(i + 1, len(s) + 1)
        )),
        key=score_func,
    )


def best_subseq_with_gaps[T](
    a: Iterable[T],
    score_func: Callable[[Iterable[T]], float],
) -> Sequence[T]:
    def find_rec(alen: int) -> tuple[
        # Score of best subseq
        float,
        # Best subseq
        list[T],
    ]:
        """
        To find the best subseq of `a[:alen]`
        """

        if alen == 0:
            return (score_func([]), [])

        prev_score: float
        prev_seq: list[T]
        prev_score, prev_seq = find_rec(alen - 1)

        curr_seq: list[T] = [*prev_seq, s[alen - 1]]

        return max(
            # Prefers current one which is longer, if it has same score of previous one
            (score_func(curr_seq), curr_seq),
            (prev_score, prev_seq),
            key=lambda x: x[0],
        )

    s: Sequence[T] = iter_to_seq(a)
    return find_rec(len(s))[1]


def common_subseq[T](a: Iterable[T], b: Iterable[T]) -> Iterable[T]:
    @cache
    # Find the start pos in `a` for longest common subseq aligned from right to left
    # between `a[:alen]` and `b[:blen]`
    def align_rec(alen: int, blen: int) -> int:
        if alen == 0 or blen == 0 or aseq[alen - 1] != bseq[blen - 1]:
            return alen

        return align_rec(alen - 1, blen - 1)

    aseq: Sequence[T] = iter_to_seq(a)
    bseq: Sequence[T] = iter_to_seq(b)

    for k in range(*max(
        (
            (align_rec(i, j), i)
            for i in range(len(aseq) + 1)
            for j in range(len(bseq) + 1)
        ),
        key=lambda x: x[1] - x[0],
    )):
        yield aseq[k]


def is_subseq[T](a: Iterable[T], b: Iterable[T]) -> bool:
    aseq: Sequence[T] = iter_to_seq(a)
    bseq: Sequence[T] = iter_to_seq(b)

    if len(aseq) > len(bseq):
        return False

    return any(
        aseq == bseq[j:j + len(aseq)]
        for j in range(len(bseq) - len(aseq) + 1)
    )


def common_subseq_with_gaps[T](a: Iterable[T], b: Iterable[T]) -> Iterable[T]:
    alignment: tuple[Iterable[T | None], Iterable[T | None]] = align(a, b)

    return (
        x
        for x, y in zip(
            *alignment,
            strict=True,
        )
        if x is not None and y is not None
    )


def is_subseq_with_gaps[T](a: Iterable[T], b: Iterable[T]) -> bool:
    alignment: tuple[Iterable[T | None], Iterable[T | None]] = align(a, b)

    return all(
        y is not None
        for y in alignment[1]
    )


def align[T](
    a: Iterable[T],
    b: Iterable[T],
    *,
    default: T | None = None,
) -> tuple[Iterable[T | None], Iterable[T | None]]:
    def merge(
        prev: tuple[int, tuple[Sequence[T | None], Sequence[T | None]]],
        curr: tuple[T | None, T | None],
    ) -> tuple[int, tuple[Sequence[T | None], Sequence[T | None]]]:
        prev_matches: int
        u: Sequence[T | None]
        v: Sequence[T | None]
        prev_matches, (u, v) = prev

        x: T | None
        y: T | None
        x, y = curr

        return (prev_matches + 1) if x == y else prev_matches, ([*u, x], [*v, y])

    @cache
    def align_rec(alen: int, blen: int) -> tuple[
        int,
        tuple[Sequence[T | None], Sequence[T | None]],
    ]:
        if alen == 0:
            return 0, (
                [default] * blen, bseq[:blen],
            )
        if blen == 0:
            return 0, (
                aseq[:alen], [default] * alen,
            )

        return max(
            (
                merge(align_rec(alen - 1, blen), (aseq[alen - 1], default)),
                merge(align_rec(alen, blen - 1), (default, bseq[blen - 1])),
                merge(align_rec(alen - 1, blen - 1), (aseq[alen - 1], bseq[blen - 1])),
            ),
            key=lambda x: x[0],
        )

    aseq: Sequence[T] = iter_to_seq(a)
    bseq: Sequence[T] = iter_to_seq(b)

    return align_rec(len(aseq), len(bseq))[1]
