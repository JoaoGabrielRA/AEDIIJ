from csv import reader

class CsvManager():
    # Initializes by opening the desired file and storing each row within the "data" variable. If no file is specified, an empty
    # list is assigned to "data". If "hasHeader" is True, the first row will be stored in a separate variable called "header"
    def __init__(self, filename:str=None, hasHeader=False):
        if filename != None:
            opened_file = open(filename, encoding='utf8')
            read_file = list(reader(opened_file))
            self.header, self.data = read_file[0] if hasHeader else None, read_file[1:] if hasHeader else read_file
            opened_file.close()
        else:
            self.header = None
            self.data = []
    # Displays the rows between the specified endpoints. if "rows_and_columns" is True, it will also print the number of rows and
    # columns in the dataset.
    def exploreData(self, start, end, rows_and_columns=False):
        if self.data != []:
            dataset_slice = self.data[start:end]
            for app in dataset_slice:
                print(app)
                print('\n')
        if rows_and_columns:
            print('Number of rows:', len(self.data) if self.data != [] else 0)
            print('Number of columns:', len(self.data[0]) if self.data != [] else 0)
    # Displays every row that contains "name" stored in the position of index "nameCol".
    def printEntries(self, name, nameCol):
        for row in self.data:
            if row[nameCol] == name:
                print(row)
    # Returns in the first tuple position a list of all the rows that don't have the data in position "nameCol" repeated in
    # another row in the same column. Whereas in the second position is a list of rows that don't follow that condition.
    def uniqsAndDupes(self, nameCol):
        duplicate_rows = []
        unique_rows = []
        for row in self.data:
            if row[nameCol] in unique_rows:
                duplicate_rows.append(row[nameCol])
            else:
                unique_rows.append(row[nameCol])
        return unique_rows, duplicate_rows
    # Returns a dictionary that contains, for each unique entry in position "nameCol", the highest value found in column "valueCol"
    # for that unique entry.
    def onlyWithMaxValues(self, nameCol, valueCol):
        reviews_max = {}
        for app in self.data:
            name = app[nameCol]
            n_reviews = float(app[valueCol])
            if name in reviews_max and reviews_max[name] < n_reviews:
                reviews_max[name] = n_reviews
            elif name not in reviews_max:
                reviews_max[name] = n_reviews
        return reviews_max
    # Returns a new CsvManager that is a filtered version of the original but without duplicates. The rows will
    # contain unique entries of the name found in the "nameCol" column. the entry chosen among those with the same name
    # will be the one that has the highest value found in the "valueCol" column.
    def withoutDuplicates(self, nameCol, valueCol):
        reviews_max = self.onlyWithMaxValues(nameCol, valueCol)
        dataset_clean = CsvManager()
        already_added = []
        for app in self.data:
            name = app[nameCol]
            n_reviews = float(app[valueCol])
            if (reviews_max[name] == n_reviews) and (name not in already_added):
                dataset_clean.data.append(app)
                already_added.append(name)    
        return dataset_clean
    # Returns a new CsvManager that is a filtered version of the original. It will contain only rows that have english
    # text in the "nameCol" column.
    def withJustEnglish(self, nameCol):
        def is_english(string):
            non_ascii = 0
            for character in string:
                if ord(character) > 127:
                    non_ascii += 1
            if non_ascii > 3:
                return False
            else:
                return True
        apps_english = CsvManager()
        for app in self.data:
            name = app[nameCol]
            if is_english(name):
                apps_english.data.append(app)
        return apps_english
    # Returns a list of all rows that contain "value" at position "valCol"
    def withValue(self, value:str, valCol:int):
        withThatValue = []
        for row in self.data:
            if row[valCol] == value:
                withThatValue.append(row)
        return withThatValue

android = CsvManager('googleplaystore.csv', hasHeader=True)
ios = CsvManager('AppleStore.csv', hasHeader=True)

ios.exploreData(0, 10, True)

print(android.data[10472])
print(android.header)
print(android.data[0])

print(len(android.data))
del android.data[10472]
print(len(android.data))

android.printEntries('Instagram', 0)

unique_apps, duplicate_apps = android.uniqsAndDupes(0)
print('Number of duplicate apps:', len(duplicate_apps))
print('Examples of duplicate apps:', duplicate_apps[:15])

reviews_max = android.onlyWithMaxValues(0, 3)

print('Expected length:', len(android.data) - 1181)
print('Actual length:', len(reviews_max))

android_clean = android.withoutDuplicates(0, 3)
android_clean.exploreData(0, 3, True)

print(ios.data[813][1])
print(ios.data[6731][1])

print(android_clean.data[4412][0])
print(android_clean.data[7940][0])

android_english = android_clean.withJustEnglish(0)
ios_english = ios.withJustEnglish(1)

android_english.exploreData(0, 3, True)
print('\n')
ios_english.exploreData(0, 3, True)

android_final = android_english.withValue('0', 7)
ios_final = ios_english.withValue('0.0', 4)

print(len(android_final))
print(len(ios_final))