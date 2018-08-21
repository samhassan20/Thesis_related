import pandas as pd

data = pd.read_csv('features_modified.txt', sep=":", header=None, names=['index','parameters'])

serieslist = []
for index, row in data.iterrows():
    seriesvalue = pd.Series(row['parameters'])
    serieslist.append(seriesvalue)


dictlist = []
for x in serieslist:
    try:
        string_line = x.values[0]
        if (string_line == ""):
            print(string_line)
        splitted_list = [item.split('=') for item in string_line.split()]

        mydict = dict((k.strip(), v.strip()) for k, v in splitted_list)

        dictlist.append(mydict)
    except Exception as e:
        print "Data=>", x.values[0]
        print "Exception=>", e

print "NEW:", len(dictlist)

data_modified = pd.DataFrame(dictlist)
data_modified = data_modified.drop('ast_name', 1)


data_modified['name'] = data_modified['name'].astype(int)

# Use the above one line code to convert the column values to int once you impute/fill-in/discard NaNs.
