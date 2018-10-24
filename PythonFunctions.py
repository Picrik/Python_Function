def findDiff(df1, df2, nom_col):
    count_row = (df1.shape[0])
    count_col = (df1.shape[1])
    for i in range(count_row):
        for j in range(count_row):
            if df1[nom_col][i] == df2[nom_col][j]:
                for l in range(count_col):
                    if df1.iloc[i,l] != df2.iloc[j,l]:
                        print(df1.loc[i].values)
                        print(df2.loc[j].values)
                        print("--")
