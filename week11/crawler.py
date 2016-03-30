from bs4 import BeautifulSoup
import pprint
import requests
import urllib
from collections import deque
from termcolor import colored
import re

url = "http://start.bg/"
top_level_domain = ".bg"
isBG = True

def get_links(page):
	links_list = []

	# deal with Timeout exception
	try:
		r = requests.get(page, timeout=3)
		html = r.text
		soup = BeautifulSoup(html, "html.parser")

		for tag in soup.findAll('a', href=True):
			joined = urllib.parse.urljoin(url, tag['href'])
			a = urllib.parse.urlparse(joined).netloc
			isBG = a.endswith(top_level_domain) # is it a Bulgarian site?
			b = urllib.parse.urlparse(joined).path
			new_url = "http://" + str(a) + str(b)

			links_list.append(joined)
	except:
		print("Page timeout error!")

	return links_list

def get_histogram(root_url):
	servers = crawler(root_url)
	result = {}

	for value in servers.values():
		if value not in result.keys():
			result[value] = 1
		else:
			result[value] += 1

	return result

def crawler(root_url):
	frontier = deque()
	servers_map = {}
	frontier.append(root_url)
	visited = [root_url]
	count = 0

	while frontier and count <= 1:
		links = get_links(frontier[0])
		frontier.popleft()

		for index, link in enumerate(links):
			a = urllib.parse.urlparse(link).netloc
			isBG = a.endswith(top_level_domain) # is it a Bulgarian site?
			b = urllib.parse.urlparse(link).path
			new_url = "http://" + str(a) + str(b)

			if new_url not in visited and isBG:
				
				# deal with Timeout exception
				try:
					r1 = requests.head(new_url, timeout=1)
					print(new_url + " ==> " + colored(r1.headers.get('Server'), 'cyan'))
				except:
					print(colored("Page timeout error!", 'red'))

			if a not in servers_map.keys():
				# check server name using regular expressions	
				try:
					regex = re.compile('(apache|nginx|IIS|lighttpd)', re.IGNORECASE)
					server = re.search(regex, r1.headers.get('Server'))
					servers_map[a] = server.group()
				except:
					print(colored("Error", 'magenta'))

			visited.append(new_url)
			frontier.append(new_url)
			
			if index > 400:
				break

		count += 1

	return servers_map

def main():
	servers_map = get_histogram(url)

	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(servers_map)


if __name__ == "__main__":
	main()