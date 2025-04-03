[![MMM-Fair Logo](https://raw.githubusercontent.com/arjunroyihrpa/MMM_fair/main/images/mmm-fair.png)](https://github.com/arjunroyihrpa/MMM_fair)

### MMM-Fair is a multi-objective, fairness-aware boosting classifier originally inspired by the paper: "Multi-fairness Under Class-Imbalance"
https://link.springer.com/chapter/10.1007/978-3-031-18840-4_21

--- 

The original algorithm targeted Equalized Odds (a.k.a. Disparate Mistreatment). This MMM-Fair implementation generalizes to multiple fairness objectives:

•	Demographic Parity (DP)

•	Equal Opportunity (EP)

•	Equalized Odds (EO)

#### We further improve the approach by:

1.	Flexible Base Learners: Any scikit-learn estimator (e.g. DecisionTreeClassifier, LogisticRegression, ExtraTreeClassifier, etc.) can be used as the base learner.
2.	Fairness-Weighted Alpha: The boosting weight (alpha) accounts for fairness metrics alongside classification error.
3.	Dynamic Handling of Over-Boosted Samples: Reduces excessive emphasis on specific samples once fairness goals are partially met.
4.  Gradient Boosted Tree version 


#### Two Approaches: AdaBoost-Style vs. Gradient-Boosted Trees
We provide two main classifiers:

1.	MMM_Fair (Original Adaptive Boosting version)
2.	MMM_Fair_GradientBoostedClassifier (Histogram-based Gradient Boosting approach)

Both handle multi-objective, multi-attribute, and multi-type fairness constraints (DP, EP, EO) but differ in how they perform the boosting internally. You can choose via the command line argument --classifier MMM_Fair or --classifier MMM_Fair_GBT.

---

## Installation
```bash
pip install mmm-fair
```
Requires Python 3.11+.

Dependencies: numpy, scikit-learn, tqdm, pymoo, pandas, ucimlrepo, skl2onnx, etc.

---
## Usage
The mmm-fair package provides two different usage possibilities. One is a chat based on a web-based UI (specially tailored new user, with even non-technical abckground), and the other is command line based (for ML scientist, engineers, etc.)

### Usage Overview (mmm-chat)
Right now its still terminal dependent (soon will release a destop app). So after installing one needs to bash
```bash
mmm-fair-chat
```
and then in any browser copy paste:
```bash
http://127.0.0.1:5000
```
Then start chating with the interactive web app to get your MMM-Fair AI model.

## Usage Overview (AdaBoost-Style)

You can import and use MMM-Fair (original version):
```python
from mmm_fair import MMM_Fair 
from sklearn.tree import DecisionTreeClassifier
```

### Suppose you have X (features), y (labels)
### 
```python
mmm = MMM_Fair(
estimator=DecisionTreeClassifier(max_depth=5),
constraints="EO",        # or "DP", "EP"
n_estimators=1000,
saIndex=...,            # shape (n_samples, n_protected)
saValue=...,            # dictionary {'prot_att_column_name': prot value}
random_state=42,
# other parameters, e.g. gamma, saIndex, saValue...
)

mmm.fit(X, y)
preds = mmm.predict(X_test)
```
### Fairness Constraints

•	constraints="DP" → Demographic Parity

•	constraints="EP" → Equal Opportunity

•	constraints="EO" → Equalized Odds

###

In all cases, pass the relevant saIndex (sensitive attribute array) and saValue (dictionary of protected group mappings) to MMM_Fair if you want it to track fairness for different protected attributes.

---

## Usage Overview (Gradient-Boosted Trees)

We also provide MMM_Fair_GradientBoostedClassifier. This uses a histogram-based gradient boosting approach (similar to HistGradientBoostingClassifier) but includes a custom fairness loss to train and then multi-objective post-processing step to select the best pareto-optimal ensemble round. Example:

```python
from mmm_fair import MMM_Fair_GradientBoostedClassifier

clf = MMM_Fair_GradientBoostedClassifier(
    constraint="EO",        # or "DP", "EP"
    alpha=0.1,              # fairness weight
    saIndex=...,            # shape (n_samples, n_protected)
    saValue=...,            # dictionary or None
    max_iter=100,
    random_state=42,
    ## any other arguments that the HistGradientBoostingClassifier from sklearn can handle
)
clf.fit(X, y)
preds = clf.predict(X_test)
```

## 📥 In-built Data Loader for UCI Datasets

MMM-Fair includes utility functions to seamlessly work with datasets from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/datasets).

### 🔧 Load a UCI dataset (e.g. Adult dataset)
```python
from mmm_fair import data_uci
from mmm_fair import build_sensitives

# Load dataset with target column
data = data_uci(dataset_name="Adult", target="income")
```
### 🛡️ Define Sensitive Attributes
```python
saIndex, saValue = build_sensitives(
    data.data,
    protected_cols=["race", "sex"],
    non_protected_vals=["White", "Male"]
)
```

### 🔀 Optional: Use with Train/Test Split
```python
from sklearn.model_selection import train_test_split
import numpy as np

X = data.to_pred(sensitive=["race", "sex"])
y = data.labels["label"].to_numpy()
indices = np.arange(len(X))

X_train, X_test, y_train, y_test, id_train, id_test = train_test_split(
    X, y, indices, test_size=0.3, random_state=42, stratify=y
)

# Rebuild fairness attributes for the split sets
saIndex_train, saValue_train = build_sensitives(
    data.data.iloc[id_train], ["race", "sex"], ["White", "Male"]
)
saIndex_test, _ = build_sensitives(
    data.data.iloc[id_test], ["race", "sex"], ["White", "Male"]
)
```

#### ✅ saIndex is a binary matrix (0 = protected, 1 = non-protected)
#### ✅ saValue is a dictionary indicating protected status, e.g., {"race": 0, "sex": 0}
---

## Train & Deploy Script

This package provides a train_and_deploy.py script. It:
1.	Loads data (from a known UCI dataset or a local CSV).
2.	Specifies fairness constraints, protected attributes, and base learner.
3.	Selects either the original MMM_Fair or the new MMM_Fair_GradientBoostedClassifier via --classifier MMM_Fair or --classifier MMM_Fair_GBT.
4.	Trains with your chosen hyperparameters.
5.	Optionally deploys the model in ONNX or pickle format.

### Key Arguments
	•	--classifier: MMM_Fair (original boosting) or MMM_Fair_GBT (gradient-based).
	•	--constraint: e.g., DP, EP, EO.
	•	--n_learners: Number of estimators (for either version).
	•	--pos_Class: Specify the positive class label if needed.
	•	--early_stop: True or False, relevant for the GBT approach to enable scikit-learn’s early stopping.
	•	--base_learner: E.g. tree, lr, logistic, etc. (for the original MMM_Fair).
	•	--deploy: 'onnx' or 'pickle'.
	•	--moo_vis True: Optionally visualize multi-objective (3D) plots (accuracy, class-imbalance, multi-fairness) after training, opening a local HTML page with interactive charts.


### Example command:
#### 1. Original AdaBoost MMM_Fair:
[using UCI library](https://archive.ics.uci.edu)
```bash
python -m mmm_fair.train_and_deploy \
  --dataset Adult \
  --prots race sex \
  --nprotgs White Male \
  --constraint EO \
  --base_learner Logistic \
  --deploy onnx \
  --moo_vis True
```
[using local "csv" data](https://docs.python.org/3/library/csv.html)
```bash
python -m mmm_fair.train_and_deploy \
  --dataset mydata.csv \
  --target label_col \
  --prots prot_1 prot_2 prot_3 \
  --nprotgs npg1 npg2 npg3 \
  --constraint EO \
  --base_learner tree \
  --deploy onnx
```
#### 2. Gradient-Boosted MMM_Fair_GBT:
```bash
python -m mmm_fair.train_and_deploy \
  --classifier MMM_Fair_GBT \
  --dataset mydata.csv \
  --target label_col \
  --prots prot_1 prot_2 \
  --nprotgs npg1 npg2 \
  --constraint DP \
  --alpha 0.5 \
  --early_stop True \
  --n_learners 100 \
  --deploy pickle \
  --moo_vis True
```

#### Note: 
1. Setting --moo_vis True triggers an interactive local HTML page for exploring the multi-objective trade-offs in 3D plots (accuracy vs. class-imbalance vs. fairness, etc.).
2. Currently the fairness intervention only implemented for categorical groups. So if protected attribute is numerical e.g. "age" then for non-protected value i.e. --nprotgs provide a range like 30_60 as argument. 

---

### Additional options

If you want to select the best theta from only the Pareto optimal ensembles set (default is False and selects applies the post-processing to all set of solutions):   

    --pareto True

If you want to provide test data:  

    --test 'your_test_file.csv'
    
Or just test split:  

    --test 0.3
    
If you want change style (default is table, choose from {table, console}) of report displayed ([Check FairBench Library for more details](https://fairbench.readthedocs.io/material/visualization/)):

    --report_type Console


**When deploying with 'onnx'**, we change the models to ONNX file(s), and store additional parameters in a model_params.npy. This gets zipped into a .zip archive for distribution/analysis.

---

### MAMMOth Toolkit Integration

For the bias exploration using [MAMMOth](https://mammoth-ai.eu) pipeline it is really important to select 'onnx' as the '--deploy' argument. The [ONNX](https://onnxruntime.ai) model accelerator and model_params.npy are used to integrate with the [MAMMOth-toolkit](https://github.com/mammoth-eu/mammoth-toolkit-releases) or the demonstrator app from the [mammoth-commons](https://github.com/mammoth-eu/mammoth-toolkit-releases) project.


### By providing the .zip archive, you can:

    •	Upload it to MAMMOth,
    
    •	Examine bias and performance metrics across subgroups,
    
    •	Compare fairness trade-offs with a user-friendly interface.

---

### Example Workflow
1.	**Choose** Fairness Constraint: e.g., DP, EO, or EP.
2.	**Define** sensitive attributes in saIndex and the protected-group condition in saValue.
3.	**Pick** base learner (e.g., DecisionTreeClassifier(max_depth=5)) or gradient-based approach.
4.	**Train** with a large number of estimators (n_estimators=300 or max_iter=300).
5.	**Optionally** do partial ensemble selection with update_theta(criteria="all") or update_theta(criteria="fairness") .
6.	**Export** to ONNX or pickle for downstream usage.
7.  **Use** --moo_vis True to open local multi-objective 3D plots for deeper analysis.
8.  **Upload** the .zip file (if exported to onnx) to MAMMOth for bias exploration.

---

### References

“[Multi-Fairness Under Class-Imbalance](https://link.springer.com/chapter/10.1007/978-3-031-18840-4_21),”  Roy, Arjun, Vasileios Iosifidis, and Eirini Ntoutsi. International Conference on Discovery Science. Cham: Springer Nature Switzerland, 2022.

#### Maintainer: Arjun Roy (arjunroyihrpa@gmail.com)

#### Contributors: Swati Swati (swati17293@gmail.com)

### 🏛️ Funding

MMM-Fair is a research-driven project supported by several public funding initiatives. We gratefully acknowledge the generous support of:

<p align="center">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://bias-project.org/wp-content/themes/wp-bootstrap-starter/images/Bias_Logo.svg" alt="bias-logo" width="120" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://mammoth-ai.eu/wp-content/uploads/2022/09/mammoth.svg" alt="mammoth-logo" width="150" style="margin: 0 20px"/>
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="https://stelar-project.eu/wp-content/uploads/2022/08/cropped-stelar-sq.png" alt="stelar-logo" width="100" />
</p>

<p align="center">
  <a href="https://bias-project.org"><strong>Volkswagen Foundation – BIAS</strong></a> &nbsp;&nbsp;&nbsp;
  <a href="https://mammoth-ai.eu"><strong>EU Horizon – MAMMOth</strong></a> &nbsp;&nbsp;&nbsp;
  <a href="https://stelar-project.eu"><strong>EU Horizon – STELAR</strong></a>
</p>


### License & Contributing

This project is released under [Apache License Version 2.0].
Contributions are welcome—please open an issue or pull request on GitHub.

### Contact

For questions or collaborations, please contact [arjun.roy@unibw.de](mailto:arjun.roy@unibw.de) 
Check out the source code at: [GITHUB](https://github.com/arjunroyihrpa/MMM_fair).