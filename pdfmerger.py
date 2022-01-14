from PyPDF2 import PdfFileMerger, PdfFileReader
 
mergedObject = PdfFileMerger()

for fileNumber in range(1, 25):
    mergedObject.append(PdfFileReader('Chapter-' + str(fileNumber)+ '.pdf', 'rb'))
 
mergedObject.write("EconomicsBook.pdf")