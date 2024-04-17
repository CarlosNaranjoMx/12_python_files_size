import os
from os.path import join

def get_size_level(directory,level):
    total = 0
    for root, dirs, files in os.walk(directory):
        valor = root.count('\\')
        if(level >= valor):
            print("root: ",root,"\ndirs: ",dirs,"\nfiles: ",files)
    return total

def get_subforlders_size(root_dir):
    print("{:<35} {:<20}".format("Nombre","Peso"))
    bytes_list  = []
    kbytes_list = []
    mbytes_list = []
    gbytes_list = []
    
    funcion_print  = lambda dir_i02,total_str02: print("{:<50} total: {:<20}".format(dir_i02,total_str02))

    for dir_i in os.listdir(root_dir):
        if dir_i.count(".") >= 1: # otra forma de preguntar si es un archivo
            pass
        else:
            total = 0

            for root, dirs, files in os.walk(join(root_dir,dir_i)):
                for file in files:
                    try:
                        total += os.path.getsize(join(root,file))
                    except FileNotFoundError:
                        print("FileNotFoundError")
                        print("root :",root,"file :",file)
                        pass
                    except OSError:
                        print("OsError")
                        print("Permisos insuficientes")

            total_gb = total / 1024**3
            total_mb = total / 1024**2
            total_kb = total / 1024

            if total_gb < 1 :
                if total_mb < 1 :
                    if total_kb < 1: 
                        total_str =  format(total,".2f") + " B"
                        bytes_list.append((dir_i,total_str,total))
                    else: 
                        total_str =  format(total_kb,".2f") + " kB"
                        kbytes_list.append((dir_i,total_str,total_kb))
                else: 
                    total_str = format(total_mb,".2f") + " mB"
                    mbytes_list.append((dir_i,total_str,total_mb))
            else: 
                total_str = format(total_gb,".2f") + " gB"
                gbytes_list.append((dir_i,total_str,total_gb))

    order_gbytes_list = sorted(gbytes_list, key=lambda x: x[2],reverse=True)
    order_mbytes_list = sorted(mbytes_list, key=lambda x: x[2],reverse=True)
    order_kbytes_list = sorted(kbytes_list, key=lambda x: x[2],reverse=True)
    order_bytes_list  = sorted(bytes_list , key=lambda x: x[2],reverse=True)

    for (dir_i02,total_str02,total_02) in order_gbytes_list: funcion_print(dir_i02,total_str02)
    for (dir_i02,total_str02,total_02) in order_mbytes_list: funcion_print(dir_i02,total_str02)
    for (dir_i02,total_str02,total_02) in order_kbytes_list: funcion_print(dir_i02,total_str02)
    for (dir_i02,total_str02,total_02) in order_bytes_list : funcion_print(dir_i02,total_str02)


if __name__=="__main__":
    # print(get_size_level(".", 0))
    get_subforlders_size(".")