import datetime

def nowStr():
	d = datetime.datetime.now()
	string = "{date:%Y-%m-%d %H:%M:%S}".format(date=d)
	return string

if __name__ == "__main__":
	print(nowStr())