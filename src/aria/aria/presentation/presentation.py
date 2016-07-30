
from ..utils import classname, deepclone
from .utils import validate_no_short_form, validate_no_unknown_fields, validate_known_fields
from clint.textui import puts

class PresentationBase(object):
    """
    Base class for ARIA presentation classes.
    """
    
    def __init__(self, name=None, raw=None, container=None):
        self._name = name
        self._raw = raw
        self._container = container

    def _validate(self, context):
        pass

    @property
    def _fullname(self):
        if self._name is not None:
            return self._name
        elif self._container is not None:
            return self._container._fullname
        return classname(self)

    @property
    def _locator(self):
        if hasattr(self._raw, '_locator'):
            return self._raw._locator
        elif self._container is not None:
            return self._container._locator
        return None

    def _get_child_locator(self, name):
        locator = self._locator
        return locator.get_child(name) if locator is not None else None

    def _get_grandchild_locator(self, name1, name2):
        locator = self._locator
        return locator.get_grandchild(name1, name2) if locator is not None else None

    @property
    def _method_cache_info(self):
        r = {}
        for k in self.__class__.__dict__:
            p = getattr(self, k)
            if hasattr(p, 'cache_info'):
                r[k] = p.cache_info()
        return r

    def _reset_method_cache(self):
        for k in self.__class__.__dict__:
            p = getattr(self, k)
            if hasattr(p, 'cache_clear'):
                p.cache_clear()

    def _dump(self, context):
        if self._name:
            puts(context.style.node(self._name))
            with context.style.indent:
                self._dump_content(context)
        else:
            self._dump_content(context)
                            
    def _dump_content(self, context, field_names=None):
        if field_names:
            for field_name in field_names:
                self._dump_field(context, field_name)
        elif hasattr(self, '_iter_field_names'):
            for field_name in self._iter_field_names():
                self._dump_field(context, field_name)
        else:
            puts(context.style.literal(self._raw))

    def _dump_field(self, context, field_name):
        field = self.FIELDS[field_name]
        field.dump(self, context) 

    def _clone(self, container=None):
        raw = deepclone(self._raw)
        if container is None:
            container = self._container
        return self.__class__(name=self._name, raw=raw, container=container)

class Presentation(PresentationBase):
    """
    Base class for ARIA presentations. A presentation is a Pythonic wrapper around
    agnostic raw data, adding the ability to read and modify the data with proper
    validation. 
    
    ARIA presentation classes will often be decorated with @has_fields, as that
    mechanism automates a lot of field-specific validation. However, that is not a
    requirement.
    
    Make sure that your utility property and method names begin with a "_", because
    those names without a "_" prefix are normally reserved for fields. 
    """
    
    def _validate(self, context):
        validate_no_short_form(self, context)
        validate_no_unknown_fields(self, context)
        validate_known_fields(self, context)

class AsIsPresentation(PresentationBase):
    """
    Base class for trivial ARIA presentations that provide the raw value as is.
    """
    
    @property
    def value(self):
        return self._raw
    
    @value.setter
    def value(self, value):
        self._raw = value
