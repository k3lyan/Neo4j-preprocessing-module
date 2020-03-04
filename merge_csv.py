import pandas as pd
from logzero import logger
from datetime import datetime


def get_dict_key(key, payload, not_found_return=None):
    if key is None:
        return not_found_return
    if key.find('.') == -1:
        if key in payload:
            return payload[key]
        return not_found_return
    if key[:key.find('.')] not in payload:
        return not_found_return
    return get_dict_key(key[key.find('.') + 1:], payload[key[:key.find('.')]])


class NodesMerger:
    def __init__(self, paths_inputs: dict, path_output: str):
        self.paths_inputs = paths_inputs
        self.path_output = path_output

    def merge_node(self, node_type: str):
        csv_paths = self._get_node_csv_paths(node_type)
        logger.info(f'CSV paths:\n{csv_paths}')
        node_dataframes = self._load_node_dataframes(csv_paths)
        logger.info(f'{node_type} fr: \n{node_dataframes["fr"].head()}\n{node_dataframes["fr"].shape}') 
        logger.info(f'{node_type} en:\n{node_dataframes["en"].head()}\n{node_dataframes["en"].shape}') 
        self._preprocess_dataframes(node_dataframes)
        logger.info(f'Preprocessed {node_type} fr: \n{node_dataframes["fr"].head()}\n{node_dataframes["fr"].shape}') 
        logger.info(f'Preprocessed {node_type} en \n{node_dataframes["en"].head()}\n{node_dataframes["en"].shape}') 
        merged_node_dataframe = self._merge_node_dataframes(node_dataframes)
        logger.info(f'Merged node: \n{merged_node_dataframe.head()}\n{merged_node_dataframe.shape}') 
        return self._clean_dataframe(merged_node_dataframe, node_type)

    def get_duplicates(self, dataframes: dict):
        return set(dataframes['Page']['wikidata_id']) & set(dataframes['Category']['wikidata_id'])

    def export_merged_dataframes(self, merged_dataframes: dict):
        df = pd.concat([merged_dataframes['Page'], merged_dataframes['Category']], ignore_index=True, sort=True)
        df.drop_duplicates(subset='wikidata_id', inplace=True, keep=False)
        df.rename(columns={'wikidata_id': 'wikidata_id:ID'}, inplace=True)
        df.to_csv(self.path_output, index=None)
 
    def _get_node_csv_paths(self, key: str):
        return get_dict_key(key, self.paths_inputs)

    @staticmethod
    def _load_node_dataframes(paths_node: dict):
        return {key: pd.read_csv(value, sep=',') for key, value in list(paths_node.items())}

    @staticmethod
    def _preprocess_dataframes(dataframes: dict):
        for df in list(dataframes.values()):
            columns_targeted = ['_id', '_start', '_end', '_isNew', 'title', '_type', 'id']
            columns_to_delete = [col_name for col_name in columns_targeted if col_name in df]
            df.drop(columns=columns_to_delete, inplace=True)
            df.dropna(subset=['wikidata_id'], inplace=True)
    
    @staticmethod
    def _merge_node_dataframes(dataframes: dict):
        return pd.merge(dataframes['fr'], dataframes['en'], on='wikidata_id', how='outer')

    @staticmethod
    def _clean_dataframe(df, node_type):
        df.fillna(value={'wikipedia_id_fr': 0, 'wikipedia_id_en': 0}, inplace=True)
        df[':LABEL'] = node_type
        return df.astype({'wikipedia_id_fr': 'int32', 'wikipedia_id_en': 'int32'}, copy=False)
   

