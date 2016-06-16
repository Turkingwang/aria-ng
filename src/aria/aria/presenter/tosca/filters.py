
from ... import tosca_specification, has_fields, object_list_field
from .. import Presentation
from .definitions import PropertyDefinition, CapabilityDefinition

@has_fields
@tosca_specification('3.5.4')
class NodeFilter(Presentation):
    """
    A node filter definition defines criteria for selection of a TOSCA Node Template based upon the template's property values, capabilities and capability properties.
    
    See the `TOSCA Simple Profile v1.0 specification <http://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.0/csprd02/TOSCA-Simple-Profile-YAML-v1.0-csprd02.html#DEFN_ELEMENT_NODE_FILTER_DEFN>`__
    """

    @object_list_field(PropertyDefinition)
    def properties():
        """
        An optional sequenced list of property filters that would be used to select (filter) matching TOSCA entities (e.g., Node Template, Node Type, Capability Types, etc.) based upon their property definitions' values.
        
        :rtype: list of :class:`PropertyDefinition`
        """

    @object_list_field(CapabilityDefinition)
    def capabilities():
        """
        An optional sequenced list of property filters that would be used to select (filter) matching TOSCA entities (e.g., Node Template, Node Type, Capability Types, etc.) based upon their capabilities' property definitions' values.
        
        :rtype: list of :class:`CapabilityDefinition`
        """

@has_fields
@tosca_specification('3.5.3')
class PropertyFilter(Presentation):
    """
    A property filter definition defines criteria, using constraint clauses, for selection of a TOSCA entity based upon it property values.
    
    See the `TOSCA Simple Profile v1.0 specification <http://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.0/csprd02/TOSCA-Simple-Profile-YAML-v1.0-csprd02.html#DEFN_ELEMENT_PROPERTY_FILTER_DEFN>`__
    """

    # TODO