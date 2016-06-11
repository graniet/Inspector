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
test_list = ['w00t', ['2.4.10','2.4.16','2.4.17','2.4.18','2.4.19','2.4.20','2.4.21'],
		'brk',['2.4.10','2.4.18','2.4.19','2.4.20','2.4.21','2.4.22'],
		'pp_key', ['3.8.0', '3.8.1', '3.8.2', '3.8.3', '3.8.4', '3.8.5', '3.8.6', '3.8.7', '3.8.8', '3.8.9', '3.9', '3.10', '3.11', '3.12', '3.13', '3.4.0', '3.5.0', '3.6.0', '3.7.0', '3.8.0', '3.8.5', '3.8.6', '3.8.9', '3.9.0', '3.9.6', '3.10.0', '3.10.6', '3.11.0', '3.12.0', '3.13.0', '3.13.1'],
		'overlayfs', ['3.8.0','3.8.1', '3.8.2', '3.8.3', '3.8.4', '3.8.5', '3.8.6', '3.8.7', '3.8.8', '3.8.9', '3.9', '3.10', '3.11', '3.12', '3.13', '3.4.0', '3.5.0', '3.6.0', '3.7.0', '3.8.0', '3.8.5', '3.8.6', '3.8.9', '3.9.0', '3.9.6', '3.10.0', '3.10.6', '3.11.0', '3.12.0', '3.13.0', '3.13.1'],
		'rawmodePTY', ['2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36', '2.6.37', '2.6.38', '2.6.39', '3.14', '3.15'],
		'timeoutpwn', ['3.4 ', '3.5 ', '3.6 ', '3.7 ', '3.8 ', '3.8.9 ', '3.9 ', '3.10 ', '3.11 ', '3.12 ', '3.13 ', '3.4.0 ', '3.5.0 ', '3.6.0 ', '3.7.0 ', '3.8.0 ', '3.8.5 ', '3.8.6 ', '3.8.9 ', '3.9.0 ', '3.9.6 ', '3.10.0 ', '3.10.6 ', '3.11.0 ', '3.12.0 ', '3.13.0 ', '3.13.1'],
		'perf_swevent', ['3.0.0', '3.0.1', '3.0.2', '3.0.3', '3.0.4', '3.0.5', '3.0.6', '3.1.0', '3.2', '3.3', '3.4.0', '3.4.1', '3.4.2', '3.4.3', '3.4.4', '3.4.5', '3.4.6', '3.4.8', '3.4.9', '3.5', '3.6', '3.7', '3.8.0', '3.8.1', '3.8.2', '3.8.3', '3.8.4', '3.8.5', '3.8.6', '3.8.7', '3.8.8', '3.8.9'],
		'msr', ['2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36', '2.6.37', '2.6.38', '2.6.39', '3.0.0', '3.0.1', '3.0.2', '3.0.3', '3.0.4', '3.0.5', '3.0.6', '3.1.0', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7.0', '3.7.6'],
		'memodipper', ['2.6.39', '3.0.0', '3.0.1', '3.0.2', '3.0.3', '3.0.4', '3.0.5', '3.0.6', '3.1.0'],
		'american-sign-language', ['2.6.0', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36'],
		'full-nelson', ['2.6.31', '2.6.32', '2.6.35', '2.6.37'],
		'half_nelson', ['2.6.0', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36'],
		'rds', ['2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36'],
		'pktcdvd', ['2.6.0', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36'],
		'ptrace_kmod2', ['2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34'],
		'video4linux', ['2.6.0', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33'],
		'can_bcm', ['2.6.18','2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36'],
		'reiserfs', ['2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34'],
		'do_pages_move', ['2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31'],
		'pipe.c_32bit', ['2.4.4', '2.4.5', '2.4.6', '2.4.7', '2.4.8', '2.4.9', '2.4.10', '2.4.11', '2.4.12', '2.4.13', '2.4.14', '2.4.15', '2.4.16', '2.4.17', '2.4.18', '2.4.19', '2.4.20', '2.4.21', '2.4.22', '2.4.23', '2.4.24', '2.4.25', '2.4.26', '2.4.27', '2.4.28', '2.4.29', '2.4.30', '2.4.31', '2.4.32', '2.4.33', '2.4.34', '2.4.35', '2.4.36', '2.4.37', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31'],
		'udp_sendmsg_32bit', ['2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19'],
		'sock_sendpage', ['2.4.4', '2.4.5', '2.4.6', '2.4.7', '2.4.8', '2.4.9', '2.4.10', '2.4.11', '2.4.12', '2.4.13', '2.4.14', '2.4.15', '2.4.16', '2.4.17', '2.4.18', '2.4.19', '2.4.20', '2.4.21', '2.4.22', '2.4.23', '2.4.24', '2.4.25', '2.4.26', '2.4.27', '2.4.28', '2.4.29', '2.4.30', '2.4.31', '2.4.32', '2.4.33', '2.4.34', '2.4.35', '2.4.36', '2.4.37', '2.6.0', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30'],
		'sock_sendpage2', ['2.4.4', '2.4.5', '2.4.6', '2.4.7', '2.4.8', '2.4.9', '2.4.10', '2.4.11', '2.4.12', '2.4.13', '2.4.14', '2.4.15', '2.4.16', '2.4.17', '2.4.18', '2.4.19', '2.4.20', '2.4.21', '2.4.22', '2.4.23', '2.4.24', '2.4.25', '2.4.26', '2.4.27', '2.4.28', '2.4.29', '2.4.30', '2.4.31', '2.4.32', '2.4.33', '2.4.34', '2.4.35', '2.4.36', '2.4.37', '2.6.0', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30'],
		'exit_notify', ['2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29'],
		'udev', ['2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29'],
		'ftrex', ['2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22'],
		'vmsplice2', ['2.6.23', '2.6.24'],
		'vmsplice1', ['2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.24.1'],
		'h00lyshit', ['2.6.8', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16'],
		'raptor_prctl', [ '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17'],
		'elflbl', ['2.4.29'],
		'caps_to_root', ['2.6.34', '2.6.35', '2.6.36'],
		'mremap_pte', ['2.4.20', '2.2.24', '2.4.25', '2.4.26', '2.4.27'],
		'krad3', ['2.6.5', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11']]
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
				version = version.strip()
				kernel_version = kernel_version.strip()
				if version in kernel_version:
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
	print "= [+] Command : help,search,process,kernel_exploit,forensic" 
	print "========"

def process_listname():
	global process_list
	list_process = process_list.split('\n')
	for process in list_process:
		if 'mysqld' in process:
			print "# " +process
			print "	{!} MySQL run in root? =)"
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
							print "__________________________________________"
							print "| MySQL login found"
							print "|_	(!) MySQL commande line is used for login exemple : mysql -u root -p"
							print "   \	>>> " + line2.strip()
							print "     \______________________________________"
						if 'ssh' in line2:
							if '@' in line2:
								print "__________________________________________"
								print "| SSH found"
								print "|_	(!) SSH used for secure connexion"
								print "   \	>>> "+ line2.strip()
								print "     \____________________________________"
						if "sudo" in line2:
							if 'sudo su' in line2:
								print "__________________________________________"
								print "| Root login?"
								print " \	>>> "+ line2.strip()
								print "   \______________________________________"
							else:
								print "__________________________________________"
								print "| Command with root usage?"
								print " \	>>> "+line2.strip()
								print "   \_______________________________________"
													
			except:
				no_can_open = no_can_open + 1


def kernel_exploit():
	global kernel_version
	print "[!] kernel version: "+kernel_version
	getExploit()

def search_file(prompt):
	var = 0
	try:
		if "=" in prompt:
			value = prompt.split('=')[1]
			print "Start search > " + value
			try:
				history = os.popen('find '+start_dir+' -name "'+value+'" -type f -print 2>/dev/null').read()
				space = history.split('\n')
				for line in space:
					if line != '':
						print "{+} "+line.strip()
						var = var + 1
				if var == 0:
					print "{-} No file found :("
			except:
				print "Error on search"
	except:
		print "Error please leave issue"

def history_help():
	print "=========="
	print "[+] MySQL history > history mysql"
	print "[+] Shell history > history shell"
	print "=========="

def search_help():
	print "========"
	print "[+] search file=name.txt"
	print "========"

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
				if prompt == "search":
					search_help()
				if 'search file=' in prompt:
					search_file(prompt)
				if prompt == "history":
					history_help()
				if prompt == "clear":
					os.system('clear')

		except:
			print "bye ^^"
prez()
main()
#kernel_exploit()
