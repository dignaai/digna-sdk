import argparse

from digna_sdk.examples.common import get_client


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="List projects")
    parser.add_argument("--limit", type=int, default=20, help="Maximum rows to return")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    api = get_client()

    projects = api.project.get_projects(limit=args.limit)
    print(f"Found {len(projects)} project(s)")
    for project in projects:
        print(f"- {project.id}: {project.name}")


if __name__ == "__main__":
    main()
