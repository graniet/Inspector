#!/usr/env	python

import os,sys

# Global #######
start_dir = "/Users"
is_array = lambda var: isinstance(var, (list, tuple))
file_history = []
no_can_open = 0
uname = ""
process_list = ""
kernel_version = ""
test_list = ['w00t', ['2.4.10','2.4.16','2.4.17','2.4.18','2.4.19','2.4.20','2.4.21'],'brk',['15.2.0','2.4.10','2.4.18','2.4.19','2.4.20','2.4.21','2.4.22']]
history_listing = ['.bash_history','.mysql_history','.bashrc','.zshrc','.zsh_history']
################

def prez():
	print """  _____                           _             
  \_   \_ __  ___ _ __   ___  ___| |_ ___  _ __ 
   / /\/ '_ \/ __| '_ \ / _ \/ __| __/ _ \| '__|
/\/ /_ | | | \__ \ |_) |  __/ (__| || (_) | |   
\____/ |_| |_|___/ .__/ \___|\___|\__\___/|_|   
                 |_|                            

{c} Github.com/Graniet"""

def getShell():
	global start_dir
	if len(os.popen('find '+start_dir+' -name ".bashrc" -type f -print 2>/dev/null').read().strip()) > 1:
		return "bash"
	elif len(os.popen('find '+start_dir+' -name ".zshrc" -type f -print 2>/dev/null').read().strip()) > 1:
		return "zsh"
	else:
		return "sh?"


def getExploit():
	found = 0
	exploit_name = ""
	global test_list
	global kernel_version
	for exploit in test_list:
		if is_array(exploit):
			for version in exploit:
				if version == kernel_version:
					print "{ok} exploit found: "+exploit_name
					found = 1
		else:
			exploit_name = exploit
	if found == 0:
		print "Can't found exploit"

def checkShellHistory():
	global start_dir
	shell = getShell()
	if len(os.popen('find '+start_dir+' -name ".'+shell+'_history" -type f -print 2>/dev/null').read()) > 0:
		files = os.popen('find '+start_dir+' -name ".'+shell+'_history" -type f -print 2>/dev/null').read()
		files = files.split('\n')
		for line in files:
			if line != '':
				for element in open(line, 'r'):
					if element != '':
						print "[#] "+element.strip()
			else:
				print "{!} Can't read ."+shell+"_history"
def checkMySQL():
	global start_dir
	if len(os.popen('find '+start_dir+' -name ".mysql_history" -type f -print 2>/dev/null').read()) > 0:
		files = os.popen('find '+start_dir+' -name ".mysql_history" -type f -print 2>/dev/null').read()
		files = files.split('\n')
		for line in files:
			for element in open(line, 'r'):
				print "[#] "+element
	else:
		print "{!} Can't read .mysql_history"

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
	print "= [!] Shell > "+getShell()
	print "= [!] "+uname.strip()
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
							if '@' in line2:
								print "# SSH found"
								print "	(!) SSH used for secure connexion"
								print "	>>> "+ line2.strip()
						if "sudo" in line2:
							if 'su' in line2:
								print "# Root login ?"
								print "	>>> "+ line2.strip()
							else:
								print "# Root using ?"
								print "	>>> "+line2.strip()
													
			except:
				no_can_open = no_can_open + 1


def kernel_exploit():
	global kernel_version
	print "[!] kernel version: "+kernel_version
	getExploit()

def history_help():
	print "=========="
	print "[+] MySQL history > history mysql"
	print "[+] Shell history > history shell"
	print "=========="

def main():
	global start_dir
	x = 0
	while len(history_listing) > x:
		global file_history
		for fichier in history_listing:
			history = os.popen('find '+start_dir+' -name "'+fichier+'" -type f -print 2>/dev/null').read()
			history = history.split("\n")
			#history = open('~/.bash_history', 'r')
			for line in history:
				if(line != ""):
					file_history.append(line)
			x = x+1
		information()
	#	analyse()
		try:
			while 1:
				prompt = raw_input('Inspector > ')
				if 'forensic' in prompt:
					analyse()
				if 'process' in prompt:
					process_listname()
				if 'kernel_exploit' in prompt:
					kernel_exploit()
				if 'history mysql' in prompt:
					checkMySQL()
				if 'history shell' in prompt:
					checkShellHistory()
				if 'help' in prompt:
					information()
				if prompt == "history":
					history_help()

		except:
			print "bye ^^"
prez()
main()
