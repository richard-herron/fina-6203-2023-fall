import os
import shutil
import sys
import re

def dup_pdfs(source_folder, destination_subfolder="Duplicates"):
	# prepare destination folder
    destination_folder = os.path.join(source_folder, destination_subfolder)
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

	# get list of PDFs to duplicate
    all_files = os.listdir(source_folder)
    pattern = re.compile(r'^bkm_ch_\d{2}\.pdf$')
    pdf_files = [file for file in all_files if pattern.match(file)]
    suffixes = ["_blank", "_section_02", "_section_04", "_section_06"]

	# duplicates PDFs
    for pdf_file in pdf_files:
        original_file_path = os.path.join(source_folder, pdf_file)
        for suffix in suffixes:
            new_file_name = pdf_file.replace(".pdf", f"{suffix}.pdf")
            new_file_path = os.path.join(destination_folder, new_file_name)
            shutil.copy(original_file_path, new_file_path)

    print("Files duplicated successfully!")

source_folder = sys.argv[1] if len(sys.argv) > 1 else "."
dup_pdfs(source_folder)
