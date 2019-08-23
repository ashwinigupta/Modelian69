import csv
import codecs

f = codecs.open("template.html", 'r', 'utf-8')
oldhtml = f.read()
finalhtml = ''

with open('Book3.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            oldphotourl = 'https://drive.google.com/open?id='
            photoid = '' + row[3]
            photorecent = 'https://drive.google.com/uc?export=view&amp;id=' + photoid.replace(oldphotourl, '')
            photoid = '' + row[4]
            photoschool = 'https://drive.google.com/uc?export=view&amp;id=' + photoid.replace(oldphotourl, '')
            photoid = '' + row[20]
            photowife = 'https://drive.google.com/uc?export=view&amp;id=' + photoid.replace(oldphotourl, '')

            newhtml = oldhtml.replace('@@NAME@@', row[1])
            newhtml = newhtml.replace('@@SCHOOLPHOTO@@', photoschool)
            newhtml = newhtml.replace('@@RECENTPHOTO@@', photorecent)
            newhtml = newhtml.replace('@@WIFEPHOTO@@', photowife)
            newhtml = newhtml.replace('@@QUALIFICATION@@', row[5])
            newhtml = newhtml.replace('@@OCCUPATION@@', row[10])
            newhtml = newhtml.replace('@@DOB@@', row[6])
            newhtml = newhtml.replace('@@BLOODGROUP@@', row[12])
            newhtml = newhtml.replace('@@ANNIVERSARY@@', row[13])
            newhtml = newhtml.replace('@@WIFE@@', row[14])
            newhtml = newhtml.replace('@@WIFEQUALIFICATION@@', row[15])
            newhtml = newhtml.replace('@@EMAIL@@', row[2])
            newhtml = newhtml.replace('@@MOBILE@@', row[7])
            newhtml = newhtml.replace('@@PERMANENT@@', row[8])
            newhtml = newhtml.replace('@@CURRENT@@', row[9])
            newhtml = newhtml.replace('@@DESCRIPTION@@', row[11])
            newhtml = newhtml.replace('@@CHILD1@@', row[16])
            newhtml = newhtml.replace('@@CHILD1QUALIFICATION@@', row[17])
            newhtml = newhtml.replace('@@CHILD2@@', row[18])
            newhtml = newhtml.replace('@@CHILD2QUALIFICATION@@', row[19])
            newhtml = newhtml.replace('@@ADDITIONAL@@', row[21])
            newhtml = newhtml.replace('@@QUOTE@@', row[22])
            newhtml = newhtml.replace('@@QUOTEWRITER@@', row[23])

            finalhtml += newhtml

            # print(newhtml)
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
    # finalhtml += "</div></html>"
print(finalhtml)

text_file = codecs.open("Output.html", 'w', 'utf-8')
text_file.write(finalhtml)
text_file.close()
