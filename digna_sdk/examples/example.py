from digna_sdk import DignaClient, NotFoundError


def main() -> None:
    api = DignaClient("https://api.example.com", "<token>")

    try:
        project = api.project.get_project(project_id=1)
    except NotFoundError:
        print("Project not found")
        return

    print(f"Project: {project.name}")


if __name__ == "__main__":
    main()
