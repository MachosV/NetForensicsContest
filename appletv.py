import re

def incSearch(f):
	print "==========================="
	print "	SEARCH RESULTS"
	print "==========================="
	for line in f.readlines():
		try:
			print re.search("movie&q=(.*)HTTP",line).group(1)
		except:
			pass
	print ""

def getMovies(f):
	for line in f.readlines():
		try:
			print re.search("Page-US-(.*)20",line).group(1)
		except:
			pass

def main():
	f=open("evidence03.pcap","rb")
	#incSearch(f)
	getMovies(f)	

if __name__ == '__main__':
	main()

