##################################################################
#                   Pdf Merger and Separator                     #
#                           v 1.0                                #
#                      by : Yousef Albasel                       #
#    Assignment 1 - Structured Programming -Dr. Mohamed Elramly  #
##################################################################
import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfMerger, PdfWriter
import os
from PIL import Image
from methods import *
import sys
def main_menu_showup():
    print('---------- Main Menu ------------')
    print(' 1 - Get PDF Information')
    print(' 2 - Extract PDF Text')
    print(' 3 - Split PDF into separate files')
    print(' 4 - Split PDF into separate files up to specific page')
    print(' 5 - Split the last page of a PDF')
    print(' 6 - Merge all PDFs in a folder')
    print(' 7 - Merge Two PDFs')
    print(' 8 - Rotate a page in a PDF')
    print(' 9 - Extract images from a PDF')
    print(' 10 - Convert image to PDF')
    print(' 11 - Exit')
    print('---------------------------------')
    print('----------Instructions-----------')
    print('Always input file names or paths like so : "File-name.pdf", "Folder"\n ')
    print('Any file name or folder name you MUST include The path to it, or put the files \n you want to work on in the same directory as main.py\n ')
    print('If you find any errors please report it to Albasel#6286')

    try:
        option = int(input("Input Option Number: "))
        if option < 1 or option > 11:
            raise ValueError("Invalid input. Please enter a number in the range 1 - 10.")
    except ValueError as e:
        print("Error:", str(e))
        return main_menu_showup()
    
    return option

selection = main_menu_showup()

def switch(option):
    # 1 - Get PDF Information
    if option == 1:
        filename = input("Enter the PDF filename: ").strip('"')
        # Handle file not found error
        try:
            get_pdf_metadata(filename)
        except FileNotFoundError:
            print("Error: File not found.")
    
    # 2 - Extract PDF Text
    elif option == 2:
        print("Please note that this method will not work on pdfs with images inside it")
        file_path = input("Input file path: ").strip('"')
        # Handle file not found error
        try:
            print(extract_from_pdf(file_path))
        except FileNotFoundError:
            print("Error: File not found.")
    
    # 3 - Split PDF into separate files
    elif option == 3:
        file_path = input("Input file path: ").strip('"')
        # Handle file not found error
        try:
            split_pdf(file_path)
        except FileNotFoundError:
            print("Error: File not found.")
    
    # 4 - Split PDF into separate files up to specific page
    elif option == 4:
        file_path = input("Input file path: ").strip('"')
        start = int(input("Input Start: "))
        end = int(input("Input end: "))
        # Handle file not found error
        try:
            split_pdf_upto(file_path, start, end)
        except FileNotFoundError:
            print("Error: File not found.")
        except ValueError as e:
            print("Error:", str(e))
    
    # 5 - Split the last page of a PDF
    elif option == 5:
        file_path = input("Input file path: ").strip('"')
        # Handle file not found error
        try:
            get_last_page(file_path)
        except FileNotFoundError:
            print("Error: File not found.")
    
    # 6 - Merge all PDFs in a folder
    elif option == 6:
        folder_path = input("Input folder path: ").strip('"')
        # Handle folder not found error
        try:
            merge_pdf_files(fetch_all_pdfs(folder_path))
        except FileNotFoundError:
            print("Error: Folder not found.")
    
    # 7 - Merge Two PDFs
    elif option == 7:
        print("Input first filename: ")
        first_filename = input().strip('"')
        print("Input second filename: ")
        second_filename = input().strip('"')
        print("Input output filename eg(output.pdf): ")
        output_filename = input().strip('"')
        # Handle file not found error
        try:
            merge_two_files(first_filename,second_filename,output_filename)
        except FileNotFoundError as e:
            print("Error:", str(e))
    
    # 8 - Rotate a page in a PDF
    elif option == 8:
        file_path = input("Input file path: ").strip('"')
        page_num = int(input("Input page number: "))
        rotation = int(input("Input rotation angle: "))
        # Handle file not found error
        try:
            rotate_a_page(file_path, page_num, rotation)
        except FileNotFoundError:
            print("Error: File not found.")
    
    # 9 - Extract images from a PDF
    elif option == 9:
        file_path = input("Input file path: ").strip('"')
        # Handle file not found error
        try:
            extract_images_from_pdf(file_path)
        except FileNotFoundError:
            print("Error: File not found.")
    
    # 10 - Convert image to PDF
    elif option == 10:
        image_file = input("Input image path: ").strip('"')
        # Handle file not found error
        try:
            convert_image_to_pdf(image_file)
        except FileNotFoundError:
            print("Error: File not found.")    
    elif option == 11:
        sys.exit()

switch(selection)
