import os
import shutil

FOLDER_TYPES = {
              'pPDF':['pdf'],
              'Pimages':['png','jpeg','jpg','gif'],
              'Pvideos':['mp4','mkv','avi','3gp'],
              'Paudios':['mp3','wav'],
              'Pprograms':['exe'],
              'Pdocs':['xlsx','doc','xlsx','pptx','csv','txt','ppt']
}
RESULT_DIR = 'output'

def identifyType(ext):
    '''
    Accept extenssion Example .pdf .mp4 and
    return a category type from FOLDER_TYPES Dictionary
    '''
    ext = ext[1:]
    for key, value in FOLDER_TYPES.items():
        if ext in value: return key
    return None


def makeFolders(lst) -> None:
    '''
    Accept A List of Folder name and
    create that category name folder in RESULT_DIR
    '''
    if os.path.exists(RESULT_DIR) is False: os.mkdir(RESULT_DIR)
    for name in lst:
        if name in os.listdir(RESULT_DIR): return None
        os.mkdir(os.path.join(RESULT_DIR, name))
    return None


def moveFiles(src, dst) -> bool:
    '''
    Accept source and destination and move files .
    Return True if File is Copied other wise False
    '''
    try:
        shutil.move(src,os.path.join(RESULT_DIR,dst))
    except:
        return False
    return True

makeFolders(FOLDER_TYPES.keys())

def startProcess(folder, file):
    '''
    Accept file name and parent folder_name(folder)
    Return a Tuple(TRUE|FALSE,TYPE_OF_FILE)
    '''
    types = os.path.splitext(file)[1].lower()
    src = os.path.join(folder,file)
    dst = identifyType(types)
    if not dst is None: return moveFiles(src, dst), dst
    return False, 'Others(Not_moved)'

def strong_arrange() -> dict:
    TOTAL_COUNT: dict = {}
    for foldername, subfolders, filenames in os.walk(folder):
        for file in filenames:
            if os.path.isfile(os.path.join(folder, file)):
               status,types = startProcess(folder, file)
               if types in TOTAL_COUNT:
                   TOTAL_COUNT[types] = TOTAL_COUNT[types] + 1
               else:
                   TOTAL_COUNT[types] = 1
    return TOTAL_COUNT

def arrange() _. dict:
    TOTAL_COUNT: dict = {}
    for file in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, file)):
            status,types = startProcess(folder, file)
            if types in TOTAL_COUNT:
                TOTAL_COUNT[types] = TOTAL_COUNT[types] + 1
            else:
                TOTAL_COUNT[types] = 1
    return TOTAL_COUNT

if __name__ == '__main__':
    print("Arrange files")
    folder = os.getcwd()
    print(folder)
    while True:
      try:
        choice = int(input("Press 1 for Weak arrange\nPress 2 for Strong arrange\n0 to exit\noption:"))
        break
      except ValueError:
        print("invalid input
    choices = {1: arrange, 2: strong_arrange, exit}
    choices[choice]()
    others="Others(Not_moved)"
    print(f'{"Result":*^30s}')
    for key, value in res.items():
        if key != others:
            print(f'{value} file moved into Category {os.path.join(RESULT_DIR,key)}')
    print(f'{res[others]} file Not moved')
