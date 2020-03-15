# tm-domains

**Keyword_lookup.ipynb** is code for looping over previously extracted pickles to extract filtered json files

**random_sample.json** is 10,000 random articles for Jan to play with (tf-idf)

**travel_test_version_threshold_4.json** is a json file containing ~6500 texts - half related, half unrelated to SDG1 - this is essentially a shortcut to those who want to experiment with BERT/ NN etc. It can be read straight into a dataframe: df = pd.read_json(filename)
THIS FILE WAS UPDATED TO REMOVE DUPLICATES 
