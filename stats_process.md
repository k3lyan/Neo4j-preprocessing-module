# PROCESS LOGS

## WIKIDATA_ID EXPORT TO CSV:

### LINKS_TO_FR

    [I 200127 17:39:13 add_wikidata_ids:189]
    /Users/kmorfouesse/Desktop/DEV/Projects/iLearn/tests_ilearn/Merger/csv_outputs/links_to_fr.csv
    [I 200127 17:39:13 add_wikidata_ids:190] Elapsed time to update fr links_to: 2:04:43.315823]

### BELONGS_TO_FR

    [17:39:13 add_wikidata_ids:189]
    /Users/kmorfouesse/Desktop/DEV/Projects/iLearn/tests_ilearn/Merger/csv_outputs/links_to_fr.csv
    [I 200127 17:39:13 add_wikidata_ids:190] Elapsed time to update fr links_to: 2:04:43.315823]

### LINKS_TO_EN
    [I 200128 05:48:00 add_wikidata_ids:202]
    /Users/kmorfouesse/Desktop/DEV/Projects/iLearn/tests_ilearn/Merger/csv_outputs/links_to_en.csv
    [I 200128 05:48:00 add_wikidata_ids:203] Elapsed time to update en links_to: 8:58:07.328625

### BELONGS_TO_EN
    [I 200127 20:49:53 add_wikidata_ids:198]
    /Users/kmorfouesse/Desktop/DEV/Projects/iLearn/tests_ilearn/Merger/csv_outputs/belongs_to_en.csv
    [I 200127 20:49:53 add_wikidata_ids:199] Elapsed time to update en belongs_to: 0:06:08.210411


## MERGED CSV

