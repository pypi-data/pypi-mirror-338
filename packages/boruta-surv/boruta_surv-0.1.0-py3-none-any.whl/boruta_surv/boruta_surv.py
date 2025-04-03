import numpy as np
import pandas as pd
import scipy as sp
from sklearn.model_selection import train_test_split
from sklearn.inspection import permutation_importance
from sksurv.ensemble import RandomSurvivalForest
import seaborn as sns
from matplotlib import pyplot as plt

def get_tail_items(pmf, alpha):
    """Finds the index at which the cumulative probability mass function (PMF) reaches at least alpha."""
    total = 0
    for i, x in enumerate(pmf):
        total += x
        if total >= alpha:
            return i
    return len(pmf) - 1

def choose_features(hits, trials, thresh):
    """Categorizes features into green and blue zones based on hit thresholds."""
    important_features_thresh = trials - thresh
    tentative_features_upper = important_features_thresh
    tentative_features_lower = thresh
    
    important_features = [key for key, value in hits.items() if value >= important_features_thresh]
    tentative_features = [key for key, value in hits.items() if tentative_features_lower <= value < tentative_features_upper]
    
    return important_features, tentative_features

def boruta_rsf(
    X, y, trials, random_state=None, split=False, test_size = 0.2, n_estimators=10, max_depth=5,
    min_samples_split=10, min_samples_leaf=15, alpha = 0.05, verbose = False
):
    """Performs Boruta feature selection using a Random Survival Forest."""
    
    hits = np.zeros(len(X.columns))
    shadow_feat_names = [f'shadow_{feat}' for feat in X.columns]
    all_feat_names = X.columns.to_list() + shadow_feat_names
    importances = pd.DataFrame(index=np.arange(trials), columns=all_feat_names)

    # Define structured dtype and convert to NumPy structured array
    dt = np.dtype([('Status', '?'), ('Survival_in_days', '<f8')])
    y = np.array(y)
    y = np.array(list(zip(y[:, 1].astype(bool), y[:, 0].astype(float))), dtype=dt)
    
    for i in range(trials):
        if verbose:
            print(f'Starting trial {i + 1}')

        # Set different seed for each Trial
        if random_state:
            random_state_trial = random_state + i
            np.random.seed(random_state_trial)
        else:
            random_state_trial = None

        if not split:
            X_shadow = X.apply(np.random.permutation)
            X_shadow.columns = shadow_feat_names
            X_boruta = pd.concat([X, X_shadow], axis=1)
            
            rsf = RandomSurvivalForest(
                n_estimators=n_estimators, max_depth=max_depth,
                min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf,
                random_state=random_state_trial
            )
            rsf.fit(X_boruta, y)
            results = permutation_importance(rsf, X_boruta, y, n_repeats=1, n_jobs=None, random_state=random_state_trial)
        else:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state_trial)
            
            X_shadow_train = X_train.apply(np.random.permutation)
            X_shadow_test = X_test.apply(np.random.permutation)
            X_shadow_train.columns = shadow_feat_names
            X_shadow_test.columns = shadow_feat_names
            
            X_boruta_train = pd.concat([X_train, X_shadow_train], axis=1)
            X_boruta_test = pd.concat([X_test, X_shadow_test], axis=1)
            
            rsf = RandomSurvivalForest(
                n_estimators=n_estimators, max_depth=max_depth,
                min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf,
                random_state=random_state_trial
            )
            rsf.fit(X_boruta_train, y_train)
            results = permutation_importance(rsf, X_boruta_test, y_test, n_repeats=1, n_jobs=None, random_state=random_state_trial)
        
        feat_imp = results['importances']
        feat_imp_X = feat_imp[:len(X.columns), 0]
        feat_imp_shadow = feat_imp[len(X.columns):, 0]
        
        # If feature importance is higher than the max shadow feature importance then count as a hit
        hits += (feat_imp_X > feat_imp_shadow.max())
        importances.loc[i] = feat_imp.T
    
    hits = {feat_name: total_hits for feat_name, total_hits in zip(X.columns, hits)}
    pmf = [sp.stats.binom.pmf(x, trials, 0.5) for x in range(trials + 1)]
    thresh = get_tail_items(pmf, alpha)
    important_features, tentative_features = choose_features(hits, trials, thresh)
    
    return important_features, tentative_features, importances, hits

def plot_feature_importances(X, importances, important_features, tentative_features):
    fig, ax = plt.subplots(figsize=(8, 10))  # Create figure and axis
    
    # Separate df into original features and shadow features
    importances_ = importances.iloc[:, :len(X.columns)].copy()
    importances_shadows = importances.iloc[:, len(X.columns):].copy()
    
    # Store shadowMin, shadowMax, and shadowMean in importances_
    shadowmin_name = importances_shadows.columns[importances_shadows.mean().argmin()]
    shadowmax_name = importances_shadows.columns[importances_shadows.mean().argmax()]
    importances_['shadowMin'] = importances_shadows[shadowmin_name]
    importances_['shadowMax'] = importances_shadows[shadowmax_name]
    importances_['shadowMean'] = importances_shadows.mean(axis=1)
    
    # Organize color palette based on importance zones
    pal = {var: 'green' if var in important_features 
           else 'b' if var in tentative_features 
           else 'gray' if 'shadow' in var  
           else 'r' for var in importances_.columns}
    
    # Create boxplot of feature importances in descending order
    sns.boxplot(data=importances_[importances_.median().sort_values(ascending=False).index], 
                orient="h", palette=pal, ax=ax)
    ax.set_xlabel('Feature Importance')
    
    return fig, ax  # Return figure and axis for future modifications