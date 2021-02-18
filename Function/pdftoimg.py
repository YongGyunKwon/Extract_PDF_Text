import fitz 

# from pdf2image import convert_from_path
# from pdf2image import convert_from_path, convert_from_bytes


# def pdf2img_converter(filename):
#     pages= convert_from_path("ISO26262_guide.pdf",500,poppler_path=r'D:\\2_CodeBase\\1_ISO26262Text\\Extract_PDF_Text\\pdffile')

    

#     for page in pages:
#         print(page)
#         #page.save('out_{}'.format(page),'JPEG')
    
# pdf2img_converter("D:/2_CodeBase/1_ISO26262Text/Extract_PDF_Text/pdffile/ISO26262_guide.pdf")




pdffile="D:/2_CodeBase/1_ISO26262Text/Extract_PDF_Text/pdffile/ISO26262_guide.pdf"

doc= fitz.open(pdffile)

page =doc.loadPage(0)

pix= page.getPixmap()

output= "outfile.png"

pix.writePNG(output)