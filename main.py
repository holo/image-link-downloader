import os, urllib.request

cyan = '\033[36m'
off = '\033[0m'

def ui():
	os.system('cls' if os.name in ('nt', 'dos') else 'clear')
	print(rf"""
		 _ _       _       _                     _                 _           
		| (_)     | |     | |                   | |               | |          
		| |_ _ __ | | ____| | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
		| | | '_ \| |/ / _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
		| | | | | |   < (_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
		|_|_|_| |_|_|\_\__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                              by {colour('alf')}""")

def colour(text):
	return cyan+str(text)+off

def setup():
	try:
		os.mkdir("output")
	except:
		pass

	with open("links.txt", "a"):
		pass

def download():
	with open("links.txt", "r") as f:
		count = 0
		links = f.readlines()
		for link in links:
			try:
				urllib.request.urlretrieve(link.strip(), f"./output/{link.strip().split('/')[-1]}")
			except:
				pass
			count += 1
			print(f"		    [{colour('*')}] Downloaded ({colour(count)}/{colour(len(links))})", end="\r")

if __name__ == "__main__":
	ui()
	setup()
	print(f"		    [{colour('*')}] Put images links in {colour('links')}.{colour('txt')}")
	input(f"		    [{colour('!')}] Press {colour('enter')} to continue")
	ui()
	download()
	input()
