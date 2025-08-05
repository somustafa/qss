import pandas as pd


#Case Study
df = pd.read_csv(r"C:\Users\UniSoft PC\Downloads\train (1).csv")

#Show first 7 observations in dataset
#print(df.head(7))

#Check if there are any missing values.
#print(df['target'].unique())
#print(df.isnull().sum())

#Find mean of each variable according to target
#print(pd.DataFrame([df.groupby(['target']).mean(numeric_only = True).loc[0]])) #data frame ile (table kimi olur)
#print((df.groupby(['target']).mean(numeric_only=True).loc[0])) #series ile

#Remove ID_code column.
#df = df.drop(columns=['ID_code'])
#print(df.head(7))

#Count number of values for each target.
#print(df.value_counts())


#Get statistical summary for each variable.
#a. Give interpretation for std, min, max, mean.
#print(df.describe())
#b. Show mean of var_0 by using indexing.
#print(df.describe().loc['mean', 'var_0'])


#Filter var_0 variable from minimum to mean.
sona  = df.describe().loc['mean', 'var_0']
sonb = df.describe().loc['min', 'var_0']
#print(df[(df['var_0'] >= sonb) & (df['var_0'] <= sona)])


#8. Filter var_6 greater than 5 and var_196 less than 2.
#print((df['var_6']> 5) & (df['var_196'] < 2))

#9. Show observations between 20000 and 30000 for 11th column.
filtered_df = df[(df.iloc[:, 10] >= 20000) & (df.iloc[:, 10] <= 30000)]
#print(filtered_df)

#10. Create features list including variables from var_0 to var_9.
#a. Find correlations in features.
#b. Sort most correlated variables in features.
#c. Show top 10 most correlated variables in features.
features = [f"var_{i}" for i in range(10)]
df_features = df[features]
#a
correlation_matrix = df_features.corr()
#print(correlation_matrix)
#b
sorted_correlation = correlation_matrix.abs().unstack().sort_values(ascending=False)
#c
top_10_correlated = sorted_correlation[sorted_correlation < 1].head(10)
#print(top_10_correlated)



#11. Remove outliers from dataset.
import pandas as pd

# 1. var_0-dan var_9-a qədər sütunları seç
features = [f'var_{i}' for i in range(10)]

# Başlanğıc olaraq bütün sətirləri qəbul edirik
mask = pd.Series(True, index=df.index)

# 2. Hər sütun üçün IQR hesablayıb outlier-ləri tap
for col in features:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    # mask yenilənir: yalnız limiti keçməyən dəyərlər saxlanılır
    mask = mask & df[col].between(lower_bound, upper_bound)

# 3. Outlier olmayan sətirləri seç
df_clean = df[mask]

# 4. Nəticə
#print(f"Əvvəlki satır sayı: {len(df)}")
#print(f"Outlier-lərsiz satır sayı: {len(df_clean)}")






#Homework
#1. Import dataset as FIFA.
FIFA = pd.read_csv(r"C:\Users\UniSoft PC\Downloads\fifa19.csv")
#2. Show first 12 entries of dataset.
print(FIFA.head(13))
#3. Get information about dataset.
print(FIFA.info())
#4. Show the number of observations in dataset.
print(len(FIFA))
#5. Print column names.
print(FIFA.columns.tolist())
#6. Show 5000th observation.
print(FIFA.iloc[4999])
#7. Select user_id column.
print(FIFA['user_id'])
#8. Sort teams by Club and Name columns.
print(FIFA.sort_values(by=['Club', 'Name']))
#9. Filter Players whose Overall score is more than 90.
print(FIFA[FIFA['Overall'] > 90])
#10. Remove 'Unnamed:0' column.
FIFA.drop(columns='Unnamed: 0', inplace=True, errors='ignore')
#11. How many distinct Positions exist in dataset?
FIFA['Position'].nunique()
#12. Show null values.
print(FIFA.isnull().sum())
#13. Fill empty values in 'Release Clause' column with 'unknown'.
FIFA['Release Clause'].fillna('unknown', inplace=True)  
#14. Find mean of Age.
print(FIFA['Age'].mean())
#15. Find maximum of Shot Power.
print(FIFA['Shot Power'].max())
#16. Show footballer has maximum Shot Power.
print(FIFA.loc[FIFA['Shot Power'].idxmax(), 'Name'])
#17. Describe Data. 
print(FIFA.describe())