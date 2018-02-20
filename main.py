class MeetingManager(object):

	def __init__(self):
		self.dictionary_name = {'1':"9:00 a.m-10 a.m",
		'2':"10:30 a.m-11:30 a.m",
		'3':"12 p.m-1 p.m",
		'4':"3 p.m-4 p.m",
		'5':"4:30 p.m-5:30 p.m"}  
		self.dictionary_name2 = {}

	def time_view(self):
		for key,value in self.dictionary_name.items():
			print(key,value)

	def schedule(self):
		a=input('Enter the key to book a slot for meeting:')
		for key,value in list(self.dictionary_name.items()):
			if a in key:
				self.dictionary_name2[a]=value
				print('Meeting has been scheduled.')
				del self.dictionary_name[a]
				break
				
	def see_booked_slots(self):
		for key,value in sorted(self.dictionary_name2.items()):
			print(key,value)
		



					
				