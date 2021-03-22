# Graph_Link_Prediction
COMP90051 UniMelb Project1

### Baseline Model

In the baseline model, all edges are added into one Graph (in networkx package). Then the feature engineering extracts some similarity metrics such as Jaccard, Neighbors, etc. and generate fake edges from the Graph. Next, a 3-layer neural network was trained to make prediction on the test-public data. 


### Random Walk

The ramdom walk was implemented via [Graphvite]:https://github.com/DeepGraphLearning/graphvite library. 
