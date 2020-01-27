# tweet classifier
Classification model for tweets aiming at predicting dengue, zika and chikungunya.

# Main files
## Scripts
* classifier.ipynb: first classifier which just uses term frequency of 500 main words
* classifier_postag.ipynb: uses part of speech tag from spaCy to generate morphological info which are used as variables
* classifier_word2vec.ipynb: uses word2vec space.
* classifier_word2vec_AUX.ipynb: notebook to generate word2vec models which are used by classifier_word2vec.ipynb
* keyword_retrieval.ipynb: gets all possible variations (mispellings) for word chikungunya.
* exploratory_analysis.ipynb: build visualizations for the data (years 2016-2018).
* anvil_data_builder.ipynb: builds data (in JSON format) which feeds the anvil app for people to classify each tweet.
* dengue-2012: Old notebook which tries to predict dengue by using UFMG database (from 2010-2018, doesn't contain extended_text) and old classification model. It should be kept as reference. What it does: simulates predictions over the year 2012, uses TF (TF-IDF doesn't work because each text sample is too long as it comprises tweets over a whole week), gets most important features (using Lasso and Random Forest), applies Machine Learning (just linear model as a baseline).

Database notebooks:
* file_manager.ipynb: fixes dengue.json.bz2 (which had a parsing error), building the dengue_fixed.json.bz2. Then it inserts all relevant data into a MongoDB collection. Warning: special characters had to be removed in order for the fix to work properly.

## Databases
### Iputs Out of github (files were too big)
* dengue.json.bz2: main database from UFMG, with all variables. This database has a parsing error and had to be fixed.
<!--- * dengue_fixed.json.bz2: fixed from previous database. Warning: special characters had to be removed in order for the fix to work properly. --->
* mongo_ufmg_filtered (folder) 
	* mongo_ufmg_filtered/twitter/ufmg_filtered.bson.gz: MongoDB collection containing only relevant variables from previous file. Needs to unzip to restore.
* amostra.tgz: another UFMG database (doesn't contain extended_text and other variables)
* tweets_anvil_input.json: input for anvil app.

### Inputs
* Base_de_dados_dos_municipios.xls: geocodes (IBGE source) of Brazilian municipalities which are necessary to retrieve city data from Infodengue.

### Outputs
* Word2vec models: 
	* virus_tweets.w2v: Main unaltered word2vec model
	* virus_tweets_encoded.w2v: word2vec model where special characters from Portuguese language were removed (accents, "ç")
	* virus_tweets_encoded_bigrams.w2v: word2vec model built using bigrams
* tweets_filtered.json: A file even more filtered from the MongoDB (ufmg_filtered.bson) to save memory usage. This is a file which feeds the classifiers as it recovers info from tweets by their IDs.
* tweets_anvil_input.json: input for Anvil database which was used for data annotation
* Anvil outputs:
	* from_anvil/classifications_finished.csv: Training data which feeds the classifiers (data were annotated inside Anvil)
	* from_anvil/tweets.csv:  equivalente to tweets_anvil_input.json, but was slightly transformed inside Anvil

## About Train Set
Location: outputs/from_anvil/classifications_finished.csv

Train set was built by collecting tweets from 2016-2018. The samples for data annotation were collected from a MongoDB collection (built from a JSON provided by UFMG) from weeks of virus peaks between 2016 and 2018, as there would be more relevant tweets during peaks (which would help with unbalanced data). 
* Total sample size: 5.000.
* Subsample size which was used for data annotation: 1.000.
* Data was annotated following instructions decided internally. See link: [Classifications instructions](https://github.com/AlertaDengue/tweet_classifier/blob/master/classification_instructions.md)
* The annotation process was organized with the creation of an app, with the objective of being faster and more interesting to participants to complete the task. The app was built using [Anvil](https://anvil.works/) and the scripts are located on 'notebooks/anvil_scripts' folder.

Participants in the data annotation: sandrabiafe@gmail.com, marcelo.gomes@fiocruz.br, lucas_bianchi123@hotmail.com, vcbbio@hotmail.com, bmacedocoimbra@gmail.com, iasmimalmeida26@gmail.com, felipebottega@gmail.com, alfcury@yahoo.com.br, biancadsloiola@gmail.com, catoper@gmail.com, sheylacitrangulo@gmail.com, nadja.lopes@gmail.com, emiledanielly@gmail.com, marcelobbribeiro@gmail.com, karinasantana.bqi@gmail.com, fccoelho@gmail.com, raquelmlana@gmail.com, claudia.codeco@gmail.com

