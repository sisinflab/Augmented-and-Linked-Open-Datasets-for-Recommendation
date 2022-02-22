![GitHub repo size](https://img.shields.io/github/repo-size/sisinflab/elliot) ![GitHub](https://img.shields.io/github/license/sisinflab/Augmented-and-Linked-Open-Datasets-for-Recommendation.svg)

[Main page](https://sisinflab.github.io/Augmented-and-Linked-Open-Datasets-for-Recommendation/)

# Augmented and Linked Open Datasets for Recommendation

This is the official repository of the paper *Augmented and Linked Open Datasets for Recommendation*.
This work covers the enrichment of two widely used recommendation datasets from the movie and book domain, [MovieLens 25M](https://grouplens.org/datasets/movielens/25m/) and [LibraryThing](https://cseweb.ucsd.edu/~jmcauley/datasets.html#social_data) respectively. We collected metadata, reviews, and the associated knowledge graphs (KGs) for each of them.
Metadata includes titles, authors, genres, and tags from the LibraryThing website for books. Actors, directors, genres, and keywords are extracted from the Internet Movie Database (IMDb) for movies.
Publicly available reviews of the items are fetched from LibraryThing and IMDb websites. 
The domain-specific KGs contain RDF triples from the Wikidata and DBpedia KGs.
Additionally, we publish a mapping for each item in the two datasets with the corresponding entity in the original Wikidata, DBpedia, and Freebase KGs.
Inspired by the advances in knowledge graph, Graph Convolutional Networks, Link Prediction, and Recommender Systems research, these augmented datasets aim to meet their cutting-edge research needs. Moreover, these datasets pave the way to further research to investigate different recommendation modalities simultaneously.

<p align="center">
<img src="images/resources.png" alt="drawing" width="500" />
</p>

Resources are available [here](https://tny.sh/sisinflab-alod) . 



## Resources
Our resources collect metadata, reviews, and the associated knowledge graphs (KGs) for each dataset. 

As for metadata:
- actors, directors, genres, keywords, and reviews from the [Internet Movie Database](https://www.imdb.com/) for movies
- titles, authors, genres, tags, and reviews from the [LibraryThing](https://www.librarything.com/) website for books

As for knowledge graphs:
- links from Item IDs to URI resources on [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page), [DBpedia](https://www.dbpedia.org/) and [Freebase](https://developers.google.com/freebase) KGs for both movies and books
- RDF-triples from the Wikidata and DBpedia KGs for both movies and books 

The files are split into tar.gz archives as follows:
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

The table below shows the statistics of the collected resource categorized by dataset and data source.

<p align="center">
<img src="images/stats.png" alt="drawing" width="500" />
</p>


## Contributing
We welcome any contibution that could improve our datasets. Please, contact us by email.

## The Team
This work is developed by
* Vito Walter Anelli (vitowalter.anelli@poliba.it)
* Antonio Ferrara (antonio.ferrara@poliba.it)
* Tommaso Di Noia (tommaso.dinoia@poliba.it)
* Alberto Carlo Maria Mancino<sup id="a1">[*](#f1)</sup> (alberto.mancino@poliba.it)
* Vincenzo Paparella<sup id="a1">[*](#f1)</sup> (vincenzo.paparella@poliba.it)
* Claudio Pomo (claudio.pomo@poliba.it)

<b id="f1"><sup>*</sup></b> Corresponding authors

## License
This work is under [APACHE2 License](./LICENSE).

## Acknowledgements
Our datasets are constructed thanks to 
- MovieLens dataset (https://grouplens.org/)
- LibraryThing dataset(https://cseweb.ucsd.edu/~jmcauley/datasets.html#social_data)
- The Internet Movie Database (https://www.imdb.com/)
- LibraryThing website (https://www.librarything.com/)
- Wikidata (https://www.wikidata.org/wiki/Wikidata:Main_Page)
- DBpedia (https://www.dbpedia.org/)
- Freebase (https://developers.google.com/freebase)
