import aiml
import os.path
import sys


class AimlBot:
	brainFileName = "politics-bot-brain.brn"
	kernel = aiml.Kernel()
	botName = "Ivan"

	def __init__(self):
		self.kernel.verbose(False)
		self.kernel.setBotPredicate("name", self.botName)

		if os.path.isfile(self.brainFileName):
		    self.kernel.bootstrap(brainFile = self.brainFileName)
		else:
		    self.kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
		    self.kernel.saveBrain(self.brainFileName)

	# runs bot on input and returns answer
	def run(self, inputString):
		answer =  self.kernel.respond(inputString) # second argument is string
		self.kernel.saveBrain(self.brainFileName)
		return answer
		
	# clears bot's brain
	def clearBrain(self):
		os.remove(self.brainFileName)
	
	# method for runing bot with command line for testing and debugging
	def runWithCommandLine(self):
		try:
			while True: 
				print self.kernel.respond(raw_input("> "))
		except KeyboardInterrupt:
			self.kernel.saveBrain(self.brainFileName)
			return

def testBot(bot):
	if len(sys.argv) == 2:
		if sys.argv[1] == "--cline": # command line input
			bot.runWithCommandLine()
			return
		else:
			answer = bot.run(sys.argv[1])
			return answer
	else: 
		print "Pass parameter '--cline' (for using command line) or string"
		return


bot = AimlBot()
print testBot(bot)