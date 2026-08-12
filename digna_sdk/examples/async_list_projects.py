import argparse
import asyncio

from digna_sdk.examples.common import get_client


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="List projects asynchronously")
    parser.add_argument("--limit", type=int, default=20, help="Maximum rows to return")
    return parser.parse_args()


async def _run(limit: int) -> None:
    api = get_client()
    projects = await api.project.get_projects_async(limit=limit)
    print(f"Found {len(projects)} project(s)")
    for project in projects:
        print(f"- {project.id}: {project.name}")


def main() -> None:
    args = _parse_args()
    asyncio.run(_run(limit=args.limit))


if __name__ == "__main__":
    main()
