from postbin import main
import argparse

parser = argparse.ArgumentParser(description="Run a request logging server.")
parser.add_argument(
    "--port", type=int, default=5000, help="Port to run the server on (default: 5000)"
)
args = parser.parse_args()
port = args.port
main(port)
