import os, fnmatch, sys, shutil, string, unicodedata

def moveFiles(files : [], overwrite : bool):
    for source, target in files:
        pos       = target.rfind("/")
        targetDir = "./"
        if pos != -1:
            targetDir = target[:pos]
        
        # check if directory exists or not yet
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)

        if os.path.isfile(target) and overwrite:
            os.remove(target)

        if os.path.exists(targetDir):
            print ('move ' + source + ' target' + target)
            shutil.move(source, target)

def isFileToBeAddToList(file, ignorePattern):
    for x in ignorePattern:
        if fnmatch.fnmatch(file, x):
            return False
    return True

def getFileList(path, ignorePattern):
    fileList = []

    for root, dirs, files in os.walk(path):
        for file in files:
            f = os.path.join(root,file)
            if isFileToBeAddToList(f, ignorePattern):
                fileList.append(f)
    
    return fileList

validFilenameChars = ":-_.()/ %s%s" % (string.ascii_letters, string.digits)

def removeDisallowedFilenameChars(filename):
    cleanedFilename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode('utf-8')
    return ''.join(c for c in cleanedFilename if c in validFilenameChars)