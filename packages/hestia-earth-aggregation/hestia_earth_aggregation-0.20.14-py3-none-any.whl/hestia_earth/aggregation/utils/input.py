from hestia_earth.schema import SchemaType, InputStatsDefinition
from hestia_earth.utils.model import linked_node


def new_input(data: dict):
    node = {'@type': SchemaType.INPUT.value}
    term = data.get('term')
    node['term'] = linked_node(term)
    value = data.get('value')
    if value is not None:
        node['value'] = [value]
        node['statsDefinition'] = InputStatsDefinition.CYCLES.value
    return node
