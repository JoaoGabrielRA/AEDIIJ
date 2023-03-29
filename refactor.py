from csv import reader

class CsvManager():
    def __init__(self, filename):
        f = open(filename, encoding='utf8')
        read_f = list(reader(f))
        self.header, self.data = read_f[0], read_f[1:]
        f.close()
    def exploreData(self, start, end, rows_and_columns=False):
        dataset_slice = self.data[start:end]    
        for row in dataset_slice:
            print(row)
        if rows_and_columns:
            print('Number of rows:', len(self.data))
            print('Number of columns:', len(self.header))
    def printEntries(self, name):
        for item in self.data:
            if item[0] == name:
                print(item)
    def uniqsAndDupes(self):
        dupes = []
        uniqs = []
        for item in self.data:
            if item[0] in uniqs:
                dupes.append(item[0])
            else:
                uniqs.append(item[0])
        return uniqs, dupes


android = CsvManager('googleplaystore.csv')
ios = CsvManager('AppleStore.csv')

# ios.exploreData(0, 10, True)

# print(android.data[10472])
# print(android.header)
# print(android.data[0])

# print(len(android.data))
# del android.data[10472]
# print(len(android.data))

# android.printEntries('Instagram')

unique_apps, duplicate_apps = android.uniqsAndDupes()
print('Number of duplicate apps:', len(duplicate_apps))
print('Examples of duplicate apps:', duplicate_apps[:15])