from datetime import datetime
import numpy as np
from typing import Any, Mapping, NotRequired, Optional
import pandas as pd

from ...common.pandas_utils import is_series_or_frame
from ..basics import ModelRecipe
from ..model_wrapper import ModelWrapper
from ..resource_types._list import Datasource
from .profiling_types import ModelRunStats


class DetailedModelRecipe(ModelRecipe):
    resource_type: NotRequired[str]
    datasource: NotRequired[Datasource]


_ignored_params = ['location', 'interval', 'context']


def _make_recipe_params_from_bound(bound_params: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in bound_params.items():
        translated = None
        if is_series_or_frame(value):
            if 'origin' in value.attrs:
                origin: DetailedModelRecipe = value.attrs['origin'].copy()
            else:
                origin = {'model_name': 'unknown'}
            if origin['model_name'] == 'read_cached_resource':
                translated = {'model_name': 'cache'}
            else:
                origin['resource_type'] = value.attrs.get('resource_type')
                if 'datasource' in value.attrs:
                    result[key] = value.attrs['datasource']
                translated = origin
        elif key in _ignored_params:
            continue
        elif isinstance(value, (int, float, str, bool, pd.Timestamp, datetime)):
            translated = value
        elif isinstance(value, (list, np.ndarray)):
            translated = {'data_type': 'array', 'length': len(value)}
        else:
            translated = {'data_type': 'unknown'}
        result[key] = translated
    return result


def _make_model_recipe(model_wrapper: ModelWrapper, bound_params) -> ModelRecipe:
    return {
        'model_name': model_wrapper.name,
        'params': _make_recipe_params_from_bound(bound_params),
    }


def origin_collector_output_filter(
    model_wrapper: ModelWrapper,
    bound_params: dict[str, Any],
    result: Any,
) -> Any:
    if is_series_or_frame(result):
        result.attrs['origin'] = _make_model_recipe(model_wrapper, bound_params)
    return result


def origin_tree_to_flowchart(
    origin: DetailedModelRecipe | pd.Series | pd.DataFrame,
    *,
    model_stats_dict: Optional[dict[str, ModelRunStats]] = None,
) -> str:
    if is_series_or_frame(origin):
        origin = origin.attrs['origin']
    assert isinstance(origin, dict)
    id_counter = 1

    nodemap = {}

    # nodes = []
    edges = []

    def add_node(id: str, name: str, params: Optional[Mapping] = None, edge: Optional[str] = None) -> None:
        nonlocal id_counter

        if params is None:
            params = {}

        node_text = f'`**{name}**'
        deps = []
        for key, value in params.items():
            if isinstance(value, dict):
                if 'model_name' in value:
                    if value['model_name'] == 'cache':
                        continue
                    id_counter += 1
                    deps.append(value)
            else:
                node_text += f'\n{key}: {value}'
        if node_text in nodemap:
            id = nodemap[node_text]['id']
            nodemap[node_text]['times'] += 1
        else:
            # nodes.append(full_text)
            nodemap[node_text] = {
                'id': id,
                'text': node_text,
                'times': 1,
                'model_name': name,
            }
        if edge:
            edge_text = f'{id} --> {edge}'
            if edge_text not in edges:
                edges.append(edge_text)
        for dep in deps:
            id_counter += 1
            new_id = f'node{id_counter}'
            add_node(new_id, dep['model_name'], dep.get('params'), edge=id)

    add_node('node1', origin['model_name'], origin.get('params'))

    result = 'flowchart RL\n\n'
    for mapping in nodemap.values():
        text = mapping['text']
        if mapping['times'] > 1:
            text += f"\n<span style='color:#cc5555'>used **{mapping['times']}** times</span>"
        if model_stats_dict and mapping['model_name'] in model_stats_dict:
            text += f"\n<span style='color:#5555cc'>execution time: {model_stats_dict[mapping['model_name']].sum_execution_time:.3f}s</span>"
        full_text = f'{mapping["id"]}["{text}`"]'

        result += f'{full_text}\n\n'

    for edge in edges:
        result += f'{edge}\n'

    return result
