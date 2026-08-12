import argparse

from digna_sdk.examples.common import get_client


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="List data sets for a data source")
    parser.add_argument("--data-source-id", type=int, required=True, help="Data source ID")
    parser.add_argument("--limit", type=int, default=50, help="Maximum rows to return")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    api = get_client()

    data_sets = api.data_set.get_data_sets(data_source_id=args.data_source_id, limit=args.limit)
    print(f"Found {len(data_sets)} data set(s) for data source {args.data_source_id}")
    for data_set in data_sets:
        print(f"- {data_set.id}: {data_set.name}")


if __name__ == "__main__":
    main()
