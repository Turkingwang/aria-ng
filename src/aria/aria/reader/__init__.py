
from exceptions import *
from reader import *
from source import *
from yaml import *

class DefaultReaderSource(ReaderSource):
    """
    The default ARIA reader source will generate a :class:`YamlReader` for
    locators that end in ".yaml".
    """

    def get_reader(self, locator, loader):
        if isinstance(locator, basestring) and locator.endswith('.yaml'):
            return YamlReader(loader)
        return super(DefaultReaderSource, self).get_reader(locator, loader)

__all__ = [
    'ReaderError',
    'ReaderNotFoundReaderError',
    'Reader',
    'ReaderSource',
    'DefaultReaderSource']
