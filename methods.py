import PyPDF2 as pdf
from PyPDF2 import PdfReader,PdfMerger,PdfWriter
import os
from PIL import Image
# Reading a Pdf File
def get_pdf_metadata(pdf_path):
    with open(pdf_path,'rb') as f:
        reader = PdfReader(f)
        info = reader.metadata
    print(info.title)
    print(info.author)

# Extracting pages from a pdf file
def extract_from_pdf(pdf_path):
    with open(pdf_path,'rb') as f:
        reader = PdfReader(f)
        results = []
        for i in range(0,len(reader.pages)):
            page = reader.pages[i]
            extracted_text = page.extract_text()
            results.append(extracted_text)
        return ''.join(results)
    
# print(extract_from_pdf('imrad.pdf'))
# Get a number of pages - > len(reader.pages)

# Pdf Splitting

def split_pdf(pdf_path):
    with open(pdf_path,'rb') as f:
        reader=PdfReader(f)
        writer = PdfWriter()
        # get all pages
        for i in range(0,len(reader.pages)):
            selected_page = reader.pages[i]
            # Writer to initiate multiple pdfs
            writer.add_page(selected_page)
            filename = os.path.splitext(pdf_path)[0]
            output_name = f'{filename}_{i+1}.pdf'
            # save and compile
            with open(output_name,'wb') as out:
                writer.write(out)
            print(f"Created a pdf: {output_name}")

# Pdf Splitting up to a certain page


def split_pdf_upto(pdf_path,start:int=0,end:int=0,output_page='output'):
    with open(pdf_path,'rb') as f:
        reader=PdfReader(f)
        writer = PdfWriter()
        # get all pages
        for i in range(start,end):
            selected_page = reader.pages[i]
            # Writer to initiate multiple pdfs
            writer.add_page(selected_page)
            filename = os.path.splitext(pdf_path)[0]
            output_name = f'{filename}_from_{start}_to_{end}_{i+1}.pdf'
            # save and compile
            with open(output_name,'wb') as out:
                writer.write(out)
            print(f"Created a pdf: {output_name}")

def get_last_page(file_path):
    with open(file_path,'rb') as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        last_page = len(reader.pages) - 1
        selected_page = reader.pages[last_page]
        writer.add_page(selected_page)
        filename = os.path.splitext(file_path)[0]
        output_name = f'{filename}_lastpage.pdf'
        with open(output_name,'wb') as out:
            writer.write(out)
        print(f"Created a pdf: {output_name}")

# Merging Pdf Files

# Get all pdfs you want to work in 
# then use pdf merger

def fetch_all_pdfs(parent_folder = str):
    target_files =[]
    for path,subdirs,files in os.walk(parent_folder):
        for name in files:
            if name.endswith('.pdf'):
                target_files.append(os.path.join(path,name))
    return target_files

def merge_pdf_files(list_of_pdfs,out_put_filename = "Final_Merged_File.pdf"):
    merger = PdfMerger()
    with open(out_put_filename,'wb') as f:
        for file in list_of_pdfs:
            merger.append(file)
        merger.write(f)
    print("Files Merged Succesfully")

def merge_two_files(first_filename, second_filename, output_filename="Final_Merged_File.pdf"):
    list_of_pdfs = [first_filename, second_filename]
    merger = PdfMerger()

    for file in list_of_pdfs:
        merger.append(file)

    with open(output_filename, 'wb') as f:
        merger.write(f)

    print("Files Merged Successfully")

def rotate_a_page(pdf_path, page_num, rotation: float = 90):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        selected_page = reader.pages[page_num]
        writer.add_page(selected_page)
        writer.pages[page_num].rotate(rotation)
        filename = os.path.splitext(pdf_path)[0]
        output_name = f'{filename}_rotated.pdf'
        with open(output_name, 'wb') as out:
            writer.write(out)
        print(f"Created a pdf: {output_name}")

def extract_images_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PdfReader(f)
        for i in range(0,len(reader.pages)):
            selected_page = reader.pages[i]
            for img_file_obj in selected_page.images:
                with open(img_file_obj.name,'wb') as out :
                    out.write(img_file_obj.data)
    print("Images extracted successfully")

# Convert Images to PDFs

def convert_image_to_pdf(image_file):
    my_image = Image.open(image_file)
    img = my_image.convert("RGB")
    file_name = f"{os.path.splitext(image_file)[0]}.pdf"
    img.save(file_name)
    print("Images Converted to PDFs Successfully")