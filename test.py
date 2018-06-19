import os

def enter_path():
    #path_dir = input ('Enter path of directory: ')

    while (True):
        path_dir = '/home/declo/Downloads/Test_SibEDGE/test/'
        if os.path.isdir(path_dir) == False:
            #path_dir = input ('Please enter rigth path of directory: ')
            print ('Wrong')
        else:
            return path_dir

def work_with_files (path_dir):
    to_write = ''
    files = os.listdir(path_dir)
    for name in files:
        fullname = os.path.join(path_dir, name)
        if os.path.isfile(fullname):
            to_write = to_write + '"' + name + '",'
    file_res.write ('[%s]' % (to_write[:len(to_write)-1]))

        
path_dir = enter_path ()
script_dir = os.path.dirname(os.path.abspath(__file__))

name_file = os.path.join(script_dir,'result.txt')
#if os.path.exists(name_file):
    
file_res = open (name_file, 'w')     


file_res.close()
