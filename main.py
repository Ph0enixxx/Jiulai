class App:
	def __init__(self, jobs):
		self.jobs = jobs

	def start(self):
		# TODO deal arguments
		# start all job
		for job in self.jobs:
			print("[INFO] Starting ...")
			job.start()
			job.join()
		# TODO wait

import subprocess
import time
import threading
import datetime
import os

class Job(threading.Thread):
	def __init__(self, command, period, saver):
		threading.Thread.__init__(self)
		self.command = command
		self.period = period
		self.saver = saver

	def run(self):
		while True:
			result = subprocess.check_output(self.command, shell=True).decode("utf-8")
			self.saver.save(str(result))
			time.sleep(self.period)

class CurlJob(Job):
	pass

class GitSaver:
	def __init__(self, path):
		self.path = path

	def save(self, data):
		print(data)
		path = self.path
		os.system(f"mkdir -p {path}")
		os.system(f"cd {path} && git init")
		with open(path + "index.html", "w") as fp:
			fp.write(data)
		os.system(f" cd {path} && git add *")
		os.system(f" cd {path} && git commit -m ':rainbow: changed'")

if __name__ == '__main__':
	# 这个网站是假的
	# 		CurlJob(command="""curl 'https://www.emailidfa.com/mobile' \
    # -H 'user-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1' \
    # --compressed""", period=12, saver=GitSaver("../db/emailidfa/")),
	
	# 太乱
	# app = App(jobs=[
	# 	CurlJob(command="""curl 'https://accfarm.com/buy-instagram-accounts' -H 'user-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'""", period=12, saver=GitSaver("../db/accfarm-ins/"), )
	# ])

	app = App(jobs=[
		CurlJob(command="""curl --insecure 'https://accsmarket.com/' -H 'user-agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html'""", period=12, saver=GitSaver("../db/accsmarket/"), )
	])
	print(app)
	app.start()