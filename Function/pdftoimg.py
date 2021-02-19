import fitz 

#pdffile => pdf 파일명 string 파라미터로 입력
def pdf_to_image(pdffile,savepath):
    doc=fitz.open(pdffile)
    #page count 
    pagecount=doc.pageCount

    print(pagecount)

    #read pdf page to png
    for i in  range(0,pagecount):
        
        page =doc.loadPage(i)
        pix= page.getPixmap()
        output= savepath+ "\\outfile_{}.jpg".format(i)
        pix.writePNG(output)
        print(output)

#example path
savepath="D:\\2_CodeBase\\1_ISO26262Text\\Extract_PDF_Text\\pdffile"
#example file path
pdffile="D:\\2_CodeBase\\1_ISO26262Text\\Extract_PDF_Text\\pdffile\\ISO26262_guide.pdf"

#For test 
pdf_to_image(pdffile,savepath)

