class diseaseReport(object):

	def __init__(self):
		self.reporter = ""
		self.severity = 1
	
	def setSeverity(self,sev):
		self.severity = sev
	
dr = diseaseReport()

print(dr.severity)
dr.setSeverity(4)
print(dr.severity)
