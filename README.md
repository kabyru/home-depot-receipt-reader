# home-depot-receipt-reader
A crudge reg-ex powered receipt reader

This program takes PDF files provided by Home Depot at checkout, as input, and outputs a tabulated itemized receipt as a CSV file. This functionality is particularly useful because Home Depot locks automated spreadsheet generation from purchases behind a paywall. (ProXtra). 

This software requires PyPDF2. Other dependencies should come pre-installed with Python3 (re, csv, tkinter).

To run, use Python in Terminal:
`
python .\main.py
`

The output file will match the same filename as input, just as a .csv extension.

NOTE: This project's processing of receipts is a crude implementation of regex expressions to extract out descriptions and prices of an itemized receipt. This program contains no OCR functionality. I preemptively apologize for any difficulties with this program as I view it as a personal exercise on regexs... however the basis of this program has potential to be expanded upon to adapt for other store receipt formats, and OCR functionality. 

Consider program as-is but will answer to issues as I find able. 
