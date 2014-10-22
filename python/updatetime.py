#!/usr/bin/env python

import MySQLdb
import sys


if len(sys.argv) != 2:
	print "Not correct argument"
	sys.exit(-1)

muninumber = int(sys.argv[1])


db = MySQLdb.connect(host="localhost",user="ruben",passwd="elgelg",db="beebeetle")
ecursor = db.cursor()
ecursor.execute("set names utf8")

updatestring = "date_sub(now(),INTERVAL 2 DAY)"

uquery = "update municipalities set updated="+updatestring+" where muni_id=\""+str(muninumber)+"\";"
print uquery
ret = ecursor.execute(uquery)
if(ecursor.rowcount == 0):
	uquery = "insert into municipalities (updated,muni_id) values ("+updatestring+",\""+str(muninumber)+"\");"
	print uquery
	ret = ecursor.execute(uquery)
db.commit()
db.close()
