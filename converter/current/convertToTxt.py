#!/usr/bin/python3
"""Converts any files into txt-files"""

import docTxt
import pdfTxt
import rtfTxt
import sys
import logging

logFileName = 'logfile.log'


class Converter:

    def __init__(self):
        pass

    def main():

        logging.basicConfig(filename=logFileName, level=logging.INFO)
        logging.info('Started text extract')

        path = sys.argv[1]
        #path = '/home/siegfried/python/converter/endungen/doc_example.doc'
        filename, extension = path.split(".")
        if extension == "doc":
            text = docTxt.doc_txt(path)
        if extension == "pdf":
            text = pdfTxt.pdf_txt(path)
        if extension == "rtf":
            text = rtfTxt.rtf_txt(path)
        logging.info('End text extract')
        print(text)

    if __name__ == '__main__':
        main()