### NODES

    [I 200130 15:05:39 merge_csv:26] CSV paths:
    {'fr': './csv_wikidata_ids/pages_fr.csv', 'en': './csv_wikidata_ids/pages_en.csv'}
    [I 200130 15:05:41 merge_csv:28] Page fr:
      wikidata_id                title_fr  wikipedia_id_fr
    0     Q347001         Antoine_Meillet              3.0
    1      Q82571        Algèbre_linéaire              7.0
    2   Q13636890           Algorithmique             10.0
    3    Q1154647  Politique_en_Argentine             11.0
    4         Q40                Autriche             15.0
    (425120, 3)
    [I 200130 15:05:41 merge_csv:29] Page en:
      wikidata_id   title_en  wikipedia_id_en
    0       Q6199  Anarchism               12
    1      Q38404     Autism               25
    2     Q101038     Albedo               39
    3       Q9659          A              290
    4        Q173    Alabama              303
    (1296755, 3)
    [I 200130 15:05:41 merge_csv:31] Preprocessed Page fr:
      wikidata_id                title_fr  wikipedia_id_fr
    0     Q347001         Antoine_Meillet              3.0
    1      Q82571        Algèbre_linéaire              7.0
    2   Q13636890           Algorithmique             10.0
    3    Q1154647  Politique_en_Argentine             11.0
    4         Q40                Autriche             15.0
    (418542, 3)
    [I 200130 15:05:41 merge_csv:32] Preprocessed Page en
      wikidata_id   title_en  wikipedia_id_en
    0       Q6199  Anarchism               12
    1      Q38404     Autism               25
    2     Q101038     Albedo               39
    3       Q9659          A              290
    4        Q173    Alabama              303
    (1290539, 3)
    [I 200130 15:05:42 merge_csv:34] Merged node:
      wikidata_id                title_fr  wikipedia_id_fr               title_en  wikipedia_id_en
    0     Q347001         Antoine_Meillet              3.0        Antoine_Meillet         797350.0
    1      Q82571        Algèbre_linéaire              7.0         Linear_algebra          18422.0
    2   Q13636890           Algorithmique             10.0                    NaN              NaN
    3    Q1154647  Politique_en_Argentine             11.0  Politics_of_Argentina          67621.0
    4         Q40                Autriche             15.0                Austria       26964606.0
    (1507315, 5)
    [I 200130 15:05:43 merge_csv:26] CSV paths:
    {'fr': './csv_wikidata_ids/categories_fr.csv', 'en': './csv_wikidata_ids/categories_en.csv'}
    [I 200130 15:05:45 merge_csv:28] Category fr:
      wikidata_id                  title_fr  wikipedia_id_fr
    0       Q6508                Astronomie            80753
    1    Q1970530                  Écologie            80787
    2    Q9115279  Sept_Merveilles_du_monde            81060
    3    Q8419352             Environnement            81355
    4    Q1457402                  Biologie            81357
    (289403, 3)
    [I 200130 15:05:45 merge_csv:29] Category en:
      wikidata_id                title_en  wikipedia_id_en
    0    Q8476222                Futurama           690070
    1    Q6816704            World_War_II           690451
    2      Q34059   Programming_languages           690571
    3    Q7144134  Professional_wrestling           690578
    4    Q8234869                 Algebra           690637
    (1125127, 3)
    [I 200130 15:05:45 merge_csv:31] Preprocessed Category fr:
      wikidata_id                  title_fr  wikipedia_id_fr
    0       Q6508                Astronomie            80753
    1    Q1970530                  Écologie            80787
    2    Q9115279  Sept_Merveilles_du_monde            81060
    3    Q8419352             Environnement            81355
    4    Q1457402                  Biologie            81357
    (284826, 3)
    [I 200130 15:05:45 merge_csv:32] Preprocessed Category en
      wikidata_id                title_en  wikipedia_id_en
    0    Q8476222                Futurama           690070
    1    Q6816704            World_War_II           690451
    2      Q34059   Programming_languages           690571
    3    Q7144134  Professional_wrestling           690578
    4    Q8234869                 Algebra           690637
    (1098192, 3)
    [I 200130 15:05:47 merge_csv:34] Merged node:
      wikidata_id                  title_fr  wikipedia_id_fr                            title_en  wikipedia_id_en
    0       Q6508                Astronomie          80753.0                           Astronomy         692915.0
    1    Q1970530                  Écologie          80787.0                             Ecology         691262.0
    2    Q9115279  Sept_Merveilles_du_monde          81060.0  Seven_Wonders_of_the_Ancient_World       46913702.0
    3    Q8419352             Environnement          81355.0                 Natural_environment        3103170.0
    4    Q1457402                  Biologie          81357.0                             Biology         692675.0
    (1240083, 5)
    [I 200130 15:06:01 merge_csv:154] Elapsed time to merge and export Nodes: 0:00:22.611189

