# Détection de fraude avec du Deep Learning


## Description

Dans ce projet, on va implémenter des méthodes de Deep Learning pour la détection de fraude. L'objective est d'avoir un algorithme facilement généralisable pour traiter des différentes sources des données. Pour ce faire, on a téléchargé un dataset venant du challenge Kaggle [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud). L'historique des données est de deux jours du mois de septembre 2013.

Les données ont été anonimisées pour des raisons des confidentialité et ses variables explicatives ont été déjà traitées par une transformation PCA. En plus, ces données sont très desiquilibrés car seulement 0.192% d'observations sont des operations frauduleuses (492/284807)

Données - Description des variables explicatives :
* **V[1-28]**, sont les composantes principales transformation PCA.
* **amount**, c'est la quantité de la transaction
* **time**, c'est le temps entre la première transaction dur dataset et l'observation en cours.
* **Class**, indicatuer de fraude/non fraude étant 1 une opération frauduleuse.

Dossier de développement de la détection de fraude et comparaison entre DeepLearning and MachineLearning

## Objectifs

- Implémenter un algorithme de Deep Learning qui soit facilement généralisable pour des nouvelles donées
- Alimenter l'AxioLib

## Réferences

- A compléter...

