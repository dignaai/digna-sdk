import argparse

from digna_sdk import ApiResponseError, NotFoundError
from digna_sdk.examples.common import get_client


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Demonstrate SDK error handling")
    parser.add_argument("--project-id", type=int, required=True, help="Project ID to fetch")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    api = get_client()

    try:
        project = api.project.get_project(project_id=args.project_id)
        print(f"Project found: {project.id} - {project.name}")
    except NotFoundError:
        print("Project not found")
    except ApiResponseError as exc:
        print(f"Request failed: {exc}")


if __name__ == "__main__":
    main()
