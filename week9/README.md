Group:
- João Gabriel Rodrigues de Azevedo
- João Victor Moura Monteiro Madruga
- Lucas Morais Freire

Steps:
- Data used provided by 'alvarofpp' 
- First install and import the dependencies required to generate our graphs and to create graphics so we can have a visual notion of the results. Update the data to be up-to-date by running the proper scripts provided.
- Instantiate a Graph() object and put the data from the .graphml file inside it.
- We will exclude the international flights from this graph, because in this analysis only the national flights are important.
- we will be using the networkX library to do our analysis of the data.
- we will use matplotlib.pyplot to plot a graphs and images to help us understand the results.
- Requirement 1 -> Use nx.attribute_assortativity_coefficient(G, 'region') to get the assortativity coefficient with respect to the region of the airport.
- Requirement 2 -> Use nx.degree_assortativity_coefficient(G, 'region') to get the degree assortativity.
- Requirement 3 -> S = nx.connected_components(G), loop through the S list, get the amount of nodes from each region and then calculate the percentagem of airports that contained in each region
- Requirement 4 -> Find a path to travel through a city from each region by taking the shortest path. Considering that it is more likely for there to be direct flights between bigger cities, we searched for the airport code of each city of interest in the airports.csv file and then ran nx.shortest_path(G,"city1","city2"). With this in our hands, we search in the major air companies' websites and checked the average price for those flights.
- Requirement 5 -> Generate subgraphs for each region, and use nx.average_clustering(region_graph) to do the clustering analysis for each one, and compare them with the clustering of the whole graph.

Major fidings:
- The positive value of the assortativity coefficient implies that indeed there is a tendency for flights to occur between airports that are in the same region.

- There is a clear tendency in some regions that suggest that there are more flights inside the regions instead of in between, although the sum of the flights between regions for any region might get close to the internal flights.

- The negative value from the bivariate analysis suggests that nodes with lots of neighbours tend to have a low average neighbour degree. This makes sense because airports from cities that are not very big tend to only have flights to the bigger cities in the same region or state, often the capitals. So the big cities end up having lots of neighbours of small degree and with just a few neighbours of high degree.

- From the connected componets that exist in the network, we can see that most nodes are connected, but there are a few isolated nodes. We could assume it's because they are international-only airports or private airports.

- Most of each airport's neighbours are connected to each other, meaning that most airports have a tendency to cluster together. Inside regions this coefficient is a bit lower, that could be because, in Brazil, it is more likely for someone to fly to other regions than their own, given that the usual circumstance to travel by plane is that you are going somewhere so far that it is unfeasible to go by car or other methods.
