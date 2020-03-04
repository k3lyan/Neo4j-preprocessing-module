from neo4j import GraphDatabase
import argparse
import csv
from logzero import logger
from datetime import datetime
import sys


class WikidataIdManager(object):
    def __init__(self, uri: str, user: str, password: str):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def get_wikidata_ids(self, path: str) -> dict:
        """ Return a dictionary with title as keys and wikidata_id as values."""
        with open(path, 'r') as samples:
            return {str(row[0]) : str(row[2]) for row in csv.reader(samples, delimiter=';')}

    def add_wikidata_ids_to_pages(self, ids: dict, language: str):
        """ Add Wikidata_id to the Page nodes."""
        with self._driver.session() as session:
            session.write_transaction(self._set_index_page)
            for title in ids.keys():
                if language == 'fr':
                    session.write_transaction(self._update_fr_page_node, title, ids[title])
                elif language == 'en':
                    session.write_transaction(self._update_en_page_node, title, ids[title])

    def add_wikidata_ids_to_categories(self, ids: dict, language: str):
        """ Add wikidata_id to the Category nodes."""
        with self._driver.session() as session:
            session.write_transaction(self._set_index_category)
            for title in ids.keys():
                if language == 'fr':
                    session.write_transaction(self._update_fr_category_node, title, ids[title])
                elif language == 'en':
                    session.write_transaction(self._update_en_category_node, title, ids[title])

    def export_to_csv(self, target: str, filename: str, language=None):
        """ Export all the targetet data (specific node or edge type) to a csv file."""
        with self._driver.session() as session:
            if language is not None:
                if target == 'page':
                    return session.write_transaction(self._export_node_to_csv, filename, language, target)
                elif target == 'category':
                    return session.write_transaction(self._export_node_to_csv, filename, language, target)
            else:
                if target == 'links_to':
                    return session.write_transaction(self._export_links_to_csv, filename)
                elif target == 'belongs_to':
                    return session.write_transaction(self._export_belongs_to_csv, filename)
   
    @staticmethod
    def _set_index_page(tx):
        tx.run("CREATE INDEX ON :Page(title)")
        logger.info('Index created on Page.')

    @staticmethod
    def _set_index_category(tx):
        tx.run("CREATE INDEX ON :Category(title)")
        logger.info(f'Index created on Category.')
 
    @staticmethod
    def _update_fr_page_node(tx, page_title: str, wikidata_id: str):
        tx.run("MATCH (n:Page {title:$page_title})"
                "SET n = {title_fr: $page_title, wikipedia_id_fr: n.id, wikidata_id:$wikidata_id}"
                "REMOVE n.is_New, n.title, ", 
                page_title=page_title, wikidata_id=wikidata_id)

    @staticmethod
    def _update_fr_category_node(tx, category_title: str, wikidata_id: str):
        tx.run("MATCH (n:Category {title:$category_title})"
                "SET n = {title_fr: $category_title, wikipedia_id_fr: n.id, wikidata_id:$wikidata_id}", 
                category_title=category_title, wikidata_id=wikidata_id)

    @staticmethod
    def _update_en_page_node(tx, page_title: str, wikidata_id: str):
        tx.run("MATCH (n:Page {title:$page_title})"
                "SET n = {title_en: $page_title, wikipedia_id_en: n.id, wikidata_id:$wikidata_id}", 
                page_title=page_title, wikidata_id=wikidata_id)

    @staticmethod
    def _update_en_category_node(tx, category_title: str, wikidata_id: str):
        tx.run("MATCH (n:Category {title:$category_title})"
                "SET n = {title_en: $category_title, wikipedia_id_en: n.id, wikidata_id:$wikidata_id}", 
                category_title=category_title, wikidata_id=wikidata_id)

    @staticmethod
    def _export_node_to_csv(tx, csv_filename, language, node_type):
        if language == 'fr' and node_type == 'page':
            return tx.run("WITH 'MATCH (n:Page)"  
                   "RETURN n.wikidata_id AS wikidata_id, n.title_fr AS title_fr, n.wikipedia_id_fr AS wikipedia_id_fr' AS query "
                   "CALL apoc.export.csv.query(query, $filename, {}) "
                   "YIELD file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data "
                   "RETURN file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data ",
                   filename=csv_filename).single().value()
        elif language == 'en' and node_type == 'page':
            return tx.run("WITH 'MATCH (n:Page)"  
                   "RETURN n.wikidata_id AS wikidata_id, n.title_en AS title_en, n.wikipedia_id_en AS wikipedia_id_en' AS query "
                   "CALL apoc.export.csv.query(query, $filename, {}) "
                   "YIELD file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data "
                   "RETURN file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data ",
                   filename=csv_filename).single().value()
        if language == 'fr' and node_type == 'category':
            return tx.run("WITH 'MATCH (n:Category)"  
                   "RETURN n.wikidata_id AS wikidata_id, n.title_fr AS title_fr, n.wikipedia_id_fr AS wikipedia_id_fr' AS query "
                   "CALL apoc.export.csv.query(query, $filename, {}) "
                   "YIELD file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data "
                   "RETURN file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data ",
                   filename=csv_filename).single().value()
        elif language == 'en' and node_type == 'category':
            return tx.run("WITH 'MATCH (n:Category)"  
                   "RETURN n.wikidata_id AS wikidata_id, n.title_en AS title_en, n.wikipedia_id_en AS wikipedia_id_en' AS query "
                   "CALL apoc.export.csv.query(query, $filename, {}) "
                   "YIELD file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data "
                   "RETURN file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data ",
                   filename=csv_filename).single().value()

    @staticmethod
    def _export_links_to_csv(tx, csv_filename):
        return tx.run("WITH 'MATCH (n)-[r:LINKS_TO]->(m) "  
               "RETURN n.wikidata_id AS start_id, m.wikidata_id AS end_id' AS query "
               "CALL apoc.export.csv.query(query, $filename, {}) "
               "YIELD file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data "
               "RETURN file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data ",
               filename=csv_filename).single().value()

    @staticmethod
    def _export_belongs_to_csv(tx, csv_filename):
        return tx.run("WITH 'MATCH (n)-[r:BELONGS_TO]->(m) "  
               "RETURN n.wikidata_id AS start_id, m.wikidata_id AS end_id' AS query "
               "CALL apoc.export.csv.query(query, $filename, {}) "
               "YIELD file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data "
               "RETURN file, source, format, nodes, relationships, properties, time, rows, batchSize, batches, done, data ",
               filename=csv_filename).single().value()

    @staticmethod
    def _get_updated_node(tx, wikidata_id):
        for node in tx.run(
            "MATCH (n:Page {wikidata_id:$wikidata_id})"
            "RETURN n.language", 
            wikidata_id=wikidata_id):
            logger.info(f' Here is my title: {node["n.language"]}')


