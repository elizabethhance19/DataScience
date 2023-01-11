# sklearn random and grid search
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from catboost import CatBoostRegressor
import numpy as np
import pandas as pd

train_data = pd.DataFrame(np.random.randint(1, 100, size=(100, 10)))
train_data["cat_col"] = ["a"] * 75 + ["b"] * 25
train_labels = pd.DataFrame(np.random.randint(1, 100, size=(100)))
model = CatBoostRegressor(
	early_stopping_rounds=40,
	loss_function="RMSE",
	cat_features=["cat_col"]
)
grid = {
	'learning_rate': [0.03, 0.1],
	'depth': [4, 6, 7]}
grid = {
	'learning_rate': [0.03],
	'depth': [4],
	'early_stopping_rounds': [5]}
clf = GridSearchCV(model, grid, return_train_score=True, cv=3)
clf.fit(train_data, train_labels)
a = pd.DataFrame.from_dict(clf.cv_results_)

clfR = RandomizedSearchCV(model, grid, return_train_score=True, cv=3)
clfR.fit(train_data, train_labels)
a = pd.DataFrame.from_dict(clfR.cv_results_)
