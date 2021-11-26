import collections
import requests

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


# def write(page, content, conflict=False):
#     pass
