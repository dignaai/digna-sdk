from digna_sdk import DignaClient


def main() -> None:
    api = DignaClient("https://api.example.com", "<token>")
    project_id = 1

    data_sources = api.data_source.get_data_sources(project_id=project_id, limit=50)
    print(f"Found {len(data_sources)} data source(s) for project {project_id}")

    for data_source in data_sources:
        data_sets = api.data_set.get_data_sets(data_source_id=data_source.id, limit=50)
        print(f"- {data_source.name}: {len(data_sets)} data set(s)")


if __name__ == "__main__":
    main()
