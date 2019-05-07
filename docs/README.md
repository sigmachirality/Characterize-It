# Characterize-It
![](/superhero.png)

#

Comic book characters come in all shapes and sizes. But do we view comic characters as their original artist intended? Does the gender or appearance of a character influence how we describe them? To answer these questions, we will ask MTurkers to describe different comic book characters with specific terms. Then, using machine learning models, we will seek to determine which features and terms are commonly associated with characters of a certain gender and alignment. We hope that the results of our project can be used to help artists and creators avoid stereotypes, push the envelope of character design, and ensure their character isn't misinterpreted by an audience.

## Components
1. Data - Our initial data comes from the FiveThirtyEight Comic Characters dataset, which we have additionally cleaned and added images too. 
2. MTurk Collection - Our MTurk HITs elicit feedback on the appearance of characters in the form of adjectives, which we will then compile and add as additional features for our dataset.
3. Prediction Model - We will train several models to attempt to classify comic characters alignment based on the dataset features. We will train several initial models including a Random Forest model, an SVM model, a logistic regression model and a Naive Bayes model and compare the models using n-fold cross validation to select the best one.
4. Feature Extraction - We will determine which features are strongly correlated with both alignment and gender using PCA and unsupervised learning techniques.
5. Generative Model - We will build a model using a Generative Adversarial Network that attempts to create fake characters based on the qualities of real comic characters.
6. Web Application - We will host a subset of our models in a web app to allow users to generate comic character ideas and make sure that they are avoiding biases in their character creation.


## Milestones
- Data Cleaning: 1pt - remove data points with missing features
- Image Scraping: 2pt - write a python script to add image URLs to the dataset
- HIT creation: 3pt - post HITs for MTurk users to add image descriptions, then add the results as dataset features
- HIT data extraction: 2pt - Use LDA or some other technique to classify MTurk descriptions as new features for the dataset
- EDA: 2pt - Create plots and graphs showing initial findings based on correlation amongs data features
- Prediction Model: 3pt - Train and compare multiple models for classifying comic characters
- Feature Extraction: 2pt - Run PCA and other techniques
- GANs Model: 3pt - Build model to generate comic characters
- Web app: 4pt - Host subset of models online

## Data

### Quality Control
The quality control module `qc.py` is in the `src/` directory. It cleans data input, strips unneeded information, checks the validity of responses to a test question, ensures validity of given adjectives and removes duplicate responses.

Input to the quality control module comes in the form of a large CSV file with many fields. The following fields are relevant:
- HITId - The ID of the HIT in question.
- WorkerId - The ID of the worker who completed the HIT.
- Input.image_url - The URL for the image shown to the worker.
- Input.prompt - The prompt for the verification test.
- Answer.adjective0 through Answer.adjective9 - The worker's responses to the shown image.
- Answer.seen.on - Whether or not the worker has seen the character before.
- Answer.type_test - The worker's response to the verification test.

Output is a CSV that contains similar fields:
- hit_id - The ID of the HIT in question.
- worker_id - The ID of the worker who completed the HIT.
- image_url - The URL for the image shown to the worker.
- seen - Whether or not the worker has seen the character before.
- prompt - The prompt for the verification test.
- type_test - The worker's response to the verification test.
- adjective0 through adjective9 - The worker's responses to the shown image.


### Aggregation
The aggregation module `ag.py` is in the `src/` directory. It collects the most popular responses for each image and returns a file with the top five responses for each given image.

Input to the aggregation module is the output of the quality control module above.

Output from the aggregation module is a CSV with the following fields:
- image_url - The URL for the image shown to the worker.
- adjective0 through adjective4 - The top 5 adjectives by response frequency in descending order.
