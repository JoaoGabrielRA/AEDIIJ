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
        self.freqTable = {}
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
    def printRows(self, name, nameCol):
        for row in self.data:
            if row[nameCol] == name:
                print(row)
    # for each entry in the "entryCol" column that has "entry" as its data, print the data in column "nameCol" in relation
    # to the data in column "valueCol"
    def printEntries(self, nameCol, entry, entryCol, valueCol):
        for row in self.data:
            if row[entryCol] == entry:
                print(row[nameCol], ':', row[valueCol])
    # print name and number of ratings
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
        with_max = {}
        for row in self.data:
            name = row[nameCol]
            value = float(row[valueCol])
            if name in with_max and with_max[name] < value:
                with_max[name] = value
            elif name not in with_max:
                with_max[name] = value
        return with_max
    # Returns a new CsvManager that is a filtered version of the original but without duplicates. The rows will
    # contain unique entries of the name found in the "nameCol" column. the entry chosen among those with the same name
    # will be the one that has the highest value found in the "valueCol" column.
    def withoutDuplicates(self, nameCol, valueCol):
        with_max = self.onlyWithMaxValues(nameCol, valueCol)
        dataset_clean = CsvManager()
        already_added = []
        for row in self.data:
            name = row[nameCol]
            value = float(row[valueCol])
            if (with_max[name] == value) and (name not in already_added):
                dataset_clean.data.append(row)
                already_added.append(name)
        dataset_clean.header = self.header
        return dataset_clean
    # Returns a new CsvManager that is a filtered version of the original. It will contain only rows that have english
    # text in the "nameCol" column.
    def onlyWithEnglish(self, nameCol):
        def is_english(string):
            non_ascii = 0
            for character in string:
                if ord(character) > 127:
                    non_ascii += 1
            if non_ascii > 3:
                return False
            else:
                return True
        just_english = CsvManager()
        for row in self.data:
            if is_english(row[nameCol]):
                just_english.data.append(row)
        just_english.header = self.header
        return just_english
    # Returns a list of all rows that contain "value" at position "valCol"
    def withValue(self, value:str, valCol:int):
        withThatValue = CsvManager()
        for row in self.data:
            if row[valCol] == value:
                withThatValue.data.append(row)
        return withThatValue
    def generateFreqTable(self, nameCol):
        if nameCol < 0 and nameCol >= -len(self.data[0]):
            nameCol = len(self.data[0]) + nameCol
        table = {}
        total = 0
        for row in self.data:
            total += 1
            if row[nameCol] in table:
                table[row[nameCol]] += 1
            else:
                table[row[nameCol]] = 1
        table_percentages = {}
        for key in table:
            percentage = (table[key] / total) * 100
            table_percentages[key] = percentage
        self.freqTable[nameCol] = table_percentages
        return table_percentages
    def displayTable(self, nameCol):
        if nameCol < 0 and nameCol >= -len(self.data[0]):
            nameCol = len(self.data[0]) + nameCol
        if nameCol not in self.freqTable:
            self.generateFreqTable(nameCol)
        table = self.freqTable[nameCol]
        table_display = []
        for key in table:
            key_val_as_tuple = (table[key], key)
            table_display.append(key_val_as_tuple)
        table_sorted = sorted(table_display, reverse = True)
        for entry in table_sorted:
            print(entry[1], ':', entry[0])
    def avgPerEntry(self, nameCol, valueCol):
        if nameCol < 0 and nameCol >= -len(self.data[0]):
            nameCol = len(self.data[0]) + nameCol
        if nameCol not in self.freqTable:
            self.generateFreqTable(nameCol)
        entries = self.freqTable[nameCol]
        for entry in entries:
            total = 0
            entry_occurrences = 0
            for row in self.data:
                if row[nameCol] == entry:
                    total += float(row[valueCol].replace(',','').replace('+',''))
                    entry_occurrences += 1
            avg_value = total / entry_occurrences
            print(entry, ':', avg_value)
    def withEntries(self, entry:str, entryCol:int, valueCol:int, nameCol:int, *args:str):
        for row in self.data:
            conditions = False
            for condition in args:
                conditions = conditions or (condition == row[valueCol])
            conditions = conditions and (row[entryCol] == entry)
            if conditions:
                print(row[nameCol], ':', row[valueCol])
    def avgExcludingLessThan(self, maximum, entry, entryCol, valueCol):
        under_max = []
        for row in self.data:
            value = row[valueCol]
            value = value.replace(',', '')
            value = value.replace('+', '')
            if (row[entryCol] == entry) and (float(value) < maximum):
                under_max.append(float(value))
        return sum(under_max)/len(under_max)

