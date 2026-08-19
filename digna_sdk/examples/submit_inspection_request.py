import argparse
import datetime

from digna_sdk.examples.common import get_client
from digna_sdk.models.stable_inspection_request_mode import StableInspectionRequestMode


def _parse_iso_date(value: str) -> datetime.date:
    try:
        return datetime.date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Dates must be in YYYY-MM-DD format") from exc


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Submit an inspection request")
    parser.add_argument("--project-id", type=int, required=True, help="Project ID")
    parser.add_argument(
        "--data-source-id",
        dest="data_source_ids",
        action="append",
        type=int,
        default=[],
        help="Data source ID (can be repeated)",
    )
    parser.add_argument(
        "--include-all-data-sources",
        action="store_true",
        help="Ignore --data-source-id and run for all project data sources",
    )
    parser.add_argument(
        "--mode",
        choices=[mode.value.lower() for mode in StableInspectionRequestMode],
        default="weekly",
        help="Inspection mode",
    )
    parser.add_argument("--start-date", type=_parse_iso_date, required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", type=_parse_iso_date, required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument(
        "--weekday",
        dest="weekdays",
        action="append",
        type=int,
        default=[],
        help="Weekday integer for weekly mode (repeatable)",
    )
    parser.add_argument(
        "--month-day",
        dest="month_days",
        action="append",
        type=int,
        default=[],
        help="Day of month for monthly mode (repeatable)",
    )
    parser.add_argument("--use-notification", action="store_true", help="Enable notifications")
    return parser.parse_args()


def _validate_args(args: argparse.Namespace) -> None:
    if args.end_date < args.start_date:
        raise ValueError("end-date must be greater than or equal to start-date")

    if not args.include_all_data_sources and not args.data_source_ids:
        raise ValueError("Provide at least one --data-source-id or set --include-all-data-sources")

    if args.mode == "weekly" and not args.weekdays:
        raise ValueError("Weekly mode requires at least one --weekday")

    if args.mode == "monthly" and not args.month_days:
        raise ValueError("Monthly mode requires at least one --month-day")


def main() -> None:
    args = _parse_args()
    _validate_args(args)

    api = get_client()
    mode = StableInspectionRequestMode(args.mode.upper())

    resp = api.inspection_request.submit_inspection_request(
        project_id=args.project_id,
        data_source_ids=args.data_source_ids,
        include_all_data_sources=args.include_all_data_sources,
        mode=mode,
        start_date=args.start_date,
        end_date=args.end_date,
        monthly_mode_days=args.month_days,
        weekly_mode_weekdays=args.weekdays,
        use_notification=args.use_notification,
    )
    print(f"Inspection request submitted successfully, ID: {resp.id}")


if __name__ == "__main__":
    main()
