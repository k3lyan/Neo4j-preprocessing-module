# Wikipedia graph database preprocessing module

## What is it for ?

This module aims at getting a preprocessed and cleant merged Graph Database. 

### What we have

We have at our disposal:

* 2 Neo4j databases dumps: Wikipedia FR and Wikipedia EN (see BDD section)
    --> each of them containing:
  * Pages and Categories nodes (attributes: title, id, isNew), 
  * Links_to relations linking Pages nodes between them if related, 
  * Belongs_to relations linking Pages and Categories or Categories between them if related
* 4 CSVs:
  * 1 CSV per language for the pages (fields: page_title; page_id; wikidata_id) 
  * 1 CSV per language for the categories (fields: category_title; category_id; wikidata_id)  

### What we want

We would like to merge English and French nodes sharing the same wikidata_id without loosing neither creating duplicated relations in. The result should make possible the creation of a new merged neo4j database. 

### Process description  

1) Load the Wikipedia fr & en dumps to your Neo4j databases (one for each dump)  
2) Update both wikipedia\_fr and wikipedia\_en original graph databases by renaming the property and adding the wikidata\_id thanks to CSV input documents
3) Export CSVs corresponding to these new databases: 2 for pages nodes, 2 for categories nodes, 2 for links_to edges (start_id == wikidata_id input node, end_id == wikidata_id output node), 2 for belongs_to edges
4) Load newly created CSVs as Pandas dataframes and properly merge them, this should lead to 3 exported CSVs: one for the nodes, one for the links_to relations and one for the belongs_to relations
5) Load the new database from the merged CSV  

3 classes enable us to do so:

* WikidataIdManager
* NodesMerger
* EdgeMerger

### Prerequesites

Before you continue, ensure you meet the following requirements:

* You have an installed version of Python3.7+ running on your computer
* Download Neo4j from the official website: https://neo4j.com/download/  

## How to use

### 1. Load the Wikipedia fr & en dumps to your Neo4j databases

* First you need to go to your neo4j_home directory 
* Then depending on the db number that you can find on the browser (manage section - logs), move to: 

`cd Application/neo4jDatabases/database-deaXXXa-5789-4b25-XXX6-5e5c6XXXXX/installation-x.x.x` 

* Then go to installation-x.x.x directory and enter the following look-like command, passing the path where is located your dump to import in your db:

` bin/neo4j-admin load --from=absolute_path_to_the_dump/wikipedia_fr.dump --database=graph.db --force`

/!\ WARNING /!\ The database must be shutdown while doing this action.
Do the same process for the English database.

### 2-3. Add wikidata_id to the nodes, export them and their relationships

#### Settings requirements

1. You need to have the APOC plugin installed
2. In neo4j.conf, add/uncomment/modify the following lines:
* `dbms.memory.heap.initial_size=2G`
* `dbms.memory.heap.max_size=4G`
* `dbms.memory.pagecache.size=2G`
* `dbms.security.procedures.unrestricted=apoc.export.*,apoc.import.*`
* `apoc.export.file.enabled=true`
* `apoc.import.file.enabled=true`
* `apoc.import.file.use_neo4j_config=false`
(this last condition enables you to export your CSV in a different location than the import directory of your database)
3. Install the neo4j liibrary in your environment: `pip install neo4j`

#### Process

Once you have uploaded a Wikipedia_en and Wikipedia_fr local databases from the original dump. Do the following actions for each database (fr in that case):

* Launch the fr database
* Run: `python3 export_with_wikidata_ids.py fr`
* Stop the database

Do the same with the english database modifying "fr" by "en" in the comand line, and modifying the paths accorging to those matching with English data. 

/!\ Do not forget to put the appropriate uri, username, password and possibly paths to the csv values in the main() function. /!\

### 4. Load newly created CSVs as Pandas dataframes, merge and export them

#### Settings requirements

Install these libraries in your environment: pandas.  

#### Process

Launch the folowing python script:  `python3 merge_csv.py`

### 5. Load the final database from the merged CSV

Use the method mentioned here: https://neo4j.com/docs/operations-manual/current/tutorial/import-tool/.

Exactly like you would do in 1. for the load of the dump, go to the installation-x.x.x. repository of your neo4j database and launch the look-like command:  
` bin/neo4j-admin import --nodes=absolute-path-to-my-module-source/merged_csv/nodes.csv --relationships=absolute-path-to-my-module-source/merged_csv/links_to.csv --relationships=absolute-path-to-my-module-source/merged_csv/belongs_to.csv`