# initializing the managers for each dataset

android = CsvManager('googleplaystore.csv', hasHeader=True)
ios = CsvManager('AppleStore.csv', hasHeader=True)

# printing the header for the android dataset and the first three rows of the dataset

print(android.header)
print('\n')
android.exploreData(0, 3, True)

print('\n') # printing the header for the ios dataset and the first three rows of the dataset

print(ios.header)
print('\n')
ios.exploreData(0, 3, True)

print('\n') # identifying a row with incorrect information

print(android.data[10472])  # incorrect row
print('\n')
print(android.header)  # header
print('\n')
print(android.data[0])      # correct row

print('\n') # deleting the incorrect row

print(len(android.data))
del android.data[10472]
print(len(android.data))

print("\n") # printing every row that has 'Instagram' in the first column

android.printRows('Instagram', 0)

print('\n') # getting lists of all the apps that don't have duplicates and the ones who do

unique_apps, duplicate_apps = android.uniqsAndDupes(0)
print('Number of duplicate apps:', len(duplicate_apps))
print('\n')
print('Examples of duplicate apps:', duplicate_apps[:15])

print('\n') # getting a dictionary containing only entries that have the maximum rating for each app

reviews_max = android.onlyWithMaxValues(0, 3)

print('Expected length:', len(android.data) - 1181)
print('Actual length:', len(reviews_max))

print('\n') # removing the duplicate apps while choosing the ones that have the maximum user rating

android_clean = android.withoutDuplicates(0, 3)
android_clean.exploreData(0, 3, True)

print('\n') # identifying apps that are not in english

print(ios.data[813][1])
print(ios.data[6731][1])

print(android_clean.data[4412][0])
print(android_clean.data[7940][0])

print('\n') # filtering the dataset further to contain only the apps that have english names

android_english = android_clean.onlyWithEnglish(0)
ios_english = ios.onlyWithEnglish(1)

android_english.exploreData(0, 3, True)
print('\n')
ios_english.exploreData(0, 3, True)

print('\n') # getting a list of the free apps

android_final = android_english.withValue('0', 7)
ios_final = ios_english.withValue('0.0', 4)

print(len(android_final.data))
print(len(ios_final.data))

print('\n') # displays the frequency tables for entries in specific columns

ios_final.displayTable(-5)
print('\n')
android_final.displayTable(1)
print('\n')
android_final.displayTable(-4)

print('\n') # prints the average value of the number of downloads for each app genre (genres in 5th to last column, )

ios_final.avgPerEntry(-5, 5)

print('\n') # prints the number of downloads for all apps in the 'Navigation' genre (names in column 1, searching for
# 'Navigation' in column -5 and displaying what's in column 5)

ios_final.printEntries(1, 'Navigation', -5, 5)

print('\n') # prints the number of downloads for all apps from the 'Reference' genre

ios_final.printEntries(1, 'Reference', -5, 5)

print('\n') # displays frequency table for column 5 (number of downloads)

android_final.displayTable(5)

print('\n') # displays the average number of downloads for each category (categories in column 1, ratings in column 5)

android_final.avgPerEntry(1, 5)

print('\n') # displays the name of apps with communication as its category and number of downloads matching any of those values
# (searches for 'COMMUNICATION' in column 1, searches for download numbers in column 5 and displays the name found in 0)

android_final.withEntries('COMMUNICATION', 1, 5, 0, '1,000,000,000+', '500,000,000+', '100,000,000+')

print('\n') #

print(android_final.avgExcludingLessThan(100000000, 'COMMUNICATION', 1, 5))

print('\n') #

android_final.printEntries(0, 'BOOKS_AND_REFERENCE', 1, 5)

print('\n') #

android_final.withEntries('BOOKS_AND_REFERENCE', 1, 5, 0, '1,000,000,000+', '500,000,000+', '100,000,000+')

print('\n') #

android_final.withEntries('BOOKS_AND_REFERENCE', 1, 5, 0, '1,000,000+', '5,000,000+', '10,000,000+', '50,000,000+')