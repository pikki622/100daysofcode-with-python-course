import uplink
from requests import Response


class FormatError(Exception):
    pass


@uplink.response_handler
def raise_for_status(response: Response):
    response.raise_for_status()
    return response


@uplink.response_handler
def response_to_data(response: Response):
    try:
        return response.json()
    except Exception as x:
        raise FormatError(
            f"Invalid format, could not parse JSON. Error: {x}, status={response.status_code}, text={response.text}"
        ) from x
