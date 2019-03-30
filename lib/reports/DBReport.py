# -*- coding: utf-8 -*-
# This script was written by David Thompson to facilitate a database connection.
# To call this script, simply use the --database=(mandatory file here).txt flag.

from lib.reports import *
from lib.utils.FileUtils import *
import mysql.connector as mariadb
import hashlib

#Connects to the database defined below
#TODO: Create a .conf and flags for this stuff.
mariadb_connection = mariadb.connect(host = 'localhost',user = 'outpost',password = 'password',db = 'outpost')
cursor = mariadb_connection.cursor()




class DBReport(BaseReport):

    def generate(self):
        result = ''
        status = ''
        length = ''
        url = ''

        for path, status, contentLength, response in self.pathList:
            status = '{0}  '.format(status)
            length = '{0}  '.format(FileUtils.sizeHuman(contentLength).rjust(6, ' '))
            url = '{0}://{1}:{2}/'.format(self.protocol, self.host, self.port)
            url += ('{0}\n'.format(path) if self.basePath is '' else '{0}/{1}\n'.format(self.basePath, path))
            content = response.body

            pageHash = hashlib.sha256(content).hexdigest()
#This connects to the db, and inserts all the info.
            cursor.execute("INSERT INTO scanner (status,hash,length,url,content) VALUES (%s,%s,%s,%s,%s)", (status, pageHash, length, url,content))
            mariadb_connection.commit()
#this stuff is to report to the text file. I didn't feel like removing this functionality 
            result += '{0}  '.format(status)
            result += '{0}  '.format(FileUtils.sizeHuman(contentLength).rjust(6, ' '))
            result += '{0}://{1}:{2}/'.format(self.protocol, self.host, self.port)
            result += ('{0}\n'.format(path) if self.basePath is '' else '{0}/{1}\n'.format(self.basePath, path))

        return result
        return url
        print(url)
        print(result)
        print(result)
        print(result)
'''
class DBReport(BaseReport):

    def generate(self):
        result = ''

        for path, status, contentLength in self.pathList:
        	dbStatus = '{0}  '.format(status)
        	dbLength = '{0}  '.format(FileUtils.sizeHuman(contentLength).rjust(6, ' '))
        	result += '{0}://{1}:{2}/'.format(self.protocol, self.host, self.port)      
        	result += ('{0}\n'.format(path) if self.basePath is '' else '{0}/{1}\n'.format(self.basePath, path))
            #result += '{0}  '.format(status)
            #result += '{0}://{1}:{2}/'.format(self.protocol, self.host, self.port)
            #result += ('{0}\n'.format(path) if self.basePath is '' else '{0}/{1}\n'.format(self.basePath, path))

       # return result
'''



'''
with open(sitelist) as f, open(wordlist) as w:
	for url in f:
		print(url)
		print(f)
		s = url.rstrip()
		print(s)
		print(s)
		print(w)
		r = requests.get(s)+w
		print(r)
		print(r.status_code)	
		#print(r.json)
		#print(r.headers)
		#print(r.text)
		pageHash = hashlib.sha256(r.text.encode('utf-8')).hexdigest()
		print(pageHash)
		status=r.status_code
		sha256=pageHash
		length=len(r.content)
		url=url.rstrip()
		cursor.execute("INSERT INTO scanner (status,hash,length,url) VALUES (%s,%s,%s,%s)", (status, sha256, length, url))
		mariadb_connection.commit()





class DBReport(BaseReport):

    def generate(self):
        result = ''

        for path, status, contentLength in self.pathList:
            result += '{0}  '.format(status)
            result += '{0}  '.format(FileUtils.sizeHuman(contentLength).rjust(6, ' '))
            result += '{0}://{1}:{2}/'.format(self.protocol, self.host, self.port)
            result += ('{0}\n'.format(path) if self.basePath is '' else '{0}/{1}\n'.format(self.basePath, path))

        return result



#############
class DBReport(BaseReport):

    def generate(self):
        result = ''

        for path, status, contentLength in self.pathList:
            result += '{0}  '.format(status)
            result += '{0}  '.format(FileUtils.sizeHuman(contentLength).rjust(6, ' '))
            result += '{0}://{1}:{2}/'.format(self.protocol, self.host, self.port)
            result += ('{0}\n'.format(path) if self.basePath is '' else '{0}/{1}\n'.format(self.basePath, path))

        return result
'''