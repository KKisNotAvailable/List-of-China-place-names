import cv2 # pip install opencv-python
import numpy as np
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os

# [pytesseract requirement]
# get tesseract-ocr from github:# https://github.com/UB-Mannheim/tesseract/wiki
# pytesseract is just a python wrapper of tesseract-ocr

# [pdf2image requirement]
# https://poppler.freedesktop.org/



class PDF_extractor():
    def __init__(self, pdf_path: str = "") -> None:
        self.__use_gpu = cv2.cuda.getCudaEnabledDeviceCount() > 0
        self.pdf_path = pdf_path

    # Function to preprocess an image with OpenCV
    def pdf_to_image(self, image):
        image_cv = np.array(image)
        if self.__use_gpu:
            # Upload image to GPU
            image_gpu = cv2.cuda_GpuMat(image_cv)
            # Convert to grayscale
            gray_gpu = cv2.cuda.cvtColor(image_gpu, cv2.COLOR_BGR2GRAY)
            # Download image from GPU to CPU
            image_cv = gray_gpu.download()
        else:
            # Convert to grayscale
            image_cv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
        return Image.fromarray(image_cv)

    # Function to process a batch of pages as images
    def process_per_batch(self, start: int, end: int, batch_number: int) -> None:
        # Convert a range of pages to images
        images = convert_from_path(self.pdf_path, first_page=start, last_page=end, dpi=200)

        # Perform OCR on each image after preprocessing
        for i, image in enumerate(images):
            # Preprocess the image
            image = self.pdf_to_image(image)

            # Perform OCR using pytesseract
            text = pytesseract.image_to_string(image)

            # Save the text in a file
            text_file_path = f'/content/batch_texts/batch_{batch_number}_page_{start + i}.txt'
            with open(text_file_path, 'w') as file:
                file.write(text)

            # Save the image
            image_file_path = f'/content/batch_images/batch_{batch_number}_page_{start + i}.png'
            image.save(image_file_path)

        # Clear the images list to free up memory
        del images

    def batch_process(self, start: int, end: int, batch_size: int = 10) -> None:
        total_pages = end - start + 1  # Total number of pages in your PDF
        batches = (total_pages + batch_size - 1) // batch_size
        print(batches)
        # Process each batch
        for batch in range(batches):
            start_page = batch * batch_size + start
            end_page = min(start_page + batch_size - 1, end)
            print(f"B: {batch} >> S: p.{start_page}, E: p.{end_page}")
            self.process_per_batch(start_page, end_page, batch)






def main():
    pdf_path = '.\\books\\List_of_Post_Offices.pdf'  # Replace with the path to your PDF

    # Create directories for saving output
    os.makedirs('.\\content\\batch_texts', exist_ok=True)
    os.makedirs('.\\content\\batch_images', exist_ok=True)

    p = PDF_extractor(pdf_path)

    p.batch_process(15, 16)


if __name__ == "__main__":
    main()