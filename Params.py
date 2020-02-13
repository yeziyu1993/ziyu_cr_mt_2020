# this is a parameter list class

class Params:
	def __init__(self, **args):
		# input default parameter values upon creating an object
		self.__dict__ = args
	
	""" parse arguments """
	def parse(self, args):
		# update parameter values according to arguments
		# parameters not mentioned in args stay unchanged
		# arguments not match any existing parameter get ignored 
		for key, value in args.items():
			if key in self.__dict__.keys():
				self.__dict__[key] = value
	
	""" return the parameter list as a dictionary """
	def dict(self):
		return self.__dict__
		
	""" return iterable """
	def items(self):
		return self.dict().items()
	
	def keys(self):
		return self.dict().keys()