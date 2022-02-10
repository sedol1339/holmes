Diverse and detailed ML benchmark on tabular data for reproducible research

Contributions:
	1. Provide a diverse collection of datasets on tabular data
	2. Provide a detailed description for each dataset
	3. Provide a library for downloading these datasets
	4. Provide an online evaluation system based on this collection
	5. Provide a detailed information about each model predictions
	6. Provide different types of features, missing features, outliers, and data shift
Purpose:
	1. Compare a lot of existing methods
	2. Provide a reproducible code for a lot of existing methods
	3. Facilitate development and evaluation of new methods

------------------------

TODO list:

(10.02.22) Make a collection of some datasets and a library for downloading them

------------------------

Dataset subsets:
	Main subset
	Subset with data shift
	Subset with toy model tasks
	Subsets with fine-tuning and representation learning?
	
Dataset types:
	Classification (2-50000 classes), regression
	Balanced and imbalanced, different metrics (MSE, MAPE, F1, ROC AUC, ...)
	Small and large (optionally: make small by truncating large)
	With and without outliers and missing features
	With different type of features (quantitative, categorial, ordinal, sparse binary,
			bag-of-words, TF-IDF, text/image embeddings)
	Diverse: economical, biological, synthetic, time series etc.

Dataset examples:
	model parameters -> validation metrics

Model(s) + dataset = 
	accuracies
	partial dependency plots (1D, 2D, between 2 or 3 examples)
	stratified accuracies (on subsets)
	OOD accuracies (and optionally confidences)
	correlation between models
	ensemble accuracies
	accuracy dependencies: from iteration, number of train examples
	cross validation score
	reproducible code
	fine-tuning accuracy
	measure bias and variance
	representation learning?

Evaluation method:
	choose feature preprocessing method and hyperparameters
	provide concise and reproducible code (same for every dataset)
	provide best hyperparameters for every dataset?
	provide tags (auto feature selection, autoML, confidence, ...)
	- method should optionally return confidences, accuracy per epoch
	system will automatically make predictions on test data

Try:
	- GBDT, DL models, SVM, models from sklearn, bayesian neural networks
	- SP-models
	- multitask tabular pretraining
	- language models on numerical data
	- generative FT-transformers