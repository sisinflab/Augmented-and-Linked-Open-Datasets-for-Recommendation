import pandas as pd


def subgraph_info(data):
    retrieved_triples = len(data)
    subjects = len(data['subject'].unique())
    predicates = len(data['predicate'].unique())
    objects = len(data['object'].unique())
    entities = len(set.union(set(data['subject'].unique()), set(data['object'].unique())))
    density = retrieved_triples / (entities * (entities-1))

    print(f'\tretrieved triples: {retrieved_triples}\n'
          f'\tsubjects: {subjects}\n'
          f'\tpredicates: {predicates}\n'
          f'\tobjects: {objects}\n'
          f'\tdensity: {density}\n')


print("+++ MovieLens 25M +++")
data = pd.read_csv('data/ml25m_wikidata_1hop.tsv', sep='\t')
print("Wikidata Graph Collection at 1-hop")
subgraph_info(data)
data = pd.read_csv('data/ml25m_wikidata_2hop.tsv', sep='\t')
print("Wikidata Graph Collection at 2-hop")
subgraph_info(data)
data = pd.read_csv('data/ml25m_dbpedia_1hop.tsv', sep='\t')
print("DBpedia Graph Collection at 1-hop")
subgraph_info(data)
data = pd.read_csv('data/ml25m_dbpedia_2hop.tsv', sep='\t')
print("DBpedia Graph Collection at 2-hop")
subgraph_info(data)
print("+++ LibraryThing +++")
data = pd.read_csv('data/lt_wikidata_1hop.tsv', sep='\t')
print("Wikidata Graph Collection at 1-hop")
subgraph_info(data)
data = pd.read_csv('data/lt_wikidata_2hop.tsv', sep='\t')
print("Wikidata Graph Collection at 2-hop")
subgraph_info(data)
data = pd.read_csv('data/lt_dbpedia_1hop.tsv', sep='\t')
print("DBpedia Graph Collection at 1-hop")
subgraph_info(data)
data = pd.read_csv('data/lt_dbpedia_2hop.tsv', sep='\t')
print("DBpedia Graph Collection at 2-hop")
subgraph_info(data)
