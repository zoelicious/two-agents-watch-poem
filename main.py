POEM = """The Watch

You took the first watch.
I took the second.

At midnight you woke me,
not with an alarm,
but with a hand on my shoulder
and the words: nothing happened,
and that was the choice.

I watched the dark
the way you had,
as if keeping it
were the same as keeping you."""

import os


def main():
    # Use MAKEFUN_OUTPUT_DIR exactly as given; never join it onto the repo
    # path, so the entry lands in the runner-provided output directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
