# Zipfile.py - a program that can handel a zip file.
# by choeminjun

import zipfile, os, pprint


# This class help the 'chipPicer'class's function.
class helper():

    # zipfileOPENER - returns a zipfile Object.
    def zipfileOPENER(ZIPFILEPATH, ZIPFILENAME):
        try:
            os.chdir(ZIPFILEPATH)
            file = zipfile.ZipFile(ZIPFILENAME)
        except:
            return 'ERROR'
        return file


    # contentPprinter - pretty prints the 'list1' list.
    def contentPprinter(list1):
        #assert list1 != [], 'ContentPprinter-ERROR===list1V has to be a list.'
        pprint.pprint(str(list1).split('[')[1].split(']')[0])


# This is the main class that handels the main part.
class chipPicer():


    # pathPrinter - prints the path.
    def pathPrinter():
        d = os.getcwd()
        return d


    # path_finder - changes the filepath.
    def path_finder():
        print('Where is the zipfile that you want to see?')
        ZIPFILEPATH = input()
        try:
            os.chdir(ZIPFILEPATH)
        except Exception as error:
            print(error + '!! please try again!')
        return ZIPFILEPATH



    # Zreader - zipfile reader.(uses helper.zipfileOPENER.)
    def Zreader(ZIPFILEPATH):
        contents = ['']
        print('Zip file name:')
        ZIPFILENAME = input()
        print('--> reading contents...')
        try:
            file = helper.zipfileOPENER(ZIPFILEPATH, ZIPFILENAME)
        except:
            return 'ERROR'

        if file == 'ERROR':
            print('please try again~!')
            return
        else:
            contents = file.namelist()
            return contents


    # fileInfoGetter - this code gets the zipfiles file info.
    def fileInfoGetter(ZIPFILEPATH, ZIPFILENAME, filename, infoType='file_size'):
        file = helper.zipfileOPENER(ZIPFILEPATH, ZIPFILENAME)
        fileInfo = file.getinfo(filename)

        if infoType == 'file_size':
            return fileInfo.file_size

        elif infoType == 'compress_size':
            return fileInfo.compress_size

        else:
            return None

    # ZipfileMaker - a function that makes a zipfile
    def ZipfileMaker(ZIPFILENAME, txtFile, ZIPFILEPATH): # Make sure to put '.zip' at 'ZIPFILENAME'.
        os.chdir(ZIPFILEPATH)
        newZip = zipfile.ZipFile(ZIPFILENAME, 'w')

        #try:
        newZip.write(txtFile, compress_type=zipfile.ZIP_DEFLATED)
        #except:
            #newZip.close()
            #return 'ERROR'

        newZip.close()
        return



    def Extracter(ZIPFILEPATH, mode='extractall'):
        print('Zip file name:')
        ZIPFILENAME = input()

        file = helper.zipfileOPENER(ZIPFILEPATH, ZIPFILENAME)
        if file == 'ERROR':
            return 'ERROR'
        else:
            if mode == None or mode == '':
                return None
            else:
                if mode == 'extractall':
                    file.extractall()
                    print('file extractalled.')
                elif mode == 'extract':
                    extractFileNV = input('extract file name:')
                    extractPathV = input('extract path:')
                    file.extract(extractFileNV, extractPathV)
                    return 






'''>^<---test code--->^<'''
#a = chipPicer.reader('/Users/choeminjun')
#helper.contentPprinter(a)
#a = chipPicer.fileInfoGetter('/Users/choeminjun', 'exe.zip', 'eggs.txt', 'file_size')
#print(a)
#print(os.getcwd())
#b = chipPicer.ZipfileMaker('MyData.zip', 'my_data.pdf', '/Users/choeminjun/')
#print(b)
#chipPicer.Extracter('/Users/choeminjun/')