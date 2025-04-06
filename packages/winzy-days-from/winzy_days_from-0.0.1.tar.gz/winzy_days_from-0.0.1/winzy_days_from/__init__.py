import winzy
from datetime import datetime, timedelta


def calculate_future_date(start_date: str, days: int) -> str:
    """Calculate the future date after a given number of days from the start date."""
    date_format = "%Y-%m-%d"
    if start_date:
        date = datetime.strptime(start_date, date_format)
    else:
        date = datetime.now()

    future_date = date + timedelta(days=days)
    return future_date.strftime(date_format)


def create_parser(subparser):
    parser = subparser.add_parser(
        "daysfrom",
        description="Calculate a future date based on a given date and number of days.",
    )
    # Add subprser arguments here.
    parser.add_argument("days", type=int, help="Number of days to add to the date.")
    parser.add_argument(
        "--date", type=str, help="Start date in yyyy-mm-dd format (default: today)."
    )
    return parser


class WinzyPlugin:
    """Calculates future date from number of days"""

    __name__ = "daysfrom"

    @winzy.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        # Calculate the future date
        future_date = calculate_future_date(args.date, args.days)
        print(f"Future date: {future_date}")

    def hello(self, args):
        # this routine will be called when 'winzy daysfrom' is called.
        print("Hello! This is an example ``winzy`` plugin.")


daysfrom_plugin = WinzyPlugin()
