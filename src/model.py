from pipeline import FraudData
from sklearn.ensemble import GradientBoostingClassifier


def get_training_data(path):
    '''
    Summary:
    Retrieve training data from a file then clean, transform, separate target from features, 
    and perform a split on training/test data with stratification of classes.

    Input: path (optional - default is initial dataset for this project)
    Output: X_train, X_test, y_train, y_test - splits on the data with stratification
    '''
    D = FraudData(path)
    df = D.get_enriched_df()

    return D.get_train_test_data()


def train_model(X_train, y_train):
    '''
    Summary:
    Take training data, fit a gradient boosting classifier with predetermined hyperparameters,
    and return the trained model.

    Input: path (optional - default is initial dataset for this project)
    Output: A trained gradient boosting model
    '''
    gb = GradientBoostingClassifier(learning_rate=.1,
                                    n_estimators=1000,
                                    max_depth=5,
                                    max_features='auto')
    gb.fit(X_train, y_train)

    return gb


if __name__ == '__main__':

    X_train, X_test, y_train, y_test = get_training_data('../data/data.json')
    model = train_model(X_train, y_train)
    print('The accuracy for this model is {:.2f}%.'.format(model.score(X_test, y_test) * 100
                                                           ))
