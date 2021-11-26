'''The page reading/writing functions.'''
import collections
import json
import requests
from .exceptions import ConflictError, UnmodifiedError, WriteError  # noqa

# I could just return the ETT API data directly, but this ensures that if the
# ETT API ever changes, the output of these functions will stay the same.
PageData = collections.namedtuple('PageData', [
    # title is simply the name of the page. There is no leading '/'!
    'title',

    # timestamp holds the Unix epoch time of when the page was last edited.
    # This value will *always* be an integer, even on never-modified pages.
    'timestamp',

    # ip holds the IP address of the last person to edit the page as a string.
    # On a page that has never been editted, this will be set to None.
    'ip',

    # content holds the text that is on the requested page.
    'content'
])


def get(page):
    '''
    Retreives the content and metadata of a page and then returns it as a
    PageData named tuple. Find more information at PageData's definition.
    '''
    resp = requests.get(f'https://tikolu.net/edit/.api/{page}')
    resp.raise_for_status()
    data = resp.json()

    if data['timestamp'] is None:
        data['timestamp'] = 0

    return PageData(
        title=page,
        timestamp=data['timestamp'],
        ip=data['ip'],
        content=data['content']
    )


def get_raw(page):
    '''
    Retreives *only* the text on a page without its metadata.
    This is slightly faster than ettil.get and uses less bandwidth.
    '''
    resp = requests.get(f'https://tikolu.net/edit/.text/{page}')
    resp.raise_for_status()

    return resp.text


def write(page, content, conflict=None):
    '''
    Writes the provided content to the provided page.

    The conflict variable can optionally be set to the timestamp at which the
    page was last  retrieved. If it is, write will throw a ConflictError if
    the page has been updated since then to avoid overwriting those changes.
    '''
    # The ETT API has issues if you provide the data out of order.
    # I have no idea why this is the case, but it's dealt with here.
    ignoreconflict = conflict is None
    timestamp = '0' if ignoreconflict else str(conflict)

    payload = json.dumps(collections.OrderedDict(
        title=page,
        content=content,
        timestamp=timestamp,
        ignoreconflict=ignoreconflict
    ), separators=(',', ':'))

    resp = requests.post('https://tikolu.net/edit/.index.php', data=payload)
    resp.raise_for_status()

    data = resp.json()
    if data['status'] == 'error':
        if data['cause'] == 'conflict':
            raise ConflictError
        if data['cause'] == 'unmodified':
            raise UnmodifiedError
        raise WriteError(data['cause'], data['message'])

    return data['timestamp']
