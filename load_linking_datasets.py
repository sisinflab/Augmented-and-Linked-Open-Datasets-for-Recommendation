import pandas as pd

ml25m_linking = pd.read_csv('data/ml25m_linking.tsv', sep='\t')  # example on how to load m25m linking dataset
print("+++ MovieLens 25M +++")
print(f"Linked movies on Wikidata: {ml25m_linking.dropna(subset=['wikidata_uri']).shape[0]}")
print(f"Linked movies on DBpedia: {ml25m_linking.dropna(subset=['dbpedia_uri']).shape[0]}")
print(f"Linked movies on Freebase: {ml25m_linking.dropna(subset=['freebase_uri']).shape[0]}")

lt_linking = pd.read_csv('data/lt_linking.tsv', sep='\t')  # example on how to load lt linking dataset
print("+++ LibraryThing +++")
lt_w_freebase_linking = pd.read_csv('data/lt_wikidata_freebase_linking.tsv', sep='\t')  # example on how to load lt-freebase linking dataset
lt_db_freebase_linking = pd.read_csv('data/lt_dbpedia_freebase_linking.tsv', sep='\t')  # example on how to load lt-freebase linking dataset
lt_db_freebase_linking.dropna(inplace=True)
lt_w_freebase_linking.dropna(inplace=True)
lt_links_freebase = set.union(set(lt_db_freebase_linking.work_id), set(lt_w_freebase_linking.work_id))
print(f"Linked books on Wikidata: {lt_linking.dropna(subset=['wikidata_uri']).shape[0]}")
print(f"Linked books on DBpedia: {lt_linking.dropna(subset=['dbpedia_uri']).shape[0]}")
print(f"Linked books on FreeBase: {len(lt_links_freebase)}")
