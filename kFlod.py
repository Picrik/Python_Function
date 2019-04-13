'''This is a test for an NLP training between two classes with an 8 fold testing'''

# import des données

df_donnees = pd.DataFrame(columns=["question", "type"])
df_donnees["question"] = listeQuestions
df_donnees["type"] = "0"
df_ref = pd.read_excel("donnees")
df_ref2 = pd.DataFrame(columns=["question", "type"])
df_ref2["question"] = df_ref["Question"].unique()
df_ref2["type"] = "1"
df_donnees = df_donnees.append(df_ref2)
df_donnees = df_donnees.reset_index(drop=True)

Lfold = []
for i in range(df_donnees.shape[0]):
    Lfold.append(i%8)
df_donnees["fold"] = Lfold

X, y = df_donnees["question"], df_donnees["type"]

#fonction necessaire

# preproccessing des données

def preprocessBoW(data):
    vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7)
    documents = []
    for sen in range(len(data)):
        document = re.sub(r'\W', ' ', str(data[sen]))
        document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
        document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
        document = re.sub(r'\s+', ' ', document, flags=re.I)
        document = re.sub(r'^b\s+', '', document)
        document = document.lower()
        documents.append(document)
    X = vectorizer.fit_transform(documents).toarray()
    tfidconverter = TfidfTransformer()
    X = tfidconverter.fit_transform(X).toarray()
    return X

#k-fold maison, ici 8 fold
def Fold8Maison(data):
    liste_score = []
    for i in range(8):
        print("Ceci est le fold n° : " + str(i+1) + "\n")
        
        # créations des trainings et preprocessing
        X = data["question"]
        X = preprocessBoW(X)
        X_train = X[df_donnees["fold"] != i]
        X_test = X[df_donnees["fold"] == i]

        # création des targets
        y_train = data["type"].loc[data["fold"] != i]
        y_train = y_train.reset_index(drop=True)
        y_test = data["type"].loc[data["fold"] == i]
        y_test = y_test.reset_index(drop=True)

        #entrainement
        classifier = RandomForestClassifier(n_estimators = 1000, random_state = 0)
        classifier.fit(X_train, y_train)

        #prédiction
        y_pred = classifier.predict(X_test)
        print(confusion_matrix(y_test, y_pred))
        print(classification_report(y_test, y_pred))
        print("Accuracy : " + str(accuracy_score(y_test, y_pred)))
        liste_score.append(accuracy_score(y_test, y_pred))
        print("---")
    print("Le score moyen est de : " + str(round(sum(liste_score)/float(len(liste_score)),2)))
