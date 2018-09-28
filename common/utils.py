import os
import random
import string
import hashlib
import functools
import contextlib
from datetime import datetime

from django.conf import settings

TEST_PATH = path = os.path.join(settings.MEDIA_ROOT, 'test')


def is_int(v):
    try:
        int(v)
        return True
    except (TypeError, ValueError):
        return False


def str2bool(v):
    return isinstance(v, str) and v.lower() in ("yes", "true", "t", "1")


def random_string(n=16):
    choices = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(choices) for _ in range(n))


def random_email():
    return f'{random_string()}@test.com'


def make_path(pattern, name=None):
    now = datetime.now()
    key1 = hashlib.md5(f'{now.year}{now.month}'.encode()).hexdigest()[:6]
    key2 = hashlib.md5(f'{now.day}'.encode()).hexdigest()[:6]
    args = [pattern, key1, key2]
    if name:
        args.append(name)
    return os.path.join(*args)


def parse_ids_list(_list):
    ids_list = []
    if isinstance(_list, list):
        for _id in _list:
            if is_int(_id):
                ids_list.append(int(_id))
    return ids_list


def str_without_symbols(_string):
    return str(_string or '').translate(str.maketrans({key: None for key in string.punctuation})).strip()


def str_multiple_replace(text: str, mapping: dict)-> str:
    return functools.reduce(
        lambda t, p: t.replace(p[0], p[1]),
        mapping.items(), text
    )


@contextlib.contextmanager
def multiple_patch(mock_patches):
    mocks = []
    for mock_patch in mock_patches:
        _mock = mock_patch.start()
        mocks.append(_mock)
    yield mocks
    for mock_patch in mock_patches:
        mock_patch.stop()
