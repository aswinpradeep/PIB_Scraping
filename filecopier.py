import os
import csv
import errno
import os
import shutil

total = 0
with open("countfile.csv") as csv_file:
   for row in csv.reader(csv_file, delimiter=','):
        path=row[0]+"/"+row[1]+"/"+row[2]+"/"+row[3]
        print(str(path))
        src = "./"+row[3]+".txt"
        dest = "./Categorizedtxtfiles/"+row[0]+"/"+row[1]+"/"+row[2]+"/"+row[3]+".txt"
        try:
            try:
                shutil.copy(src, dest)
                print(row[3]," *** SUCCESS ***")
            except IOError as e:
                # ENOENT(2): file does not exist, raised also on missing dest parent dir
                if e.errno != errno.ENOENT:
                    raise
                # try creating parent directories
                os.makedirs(os.path.dirname(dest))
                shutil.copy(src, dest)
        except Exception as e:
            print(e)        
            print(e)
            print(row[3]," *** failed ***")
            file2 = open("failedfiles.txt","a")
            file2.write("\n")
            file2.write(str(row[3])) 
            file2.close()

