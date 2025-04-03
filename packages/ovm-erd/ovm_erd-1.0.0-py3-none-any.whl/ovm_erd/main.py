import argparse
from ovm_erd import erd_graphviz
from ovm_erd.erd_sql import erd_sql


def main():
    parser = argparse.ArgumentParser(description="Generate ERDs and SQL from a repository.")
    subparsers = parser.add_subparsers(dest="command")

    graph_parser = subparsers.add_parser("graphviz")
    graph_parser.add_argument("--path", type=str, default="./examples")
    graph_parser.add_argument("--ensemble", type=str, default=None)

    sql_parser = subparsers.add_parser("sql")
    sql_parser.add_argument("--path", type=str, default="./examples")
    sql_parser.add_argument("--ensemble", type=str, required=True)

    args = parser.parse_args()

    if args.command == "graphviz":
        erd_graphviz(path=args.path, ensemble=args.ensemble)
    elif args.command == "sql":
        erd_sql(path=args.path, ensemble=args.ensemble)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
