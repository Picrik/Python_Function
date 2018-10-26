# First function : compare two dataframes

def findDiff(df1, df2, nom_col):
    """ findDiff(df1, df2, nom_col)
    nom_col = name of the column with the uniques value (index for example)
    Print Difference between two dataframe
    They have to be the same size
    """
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

# Find out if a number is a prime number

def primeNumber(num):
    test = 0
    for i in range(2,num):
        if (num % i) == 0:
            test += 1
    if test != 0:
        print(num, " it's not a prime number !")
    else:
        print(num, " it's a prime number !")
