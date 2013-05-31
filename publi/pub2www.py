#! /usr/bin/python
import sys
import re

hed=[ ii for ii in open( '../raolab_header' ).readlines() ]
fot=[ ii for ii in open( '../raolab_footer' ).readlines() ]
raw=[ ii for ii in open(     sys.argv[1]    ).readlines() ]


# DEFINE PUBLICATIONS
dbp=[]
publi={}
chk={}
nl=0
for ii in raw:
	
	nl+=1

	if nl == 1: 
		new=[]
		np=ii.split()[0]
		new.append(np)

		title=ii[len(np):-1]
		new.append(title)
		

	if nl == 2: 
		author=ii.split()[0][:-1].lower()
		new.append(author)
		
		authors=ii[:-1]
		new.append(authors)

	if nl == 3: 
		
		cita=ii[:-1]
		new.append(cita)

		oup=re.search( '\((.*)\)' , ii )
		year=oup.group(1)
		new.append(year)

		jrn = "".join([ cc[0].lower() for cc in ii.split(',')[0].split() ])
		new.append(jrn)

		dbp.append(new)

	if ii=='\n': nl=0
	
dupl={}
for ii in range(len(dbp))[::-1]:
	
	pid=dbp[ii][2]+dbp[ii][5]
	try:
		dupl[pid]
		pdf="publi/"+"%s/"%dbp[ii][5]+pid+dbp[ii][6]+".pdf"
	except:
		dupl[pid]=1
		pdf="publi/"+"%s/"%dbp[ii][5]+pid+".pdf"

	dbp[ii].append(pdf)

# HEADER
if 1: 
	for ii in hed: print ii


# CONTAINER
if 1: 
	print '\t<div class="twothird">'


# FORMATING
for pp in dbp:
	
	print '<a class="box" href="%s">'%pp[7]
	print '<div class="paperbox">'
	print '<span class="normaltxt">%s <span class="title">%s.</span>'%(pp[0],pp[1])
	print '<span class="authors">%s.</span>'%pp[3]
	print '<span class="journal">%s</span>'%pp[4]
	print '</div></a>\n'

print '</div>\n'

# FOOTER
if 1: 
	for ii in fot: print ii

