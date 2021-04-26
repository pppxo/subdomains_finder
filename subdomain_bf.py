import requests

protocol = input('Protocol: ')
website = input('Website: ')
list= input('list: ')

pathlist = open(list).read().splitlines()
i=1

print("Subdomains Founded: ")
for subdomain in pathlist:
	try:
		if (requests.get(protocol+'://'+subdomain+'.'+website).status_code == 200):
			print(i, " =>" , protocol+'://'+subdomain+'.'+website)
			i+=1
		elif (requests.get(protocol+'://'+subdomain+'.'+website).status_code == 301):
			print(i, " =>" ,protocol+'://'+subdomain+'.'+website, "(Moved Permanently)")
			i+=1
		else:
			pass
	except:
		pass
		




