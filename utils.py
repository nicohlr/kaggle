import matplotlib as plt
import seaborn as sns
import pandas as pd
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.tree import export_graphviz


def display_confusion_matrix(y, prediction, score=None):
    """
    Create a confusion matrix and display it with a classification report (for classification task only)

    Args:
        y: true value of output
        prediction: prediction of the model
        score: score calculated from the model
    """
    cm = metrics.confusion_matrix(y, prediction)
    plt.figure(figsize=(9, 9))
    sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r')
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')

    if score:
        all_sample_title = 'Accuracy Score: {0}'.format(score)
        plt.title(all_sample_title, size=15)

    print(metrics.classification_report(y, prediction))


def visualize_tree(tree, feature_names, class_names):
    """
    Create tree png using graphviz
    Call "! dot -Tpng dt.dot > dt.png" to convert .dot into .png

    Args:
        tree: model which created the tree
        feature_names: names of the features
        class_names: names of the classes
    """

    with open('dt.dot', 'w') as f:
        export_graphviz(tree, out_file=f, feature_names=feature_names, class_names=class_names, filled=True, impurity=False)

    command = ['dot', '-Tpng', 'dt.dot', '-o', 'dt.png']
    try:
        subprocess.check_call(command)
    except:
        exit('Could not run dot, ie graphviz, to produce visualization')
        

def draw_missing_data_table(df):
    """
    Create table for missing data analysis

    Args:
        df (pd.DataFrame): dataframe to be analysed

    Returns (pd.DataFrame): dataframe containing the number dans percentage of missing data for each class of original df
    """
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    return missing_data


def standardize(df, target=None, categorical=None):
    """
    Standardize dataframe by setting its mean to 0 and it's variance to 1
    Args:
        df (pd.DataFrame): dataframe to be standardized
        target (String): target column which should not be standardized
        categorical (List): columns containing categorical variable

    Returns (pd.DataFrame): standardized dataframe
    """
    standardize_df = df
    
    if target:
        target_serie = standardize_df[target]  # Separating out the target before standardizing
        standardize_df = standardize_df.drop([target],  axis=1)
    
    if categorical:
        cat_serie = standardize_df[categorical]  # Separating out categorical feature(s) before standardizing
        standardize_df = standardize_df.drop([categorical],  axis=1)

    # Standardizing the features
    scaled_values = StandardScaler().fit_transform(standardize_df.values)
    standardize_df = pd.DataFrame(scaled_values, index=standardize_df.index, columns=standardize_df.columns)
    
    if target:
        standardize_df = standardize_df.join(target_serie)
        
    if categorical:
        standardize_df = standardize_df.join(cat_serie)
    
    return standardize_df
