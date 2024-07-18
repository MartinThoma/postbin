from flask import Flask, request
from rich.console import Console
from rich.table import Table

app = Flask(__name__)
console = Console()


@app.route(
    "/",
    defaults={"path": ""},
    methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
)
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
def catch_all(path):
    console.log(f"Received request at: {request.path}")

    # Create a table for headers
    table = Table(title="Request Headers")
    table.add_column("Header", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    for header, value in request.headers.items():
        table.add_row(header, value)

    console.print(table)

    if request.is_json:
        console.log(f"JSON Payload: {request.json}")
    else:
        console.log(f"Data Payload: {request.data}")

    return "Request logged", 200


def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
