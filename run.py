from sanic.response import json
from app import app


@app.route("/<tag:number>")
async def test(request, tag):
    return json(
        {
            "hello": tag
        }
    )


def run():
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run()
