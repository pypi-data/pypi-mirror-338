from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
from xgboost import XGBClassifier
import warnings

warnings.filterwarnings('ignore')


def test_all_classifiers(X, y, test_size=0.2, random_state=42, scale_data=True):
    """
    Test multiple classification models and return their performance metrics.
    
    Parameters:
    X (array-like): Feature matrix
    y (array-like): Target vector
    test_size (float): Proportion of dataset to include in test split
    random_state (int): Random seed for reproducibility
    scale_data (bool): Whether to scale the data before fitting models
    
    Returns:
    DataFrame: Results comparing all classifiers
    """
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    # Scale data if requested
    if scale_data:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
    
    # Initialize classifiers
    classifiers = [
        ('Logistic Regression', LogisticRegression(max_iter=1000, random_state=random_state)),
        ('Decision Tree', DecisionTreeClassifier(random_state=random_state)),
        ('Random Forest', RandomForestClassifier(random_state=random_state)),
        ('Gradient Boosting', GradientBoostingClassifier(random_state=random_state)),
        ('AdaBoost', AdaBoostClassifier(random_state=random_state)),
        ('SVM', SVC(random_state=random_state)),
        ('k-NN', KNeighborsClassifier()),
        ('Naive Bayes', GaussianNB()),
        ('Linear Discriminant Analysis', LinearDiscriminantAnalysis()),
        ('Quadratic Discriminant Analysis', QuadraticDiscriminantAnalysis()),
        ('MLP Neural Net', MLPClassifier(random_state=random_state, max_iter=1000)),
        ('SGD Classifier', SGDClassifier(random_state=random_state)),
        ('XGBoost',XGBClassifier(random_state=random_state, eval_metric = 'mlogloss', use_label_encoder=False)),
        ('LightGBM', LGBMClassifier(random_state=random_state))
    ]
    
    results = []
    
    for name, clf in classifiers:
        try:
            clf.fit(X_train, y_train)
            y_pred = clf.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred, output_dict=True)
            
            results.append({
                'Classifier': name,
                'Accuracy': accuracy,
                'Precision (weighted)': report['weighted avg']['precision'],
                'Recall (weighted)': report['weighted avg']['recall'],
                'F1-score (weighted)': report['weighted avg']['f1-score']
            })
            
        except Exception as e:
            print(f"Error with {name}: {str(e)}")
            results.append({
                'Classifier': name,
                'Accuracy': None,
                'Precision (weighted)': None,
                'Recall (weighted)': None,
                'F1-score (weighted)': None
            })
    
    # Convert results to DataFrame and sort by accuracy
    results_df = pd.DataFrame(results)
    results_df = results_df.sort_values('Accuracy', ascending=False).reset_index(drop=True)
    
    return results_df