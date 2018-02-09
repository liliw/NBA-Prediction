import xlsxwriter

#open source file
fname = raw_input("Enter file name: ")
inputfile = fname + '.txt'
f = open(inputfile, 'r')

# create a new Excel file and add a worksheet
#outputfile = raw_input("Enter output file name: ")
outputfile = fname + '.xlsx'
workbook = xlsxwriter.Workbook(outputfile)
worksheet = workbook.add_worksheet()

#widen the first column to make the text clearer
# worksheet.set_column('A:A', 20)

#add a blod format to use to hightlight cells
bold = workbook.add_format({'bold': True})

#write some text ---- worksheet.write(row, col, some_data)
content = f.read()

items = content.split('"headers":', 1)[1]
items = items.split('"rowSet":')[0]
#print items
attributes, attribute_name = [], ''
for i in range(len(items)):
    letter = items[i]
    if letter == ',':
        attributes += [attribute_name]
        attribute_name = ''
    elif letter != '"' and letter != '[' and letter != ']' and letter != '\n':
        attribute_name += letter
#print attributes

for i in range(len(attributes)):
    worksheet.write(0, i, attributes[i])


raw_data = content.split('"rowSet":', 1)
# print raw_data[1]
data, element = [], ''
for i in range(len(raw_data[1])):
    letter = raw_data[1][i]
    if letter == '[':
        newList, element = [], ''
    elif letter == ',':
        newList = newList + [element]
        element = ''
    elif letter == ']':
        newList = newList + [element]
        data = data + newList
        newList, element = [], ''
    elif letter != '"' and letter != '}':
        element = element + letter
print data

for i in range(len(data)):
    colNum = i % len(attributes)
    rowNum = i / len(attributes)
    worksheet.write(rowNum+1, colNum, data[i])

workbook.close()