def main():
    # 1. Initialize parameters and DB session
    t0 = datetime.now()
    language = str(sys.argv[1]).lower()
    uri = "bolt://localhost:7687"
    manager = WikidataIdManager(uri, "neo4j", "kiki")
    base_input_path = "./csv_inputs/"
    base_output_path = "./csv_wikidata_ids/"
    paths_inputs = {
                "fr": 
                    {
                        "pages": f"{base_input_path}allchunks.csv", 
                        "categories": f"{base_input_path}fr_categories_full_graph_after_wikidata_id_retrieval.csv"
                    }, 
                "en":
                     {
                        "pages": f"{base_input_path}en_pages_wikidata_id.csv", 
                        "categories": f"{base_input_path}en_categories_wikidata_id.csv"
                    }
            }
    paths_outputs = {
                "fr": 
                    {
                        "pages": f"{base_output_path}pages_fr_test.csv", 
                        "categories": f"{base_output_path}categories_fr_test.csv",
                        "links_to": f"{base_output_path}links_to_fr.csv", 
                        "links_limit": f"{base_output_path}links_limit_fr.csv", 
                        "belongs_to": f"{base_output_path}belongs_to_fr.csv" 
                    }, 
                "en":
                     {
                        "pages": f"{base_output_path}pages_en_test.csv", 
                        "categories": f"{base_output_path}categories_en_test.csv",
                        "links_to": f"{base_output_path}links_to_en.csv", 
                        "belongs_to": f"{base_output_path}belongs_to_en.csv" 
                    }
            }
    # 2. Update Pages
    ids_pages = manager.get_wikidata_ids(paths_inputs[language]["pages"])
    manager.add_wikidata_ids_to_pages(ids_pages, language)
    logger.info(f'Elapsed time to update {language} Pages: {datetime.now() -  t0}')
    # 3. Update Categories
    t1 = datetime.now()
    ids_categories = manager.get_wikidata_ids(paths_inputs[language]["categories"])
    manager.add_wikidata_ids_to_categories(ids_categories, language)
    logger.info(f'Elapsed time to update {language} Categories: {datetime.now() -  t1}')
    # 4. Export CSVs
    t2 = datetime.now()
    pages_export_stats = manager.export_to_csv("page", paths_outputs[language]['pages'], language)
    logger.info(f'\n{pages_export_stats}')
    logger.info(f'Elapsed time to export {language} pages to csv: {datetime.now() -  t2}')
    t3 = datetime.now()
    categories_export_stats = manager.export_to_csv("category", paths_outputs[language]['categories'], language)
    logger.info(f'\n{categories_export_stats}')
    logger.info(f'Elapsed time to export {language} pages to csv: {datetime.now() -  t3}')
    t4 = datetime.now()
    belongs_to_export_stats = manager.export_to_csv("belongs_to", paths_outputs[language]['belongs_to'])
    logger.info(f'\n{belongs_to_export_stats}')
    logger.info(f'Elapsed time to update {language} belongs_to: {datetime.now() -  t4}')
    t5 = datetime.now()
    links_to_export_stats = manager.export_to_csv("links_to", paths_outputs[language]['links_to'])
    logger.info(f'\n{links_to_export_stats}')
    logger.info(f'Elapsed time to update {language} links_to: {datetime.now() -  t5}')
    # 5. Close DB session
    manager.close()


if __name__ == '__main__':
    main()
