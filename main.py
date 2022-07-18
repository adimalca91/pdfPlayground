import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)                       # number of pages
    print(reader.getPage(0))                     # get the page object
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)       # rotate the page object
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

