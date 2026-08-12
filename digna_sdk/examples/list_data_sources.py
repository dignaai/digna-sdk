import argparse

from digna_sdk import DignaClient
from digna_sdk.examples.common import get_client


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="List data sources for a project")
    parser.add_argument("--project-id", type=int, help="Project ID; if omitted, the first project is used")
    parser.add_argument("--limit", type=int, default=50, help="Maximum rows to return")
    parser.add_argument(
        "--include-data-sets",
        action="store_true",
        help="Also query and print data set counts per data source",
    )
    return parser.parse_args()


def _resolve_project_id(project_id: int | None, api: DignaClient) -> int:
    if project_id is not None:
        return project_id

    projects = api.project.get_projects(limit=1)
    if not projects:
        raise RuntimeError("No projects found. Pass --project-id explicitly.")
    return projects[0].id


def main() -> None:
    args = _parse_args()
    api = get_client()
    project_id = _resolve_project_id(args.project_id, api)

    data_sources = api.data_source.get_data_sources(project_id=project_id, limit=args.limit)
    print(f"Found {len(data_sources)} data source(s) for project {project_id}")

    for data_source in data_sources:
        if args.include_data_sets:
            data_sets = api.data_set.get_data_sets(data_source_id=data_source.id, limit=args.limit)
            print(f"- {data_source.id}: {data_source.name} ({len(data_sets)} data set(s))")
        else:
            print(f"- {data_source.id}: {data_source.name}")


if __name__ == "__main__":
    main()
