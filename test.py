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

script_dir = os.path.dirname(os.path.abspath(__file__))


        
