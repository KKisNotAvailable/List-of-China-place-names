# List-of-China-place-names
The original list are from the following sources:
1. https://books.google.com.tw/books?id=om8uAQAAIAAJ&printsec=frontcover&hl=zh-TW#v=onepage&q&f=false
2. https://archive.org/details/mapofchinashan/mode/1up
3. https://books.google.com.tw/books?id=3X1OAQAAMAAJ&printsec=frontcover&hl=zh-TW#v=onepage&q&f=false

so in the end there will be three folders to include all tables mentioned in these books seperately.

There will be a huge amount of work to do, hope I can finish them before the end of this year.

# Tools I tried
## pdf2image + tesseract OCR
Get the idea from this [post](https://community.openai.com/t/what-is-the-best-way-to-parse-a-pdf-file-with-chatgpt/525733/3)
Both pdf2image and pytesseract are just wrappers, so need to download respective executable or compiled binaries, please refer to the top of pg.py

In sum, the result is unacceptably bad.

## PyMuPDF
This package supports the extraction of tables, but I guess because the tables in the book have too blurred lines, so the machine cannot recognize them. On the other hand, simply recognizing words in pages gave way better results than the OCR one. However, still, there are too many missing chinese words in the result to make this method practical.
