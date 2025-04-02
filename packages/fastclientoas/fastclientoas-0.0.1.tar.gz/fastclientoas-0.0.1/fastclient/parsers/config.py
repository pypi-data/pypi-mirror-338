from pathlib import Path

from fastclient import const
from fastclient.os import HTTP
from fastclient.utils import temp
from fastclient.utils import urls


def getconfig(file: str) -> tuple[Path, bool]:
    if urls.checkurl(file):
        return temp.getfile(HTTP.download(file), extension=const.EXTENSION_TOML), True
    else:
        return Path(file), False
