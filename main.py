import csv, urllib,re
import threading

email_list = []
email_addresses = []

print "Reading CSV File"

with open("contractors.csv", "rU") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        # print 'line[{0}] = {1}'.format(i, line)
        email_list.append(line[0])

print "Import Complete"



def thread_scan(_range):
	print "Scanning for email addresses - range {0} - {1}".format(_range[0],_range[1])

	for i in range(_range[0],_range[1]):
		print "Scanning {0} of {1} : {2}".format(i+1, len(email_list), email_list[i])
		f = urllib.urlopen(email_list[i])
		s = f.read()
		emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)

		for email in emails:
			email_addresses.append(email)

	print "Email scan complete"

	print "Writing to file"

	with open("email_addresses_{0}_{1}.csv".format(_range[0],_range[1]), "wb") as f:
	    writer = csv.writer(f, delimiter="\n")
	    writer.writerow(email_addresses)

	print "File saved"


threading.Thread(target=thread_scan, args=([0,500],)).start()
threading.Thread(target=thread_scan, args=([501,1000],)).start()

threading.Thread(target=thread_scan, args=([1001,1500],)).start()
threading.Thread(target=thread_scan, args=([1501,2000],)).start()

threading.Thread(target=thread_scan, args=([2001,2500],)).start()
threading.Thread(target=thread_scan, args=([2500,2999],)).start()



