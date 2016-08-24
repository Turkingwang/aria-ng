#
# Copyright (c) 2016 GigaSpaces Technologies Ltd. All rights reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#

from ..loading import LiteralLocation, UriLocation
from .exceptions import ReaderNotFoundError
from .yaml import YamlReader
from .jinja import JinjaReader

class ReaderSource(object):
    """
    Base class for ARIA reader sources.
    
    Reader sources provide appropriate :class:`Reader` instances for locations.
    """

    def get_reader(self, context, location, loader):
        raise ReaderNotFoundError('location: %s' % location)

EXTENSIONS = {
    '.yaml': YamlReader,
    '.jinja': JinjaReader}

class DefaultReaderSource(ReaderSource):
    """
    The default ARIA reader source will generate a :class:`YamlReader` for
    locations that end in ".yaml", and a :class:`JinjaReader` for locations
    that end in ".jinja". 
    """
    
    def __init__(self, literal_reader_class=YamlReader):
        super(DefaultReaderSource, self).__init__()
        self.literal_reader_class = literal_reader_class

    def get_reader(self, context, location, loader):
        if isinstance(location, LiteralLocation):
            return self.literal_reader_class(context, self, location, loader)
        
        elif isinstance(location, UriLocation):
            for extension, reader_class in EXTENSIONS.iteritems():
                if location.uri.endswith(extension):
                    return reader_class(context, self, location, loader)
                
        return super(DefaultReaderSource, self).get_reader(context, location, loader)
