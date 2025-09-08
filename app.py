import pandas as pd 
df = pd.read_csv('data.csv') 
print(df.head()) 
print(df.sample()) 
import matplotlib.pyplot as plt 
x = df['gender'] 
y = df['score'] 
plt.bar(x, y) 
plt.show() 
data = df['major'].value_counts() 
plt.pie(data, labels=data.index) 
plt.title('Pie Chart: Students by Major') 
plt.show() 
