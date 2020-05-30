from pathlib import Path

import flask


def static_filename_get(filename):  # noqa: E501
    directory = Path(__file__).parent.parent / 'static'
    response = flask.send_from_directory(directory, filename)
    response.direct_passthrough = False
    return response