class EdgeMerger:
    def __init__(self, paths_inputs: dict, path_output: str, duplicate_nodes: set):
        self.paths_input = paths_inputs
        self.path_output = path_output
        self.duplicate_nodes = duplicate_nodes
    
    def merge_edge(self, edge_type: str):
        csv_paths = self._get_edge_csv_paths(edge_type)
        logger.info(f'CSV paths:\n{csv_paths}')
        edge_dataframes = self._load_edge_dataframes(csv_paths)
        logger.info(f'{edge_type} fr: \n{edge_dataframes["fr"].head()}\n{edge_dataframes["fr"].shape}') 
        logger.info(f'{edge_type} en: \n{edge_dataframes["en"].head()}\n{edge_dataframes["en"].shape}') 
        self._preprocess_dataframes(edge_dataframes)
        logger.info(f'Preprocessed {edge_type} fr: \n{edge_dataframes["fr"].head()}\n{edge_dataframes["fr"].shape}')
        logger.info(f'Preprocessed {edge_type} en: \n{edge_dataframes["en"].head()}\n{edge_dataframes["en"].shape}')
        merged_edge_dataframe = self._merge_edge_dataframes(edge_dataframes)
        logger.info(f'Merged {edge_type}: \n{merged_edge_dataframe.head()}\n{merged_edge_dataframe.shape}')
        return self._drop_duplicates(merged_edge_dataframe, edge_type)

    def export_edge_to_csv(self, df, edge_type):
        df.to_csv(self.path_output[edge_type], index=None)

    def _drop_duplicates(self, df, edge_type: str):
        df.drop_duplicates(inplace=True) 
        df.rename(columns={'start_id':':START_ID', 'end_id':':END_ID'}, inplace=True)
        logger.info(f'Merged df after deleting duplicate lines and renaming columns:\n{df.head()}\n{df.shape}')
        logger.info(f'Duplicate nodes:\n{self.duplicate_nodes}')
        df.drop(df[df[':START_ID'].isin(self.duplicate_nodes)].index, inplace=True)
        df.drop(df[df[':END_ID'].isin(self.duplicate_nodes)].index, inplace=True)
        logger.info(f'No duplicate and merged shape (before renaming columns and after deleting duplicate nodes):\n{df.head()}\n{df.shape}')
        df[':TYPE'] = edge_type.upper() 
        logger.info(f'No duplicate and typed merged {edge_type} dataframe: \n{df.head()}\n{df.shape}')
        return df

    def _get_edge_csv_paths(self, key: str):
        return get_dict_key(key, self.paths_input)

    @staticmethod
    def _load_edge_dataframes(paths_node: dict):
        return {key: pd.read_csv(value, sep=',') for key, value in paths_node.items()} 

    @staticmethod
    def _preprocess_dataframes(dataframes: dict):
        for df in list(dataframes.values()):
            df.dropna(inplace=True)

    @staticmethod
    def _merge_edge_dataframes(dataframes: dict):
        return pd.concat([dataframes['fr'], dataframes['en']], ignore_index=True)


def main():
    # 1. Manage nodes
    t0 = datetime.now()
    base_input_path = './csv_wikidata_ids/'
    base_output_path = './merged_csv/'
    paths_inputs_nodes = {
                    "Page": 
                        {
                            "fr": f"{base_input_path}pages_fr.csv", 
                            "en": f"{base_input_path}pages_en.csv"
                        }, 
                    "Category":
                         {
                            "fr": f"{base_input_path}categories_fr.csv", 
                            "en": f"{base_input_path}categories_en.csv"
                        }
                } 
    paths_output_nodes = f"{base_output_path}nodes.csv"
    nodes_merger = NodesMerger(paths_inputs_nodes, paths_output_nodes)
    merged_dataframes = {}
    merged_dataframes['Page'] = nodes_merger.merge_node('Page')
    merged_dataframes['Category'] = nodes_merger.merge_node('Category')
    duplicates_wikidata_id = nodes_merger.get_duplicates(merged_dataframes)
    nodes_merger.export_merged_dataframes(merged_dataframes)
    logger.info(f'Elapsed time to merge and export Nodes: {datetime.now() -  t0}')
    # 2. Manage edges
    t1 = datetime.now()
    paths_inputs_edges = {
        "links_to":
            {
                "fr": f"{base_input_path}links_to_fr.csv", 
                "en": f"{base_input_path}links_to_en.csv"
            },
        "belongs_to":
            {
                "fr": f"{base_input_path}belongs_to_fr.csv", 
                "en": f"{base_input_path}belongs_to_en.csv"
            } 
    }
    paths_output_edge = {
        "links_to": f'{base_output_path}links_to.csv',
        "belongs_to": f'{base_output_path}belongs_to.csv'
    }
    edge_merger = EdgeMerger(paths_inputs_edges, paths_output_edge, duplicates_wikidata_id)
    merged_links_to = edge_merger.merge_edge('links_to')
    edge_merger.export_edge_to_csv(merged_links_to, 'links_to')
    logger.info(f'Elapsed time to merge and export Nodes: {datetime.now() -  t1}')
    t2 = datetime.now()
    merged_belongs_to = edge_merger.merge_edge('belongs_to')
    edge_merger.export_edge_to_csv(merged_belongs_to, 'belongs_to')
    logger.info(f'Elapsed time to merge and export Nodes: {datetime.now() -  t2}')
    logger.info(f'Total Elapsed time to merge and export nodes and relationships: {datetime.now() - t0}')


if __name__ == '__main__':
    main()
   