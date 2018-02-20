from main import MeetingManager

meeting=MeetingManager()
while True:
	choice=int(input('What would you like to do?\n \
		1.Check available time slots\n \
		2.Book a slot\n \
		3.See booked slots\n \
		4.Exit\n'))
	if choice==1:
		meeting.time_view()
	elif choice==2:
		meeting.schedule()
	elif choice==3:
			meeting.see_booked_slots()
	else:
		break			