
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
import os



def try_pdf(path_f):
    fp = open(path_f, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.
    str = ""
    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                str += lt_obj.get_text().replace('-\n','').replace('\n',' ')
    print(str)



def convert_pdf(path):
    from pdfminer.pdfinterp import PDFResourceManager, process_pdf
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from io import StringIO
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'cp1252'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    fp = open(path, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()

    string = retstr.getvalue()
    retstr.close()
    return string.replace('-\n', '').replace('\n',' ')


#print(convert_pdf('k:\Andrew\\vkr\elib\\1.pdf'))
s = "Çàâîäcêàÿ ëàáîpàòîpèÿ. Äèàãíîcòèêà ìàòåpèàëîâ». Ñïåöèàëüíûé âûïóñê"

s = s.encode('cp1252').decode('cp1251')
print(s)
print("Çàâîäcêàÿ ëàáîpàòîpèÿ. Äèàãíîcòèêà ìàòåpèàëîâ». Ñïåöèàëüíûé âûïóñê")
# path_dir = 'k:\Andrew\\vkr\elib\\'
# list_f = os.listdir(path_dir)
# for el in list_f:
#     if el[-4:] == '.pdf':
#         try_pdf(path_dir+el)
#         print('=========================finished=========================')
