
from misc import Input, Output
from types import NodeType, RelationshipType
from templates import NodeTemplate
from aria.presenter import has_fields, object_dict_field
from aria.presenter.tosca_simple import Profile as BaseProfile

@has_fields
class Profile(BaseProfile):
    @object_dict_field(Input)
    def inputs(self):
        """
        :class:`Input`
        """

    @object_dict_field(Output)
    def outputs(self):
        """
        :class:`Output`
        """
    
    @object_dict_field(NodeType)
    def node_types(self):
        """
        :class:`NodeType`
        """

    @object_dict_field(RelationshipType)
    def relationships(self):
        """
        :class:`RelationshipType`
        """
        return self._get_object_dict('relationships', RelationshipType)
    
    @object_dict_field(NodeTemplate)
    def node_templates(self):
        """
        :class:`NodeTemplate`
        """