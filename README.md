![GitHub repo size](https://img.shields.io/github/repo-size/sisinflab/elliot) ![GitHub](https://img.shields.io/github/license/sisinflab/Augmented-and-Linked-Open-Datasets-for-Recommendation.svg)

[Main page](https://sisinflab.github.io/Augmented-and-Linked-Open-Datasets-for-Recommendation/) - [GitHub Repository](https://github.com/sisinflab/Augmented-and-Linked-Open-Datasets-for-Recommendation/)

# Augmented and Linked Open Datasets for Recommendation

This is the official repository of the paper *Linked Open Datasets for Recommendation*.
This work covers the enrichment of two widely used recommendation datasets from the movie and book domain, [MovieLens 25M](https://grouplens.org/datasets/movielens/25m/) and [LibraryThing](https://cseweb.ucsd.edu/~jmcauley/datasets.html#social_data) respectively. Specifically:
- we link the items in the LibraryThing (LT) and MovieLens 25M (ML25M) datasets with the entities available in three well-known knowledge graphs: Wikidata, DBpedia, and Freebase;
- starting from item entity linking, we explore the Wikidata and DBpedia knowledge graphs connections up to two hops to collect all the structured information connected to these resources, thus providing persistenta nd ready-to-use enriched datasets for performing reproducible experiments; 

Inspired by the advances in knowledge graph, Graph Convolutional Networks, Link Prediction, and Recommender Systems research, these augmented datasets aim to meet their cutting-edge research needs. Moreover, these datasets pave the way to further research to investigate different recommendation modalities simultaneously.


<!-- <p align="center">
<img src="images/resources.png" alt="drawing" width="500" />
</p> -->

## Download the Datasets
All the resources are available [here](https://tny.sh/sisinflab-alod) . 

Please note that the resources cannot be hosted on GitHub due to [GitHub size limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

## Resources
Our resources collect:
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


  ```
  
  <table>
    <tr>
        <td>File Name </td> 
        <td>Descriptions</td> 
   </tr>
   <tr>
        <td align='center', colspan="2">MovieLens 25M</td>    
   </tr>
   <tr>
        <td>ml25m_linking.tsv</td> 
        <td>This file contains the link of items in the MovieLens 25M dataset to Wikidata, DBpedia, and FreeBase Knowledge Graphs. This is a tab separated file containing the following fields: <ul><li><i>movie_id</i> : the movie identifier in the MovieLens 25M dataset</li><li><i>wikidata_uri</i> : the uri resource on Wikidata associated to the movie </li><li><i>dbpedia_uri </i>: the uri resource on DBpedia associated to the movie  </li><li><i>freebase_uri</i> : the uri resource on FreeBase associated to the movie </li></ul></td> 
   </tr>
   <tr>
        <td align='center', colspan="2">LibraryThing</td>    
   </tr>
 <tr>
        <td>lt_linking.tsv</td> 
        <td> This file contains the link of items in the LibraryThing dataset to Wikidata and DBpedia Knowledge Graphs. This is a tab separated file containing the following fields: <ul><li><i>work_id </i>: the book identifier in the LibraryThing dataset</li><li><i>wikidata_uri </i>: the uri resource on Wikidata associated to the book </li><li><i>wikidata_similarity</i> : the similarity between dataset and Wikidata side information value  </li><li><i>dbpedia_uri</i> : the uri resource on DBpedia associated to the book  </li><li><i> dbpedia_similarity</i> : the similarity between dataset and DBpedia side information value </li></ul></td> 
   </tr>
    <tr>
        <td rowspan="2">I am a merged column</td>    
        <td>3.rows and two columns</td>  
    </tr>
    <tr>
        <td> Row, 4. Column, Two</td>  
    </tr>
</table>
| File Name | Descriptions |
|-----------|--------------|
|| MOVIELENS 25M ||
| ml25m_linking.tsv | This file contains the link of items in the MovieLens 25M dataset to Wikidata, DBpedia, and FreeBase Knowledge Graphs. This is a tab separated file containing the following fields: <ul><li><i>movie_id</i> : the movie identifier in the MovieLens 25M dataset</li><li>wikidata_uri : the uri resource on Wikidata associated to the movie </li><li>dbpedia_uri : the uri resource on DBpedia associated to the movie  </li><li>freebase_uri  : the uri resource on FreeBase associated to the movie </li></ul>|
| lt_linking.tsv | This file contains the link of items in the LibraryThing dataset to Wikidata and DBpedia Knowledge Graphs. This is a tab separated file containing the following fields: <ul><li>` work_id ` : the book identifier in the LibraryThing dataset</li><li>` wikidata_uri ` : the uri resource on Wikidata associated to the book </li><li>` wikidata_similarity ` : the similarity between dataset and Wikidata side information value  </li><li>` dbpedia_uri ` : the uri resource on DBpedia associated to the book  </li><li>` dbpedia_similarity ` : the similarity between dataset and DBpedia side information value </li></ul>|
| lt_wikidata_freebase_linking.tsv | This file contains the link of items in the LibraryThing dataset to FreeBase Knowledge Graph from Wikidata. This is a tab separated file containing the following fields: <ul><li>` work_id ` : the book identifier in the LibraryThing dataset</li><li>` wikidata_uri ` : the uri resource on Wikidata associated to the book </li><li>` wikidata_similarity ` : the similarity between dataset and Wikidata side information value  </li><li>` freebase_uri ` : the uri resource on FreeBase associated to the book from the Wikidata uri </li></ul>|
| lt_dbpedia_freebase_linking.tsv | This file contains the link of items in the LibraryThing dataset to FreeBase Knowledge Graph from DBpedia. This is a tab separated file containing the following fields: <ul><li>` work_id ` : the book identifier in the LibraryThing dataset</li><li>` dbpedia_uri ` : the uri resource on DBpedia associated to the book </li><li>` dbpedia_similarity ` : the similarity between dataset and DBpedia side information value  </li><li>` freebase_uri ` : the uri resource on FreeBase associated to the book from the DBpedia uri </li></ul>|
| user_item.csv | This file contains the interaction of user and item.<br> This is a tab separated list: `user ID \| item ID \| timestamp \|`  |
| session_item.csv | This file contains the affiliation of session and its items. Each session has at least 2 items.<br> This is a tab separated list: `session ID \| item ID \|` <br>The session IDs are the ones used in the `session_bundle.csv` and `user_session.csv` data sets.  |
| user_session.csv| This file contains the interaction of user and session.<br> This is a tab separated list: `user ID \| session ID \| timestamp \|`  |
| session_bundle.csv| This file contains the affiliation of session and detected bundles. Each session has at least 1 bundle.<br> This is a tab separated list: `session ID \| bundle ID \|` <br>The bundle IDs are the ones used in the `bundle_item.csv` ,`user_bundle.csv` and `bundle_intent.csv` data sets. |
| bundle_intent.csv | This file contains bundle and its annotated intent.<br> This is a tab separated list: `bundle ID \| intent \|`  |
| bundle_item.csv | This file contains the affiliation of bundle and its items. Each bundle has at least 2 items.<br> This is a tab separated list: `bundle ID \| item ID \|` |
| user_bundle.csv | This file contains the interaction of user and bundle.<br> This is a tab separated list: `user ID \| bundle ID \| timestamp \|`  |
| item_categories.csv| This file contains item and its categories.<br> This is a tab separated list: `item ID \| categories \|` <br> The format of data in `categories` column is a list of string. |

### Resources Statistics

The table below shows the statistics of the collected resource categorized by dataset and data source.

<p align="center">
<img src="images/stats.png" alt="drawing" width="500" />
</p>

### Resources Description

Here we provide a description of the contents of our collection.

<p align="center">
<img src="images/description_files.png" alt="drawing" width="700" />
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
This work is released under [APACHE2 License](./LICENSE).

## Acknowledgements
Our datasets are constructed thanks to 
- MovieLens dataset (https://grouplens.org/)
- LibraryThing dataset(https://cseweb.ucsd.edu/~jmcauley/datasets.html#social_data)
- The Internet Movie Database (https://www.imdb.com/)
- LibraryThing website (https://www.librarything.com/)
- Wikidata (https://www.wikidata.org/wiki/Wikidata:Main_Page)
- DBpedia (https://www.dbpedia.org/)
- Freebase (https://developers.google.com/freebase)