### EDGES
#### LINKS_TO
    [I 200130 15:06:01 merge_csv:80] CSV paths:
    {'fr': './csv_wikidata_ids/links_to_fr.csv', 'en': './csv_wikidata_ids/links_to_en.csv'}
    [I 200130 15:07:59 merge_csv:82] links_to fr:
       start_id   end_id
    0  Q3172184  Q347001
    1   Q308640  Q347001
    2  Q2718867  Q347001
    3   Q274931  Q347001
    4  Q3211351  Q347001
    (30096602, 2)
    [I 200130 15:07:59 merge_csv:83] links_to en:
        start_id end_id
    0  Q18379905  Q6199
    1  Q10862449  Q6199
    2    Q545825  Q6199
    3   Q6123766  Q6199
    4   Q5416366  Q6199
    (116373019, 2)
    [I 200130 15:09:21 merge_csv:85] Preprocessed links_to fr:
       start_id   end_id
    0  Q3172184  Q347001
    1   Q308640  Q347001
    2  Q2718867  Q347001
    3   Q274931  Q347001
    4  Q3211351  Q347001
    (29523776, 2)
    [I 200130 15:09:21 merge_csv:86] Preprocessed links_to en:
        start_id end_id
    0  Q18379905  Q6199
    1  Q10862449  Q6199
    2    Q545825  Q6199
    3   Q6123766  Q6199
    4   Q5416366  Q6199
    (115310335, 2)
    [I 200130 15:09:40 merge_csv:88] Merged links_to:
       start_id   end_id
    0  Q3172184  Q347001
    1   Q308640  Q347001
    2  Q2718867  Q347001
    3   Q274931  Q347001
    4  Q3211351  Q347001
    (144834111, 2)
    [I 200130 15:13:36 merge_csv:97] Merged df after deleting duplicate lines and renaming columns:
      :START_ID  :END_ID
    0  Q3172184  Q347001
    1   Q308640  Q347001
    2  Q2718867  Q347001
    3   Q274931  Q347001
    4  Q3211351  Q347001
    (138682069, 2)
    [I 200130 15:13:36 merge_csv:98] Duplicate nodes:
    {'Q16943191', 'Q8465433', 'Q4089480', 'Q4116486', 'Q6606194', 'Q5589270'}
    [I 200130 15:18:55 merge_csv:108] No duplicate and merged shape (before renaming columns and after deleting duplicate nodes):
      :START_ID  :END_ID
    0  Q3172184  Q347001
    1   Q308640  Q347001
    2  Q2718867  Q347001
    3   Q274931  Q347001
    4  Q3211351  Q347001
    (138680851, 2)
    [I 200130 15:18:56 merge_csv:110] No duplicate and typed merged links_to dataframe:
      :START_ID  :END_ID     :TYPE
    0  Q3172184  Q347001  LINKS_TO
    1   Q308640  Q347001  LINKS_TO
    2  Q2718867  Q347001  LINKS_TO
    3   Q274931  Q347001  LINKS_TO
    4  Q3211351  Q347001  LINKS_TO
    (138680851, 3)
    [I 200130 15:24:17 merge_csv:176] Elapsed time to merge and export Nodes: 0:18:16.004561


#### BELONGS_TO
    [I 200130 15:24:17 merge_csv:80] CSV paths:
    {'fr': './csv_wikidata_ids/belongs_to_fr.csv', 'en': './csv_wikidata_ids/belongs_to_en.csv'}
    [I 200130 15:24:40 merge_csv:82] belongs_to fr:
        start_id end_id
    0  Q31954555  Q6508
    1       Q527  Q6508
    2   Q6542084  Q6508
    3  Q13334911  Q6508
    4    Q718647  Q6508
    (4917396, 2)
    [I 200130 15:24:40 merge_csv:83] belongs_to en:
        start_id    end_id
    0  Q15041237  Q8476222
    1   Q7905410  Q8476222
    2   Q3146483  Q8476222
    3  Q16386698  Q8476222
    4   Q1874104  Q8476222
    (9190846, 2)
    [I 200130 15:24:43 merge_csv:85] Preprocessed belongs_to fr:
        start_id end_id
    0  Q31954555  Q6508
    1       Q527  Q6508
    2   Q6542084  Q6508
    3  Q13334911  Q6508
    4    Q718647  Q6508
    (4841741, 2)
    [I 200130 15:24:43 merge_csv:86] Preprocessed belongs_to en:
        start_id    end_id
    0  Q15041237  Q8476222
    1   Q7905410  Q8476222
    2   Q3146483  Q8476222
    3  Q16386698  Q8476222
    4   Q1874104  Q8476222
    (8965861, 2)
    [I 200130 15:24:44 merge_csv:88] Merged belongs_to:
        start_id end_id
    0  Q31954555  Q6508
    1       Q527  Q6508
    2   Q6542084  Q6508
    3  Q13334911  Q6508
    4    Q718647  Q6508
    (13807602, 2)
    [I 200130 15:24:53 merge_csv:97] Merged df after deleting duplicate lines and renaming columns:
       :START_ID :END_ID
    0  Q31954555   Q6508
    1       Q527   Q6508
    2   Q6542084   Q6508
    3  Q13334911   Q6508
    4    Q718647   Q6508
    (13406887, 2)
    [I 200130 15:24:53 merge_csv:98] Duplicate nodes:
    {'Q16943191', 'Q8465433', 'Q4089480', 'Q4116486', 'Q6606194', 'Q5589270'}
    [I 200130 15:25:02 merge_csv:108] No duplicate and merged shape (before renaming columns and after deleting duplicate nodes):
       :START_ID :END_ID
    0  Q31954555   Q6508
    1       Q527   Q6508
    2   Q6542084   Q6508
    3  Q13334911   Q6508
    4    Q718647   Q6508
    (13406782, 2)
    [I 200130 15:25:02 merge_csv:110] No duplicate and typed merged belongs_to dataframe:
       :START_ID :END_ID       :TYPE
    0  Q31954555   Q6508  BELONGS_TO
    1       Q527   Q6508  BELONGS_TO
    2   Q6542084   Q6508  BELONGS_TO
    3  Q13334911   Q6508  BELONGS_TO
    4    Q718647   Q6508  BELONGS_TO
    (13406782, 3)
    [I 200130 15:25:29 merge_csv:180] Elapsed time to merge and export Nodes: 0:01:11.501671

