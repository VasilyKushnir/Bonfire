import os

def USERPROFILE():
    userprofile1 = os.getenv('USERPROFILE')
    return userprofile1    

def SaveLocation(userprofile):
    path1 = userprofile + '\\Documents\\NBGI\\DARK SOULS REMASTERED'
    if os.path.exists(path1):
        folder1 = os.listdir(path1)
    else:
        exit()
    path2 = path1 + '\\' + folder1[0] + '\\DRAKS0005.sl2'
    if os.path.exists(path2):
        return path2
    else:
        exit()

def SelectMode():
    mode1 = input('Добро пожаловать к костру. Введите команду или слово \'помощь\' для получения их списка: ')
    mode1 = mode1.lower()
    if not mode1:
        print('Команда не была введена, возвращение к титульной строке')
        return SelectMode()
    elif mode1 == 'помощь' or mode1 == 'запуск' or mode1 == 'загрузка' or mode1 == 'замена' or mode1 == 'завершение':
        return mode1
    else:
        print('Введена неверная команда, возвращение к титульной строке')
        return SelectMode()

def ShowManual():
    print('\nВведите \'запуск\' для запуска Dark Souls: Remastered\nВведите \'загрузка\' для загрузки последнего сохранения или \'замена\' для замены поледнего сохранения\nВведите \'завершение\' для выхода из этой программы\n')
    
def StartDSR():
    os.startfile('steam://rungameid/570940')
    
def UploadSave(save):
    file1 = open(os.path.dirname(save) + '\\Checkpoints\\LastSave\\DRAKS0005.sl2', 'rb')
    with open(save, 'wb') as file2:
        file2.write(file1.read())
    file1.close()
    
def ReplaceSave(save):
    file1 = open(save, 'rb')
    with open(os.path.dirname(save) + '\\Checkpoints\\LastSave\\DRAKS0005.sl2', 'wb') as file2:
        file2.write(file1.read())
    file1.close()

def CloseProgramm():
    exit()
    
while True:
    userprofile = USERPROFILE()
    save = SaveLocation(userprofile)
    mode = SelectMode()
    
    if mode == 'помощь':
        ShowManual()
    elif mode == 'запуск':
        StartDSR()
    elif mode == 'загрузка':
        UploadSave(save)
    elif mode == 'замена':
        ReplaceSave(save)
    elif mode == 'завершение':
        CloseProgramm()