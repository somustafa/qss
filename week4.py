import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


#Case Study: COVID-19 Data Analysis and Prediction

df = pd.read_csv(r"C:\Users\UniSoft PC\Downloads\Python-20250804T063909Z-1-001\Python\covid_19_data.csv")
df['ObservationDate'] = pd.to_datetime(df['ObservationDate']) # tarix sutununu formatladiq
df_global = df.groupby('ObservationDate')[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
df_global['Infected'] = df_global['Confirmed'] - df_global['Deaths'] - df_global['Recovered']
df_global['Days'] = (df_global['ObservationDate'] - df_global['ObservationDate'].min()).dt.days

#bunlar modelden evvel elediklerimizdir. umumi say tapdiq sonra olenleri ve sagalnlari cixdiq ki infected tapilsin. sonra lkinear regression tarxilerle isleye bilmir dete gunleri goturduk 
#her tarixden erken tarixi cixir
#Model merhelesi. 

X = df_global[['Days']]
models = {}
targets = ['Confirmed', 'Deaths', 'Recovered', 'Infected']

for target in targets:
    y = df_global[[target]]
    model = LinearRegression()
    model.fit(X, y)
    models[target] = model

last_day = df_global['Days'].max()
future_days = np.array([last_day + i for i in range(1, 8)]).reshape(-1, 1)

predictions = {}
for target in targets:
    predictions[target] = models[target].predict(future_days).flatten()

future_dates = [df_global['ObservationDate'].max() + timedelta(days=i) for i in range(1, 8)]

prediction_df = pd.DataFrame({
    'Date': future_dates,
    'Confirmed': predictions['Confirmed'],
    'Deaths': predictions['Deaths'],
    'Recovered': predictions['Recovered'],
    'Infected': predictions['Infected']
})

print(prediction_df)

for target in targets:
    plt.figure(figsize=(8, 4))
    plt.plot(df_global['ObservationDate'], df_global[target], label='Actual')
    plt.plot(prediction_df['Date'], prediction_df[target], label='Predicted', linestyle='--')
    plt.title(f'{target} - 7 günlük proqnoz')
    plt.xlabel('Tarix')
    plt.ylabel(target)
    plt.legend()
    plt.grid(True)
    plt.show()


#Homework
df1 = pd.read_csv(r"C:\Users\UniSoft PC\Downloads\Python-20250804T063909Z-1-001\Python\USA_Housing.csv")

# 2. Lazımsız sütunu (Address) çıxardırıq, çünki qiymətə təsir etmir
X = df1.drop(['Price', 'Address'], axis=1)
y = df1['Price']

# 3. Məlumatları train və test hissələrinə bölürük
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train) #train oyredirik 

y_pred = model.predict(X_test)

# 6. Qiymətləndirmə: Səhv dərəcələrini hesablayırıq
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# 7. Nəticələri çap edirik
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("Ortalama qiymət:", y.mean())

# 8. Həqiqi və proqnoz qiymətləri qrafiklə göstəririk
plt.scatter(y_test, y_pred, alpha=0.5, color='blue')
plt.xlabel('Həqiqi Qiymətlər')
plt.ylabel('Proqnoz Qiymətlər')
plt.title('Linear Regression Nəticəsi')
plt.show()
#“Model orta hesabla ev qiymətlərini 100 min dollar yanılma ilə proqnozlaşdırır. Ev qiymətləri milyonla ölçüldüyü üçün bu, qəbul edilə bilən bir nəticədir, amma daha dəqiq model üçün əlavə məlumat və ya daha mürəkkəb üsullar sınamaq olar.”






