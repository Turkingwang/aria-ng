
from aria import has_validated_properties, validated_property, property_type, property_default, required_property
import tosca, tosca.datatypes

@has_validated_properties
class NetworkInfo(tosca.datatypes.Root):
    """
    The Network type is a complex TOSCA data type used to describe logical network information.
    
    See the `TOSCA Simple Profile v1.0 specification <http://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.0/csprd02/TOSCA-Simple-Profile-YAML-v1.0-csprd02.html#TYPE_TOSCA_DATA_NETWORKINFO>`__
    """

    SHORTHAND_NAME = 'NetworkInfo'
    TYPE_QUALIFIED_NAME = 'tosca:NetworkInfo'
    TYPE_URI = 'tosca.datatypes.network.NetworkInfo'
    
    @property_type(str)
    @validated_property
    def network_name(self):
        """
        The name of the logical network. e.g., "public", "private", "admin". etc.
        """

    @property_type(str)
    @validated_property
    def network_id(self):
        """
        The unique ID of for the network generated by the network provider.
        """

    @property_type(tosca.List(str))
    @validated_property
    def addresses(self):
        """
        The list of IP addresses assigned from the underlying network.
        """
    
@has_validated_properties
class PortInfo(tosca.datatypes.Root):
    """
    The PortInfo type is a complex TOSCA data type used to describe network port information.
    
    See the `TOSCA Simple Profile v1.0 specification <http://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.0/csprd02/TOSCA-Simple-Profile-YAML-v1.0-csprd02.html#TYPE_TOSCA_DATA_PORTINFO>`__
    """

    SHORTHAND_NAME = 'PortInfo'
    TYPE_QUALIFIED_NAME = 'tosca:PortInfo'
    TYPE_URI = 'tosca.datatypes.network.PortInfo'
    
    @property_type(str)
    @validated_property
    def port_name(self):
        """
        The logical network port name.
        """

    @property_type(str)
    @validated_property
    def port_id(self):
        """
        The unique ID for the network port generated by the network provider.
        """
        
    @property_type(str)
    @validated_property
    def network_id(self):
        """
        The unique ID for the network.
        """

    @property_type(str)
    @validated_property
    def mac_address(self):
        """
        The unique media access control address (MAC address) assigned to the port.
        """

    @property_type(tosca.List(str))
    @validated_property
    def addresses(self):
        """
        The list of IP address(es) assigned to the port.
        """

@has_validated_properties
class PortDef(tosca.Integer):
    """
    The PortDef type is a TOSCA data Type used to define a network port.
    
    See the `TOSCA Simple Profile v1.0 specification <http://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.0/csprd02/TOSCA-Simple-Profile-YAML-v1.0-csprd02.html#TYPE_TOSCA_DATA_PORTDEF>`__
    """

    SHORTHAND_NAME = 'PortDef'
    TYPE_QUALIFIED_NAME = 'tosca:PortDef'
    TYPE_URI = 'tosca.datatypes.network.PortDef'

    CONSTRAINTS = {
        'in_range': {'type': tosca.List(str)}}

@has_validated_properties
class PortSpec(tosca.datatypes.Root):
    """
    The PortSpec type is a complex TOSCA data Type used when describing port specifications for a network connection.
    
    See the `TOSCA Simple Profile v1.0 specification <http://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.0/csprd02/TOSCA-Simple-Profile-YAML-v1.0-csprd02.html#TYPE_TOSCA_DATA_PORTSPEC>`__
    """

    SHORTHAND_NAME = 'PortSpec'
    TYPE_QUALIFIED_NAME = 'tosca:PortSpec'
    TYPE_URI = 'tosca.datatypes.network.PortSpec'
    
    @required_property
    @property_default('tcp')
    @property_type(str)
    @validated_property
    def protocol(self):
        """
        The required protocol used on the port.
        """

    @property_type(PortDef)
    @validated_property
    def source(self):
        """
        The optional source port.
        """

    @property_type(tosca.Range)
    @validated_property
    def source_range(self):
        """
        The optional range for source port.
        """

    @property_type(PortDef)
    @validated_property
    def target(self):
        """
        The optional target port.
        """

    @property_type(tosca.Range)
    @validated_property
    def target_range(self):
        """
        The optional range for target port.
        """
