#Yanisse Berroteran with Abby Mcginn (lab partner)
#Lab08

#References:
#docs.python.org/3/library/...
#os.path.html, datetime.html
#StackOverflow
#geeksforgeeks.org/os-walk-python
#Referenced your hash.py file on github

import os
import csv
import hashlib
import datetime


def main():

    root = '/'  
    skipdir = ['/usr', '/boot', '/bin', '/etc', '/dev', '/proc', '/run', '/sys', '/tmp', '/var/lib', '/var/run']    #unhashable directories to skip
    filepath = '/tmp/hashes.csv'    #location of hashfile

    if os.path.exists(filepath):   #check if hash file exists
        print('Hash file already exists. Hashing and Comparing File.')

        #open and read existing .csv hashfile
        file = open(filepath)
        compare = file.readlines()
    
        changes = []    #initialize list for future changes
        writefile = open(filepath, 'w')     #open file for writing
        for root, dirs, files in os.walk(root):     #walk through root directory and check for unhashable directories from list above
            if root in skipdir:     #skip files from unhashable directories by making those lists blank
                dirs[:] = []
                files[:] = []

            for x in files:     #loop through all files not in unhashable directories
                path = os.path.join(root, x)    #filepath of current file
                hash = hashlib.sha256()

                #Open each file and hash the content
                try:
                    checkfile = open(path, 'rb')
                    while True:
                        contentbuffer = checkfile.read(4096)  #Read content of file; Linux filesystems allocate memory in directories by factors of 4096 bytes
                        if not contentbuffer:   #once complete, break out of loop
                            break
                    hash.update(contentbuffer)  #hash content of file
                    finalhash = hash.hexdigest()
                    checkfile.close()

                except IOError:
                    continue

                #get date-time and write to file    
                date_time = datetime.datetime.now()
                final = path + ';' + finalhash + ';' + str(date_time) + '\n'

                #check to see if the new hash matches old ones; if not, count as a change
                for line in compare:
                    if finalhash not in line:
                        changes.append(final)

                writefile.write(final)
        writefile.close()
        file.close()

        #print out changes
        for x in changes:
            print(x + '\n')
       

    else:
        print('Hashing and Creating File.')

        writefile = open(filepath, 'w')     #open file for writing
        for root, dirs, files in os.walk(root):     #walk through root directory and check for unhashable directories from list above
            if root in skipdir:     #skip files from unhashable directories by making those lists blank
                dirs[:] = []
                files[:] = []

            for x in files:     #loop through all files not in unhashable directories
                path = os.path.join(root, x)    #filepath of current file
                hash = hashlib.sha256()

                #Open each file and hash the content
                try:
                    checkfile = open(path, 'rb')
                    while True:
                        contentbuffer = checkfile.read(4096)  #Read content of file; Linux filesystems allocate memory in directories by factors of 4096 bytes
                        if not contentbuffer:   #once complete, break out of loop
                            break
                    hash.update(contentbuffer)  #hash content of file
                    finalhash = hash.hexdigest()
                    checkfile.close()

                except IOError:
                    continue

                #get date-time and write to file    
                date_time = datetime.datetime.now()
                final = path + ';' + finalhash + ';' + str(date_time) + '\n'
                writefile.write(final)
        #close the file
        file.close()
        



main()