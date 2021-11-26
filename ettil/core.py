from .exceptions import ConflictError, WriteError
import collections
import requests
import json

# I could just return the ETT API data directly, but this ensures that if the
# ETT API ever changes, the output of these functions will stay the same.
PageData = collections.namedtuple('PageData', [
    'title',
    'timestamp',
    'ip',
    'content'
])


def get(page):
    r = requests.get(f'https://tikolu.net/edit/.api/{page}')
    r.raise_for_status()
    data = r.json()

    # Ensure that the parsed timestamp is an integer so that it can be passed
    # to ettil.write later if desired.
    if data['timestamp'] is None:
        data['timestamp'] = 0

    return PageData(
        title=page,
        timestamp=data['timestamp'],
        ip=data['ip'],
        content=data['content']
    )


def get_raw(page):
    r = requests.get(f'https://tikolu.net/edit/.text/{page}')
    r.raise_for_status()

    return r.text


def write(page, content, conflict=None):
    # The ETT API has issues if you provide the data out of order.
    # I have no idea why this is the case, but it's dealt with here.
    ignoreconflict = conflict is None
    timestamp = "0" if ignoreconflict else str(conflict)

    payload = json.dumps(collections.OrderedDict(
        title=page,
        content=content,
        timestamp=timestamp,
        ignoreconflict=ignoreconflict
    ), separators=(',', ':'))

    r = requests.post('https://tikolu.net/edit/.index.php', data=payload)
    r.raise_for_status()

    responce = r.json()
    if responce["status"] == "error":
        if responce["cause"] == "confilct":
            raise ConflictError
        else:
            raise WriteError(responce.cause, responce.message)

    return responce["timestamp"]
