
# Introduction to Search Engine

Three key things for Search:

1. Dataset collection ( Crawling )
2. Pre-processing ( Indexing )
3. Execution ( Querying )

## Crawling

Crawling is the discovery phase. A "crawler" is a script that systematically browses the web (or a local filesystem) to find content.

- Web for search engines
- Catalog for e-commerce websites
- Books for library 

## Indexing

Indexing is a pre-processing step before a user could ever search anything. Since the number of documents can be huge in billions, real time search will take a lot of time. So, we need to pre-process those documents so that search results happen in milliseconds.

## Querying

This happens in real-time when a user types a search. The system takes the user's input, does some cleaning and then looks up the results in the map we built during indexing to find the best matches.

