
"""
Amity Allocator
This system makes it easy to manage rooms and people at Amity.
Usage:
	create_room <room_type> <room_name>
	add_person <person_name> <person_description> [--wants_accommodation=N]
	reallocate_person <person_identifier><new_room>
	load_people <filename>
	print_room <room_name>
	print_allocations [--o=filename]
	print_unallocated [--o=filename]
	load_state [--dbname]
	save_state [--o=db_name]
	quit
	(-i | --interactive)
Options:
	-h --help Show this screen.
	-i --interactive Interactive mode.
	-v --version
"""
import cmd

from docopt import docopt, DocoptExit
from pyfiglet import figlet_format
from termcolor import cprint

from amity import Amity


def app_exec(func):
	"""
	Decorator definition for the app.
	"""
	def fn(self, arg):
		try:
			opt = docopt(fn.__doc__, arg)
		except DocoptExit as e:
			msg = "Invalid command! See help."
			print(msg)
			print(e)
			return

		except SystemExit:
			return

		return func(self, opt)

	fn.__name__ = func.__name__
	fn.__doc__ = func.__doc__
	fn.__dict__.update(func.__dict__)

	return fn


class AmityApp(cmd.Cmd):
	intro = cprint(figlet_format("Amity Room!!!", font="cosmike"),\
				"yellow")
	prompt = "Amity --> "

	amity = Amity()

	@app_exec
	def do_create_room(self, arg):
		"""Creates a new room
		Usage: create_room <room_name> <room_type>
		"""
		room_name = arg["<room_name>"]
		room_type = arg["<room_type>"]
		self.amity.create_room(room_name, room_type)

	@app_exec
	def do_add_person(self, arg):
		"""
		Adds a person and allocates rooms if available
		Usage: add_person <person_name> <person_description> [--wants_accommodation=N]
		"""
		person_description= arg["<person_description>"]
		wants_accommodation = arg["--wants_accommodation"]
		if wants_accommodation is None:
			wants_accommodation = "N"

		person_name= arg["<person_name>"]
		self.amity.add_person(person_name, person_description, wants_accommodation=wants_accommodation)



	@app_exec
	def do_print_room(self, arg):
		"""
		Prints all the people in a given rooms
		Usage: print_room <room_name>
		"""
		self.amity.print_room(arg["<room_name>"])

	@app_exec
	def do_print_allocations(self, arg):
		"""
		Prints all offices and the people in them.
		Usage: print_allocations [--o=filename]
		"""
		filename = arg["--o"] or ""
		self.amity.print_allocations(filename)

	@app_exec
	def do_print_unallocated(self, arg):
		"""
		Prints all the people that don't have rooms
		Usage: print_unallocated [--o=filename]
		"""
		filename = arg["--o"] or ""
		self.amity.print_unallocated(filename)

	@app_exec
	def do_load_people(self, arg):
		"""
		Loads people from a text file to the app.
		Usage: load_people <filename>
		"""
		self.amity.load_people(arg["<filename>"])
		print("File loaded.")

	@app_exec
	def do_reallocate_person(self, arg):
		"""
		Reallocates person
		Usage: reallocate_person <person_name> <new_room>
		"""
		person_name = arg["<person_name>"]
		new_room = arg["<new_room>"]
		self.amity.reallocate_person(person_name, new_room)

	@app_exec
	def do_load_state(self, arg):

		"""
		Loads data from the specified db into the app.
		Usage: load_state <filename>
		"""
		self.amity.load_state(arg["<filename>"])

	@app_exec
	def do_save_state(self, arg):
		"""
		Persists app data into the given db
		Usage: save_state [--db_name=sqlite_db]
		"""
		db = arg['--db_name']
		if db:
			self.amity.save_state(db)
		else:
			self.amity.save_state()


	@app_exec
	def do_quit(self, arg):
		"""
		Exits the app.
		Usage: quit
		"""
		exit()

if __name__ == '__main__':
	AmityApp().cmdloop()