### Total time for the merge and export:
    [I 200130 15:25:29 merge_csv:181] Total Elapsed time to merge and export nodes and relationships: 0:19:50.130394

## LOAD FINAL DATABASE
Available resources:
  Total machine memory: 8.00 GB
  Free machine memory: 537.44 MB
  Max heap memory : 3.56 GB
  Processors: 4
  Configured max memory: 4.00 GB
  High-IO: true

WARNING: heap size 3.56 GB is unnecessarily large for completing this import.
The abundant heap memory will leave less memory for off-heap importer caches. Suggested heap size is 1.00 GBImport starting 2020-01-30 15:31:19.415+0100
  Estimated number of nodes: 2.87 M
  Estimated number of node properties: 13.14 M
  Estimated number of relationships: 171.17 M
  Estimated number of relationship properties: 0.00
  Estimated disk space usage: 5.79 GB
  Estimated required memory usage: 1.03 GB

InteractiveReporterInteractions command list (end with ENTER):
  c: Print more detailed information about current stage
  i: Print more detailed information

(1/4) Node import 2020-01-30 15:31:19.752+0100
  Estimated number of nodes: 2.87 M
  Estimated disk space usage: 383.00 MB
  Estimated required memory usage: 1.03 GB
.......... .......... .......... .......... ..........   5% ∆5s 225ms
.......... .......... .......... .......... ..........  10% ∆801ms
.......... .......... .......... .......... ..........  15% ∆803ms
.......... .......... .......... .......... ..........  20% ∆2s 30ms
.......... .......... .......... .......... ..........  25% ∆804ms
.......... .......... .......... .......... ..........  30% ∆1s 205ms
.......... ..-....... .......... .......... ..........  35% ∆92ms
.......... .......... .......... .......... ..........  40% ∆0ms
.......... .......... .......... .......... ..........  45% ∆603ms
.......... .......... .......... .......... ..........  50% ∆403ms
.......... .......... .......... .......... ..........  55% ∆202ms
.......... .......... .......... .......... ..........  60% ∆201ms
.......... .......... .......... .......... ..........  65% ∆202ms
.......... .......... .......... .......... ..........  70% ∆0ms
.......... .......... .......... .......... ..........  75% ∆45ms
.......... .......... .......... .......... ..........  80% ∆0ms
.......... .......... .......... .......... ..........  85% ∆0ms
.......... .......... .......... .......... ..........  90% ∆0ms
.......... .......... .......... .......... ..........  95% ∆0ms
.......... .......... .......... .......... .......... 100% ∆1ms

(2/4) Relationship import 2020-01-30 15:31:32.490+0100
  Estimated number of relationships: 171.17 M
  Estimated disk space usage: 5.42 GB
  Estimated required memory usage: 1.03 GB
