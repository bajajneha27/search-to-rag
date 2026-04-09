# Search at Scale

To handle billions of queries a day across trillions of web pages in milliseconds, Google moves beyond a simple inverted index into a massive, distributed infrastructure.

## The Distributed Index

Google doesn't store its index on one machine. The index is split into thousands of pieces across different data centers. When you search, your query is sent to thousands of machines simultaneously, each checking its small piece of the web and reporting back.

## Ranking: PageRank to BERT

In the early days, Google used PageRank, which treated links like "votes". Today, it uses deep learning models like *BERT* and *MUM* to understand the actual intent of your sentence, allowing it to move past mere keyword matching.

## Caching and Global Load Balancing

To stay fast, Google uses Google Front Ends (GFEs) and heavy caching. If 1,000,000 people search for "weather" in the same minute, Google doesn't re-calculate the search every time; it serves a cached result from a server physically close to the user.

