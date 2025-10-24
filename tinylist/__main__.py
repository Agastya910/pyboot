import argparse
from tinylist import TinyList


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    # p_clear= sub.add_parser('clear', help= 'empty the list')
    p_add = sub.add_parser("add", help="append items")
    p_add.add_argument("items", nargs="+", help="strings to store")
    iris_parser = sub.add_parser("iris", help="Iris dataset utils")
    iris_parser.add_argument(
        "--summary", action="store_true", help="print mean and std of numeric colums"
    )
    args = parser.parse_args()

    if args.cmd == "iris":
        if args.summary:
            from iris_summary import show_summary

            show_summary()
        else:
            print("Use --summary to see stats")

    tl = TinyList()
    if args.cmd == "add":
        for it in args.items:
            tl.append(it)
        print(list(tl[i] for i in range(len(tl))))
        popped = tl.pop()
        print("pop ->", popped)
        print("remaining:", [tl[i] for i in range(len(tl))])

        tl.remove("b")
        print("after remove('b'):", [tl[i] for i in range(len(tl))])

    if args.cmd == "clear":
        print("TinyList cleared.")


if __name__ == "__main__":
    main()