.......... .......... .......... .......... ..........   5% ∆17s 883ms
.......... .......... .......... .......... ..........  10% ∆16s 745ms
.......... .......... .......... .......... ..........  15% ∆16s 113ms
.......... .......... .......... .......... ..........  20% ∆14s 506ms
.......... .......... .......... .......... ..........  25% ∆14s 514ms
.......... .......... .......... .......... ..........  30% ∆14s 111ms
.......... .......... .......... .......... ..........  35% ∆13s 927ms
.......... .......... .......... .......... ..........  40% ∆13s 916ms
.......... .......... .......... .......... ..........  45% ∆14s 717ms
.......... .......... .......... .......... ..........  50% ∆14s 900ms
.......... .......... .......... .......... ..........  55% ∆14s 516ms
.......... .......... .......... .......... ..........  60% ∆13s 502ms
.......... .......... .......... .......... ..........  65% ∆14s 320ms
.......... .......... .......... .......... ..........  70% ∆15s 318ms
.......... .......... .......... .......... ..........  75% ∆14s 718ms
.......... .......... .......... .......... ..........  80% ∆14s 523ms
.......... .......... .......... .......... ..........  85% ∆14s 727ms
.......... .......... .......... .......... ..........  90% ∆10s 797ms
.......... .......... .......... .......... ..........  95% ∆0ms
.......... .......... .......... .......... .......... 100% ∆1ms

(3/4) Relationship linking 2020-01-30 15:35:56.246+0100
  Estimated required memory usage: 1.02 GB
.......... .......... .......... .......... ..........   5% ∆16s 232ms
.......... .......... .......... .......... ..........  10% ∆25s 117ms
.......... .......... .......... .......... ..........  15% ∆27s 514ms
.......... .......... .......... .......... .........-  20% ∆200ms
.......... .......... .......... .......... ..........  25% ∆5s 20ms
.......... .......... .......... .......... ..........  30% ∆4s 409ms
.......... .......... .......... .......... ..........  35% ∆5s 627ms
.......... .......... .......... .......... ..........  40% ∆7s 427ms
.......... .......... .......... .......... ..........  45% ∆9s 634ms
.......... .......... .......... .......... ..........  50% ∆22s 261ms
.......... .......... .......... .......... ..........  55% ∆12s 649ms
.......... .......... .......... .......... ........-.  60% ∆417ms
.......... .......... .......... .......... ..........  65% ∆4s 809ms
.......... .......... .......... .......... ..........  70% ∆17s 473ms
.......... .......... .......... .......... ..........  75% ∆20s 274ms
.......... .......... .......... .......... ..........  80% ∆12s 442ms
.......... .......... .......... .......... ..........  85% ∆9s 622ms
.......... .......... .......... .......... ..........  90% ∆22s 274ms
.......... .......... .......... .......... ..........  95% ∆17s 643ms
.......... .......... .......... .......... .......... 100% ∆23s 214ms

(4/4) Post processing 2020-01-30 15:40:53.861+0100
  Estimated required memory usage: 1020.01 MB
.......... ..-....... ..-.....-. .......... -.........   5% ∆414ms
.......... .......... .......... .......... ..........  10% ∆401ms
.......... .......... .......... .......... ..........  15% ∆1s 7ms
.......... .......... .......... .......... ..........  20% ∆2s 406ms
.......... .......... .......... .......... ..........  25% ∆3s 208ms
.......... .......... .......... .......... ..........  30% ∆5s 418ms
.......... .......... .......... .......... ..........  35% ∆6s 219ms
.......... .......... .......... .......... ..........  40% ∆7s 26ms
.......... .......... .......... .......... ..........  45% ∆5s 218ms
.......... .......... .......... .......... ..........  50% ∆4s 617ms
.......... .......... .......... .......... ..........  55% ∆3s 411ms
.......... .......... .......... .......... ..........  60% ∆5s 415ms
.......... .......... .......... .......... ..........  65% ∆6s 16ms
.......... .......... .......... .......... ..........  70% ∆6s 825ms
.......... .......... .......... .......... ..........  75% ∆6s 625ms
.......... .......... .......... .......... ..........  80% ∆6s 20ms
.......... .......... .......... .......... ..........  85% ∆8s 28ms
.......... .......... .......... .......... ..........  90% ∆6s 619ms
.......... .......... .......... .......... ..........  95% ∆6s 20ms
.......... .......... .......... .......... .......... 100% ∆5s 115ms


IMPORT DONE in 11m 14s 44ms.
Imported:
  2747386 nodes
  152087633 relationships
  11334245 properties
Peak memory usage: 1.13 GB
