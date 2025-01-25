import string
import numpy as np

data = {
    1: {'Which of the following is used to define a function in Python?': ['func()', 'function()', 'def()', 'def']},
    2: {'Which of the following methods is used to read input from the user in Python?': ['input()', 'get()', 'read()', 'scan()']},
    3: {'Which of the following is the correct syntax to create a set in Python?': ['set(1, 2, 3)', '{1, 2, 3}', '(1, 2, 3)', '[1, 2, 3]']},
    4: {'What is the correct way to handle exceptions in Python?': ['try/except', 'catch/throw', 'catch/finally', 'try/throw']},
    5: {'Which of the following algorithms is typically used for classification problems?': ['Linear Regression', 'K-Means Clustering', 'Decision Trees', 'Principal Component Analysis']},
    6: {'In supervised learning, the algorithm is trained using:': ['Unlabeled data', 'Labeled data', 'Both labeled and unlabeled data', 'No data']},
    7: {'Which of the following techniques is used to prevent overfitting in a machine learning model?': ['Increasing the size of the dataset', 'Cross-validation', 'Both A and B', 'None of the above']},
    8: {'What does the term “underfitting” mean in machine learning?': ['The model is too complex', 'The model is too simple to capture patterns in the data', 'The model is trained with too much data', 'The model works well with new data']},
    9: {'Which of the following is the primary goal of the K-Means algorithm?': ['To cluster data into distinct groups', 'To reduce the dimensionality of the data', 'To predict continuous values', 'To classify data into labels']},
    10: {'Which Python library is commonly used for data manipulation and analysis?': ['NumPy', 'Pandas', 'Matplotlib', 'Scikit-learn']},
    11: {'In data science, what does EDA stand for?': ['Early Data Analysis', 'Exploratory Data Analysis', 'Enhanced Data Analysis', 'Efficient Data Analysis']},
    12: {'Which of the following is NOT an example of a regression algorithm?': ['Linear Regression', 'Logistic Regression', 'Decision Tree Regression', 'K-Means Clustering']},
    13: {'Which of the following techniques is used to deal with missing data in a dataset?': ['Imputation', 'Normalization', 'Feature Scaling', 'Overfitting']},
    14: {"Which of the following methods is typically used to evaluate a model's performance on a classification task?": ['Mean Squared Error', 'Accuracy, Precision, Recall', 'R-squared', 'ROC Curve']},
    15: {'What is the Output of the following code?\n\tx = [1,2,3,4,5]\n\tx[1:3] = [9,8]\n\tprint(x)': ['[1,9,8,4,5]','[1,9,8,3,4,5]','[9,8,4,5]','[1,9,8,3,4]']}

}

answers = {1: 'D', 2: 'A', 3: 'B', 4: 'A', 5: 'C', 6: 'B', 7: 'C', 8: 'B', 9: 'A', 10: 'B', 11: 'B', 12: 'D', 13: 'A', 14: 'B', 15: 'A'}

def results(total, correct, wrong):
    print("\nYour Test is Ended.")
    print(f"\nResults: Total Questions: {total}\nCorrect Answers: {correct}\nWrong Answers: {wrong}")
    return


def questions(que_list):
    total = len(que_list)
    correct = 0
    wrong = 0
    for j in que_list:
        for que, ans in data[j].items():
            print(f'\n{j}) {que}')
            for ord, i in enumerate(ans):
                print(f"{string.ascii_uppercase[ord]})", " ", i)
            ans = input("Answer the Questions: ").upper()
            crt_ans = answers[j]
            if ans == crt_ans:
                print("Congratulation. You are Right")
                correct += 1
            else:
                print("Sorry, You are Wrong")
                print(f'The Correct answer is : {answers[j]}')
                wrong += 1
    return results(total, correct, wrong)
    

if __name__ == '__main__':
    no_of_questions = int(input("Enter no of questions you want upto 15: "))
    que_list = np.random.choice(range(1, 16), size = (no_of_questions), replace = False)
    questions(que_list)