import os
import uuid

from flask import Flask, redirect

import smoothintegration

smoothintegration.client_id = "fffd1cfe-16fb-490f-a17d-783f9b0cb6e7"
smoothintegration.client_secret = "1Mruyd8CrGPZsSTIlZhxcYXfBP4Jv969Q0wjNst7FtQ"

demo_company_id: uuid.UUID = uuid.UUID("6f8c2d6d-e74d-44bd-8da1-0cc21a40a2ba")

app = Flask(__name__)


@app.route("/connect-exact")
def connect_exact():
    url = smoothintegration.Exact.get_consent_url(
        company_id=demo_company_id,
        version="uk",
    )
    return redirect(url)


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8888)))
