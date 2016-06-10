#!/usr/env	python

import os,sys

# Global #######
file_history = []
no_can_open = 0
uname = ""
process_list = ""
kernel_version = ""
################

def prez():
	print """  _____                           _             
  \_   \_ __  ___ _ __   ___  ___| |_ ___  _ __ 
   / /\/ '_ \/ __| '_ \ / _ \/ __| __/ _ \| '__|
/\/ /_ | | | \__ \ |_) |  __/ (__| || (_) | |   
\____/ |_| |_|___/ .__/ \___|\___|\__\___/|_|   
                 |_|                            

{c} Github.com/Graniet"""

def information():
	global uname
	global process_list
	global kernel_version
	kernel_version = os.popen('uname -r').read()
	uname = os.popen('uname -a').read()
	process_list = os.popen('ps axco user,command | grep root').read()
	print "========="
	print "= [!] User > "+os.popen('whoami').read().strip()
	print "= [!] Group > "+os.popen('id -Gn').read().strip()[:20]  
	print "= [!] "+uname.strip()
	print "= [+] Process list command :process"
	print "= [+] Command : process,kernel_exploit,forensic" 
	print "========"

def process_listname():
	global process_list
	list_process = process_list.split('\n')
	for process in list_process:
		if 'mysql' in process:
			print "# " +process
			print "#### [!] MySQL run in root? "
		print "# " + process

def analyse():
	global file_history
	global no_can_open
	global array_analyse
	for line in file_history:
		if os.path.isfile(line):
			try:
				files = open(line, 'r')
				print "{+} " + line.strip()
				for line2 in files:
					if line2 != '':
						if 'mysql -u' in line2:
							print "# MySQL login found"
							print "	(!) MySQL commande line is used for login exemple : mysql -u root -p"
							print "	>>> " + line2.strip()
						if 'ssh' in line2:
							print "# SSH found"
							print "	(!) SSH used for secure connexion"
							print "	>>> "+ line2.strip()
													
			except:
				no_can_open = no_can_open + 1


def kernel_exploit():
	global kernel_version
	print "[!] kernel version: "+kernel_version

def main():
	global file_history
	history = os.popen('find /Users -name ".bash_history" -type f -print 2>/dev/null').read()
	history = history.split("\n")
	#history = open('~/.bash_history', 'r')
	for line in history:
		if(line != ""):
			file_history.append(line)
	information()
#	analyse()
	try:
		while 1:
			prompt = raw_input('Inspector > ')
			if 'forensic' in prompt:
				print "=========="
				analyse()
				print "=========="
			if 'process' in prompt:
				process_listname()
			if 'kernel_exploit' in prompt:
				kernel_exploit()
			if 'help' in prompt:
				information()

	except:
		print "bye ^^"
prez()
main()
