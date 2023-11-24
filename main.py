"""
THE POWER OF THE HOME DEPOT

This application will extract the itemized data of an input Home Depot receipt.
"""

import PyPDF2
import re
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
fileName = askopenfilename()

pdfFileObj = open(fileName, 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# print(len(pdfReader.pages))

pageObj = pdfReader.pages[0]
extractedText = pageObj.extract_text()

splitText = extractedText.split('CHECKOUT')
itemizedExtractText = splitText[1].split('SUBTOTAL')[0]

receiptExtractPrices = re.split('\d{11,}',itemizedExtractText)

itemIdentifiers = re.findall('\d{11,}',itemizedExtractText)

descriptionList = []
priceList = []

# CSV Output Writing Text, also computes the regExs needed to filter the PDF file. Currently, code only looks at one page.

csvOutputFileName = fileName[:-3] + 'csv'

with open(csvOutputFileName, 'w', newline='') as csvFile:

    fieldNames = ['Description','Price']
    writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
    writer.writeheader()

    for idx, entry in enumerate(receiptExtractPrices):
        if idx == 0:
            continue
        # For idx == 1 and greater, run the price regex on the line, then combine the remnants and add to a []
        # Keep the split price in another []

        entrySplit = re.split('\d{1,}[.]\d{2}\n',entry)
        price = re.findall('\d{1,}[.]\d{2}\n',entry)[:1]
        priceString = (''.join(price)).strip()

        descriptionString = (''.join(entrySplit)).strip()

        descriptionString = itemIdentifiers[idx - 1] + ',' + descriptionString

        descriptionList.append(descriptionString)
        priceList.append(priceString)

        writer.writerow({'Description':descriptionString, 'Price':priceString})

    totalValues = splitText[1].split('SUBTOTAL')[1]
    totalValuesSplit = re.split('(?:SALES TAX)',totalValues)
    taxValue = totalValuesSplit[1].split('TOTAL')[0].strip()

    writer.writerow({'Description':'Taxes', 'Price':str(taxValue)})

    #Now, combine the itemized + tax for Total.
    priceList = [float(i) for i in priceList]
    subTotal = round(sum(priceList),2)
    total = round(subTotal + float(taxValue),2)

    writer.writerow({'Description':'', 'Price':''})
    writer.writerow({'Description':'Total', 'Price':str(total)})