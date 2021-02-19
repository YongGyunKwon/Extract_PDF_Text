from PIL import Image
import pytesseract
import os
import cv2

#인식률 안좋음
def image_to_string1(filename):
    img=Image.open(filename)

    #img2=Image.open(filename)
    #img2=deskew(img2)
    #img2=get_grayscale(img2)
    #img2=remove_noise(img2)

    text=pytesseract.image_to_string(img,lang='kor+eng')
    print(text)
    return text


# cv2 사용하여 간단한 영상처리 후 pytesseract 사용
def image_to_string2(filename):
    image=cv2.imread(filename)
    #cv2.imshow("Image",image)
    
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    filename="{}.png".format(os.getpid())

    cv2.imwrite(filename,gray)
    
    text=pytesseract.image_to_string(Image.open(filename),lang='kor')
    os.remove(filename)

    print(text)

    #cv2.imshow("Image",image)
    #cv2.waitKey(0)


def image_to_string_multi(dirname):
    filenames= os.listdir(dirname)
    #print(filenames)

    for filename in filenames:
        
        #파일형식이 .jpg인 것 고르기
        if filename[-4:]==".jpg":
            file1=dirname+"\\"+filename
            print(file1)
            image_to_string2(file1)

#image_to_string2("D:\\2_CodeBase\\1_ISO26262Text\\Extract_PDF_Text\\pdffile\\outfile_7.jpg")
image_to_string_multi("D:\\2_CodeBase\\1_ISO26262Text\\Extract_PDF_Text\\pdffile")