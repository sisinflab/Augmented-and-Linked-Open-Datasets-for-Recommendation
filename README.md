# Augmented and Linked Open Datasets for Recommendation

This is the official repository of the paper *Augmented and Linked Open Datasets for Recommendation*.
This work covers the enrichment of two widely used recommendation datasets from the movie and book domain, [MovieLens 25M](https://grouplens.org/datasets/movielens/25m/) and [LibraryThing](https://cseweb.ucsd.edu/~jmcauley/datasets.html#social_data) respectively. In their actual public release, these datasets still lack of comprehensive and extensive efforts of side information integration, despite the imaginable disruptive benefit it would provide.

<p align="center">
<img src="images/resources.jpg" alt="drawing" width="500" />
</p>

Resources are available at https://tny.sh/sisinflab-alod . 



## Resources
Our resources collect metadata, reviews, and the associated knowledge graphs (KGs) for each dataset. 

As for metadata:
- actors, directors, genres, keywords, and reviews from the [Internet Movie Database](https://www.imdb.com/) for movies
- titles, authors, genres, tags, and reviews from the [LibraryThing](https://www.librarything.com/) website for books

As for knowledge graphs:
- linking to URI resource on [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page), [DBpedia](https://www.dbpedia.org/) and [Freebase](https://developers.google.com/freebase) KGs for both movies and books
- RDF-triples from the Wikidata and DBpedia KGs for both movies and books 

The files are subdivided into tar.gz archives as follows:
  ```shell
  MovieLens 25M
  ├── ml25m_linking.tar.gz
  │   ├── ml25m_linking.tsv   
  ├── ml25m_subgraphs.tar.gz
  │   └── ml25m_wikidata_1hop.tsv
  │   └── ml25m_wikidata_2hop.tsv
  │   └── ml25m_dbpedia_1hop.tsv
  │   └── ml25m_dbpedia_2hop.tsv
  ├── ml25m_metadata.tar.gz
  │   └── ml25m_metadata.tsv
  │   └── ml25m_map_generes.tsv
  ├── ml25m_people.tar.gz
  │   └── ml25m_people.csv
  │   └── ml25m_map_directors.tsv
  │   └── ml25m_map_actors.tsv
  ├── ml25m_reviews.tar.gz
  │   └── ml25m_reviews.tsv

  LibraryThing
  ├── lt_linking.tar.gz
  │   ├── lt_linking.tsv   
  │   ├── lt_wikidata_freebase_linking.tsv   
  │   ├── lt_dbpedia_freebase_linking.tsv   
  ├── lt_subgraphs.tar.gz
  │   └── lt_wikidata_1hop.tsv
  │   └── lt_wikidata_2hop.tsv
  │   └── lt_dbpedia_1hop.tsv
  │   └── lt_dbpedia_2hop.tsv
  ├── lt_metadata.tar.gz
  │   └── lt_metadata.tsv
  │   └── lt_map_generes.tsv
  │   └── lt_map_authors.tsv
  ├── lt_reviews.tar.gz
  │   └── lt_reviews.tsv

  ```

### Resources Statistics

The table below shows the statistics of the collected resource categorized by related datasets and data sources.

<p align="center">
<img src="images/stats.jpg" alt="drawing" width="500" />
</p>
