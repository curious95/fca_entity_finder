from io import StringIO, BytesIO
import urllib.request
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re, tabula
import PyPDF2
from tika import parser
from pdfminer.converter import HTMLConverter
import pyap
import json
from datetime import datetime
from elasticsearch import Elasticsearch


def render_pdf(url):
    text_data = ''
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Open the url provided as an argument to the function and read the content
    f = urllib.request.urlopen(url).read()
    # Cast to StringIO object
    fp = BytesIO(f)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 5
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp,
                                  pagenos,
                                  maxpages=maxpages,
                                  password=password,
                                  caching=caching,
                                  check_extractable=True):

        interpreter.process_page(page)
        data = retstr.getvalue()
        text_data = text_data+' '+data
        data = ''
        retstr.truncate(0)
        retstr.seek(0)

    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()

    return text_data