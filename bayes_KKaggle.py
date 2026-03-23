import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

#Sentiment Labelled Sentences 
df = pd.read_csv("amazon_cells_labelled.txt",
                 sep="\t",
                 names=["texto","sentimiento"])

print(df.head())

#Contamos el numero de palanras en cada texto
print(df['sentimiento'].value_counts())

#Crear modelo de Naive Bayes Multinomial
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['texto'])
y = df['sentimiento']

modelo = MultinomialNB()
modelo.fit(X, y)

#prediccion
ejemplos = ["I love this movie" , "This is the worst thing ever"]
X_ejemplos = vectorizer.transform(ejemplos)
pred = modelo.predict(X_ejemplos)
print(pred)

#Evaluar el modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) #Dividimos los dtaos en entrenamiento y pureba

modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precision: {accuracy:.2f}")