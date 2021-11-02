# Software Engineering for Machine Learning Assignment (ML Microservice)

The model within the repository is used to predict the G3 performance of students with specified parameters. G3 is defined as the final year grade of a student which is based on a subset of features for a student (out of 20). A student is said to be a quality student (to CMU admissions) if their G3 > 14 in value. A description of the microservice and the model can be found in their respective sections. 

## How to Deploy the Microservice

The microservice utilizes Flask for the application interface and is deployed in a Docker container. After cloning the repo you must 

  (1) - Change directory to dockerfile
run <cd dockerfile> from the main directory /fall-2021-hw4-shrimp-gang

  (2) - Build the container
run `docker build -t ml:latest .`

  (3) - Run the container
We run the container on port 5000 with `docker run -d -p 5000:5000 ml`

## API Documentation
The microservice has one endpoint

#### /predict
  
Predict takes in 6 parameters, the number of features that we predict a quality student based on, and return 1 for a student that would be admitted to the school or zero for the negative case. When calling predict, enter the url as follows and place the appropriate arguments in this format where the letters are integers that are within the bounds that as described below the format.

format for url >>  localhost:5000/predict?studytime=x&absences=y&goout=z&Dalc=a&G1=b&G2=c

  1. Studytime: weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)

  2. Absences: number of school absences (numeric: from 0 to 93)

  3. Goout: going out with friends (numeric: from 1 - very low to 5 - very high)

  4. Dalc: workday alcohol consumption (numeric: from 1 - very low to 5 - very high)

  5. G1: first period grade (numeric: from 0 to 20)

  6. G2: second period grade (numeric: from 0 to 20)

Note that /predict automatically checks for missing parameters and correct parameter types, you will receive a 400 error with a small description of what is incorrect or missing.

## Model Description - Features and Retraining
We used a decision tree classifier for our model. The features we trained on include all the features that can be run on predict

Studytime: weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
Absences: number of school absences (numeric: from 0 to 93)
Goout: going out with friends (numeric: from 1 - very low to 5 - very high)
Dalc: workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
G1: first period grade (numeric: from 0 to 20)
G2: second period grade (numeric: from 0 to 20)

After training on a multitude of features, it was seen that studytime, absences, goout, dalc have high correlation with G3 (larger than 0.05). Furthermore G1, G2 were seen to be the most correlated variables and are a great predictor for the final grade that a student will potentially see. There were other quality variables that are correlated, when combinding these other quality variables we obtain a very random distribution that does not match what one would expect with the data, for instance a graph on activities and health had little correlation together while studytime and goout had a normal distribution when plotting against a high G3.
  
When looking at the baseline model, which considered age, absences, and health, we find the following results:
  - Precision is  0.7441860465116279
  - Recall is  0.4383561643835616
  - F1_score is  0.5517241379310345
This implies that the model does not flag students that should be predicted as quality by the school correctly in most cases, these scores are abysmal and show that the model is incredibly inaccurate, to the point of guessing. This is also seen with F1 score, and average of precision and recall, and describes the data as little more than a coin flip.
  
When running against our model we have the following results
  - Precision is  0.9565217391304348
  - Recall is  0.9166666666666666
  - F1_score is  0.9361702127659574
We see high precision and recall. When we correctly flag a student as quality, we're correct 95% of the time, however we are only flagging qualified students as qualified 91% of the time.

## Testing the Model
Automatic testing is done via the bash script in Github actions. The tests encompass both expected results and API effectiveness. A github actions task is run that does multiple requests on our predict endpoint expecting zeroes and ones for qualified and unqualified students.
  
If users want to test the model locally simply deploy as above and run the `./test_script.sh` command in the top level directory
