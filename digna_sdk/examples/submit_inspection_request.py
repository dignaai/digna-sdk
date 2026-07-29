import datetime

from digna_sdk import DignaClient
from digna_sdk.models.stable_inspection_request_mode import StableInspectionRequestMode


def main() -> None:
    api = DignaClient("https://api.example.com", "<token>")

    result = api.inspection_request.submit_inspection_request(
        project_id=1,
        data_source_ids=[1],
        include_all_data_sources=False,
        mode=StableInspectionRequestMode.ONCE,
        start_date=datetime.date(2025, 1, 1),
        end_date=datetime.date(2025, 1, 31),
        monthly_mode_days=[1],
        weekly_mode_weekdays=["MONDAY"],
        use_notification=False,
    )

    print(f"Inspection request id: {result.id}")


if __name__ == "__main__":
    main()
