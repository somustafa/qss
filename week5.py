import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(r"C:\Users\UniSoft PC\Downloads\heart.csv")
X = df.drop('target', axis=1)
y = df['target']

scaler = StandardScaler() #miqyaslasdirma- butun sutunlar eyni olcude olur,alqoritm daha duzgun muqayise aparir
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


models = {
    "Logistic Regression": LogisticRegression(),
    "Naive Bayes": GaussianNB(),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators=100),
    "SVM (Linear)": SVC(kernel='linear'),
    "SVM (RBF)": SVC(kernel='rbf')
}
results =  []
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds)
    results.append({'Model': name, 'Accuracy': acc, 'F1 Score': f1})
    print(f"\n📌 {name}")
    print(classification_report(y_test, preds))


results_df = pd.DataFrame(results).sort_values(by="F1 Score", ascending=False)
plt.figure(figsize=(10, 5))
sns.barplot(data=results_df, x="Model", y="F1 Score", palette="viridis")
plt.title("Model Müqayisəsi – F1 Score üzrə")
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.tight_layout()
#plt.show()


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

import pandas as pd

df = pd.read_csv(r"C:\Users\UniSoft PC\Downloads\income_evaluation.csv")

# Sütun adlarındakı boşluqları təmizlə
df.columns = df.columns.str.strip()

print(df.columns.tolist())

useful_columns = [
    'age', 'workclass', 'education-num', 'marital-status',
    'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'income'
]

df = df[useful_columns]


# 3. Boş və ya "?" olan dəyərləri təmizlə
df = df.replace('?', pd.NA)
df = df.dropna()

# 4. Target və feature-ları ayır
X = df.drop('income', axis=1)
y = df['income']

# 5. Kategoriyaları Label Encoding ilə ədədi formata çevir
le_dict = {}
for col in X.select_dtypes(include='object').columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    le_dict[col] = le  # lazım ola bilər, saxlayırıq

# Target-i də encode edək (<=50K = 0, >50K = 1)
y = y.apply(lambda x: 0 if x.strip() == '<=50K' else 1)

# 6. Train/test bölmə
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 7. Model qur və öyrət
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 8. Proqnoz ver
y_pred = model.predict(X_test)

# 9. Nəticələri çap et
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


