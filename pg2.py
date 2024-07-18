import pymupdf # imports the pymupdf library
doc = pymupdf.open(".\\books\\List_of_Post_Offices.pdf") # open a document

for page in doc[15:16]: # iterate the document pages
  text = page.get_text() # get plain text encoded as UTF-8
  tb = page.find_tables()

  print(text)
