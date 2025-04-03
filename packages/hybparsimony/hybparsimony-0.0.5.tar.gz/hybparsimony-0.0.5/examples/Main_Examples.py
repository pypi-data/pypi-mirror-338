
if __name__ == "__main__":

    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split, RepeatedKFold
    from sklearn.metrics import mean_squared_error
    from sklearn.datasets import load_diabetes
    from sklearn.preprocessing import StandardScaler
    from hybparsimony import HYBparsimony
    import os
    
    print('############################################################################')
    print("These are examples of using and configuring HYBparsimony().\
\nThe examples use very small data sets to reduce elapsed times.\
\nAlso, in some examples the number of iterations ('maxiter') has been reduced\
\nas well as the use of weak validation to minimize computation times.\
\nDue to these reasons some results could not be reliable.\
\nTo obtain reliable results with these datasets, it is recommended to use\
\nrepeated cross-validation and increase 'maxiter'.")
    print('############################################################################')
    
    # ------------------------------------------------------------
    
    input("\nFirst example: 'Using KernelRidge regression algorithm'.\nPress a key to continue...")
    os.system('clear')

    #####################################################
    #         Use sklearn regression algorithm          #
    #####################################################

    # Load 'diabetes' dataset
    diabetes = load_diabetes()
    X, y = diabetes.data, diabetes.target
    print(X.shape)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1234)
    
    
    # Standarize X and y (some algorithms require that)
    scaler_X = StandardScaler()
    X_train = scaler_X.fit_transform(X_train)
    X_test = scaler_X.transform(X_test)

    scaler_y = StandardScaler()
    y_train = scaler_y.fit_transform(y_train.reshape(-1,1)).flatten()
    y_test = scaler_y.transform(y_test.reshape(-1,1)).flatten()
    algo = 'KernelRidge'
    HYBparsimony_model = HYBparsimony(algorithm=algo,
                                    features=diabetes.feature_names,
                                    rerank_error=0.001,
                                    verbose=1)
    HYBparsimony_model.fit(X_train, y_train, time_limit=0.20)
    # Check results with test dataset
    preds = HYBparsimony_model.predict(X_test)
    
    print(f'\n\nBest Model = {HYBparsimony_model.best_model}')
    print(f'Selected features:{HYBparsimony_model.selected_features}')
    print(f'Complexity = {round(HYBparsimony_model.best_complexity, 2):,}')
    print(f'5-CV MSE = {-round(HYBparsimony_model.best_score,6)}')
    print(f'RMSE test = {round(mean_squared_error(y_test, preds, squared=False),6)}')
    
    # ------------------------------------------------------------
    
    input("\nNext example: 'Using different regression algorithms'.\nPress a key to continue...")
    os.system('clear')

    ########################################################
    #         Use different regression algorithms          #
    ########################################################
    algorithms_reg = ['Ridge', 'Lasso', 'KernelRidge', 'KNeighborsRegressor', 'MLPRegressor', 'SVR',
    'DecisionTreeRegressor', 'RandomForestRegressor']
    res = []
    for algo in algorithms_reg:
        print('#######################')
        print('Searching best: ', algo)
        HYBparsimony_model = HYBparsimony(algorithm=algo,
                                        features=diabetes.feature_names,
                                        maxiter=2, # Extend to more iterations to improve results (time consuming)
                                        # cv=RepeatedKFold(n_splits=5, n_repeats=10), #uncomment to improve validation (time consuming)
                                        # n_jobs=20, # each job execute one fold
                                        rerank_error=0.001,
                                        verbose=1)
        # Search the best hyperparameters and features 
        # (increasing 'time_limit' to improve RMSE with high consuming algorithms)
        HYBparsimony_model.fit(X_train, y_train, time_limit=5)
        # Check results with test dataset
        preds = HYBparsimony_model.predict(X_test)
        print(algo, "RMSE test", mean_squared_error(y_test, preds, squared=False))
        print('Selected features:',HYBparsimony_model.selected_features)
        print(HYBparsimony_model.best_model)
        print('#######################')
        # Append results
        res.append(dict(algo=algo,
                        MSE_5CV= -round(HYBparsimony_model.best_score,6),
                        RMSE=round(mean_squared_error(y_test, preds, squared=False),6),
                        NFS=HYBparsimony_model.best_complexity//1e9,
                        selected_features = HYBparsimony_model.selected_features,
                        best_model=HYBparsimony_model.best_model))

    res = pd.DataFrame(res).sort_values('RMSE')
    # Visualize results
    print(res[['best_model', 'MSE_5CV', 'RMSE', 'NFS', 'selected_features']])

    # ------------------------------------------------------------

    input("\nNext example: 'Binary Classification'.\nPress a key to continue...")
    os.system('clear')

    # ##############################################################
    # #                      BINARY CLASSIFICATION                 #
    # ##############################################################

    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.datasets import load_breast_cancer
    from sklearn.metrics import log_loss
    from hybparsimony import HYBparsimony
    
    # load 'breast_cancer' dataset
    breast_cancer = load_breast_cancer()
    X, y = breast_cancer.data, breast_cancer.target 
    print(X.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=1)
    
    # Standarize X and y (some algorithms require that)
    scaler_X = StandardScaler()
    X_train = scaler_X.fit_transform(X_train)
    X_test = scaler_X.transform(X_test)

    HYBparsimony_model = HYBparsimony(features=breast_cancer.feature_names,
                                    rerank_error=0.005,
                                    verbose=1)
    HYBparsimony_model.fit(X_train, y_train, time_limit=0.50)
    # Extract probs of class==1
    preds = HYBparsimony_model.predict_proba(X_test)[:,1]
    print(f'\n\nBest Model = {HYBparsimony_model.best_model}')
    print(f'Selected features:{HYBparsimony_model.selected_features}')
    print(f'Complexity = {round(HYBparsimony_model.best_complexity, 2):,}')
    print(f'5-CV logloss = {-round(HYBparsimony_model.best_score,6)}')
    print(f'logloss test = {round(log_loss(y_test, preds),6)}')


    # ------------------------------------------------------------
 
    input("\nNext example: 'Using different classification algorithms'.\nPress a key to continue...")
    os.system('clear')

    ###########################################################
    #         Use different classification algorithms         #
    ###########################################################
    
    algorithms_clas = ['LogisticRegression', 'MLPClassifier', 
                        'SVC', 'DecisionTreeClassifier',
                        'RandomForestClassifier', 'KNeighborsClassifier',
                        ]
    res = []
    for algo in algorithms_clas:
        print('#######################')
        print('Searching best: ', algo)
        HYBparsimony_model = HYBparsimony(algorithm=algo,
                                        features=breast_cancer.feature_names,
                                        rerank_error=0.005,
                                        maxiter=2, # extend to more iterations (time consuming)
                                        # cv=RepeatedKFold(n_splits=5, n_repeats=10), #uncomment to improve validation (time consuming)
                                        # n_jobs=20, # each job executes one fold
                                        verbose=1)
        # Search the best hyperparameters and features 
        # (increasing 'time_limit' to improve neg_log_loss with high consuming algorithms)
        HYBparsimony_model.fit(X_train, y_train, time_limit=60.0)
        # Check results with test dataset
        preds = HYBparsimony_model.predict_proba(X_test)[:,1]
        print(algo, "Logloss_Test=", round(log_loss(y_test, preds),6))
        print('Selected features:',HYBparsimony_model.selected_features)
        print(HYBparsimony_model.best_model)
        print('#######################')
        # Append results
        res.append(dict(algo=algo,
                        Logloss_10R5CV= -round(HYBparsimony_model.best_score,6),
                        Logloss_Test = round(log_loss(y_test, preds),6),
                        NFS=int(HYBparsimony_model.best_complexity//1e9),
                        selected_features = HYBparsimony_model.selected_features,
                        best_model=HYBparsimony_model.best_model))
    res = pd.DataFrame(res).sort_values('Logloss_Test')
    res.to_csv('res_models_class.csv')
    # Visualize results
    print(res[['algo', 'Logloss_10R5CV', 'Logloss_Test', 'NFS']])

    # ------------------------------------------------------------

    input("\nNext example: 'Multiclass classification'.\nPress a key to continue...")
    os.system('clear')
    
    ###############################################################
    #                   MULTICLASS CLASSIFICATION                 #
    ###############################################################
    import pandas as pd
    import numpy as np
    import os
    from sklearn.model_selection import train_test_split, RepeatedKFold
    from sklearn.preprocessing import StandardScaler
    from sklearn.datasets import load_wine
    from sklearn.metrics import f1_score
    from hybparsimony import HYBparsimony

    # load 'wine' dataset 
    wine = load_wine()
    X, y = wine.data, wine.target 
    print(X.shape)
    # 3 classes
    print(len(np.unique(y)))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=1)

    # Standarize X and y (some algorithms require that)
    scaler_X = StandardScaler()
    X_train = scaler_X.fit_transform(X_train)
    X_test = scaler_X.transform(X_test)

    HYBparsimony_model = HYBparsimony(features=wine.feature_names,
                                    cv=RepeatedKFold(n_splits=5, n_repeats=10),
                                    npart = 20,
                                    early_stop=20,
                                    rerank_error=0.001,
                                    n_jobs=10, #Use 10 cores (1 core runs 1 fold)
                                    verbose=1)
    HYBparsimony_model.fit(X_train, y_train, time_limit=5.0)
    preds = HYBparsimony_model.predict(X_test)
    print(f'\n\nBest Model = {HYBparsimony_model.best_model}')
    print(f'Selected features:{HYBparsimony_model.selected_features}')
    print(f'Complexity = {round(HYBparsimony_model.best_complexity, 2):,}')
    print(f'10R5-CV f1_macro = {round(HYBparsimony_model.best_score,6)}')
    print(f'f1_macro test = {round(f1_score(y_test, preds, average="macro"),6)}')

    # ------------------------------------------------------------

    input("\nNext example: 'Custom Evaluation: A. Using accuracy'.\nPress a key to continue...")
    os.system('clear')

    ###################################################
    #                   CUSTOM EVALUATION             #
    ###################################################

    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.datasets import load_breast_cancer, load_wine
    from sklearn.model_selection import cross_val_score, RepeatedKFold
    from hybparsimony import HYBparsimony
    from sklearn.metrics import fbeta_score, make_scorer, cohen_kappa_score, log_loss, accuracy_score
    import os


    # load 'breast_cancer' dataset
    breast_cancer = load_breast_cancer()
    X, y = breast_cancer.data, breast_cancer.target 
    print(X.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=1)

    # Standarize X and y (some algorithms require that)
    scaler_X = StandardScaler()
    X_train = scaler_X.fit_transform(X_train)
    X_test = scaler_X.transform(X_test)

    # #Example A: Using 10 folds and 'accuracy'
    # ----------------------------------------
    HYBparsimony_model = HYBparsimony(features=breast_cancer.feature_names,
                                    scoring='accuracy',
                                    cv=10,
                                    n_jobs=10, #Use 10 cores (1 core run 1 fold)
                                    rerank_error=0.001,
                                    verbose=1)

    HYBparsimony_model.fit(X_train, y_train, time_limit=0.1)
    preds = HYBparsimony_model.predict(X_test)
    print(f'\n\nBest Model = {HYBparsimony_model.best_model}')
    print(f'Selected features:{HYBparsimony_model.selected_features}')
    print(f'Complexity = {round(HYBparsimony_model.best_complexity, 2):,}')
    print(f'10R5-CV Accuracy = {round(HYBparsimony_model.best_score,6)}')
    print(f'Accuracy test = {round(accuracy_score(y_test, preds),6)}')



    input("\nNext example: 'Custom Evaluation: B: Using 10-repeated 5-fold CV and 'Kappa' score'.\nPress a key to continue...")
    os.system('clear')

    #Example B: Using 10-repeated 5-fold CV and 'Kappa' score
    # -------------------------------------------------------
    # load 'wine' dataset 
    wine = load_wine()
    X, y = wine.data, wine.target 
    print(X.shape)
    # 3 classes
    print(len(np.unique(y)))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=1)

    # Standarize X and y (some algorithms require that)
    scaler_X = StandardScaler()
    X_train = scaler_X.fit_transform(X_train)
    X_test = scaler_X.transform(X_test)


    metric_kappa = make_scorer(cohen_kappa_score, greater_is_better=True)
    HYBparsimony_model = HYBparsimony(features=wine.feature_names,
                                    scoring=metric_kappa,
                                    cv=RepeatedKFold(n_splits=5, n_repeats=10),
                                    n_jobs=10, #Use 10 cores (one core=one fold)
                                    rerank_error=0.001,
                                    verbose=1)
    HYBparsimony_model.fit(X_train, y_train, time_limit=0.1)
    print(f'\n\nBest Model = {HYBparsimony_model.best_model}')
    print(f'Selected features:{HYBparsimony_model.selected_features}')



    input("\nNext example: 'Custom Evaluation: C: Using a weighted log_loss'.\nPress a key to continue...")
    os.system('clear')

    #Example C: Using a weighted 'log_loss'
    # -------------------------------------
    # Assign a double weight to class one
    def my_custom_loss_func(y_true, y_pred):
        sample_weight = np.ones_like(y_true)
        sample_weight[y_true==1] = 2.0
        return log_loss(y_true, y_pred, sample_weight=sample_weight)

    # load 'breast_cancer' dataset
    breast_cancer = load_breast_cancer()
    X, y = breast_cancer.data, breast_cancer.target 
    print(X.shape)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=1)

    # Standarize X and y (some algorithms require that)
    scaler_X = StandardScaler()
    X_train = scaler_X.fit_transform(X_train)
    X_test = scaler_X.transform(X_test)

    # Lower is better and 'log_loss' needs probabilities
    custom_score = make_scorer(my_custom_loss_func, greater_is_better=False, needs_proba=True)
    HYBparsimony_model = HYBparsimony(features=breast_cancer.feature_names,
                                    scoring=custom_score,
                                    rerank_error=0.001,
                                    verbose=1)
    HYBparsimony_model.fit(X_train, y_train, time_limit=0.20)
    print(f'\n\nBest Model = {HYBparsimony_model.best_model}')
    print(f'Selected features:{HYBparsimony_model.selected_features}')



    input("\nNext example: 'Custom Evaluation:  D: Using a 'custom evaluation' function'.\nPress a key to continue...")
    os.system('clear')

    # Example D: Using a 'custom evaluation' function
    # -----------------------------------------------
    def custom_fun(estimator, X, y):
        return cross_val_score(estimator, X, y, scoring="accuracy", n_jobs=10)

    HYBparsimony_model = HYBparsimony(features=breast_cancer.feature_names,
                                    custom_eval_fun=custom_fun,
                                    rerank_error=0.001,
                                    verbose=1)


    HYBparsimony_model.fit(X_train, y_train, time_limit=0.20)
    preds = HYBparsimony_model.predict(X_test)
    print(f'\n\nBest Model = {HYBparsimony_model.best_model}')
    print(f'Selected features:{HYBparsimony_model.selected_features}')
    print(f'Complexity = {round(HYBparsimony_model.best_complexity, 2):,}')
    print(f'10R5-CV Accuracy = {round(HYBparsimony_model.best_score,6)}')
    print(f'Accuracy test = {round(accuracy_score(y_test, preds),6)}')


    # ------------------------------------------------------------

    input("\nNext example: 'Custom Search'.\nPress a key to continue...")
    os.system('clear')
    
    ###################################################
    #                   CUSTOM SEARCH                 #
    ###################################################

    import pandas as pd
    import numpy as np
    import os
    from sklearn.model_selection import train_test_split, RepeatedKFold
    from sklearn.neural_network import MLPRegressor
    from sklearn.metrics import mean_squared_error
    from sklearn.datasets import load_diabetes
    from sklearn.preprocessing import StandardScaler
    from hybparsimony import HYBparsimony, Population
    

    # Load 'diabetes' dataset
    diabetes = load_diabetes()

    X, y = diabetes.data, diabetes.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1234)

    # Standarize X and y
    scaler_X = StandardScaler()
    X_train = scaler_X.fit_transform(X_train)
    X_test = scaler_X.transform(X_test)
    scaler_y = StandardScaler()
    y_train = scaler_y.fit_transform(y_train.reshape(-1,1)).flatten()
    y_test = scaler_y.transform(y_test.reshape(-1,1)).flatten()

    def mlp_new_complexity(model, nFeatures, **kwargs):
        weights = [np.concatenate(model.intercepts_)]
        for wm in model.coefs_:
            weights.append(wm.flatten())
        weights = np.concatenate(weights) 
        int_comp = np.min((1E09-1,np.sum(weights**2)))
        return nFeatures*1E09 + int_comp

    MLPRegressor_new = {"estimator": MLPRegressor, # The estimator
                  "complexity": mlp_new_complexity, # The complexity
                  "hidden_layer_sizes": {"range": (1, 5), "type": Population.INTEGER},
                  "alpha": {"range": (-5, 5), "type": Population.POWER},
                  "solver": {"value": "adam", "type": Population.CONSTANT},
                  "learning_rate": {"value": "adaptive", "type": Population.CONSTANT},
                  "early_stopping": {"value": True, "type": Population.CONSTANT},
                  "validation_fraction": {"value": 0.10, "type": Population.CONSTANT},
                  "activation": {"value": "tanh", "type": Population.CONSTANT},
                  "n_iter_no_change": {"value": 20, "type": Population.CONSTANT},
                  "tol": {"value": 1e-5, "type": Population.CONSTANT},
                  "random_state": {"value": 1234, "type": Population.CONSTANT},
                  "max_iter": {"value": 200, "type": Population.CONSTANT}
                   }
    HYBparsimony_model = HYBparsimony(algorithm=MLPRegressor_new,
                                    features=diabetes.feature_names,
                                    cv=RepeatedKFold(n_splits=5, n_repeats=10),
                                    n_jobs= 25, #Use 25 cores (one core=one fold)
                                    maxiter=2, # Extend to more generations (time consuming)
                                    npart = 10,
                                    rerank_error=0.001,
                                    verbose=1)

    # Search the best hyperparameters and features 
    # (increasing 'time_limit' to improve RMSE with high consuming algorithms)
    HYBparsimony_model.fit(X_train, y_train, time_limit=1.00)
    preds = HYBparsimony_model.predict(X_test)
    print(f'\n\nBest Model = {HYBparsimony_model.best_model}')
    print(f'Selected features:{HYBparsimony_model.selected_features}')
    print(f'Complexity = {round(HYBparsimony_model.best_complexity, 2):,}')
    print(f'5-CV MSE = {-round(HYBparsimony_model.best_score,6)}')
    print(f'RMSE test = {round(mean_squared_error(y_test, preds, squared=False),6)}')
    

    # ------------------------------------------------------------
    
    input("\nNext example: 'Check getFitness() and fitness_for_parallel()'.\nPress a key to continue...")
    os.system('clear')
    
    ###################################################
    # Check getFitness() and fitness_for_parallel()   #
    ###################################################

    import pandas as pd
    import numpy as np
    from sklearn.datasets import load_breast_cancer
    from sklearn.svm import SVC
    from sklearn.model_selection import cross_val_score
    from hybparsimony import HYBparsimony
    from hybparsimony.util import getFitness, svm_complexity, population
    from hybparsimony.util.fitness import fitness_for_parallel
    import os
    # load 'breast_cancer' dataset
    breast_cancer = load_breast_cancer()
    X, y = breast_cancer.data, breast_cancer.target
    chromosome = population.Chromosome(params = [1.0, 0.2],
                                       name_params = ['C','gamma'],
                                       const = {'kernel':'rbf'},
                                       cols= np.random.uniform(size=X.shape[1])>0.50,
                                       name_cols = breast_cancer.feature_names)
    # print(getFitness(SVC,svm_complexity)(chromosome, X=X, y=y))
    print(fitness_for_parallel(SVC, svm_complexity, 
                               custom_eval_fun=cross_val_score,
                               cromosoma=chromosome, X=X, y=y))

    # ------------------------------------------------------------



    input("\nNext example: 'Custom Fitness Function:  Using Autogluon (more info see Autogluon_with_SHDD.ipynb)'.\nPress a key to continue...")
    os.system('clear')
    
    ###################################################
    #          USE CUSTOM FITNESS FUNCTION            #
    #        (see Autogluon_with_SHDD.ipynb)          #
    ###################################################
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.datasets import load_breast_cancer
    from sklearn.metrics import log_loss
    from hybparsimony import HYBparsimony
    from autogluon.tabular import TabularDataset, TabularPredictor
    from hybparsimony import util
    import openml
    import os
    
    def fitness_custom(cromosoma, **kwargs):
        global label

        X_train = kwargs["X"]
        y_train = kwargs["y"]
            
        # Extract features from the original DB plus response (last column)
        X_fs_selec = X_train.loc[: , cromosoma.columns]
        # Get 20% for validation
        x_train_custom, x_test_custom, y_train_custom, y_test_custom = train_test_split(X_fs_selec, 
                                                                                        y_train, 
                                                                                        test_size=0.20, 
                                                                                        shuffle=True, 
                                                                                        random_state=0)
        X_train_df = pd.DataFrame(np.hstack([x_train_custom, y_train_custom.reshape(-1,1).astype(int)]))
        X_train_df.columns = list(X_fs_selec.columns)+[label]
        X_test_df = pd.DataFrame(x_test_custom)
        predictor = TabularPredictor(label=label, eval_metric='log_loss', verbosity=0).fit(X_train_df, time_limit=time_autogluon)
        y_pred = predictor.predict_proba(X_test_df)
        fitness_val = -log_loss(y_true=y_test_custom, y_pred=y_pred)
        return np.array([fitness_val, np.sum(cromosoma.columns)]), predictor


    # Get COIL2000 datasetm from openml

    dataset = openml.datasets.get_dataset('COIL2000')
    label = dataset.default_target_attribute
    X_orig, y_orig, _, _ = dataset.get_data(dataset_format="dataframe", target=label)
    input_names = X_orig.columns
    print(X_orig.shape)

    # Use 50% for train/validation and 50% for testing
    train_data, test_data, y_train, y_test = train_test_split(X_orig, 
                                                            y_orig, 
                                                            test_size=0.50, 
                                                            shuffle=True, 
                                                            random_state=0)
    train_data = train_data.reset_index(drop=True)
    test_data = test_data.reset_index(drop=True)
    time_autogluon = 150 # in seconds

    # Train with features
    train_data[label] = y_train.values
    HYBparsimony_model = HYBparsimony(fitness=fitness_custom,
                                    features=input_names,
                                    rerank_error=0.001,
                                    gamma_crossover=0.50,
                                    seed_ini=0,
                                    npart=15,
                                    maxiter=2, # Extend to 100 generations (time consuming)
                                    early_stop=20,
                                    verbose=1,
                                    n_jobs=1)
    HYBparsimony_model.fit(train_data[input_names], train_data[label].values)
    best_model_probsfeats = HYBparsimony_model.best_model_conf[-len(input_names):]
    selec_feats = np.array(input_names)[best_model_probsfeats>=0.50]
    print(f'Selected feats with HYB-PARSIMONY num={len(selec_feats)}:{selec_feats}')
    print('######################################################')

    input("\nPress a key to continue...")
    os.system('clear')