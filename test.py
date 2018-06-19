import os
import json

def enter_path():
    path_dir = input('Enter path of directory: ')

    while (True):
        #path_dir = '/home/declo/Downloads/Test_SibEDGE/test/'
        if os.path.isdir(path_dir) == False:
            print ('If you use version python3, please do not use quotes, and use it fot v2.')
            path_dir = input ('Please enter rigth path of directory: ')
        else:
            return path_dir

def work_with_files (path_dir,files_info):
    names = []
    for name in os.listdir(path_dir):
        fullname = os.path.join(path_dir, name)
        if os.path.isfile(fullname):
            names.append(name)
    json.dump(names,file_res)
    return names

def save_data_from_file (file_res):
    line = json.load(file_res)

    files_info = {}
    for name in line:
        files_info[name] = files_info.get(name,'o')            # o - old
    return files_info
        
path_dir = enter_path ()
script_dir = os.path.dirname(os.path.abspath(__file__))

files_info = {}
name = path_dir[1:].replace('/','_')
name_file = os.path.join(script_dir,name+'.json')

if os.path.exists(name_file):
    file_res = open (name_file, 'r')
    files_info = save_data_from_file (file_res)
    file_res.close()

    file_res = open(name_file,'w')
    names = work_with_files (path_dir,files_info)

    for name in names:                                            # j+4 = n
        files_info[name] = chr(ord(files_info.get(name,'j'))+4)   # n- new, s- saved, o- deleted

    for name,value in files_info.items():
        if value == 'n':
            print ('{0:25} ==> {1:25}'.format(name, 'New file'))
        elif value == 'o':
            print ('{0:25} ==> {1:25}'.format(name, 'File deleted'))
else:
    file_res = open (name_file, 'w')
    work_with_files (path_dir,files_info)



file_res.close()
