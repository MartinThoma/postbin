from flask import Flask, request
from rich.console import Console
from rich.table import Table
from rich.text import Text
import logging
import argparse

# Disable Flask logging
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

app = Flask(__name__)
console = Console()


@app.route(
    "/",
    defaults={"path": ""},
    methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
)
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
def catch_all(path):
    pre_text = Text("Received Request: ")
    endpoint_text = Text(f"{request.method} {request.path}", style="bold red")
    console.log(pre_text + endpoint_text)

    # Create a table for headers
    table = Table(title="Request Headers")
    table.add_column("Header", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    for header, value in request.headers.items():
        table.add_row(header, value)

    console.print(table)

    if request.is_json:
        console.log(f"JSON Payload: {request.json}")
    elif request.form:
        console.log("Form Data:")
        form_data = request.form.to_dict(flat=False)
        for key, values in form_data.items():
            for value in values:
                console.log(f"  {key}: {value}")
    else:
        console.log(f"Data Payload: {request.data}")

    return "", 200


def main(port: int):
    print(f"Starting server on port {port}")
    print(
        "Try this: curl -X POST http://localhost:"
        + str(port)
        + "/ -H 'Content-Type: application/json' -d '{\"key\": \"value\"}'"
    )
    app.run(host="0.0.0.0", port=port, debug=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a request logging server.")
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        help="Port to run the server on (default: 5000)",
    )
    args = parser.parse_args()
    port = args.port
    main(port)
