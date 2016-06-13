
from aria import has_validated_properties, validated_property, property_type, property_default, required_property
import tosca, tosca.datatypes

@has_validated_properties
class CPUAllocation(tosca.datatypes.Root):
    """
    Granular CPU allocation requirements for NFV workloads.

    See the `TOSCA Simple Profile for NFV v1.0 specification <http://docs.oasis-open.org/tosca/tosca-nfv/v1.0/tosca-nfv-v1.0.html#TYPE_TOSCA_DATA_PORTINFO>`__ (wrong anchor)
    """

    SHORTHAND_NAME = 'CPUAllocation'
    TYPE_QUALIFIED_NAME = 'tosca:CPUAllocation'
    TYPE_URI = 'tosca.datatypes.compute.container.Container.Architecture.CPUAllocation' # mismatch with TOSCA Simple Profile
    
    @property_type(str)
    @validated_property
    def cpu_affinity(self):
        """
        Describes whether vCPU need to be pinned to dedicated CPU core or shared dynamically.
        """

    @property_type(str)
    @validated_property
    def thread_allocation(self):
        """
        Describe thread allocation requirement.
        """

    @property_type(tosca.Integer)
    @validated_property
    def socket_count(self):
        """
        Number of CPU sockets.
        """

    @property_type(tosca.Integer)
    @validated_property
    def core_count(self):
        """
        Number of cores per socket.
        """

    @property_type(tosca.Integer)
    @validated_property
    def thread_count(self):
        """
        Number of threads per core.
        """

@has_validated_properties
class NUMA(tosca.datatypes.Root):
    """
    Granular Non-Uniform Memory Access (NUMA) topology requirements for NFV workloads.

    See the `TOSCA Simple Profile for NFV v1.0 specification <http://docs.oasis-open.org/tosca/tosca-nfv/v1.0/tosca-nfv-v1.0.html#_Toc447714697>`__
    """

    SHORTHAND_NAME = 'NUMA'
    TYPE_QUALIFIED_NAME = 'tosca:NUMA'
    TYPE_URI = 'tosca.datatypes.compute.container.Container.Architecture.NUMA' # mismatch with TOSCA Simple Profile

    @property_type(tosca.Integer)
    @validated_property
    def id(self):
        """
        CPU socket identifier.
        """

    @property_type(tosca.Map(tosca.Integer))
    @validated_property
    def vcpus(self):
        """
        List of specific host cpu numbers within a NUMA socket complex.

        TODO: need a new base type, with non-overlapping, positive value validation (exclusivity),
        """

    @property_type(tosca.Size)
    @validated_property
    def mem_size(self):
        """
        Size of memory allocated from this NUMA memory bank.
        """
