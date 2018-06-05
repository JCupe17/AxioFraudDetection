# Fraud Detection using Neural Networks


## Description

This project aims to show some algorithms for fraud detection using neural networks.
Even if fraud detection mechanisms are subject-dependent, we use a deep learning approach to avoid any feature extraction.

To implement the algorithms, we used a free dataset from Kaggle: [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud).
This dataset is a history of credit card transactoins during two days in September 2013. The features are anonymized due to confidentiality and privacy reasons.
There are 28 features that are the result of a PCA processing:

* **V[1-28]**, principal features from a PCA process.
* **amount**, amount of imoney for this transaction.
* **time**, number of seconds elapsed between each transaction (over two days).
* **Class**, fraud or non-fraud.

The dataset is a highly unbalanced dataset because there are only 492 frauds out of 284807 transactions (0.172% of all transactions).

