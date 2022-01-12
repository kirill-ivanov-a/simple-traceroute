"""Function for parsing console input"""
import argparse
import socket

from traceroute import Traceroute

__all__ = ["parse_args"]


def parse_args() -> argparse.Namespace:
    """Parses console input when starting a module
    Returns
    -------
    Namespace with parsed arguments.
    """

    def positive_int(value: str) -> int:
        try:
            value = int(value)
            if value <= 0:
                raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
        except ValueError as error:
            raise argparse.ArgumentTypeError(f"{value} is not an integer") from error
        return value

    parser = argparse.ArgumentParser(
        prog="python -m traceroute",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.set_defaults(func=run_traceroute)
    parser.add_argument(
        "dest",
        metavar="dest",
        help="destination host",
    )
    parser.add_argument(
        "--max-hops",
        "-m",
        dest="max_hops",
        metavar="NUM",
        type=positive_int,
        help="set maximal hop number",
        default=64,
    )
    parser.add_argument(
        "--first-hop",
        "-f",
        dest="first_hop",
        metavar="NUM",
        type=positive_int,
        help="set initial hop number (TTL)",
        default=1,
    )
    parser.add_argument(
        "--port",
        "-p",
        type=positive_int,
        metavar="PORT",
        help="set destination port",
        default=33434,
    )

    return parser.parse_args()


def run_traceroute(args: argparse.Namespace):
    try:
        Traceroute(
            dest_name=args.dest,
            dest_ip=socket.gethostbyname(args.dest),
            port=args.port,
            first_hop=args.first_hop,
            max_hops=args.max_hops,
        ).print_trace()
    except PermissionError:
        print("Operation not permitted")
    except socket.error as e:
        print(f"Unable to resolve host {args.dest}: {e}")
