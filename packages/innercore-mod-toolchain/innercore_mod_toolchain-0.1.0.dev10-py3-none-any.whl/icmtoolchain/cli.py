import sys
from typing import Optional


def show_help():
	print("Usage: icmtoolchain [options] ... <task1> [arguments1] ...")
	print(" " * 2 + "--help: Display this message.")
	print(" " * 2 + "--list: See available tasks.")
	print("Perform commands marked with a special decorator @task.")
	print("Example: icmtoolchain selectProject --path mod1 pushEverything selectProject --path mod2 pushEverything launchApplication")

def show_available_tasks():
	from .task import TASKS
	print("All available tasks:")
	for name, task in TASKS.items():
		print(" " * 2 + name, end="")
		if task.description:
			print(": " + task.description, end="")
		print()

def run(argv: Optional[list[str]] = None):
	if not argv or len(argv) == 0:
		argv = sys.argv
	if "--help" in argv or len(argv) <= 1:
		show_help()
		exit(0)
	if "--list" in argv:
		show_available_tasks()
		exit(0)

	from time import time
	startup_millis = time()
	argv = argv[1:]

	from .parser import apply_environment_properties, parse_arguments
	from .shell import abort, debug, error, warn
	from .task import TASKS

	try:
		targets = parse_arguments(argv, TASKS, lambda name, target, callables: warn(f"* No such task: {name}."))
	except (TypeError, ValueError) as err:
		error(" ".join(argv))
		abort(cause=err)

	apply_environment_properties()

	anything_performed = False
	tasks = iter(targets)
	while True:
		try:
			callable = next(tasks)
		except StopIteration:
			break
		else:
			try:
				result = callable.callable()
				if result != 0:
					abort(f"* Task {callable.name} failed with result {result}.", code=result)
			except BaseException as err:
				if isinstance(err, SystemExit):
					raise err
				from .utils import RuntimeCodeError
				if isinstance(err, RuntimeCodeError):
					abort(f"* Task {callable.name} failed with error code #{err.code}: {err}")
				abort(f"* Task {callable.name} failed with unexpected error!", cause=err)
			anything_performed = True

	if not anything_performed:
		debug("* No tasks to execute.")
		exit(0)

	from .task import unlock_all_tasks
	unlock_all_tasks()

	startup_millis = time() - startup_millis
	debug(f"* Tasks successfully completed in {startup_millis:.2f}s!")

def test_printing_text():
	from prompt_toolkit import ANSI, HTML, print_formatted_text
	from prompt_toolkit.formatted_text import FormattedText

	# from prompt_toolkit.formatted_text import PygmentsTokens
	# import pygments
	# from pygments.token import Token
	# from pygments.lexers.python import PythonLexer

	print_formatted_text("aboba")
	print_formatted_text(HTML("<ansired><b><i>Red italic and bold aboba</i></b></ansired>"))
	print_formatted_text(HTML('<aaa fg="ansiwhite" bg="ansigreen">White on green aboba</aaa>'))

	print_formatted_text(ANSI('\x1b[31mHeya \x1b[32maboba'))

	ftext_aboba = [
		('red', 'Hello'),
		('', ' '),
		('#44ff00 italic', 'aboba'),
	]
	print_formatted_text(FormattedText(ftext_aboba))

	# ptext_aboba = [
	# 	(Token.Keyword, 'print'),
	#     (Token.Punctuation, '('),
	#     (Token.Literal.String.Double, '"'),
	#     (Token.Literal.String.Double, 'hello'),
	#     (Token.Literal.String.Double, '"'),
	#     (Token.Punctuation, ')'),
	# ]
	# print_formatted_text(PygmentsTokens(ptext_aboba))

	# tokens = list(pygments.lex('print("Hello")', lexer=PythonLexer()))
	# print_formatted_text(PygmentsTokens(tokens))

def test_asking_for_input():
	import getpass

	from prompt_toolkit import HTML, PromptSession, prompt
	from prompt_toolkit.completion import (Completer, Completion, NestedCompleter,
	                                       WordCompleter)
	from prompt_toolkit.styles import Style
	from prompt_toolkit.validation import Validator

	prompt("What is your name: ", default=f"{getpass.getuser()}")
	# print(f"You said: {simple_text}")

	# session = PromptSession()
	# session_text_1 = session.prompt()
	# session_text_2 = session.prompt()

	html_completer = WordCompleter(["<b>", "<i>", "<a>", "<h1>", "<h2>", "<br>", "<a link='aboba'>", "<table>", "<td>", "<tr>"])
	html_text = prompt("Enter something with html tags: ", completer=html_completer)

	nested_completer = NestedCompleter.from_nested_dict({
		"show": {
			"version": None,
			"clock": None,
			"ip": {
				"interface": {"brief"}
			}
		},
		"exit": None,
	})
	nested_text = prompt("# Nested commands (show or exit): ", completer=nested_completer)

	class MyCustomCompleter(Completer):
		def get_completions(self, document, complete_event):
			from time import sleep
			sleep(1.0)

			# Display this completion, black on yellow.
			yield Completion(
				"completion1",
				start_position=0,
				style="bg:ansiyellow fg:ansiblack"
			)

			# Underline completion.
			yield Completion(
				"completion2",
				start_position=0,
				style="underline"
			)
	example_custom_style = Style.from_dict({
    	"rprompt": "bg:#ff0066 #ffffff",
	})
	custom_text = prompt("Custom: ", completer=MyCustomCompleter(), rprompt="something with <completion>", complete_in_thread=True, style=example_custom_style)

	def is_number(text):
		return text.isdigit()
	validator = Validator.from_callable(
		is_number,
		error_message="This input contains non-numeric characters",
		move_cursor_to_end=True
	)
	def bottom_toolbar():
		return HTML("This is a <b><style bg=\"ansired\">Toolbar</style></b>!")
	number_text = int(prompt("Give a number: ", validator=validator, bottom_toolbar=bottom_toolbar))

	def prompt_continuation(width, line_number, is_soft_wrap):
		return " " * width
	prompt(
		"multiline input> ",
		multiline=True,
		mouse_support=True,
		wrap_lines=False,
		prompt_continuation=prompt_continuation
	)

import asyncio


async def do_async_input():
	from prompt_toolkit import PromptSession, print_formatted_text
	from prompt_toolkit.patch_stdout import patch_stdout
	await asyncio.sleep(3.0)

	session = PromptSession()
	with patch_stdout():
		print_formatted_text()
		result = await session.prompt_async("What a beautiful day! ")

	await asyncio.sleep(1.0)
	print(f"You said: {result}")

async def do_job():
	from prompt_toolkit import print_formatted_text
	from prompt_toolkit.patch_stdout import patch_stdout
	with patch_stdout():
		print_formatted_text("[] aboba job 0/3", end="\r")
	await asyncio.sleep(3.0)
	with patch_stdout():
		print_formatted_text("[] aboba job 1/3", end="\r")
	await asyncio.sleep(3.0)
	with patch_stdout():
		print_formatted_text("[] aboba job 2/3", end="\r")
	await asyncio.sleep(3.0)
	with patch_stdout():
		print_formatted_text("[] aboba job done", end="\r")

async def call_my_fucking_tasks():
	await asyncio.gather(do_job(), do_async_input())

# asyncio.run(call_my_fucking_tasks())

def simple_async_test():
	from itertools import cycle

	from prompt_toolkit import Application
	from prompt_toolkit.key_binding import KeyBindings
	from prompt_toolkit.layout import HSplit, Layout, VerticalAlign
	from prompt_toolkit.widgets import TextArea


	class AnimatedTask:
		def __init__(self, project, messages, frames, speed, metadatas = None):
			self.project = project
			self.messages = messages if isinstance(messages, list) else [messages]
			self.frames = cycle(frames)
			self.speed = speed
			self.content = TextArea(text="")
			self.metadata = ""
			self.metadatas = metadatas if isinstance(metadatas, list) else [metadatas if metadatas else ""]
			self.description = TextArea(text="")
			self.steps = 0
			self.offset = 0
			self.moffset = 0

		async def run(self):
			while True:
				if self.steps % 30 == 0:
					self.message = self.messages[self.offset]
					self.offset = self.offset + 1 if self.offset + 1 < len(self.messages) else 0
				if self.steps % 10 == 5:
					from random import randint
					if randint(0, 10) < 3:
						self.metadata = ""
					else:
						self.metadata = self.metadatas[self.moffset]
						self.moffset = self.moffset + 1 if self.moffset + 1 < len(self.metadatas) else 0
				self.steps += 1
				self.content.text = f"{next(self.frames)} [{self.project}] {self.message}"
				self.description.text = "   " * 2 + f"{self.metadata}"
				await asyncio.sleep(self.speed)

	# Конфигурация задач
	task1 = AnimatedTask(
		project="Modding Tools",
		messages="Gathering libraries metadata...",
		frames=["▁","▂","▃","▄","▅","▆","▇","█"],
		speed=0.2,
		metadatas=[
			"https://nernar.github.io/metadata/libraries/latest/BlockEngine.json",
			"https://nernar.github.io/metadata/libraries/latest/StorageInterface.json",
			"https://nernar.github.io/metadata/libraries/latest/Transition.json",
			"https://nernar.github.io/metadata/libraries/latest/BetterQuesting.json",
		]
	)
	task2 = AnimatedTask(
		project="Modding Tools: Block",
		messages="Transpiling TypeScript into JavaScript...",
		frames=["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"],
		speed=0.1,
		metadatas=[
			"script/header.js",
			"script/data/BLOCK_VARIATION.js",
			"script/data/CategoryListAdapter.js",
			"script/data/SPECIAL_TYPE.js",
			"script/data/TextureSelector.js",
			"script/data/TextureSelectorListAdapter.js",
		]
	)
	task3 = AnimatedTask(
		project="Modding Tools: Dimension",
		messages="Compiling Java... 56/234 classes",
		frames=["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"],
		speed=0.15
	)
	task4 = AnimatedTask(
		project="Modding Tools: Ui",
		messages="Pushing to ZBKL631... assets/ (30/142)",
		frames=["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"],
		speed=0.05
	)

	# Создаём layout с разделёнными областями
	root_container = HSplit([
		HSplit([
			task1.content,
			task1.description,
		], align=VerticalAlign.TOP),
		HSplit([
			task2.content,
			task2.description,
		], align=VerticalAlign.TOP),
		HSplit([
			task3.content,
			task3.description,
		], align=VerticalAlign.TOP),
		HSplit([
			task4.content,
			task4.description,
		], align=VerticalAlign.TOP),
	], align=VerticalAlign.JUSTIFY)

	layout = Layout(root_container)
	kb = KeyBindings()

	@kb.add("c-c")
	def exit_(event):
		event.app.exit()

	async def main():
		app = Application(
			layout=layout,
			key_bindings=kb,
			full_screen=False
		)
		await asyncio.gather(
			app.run_async(),
			task1.run(),
			task2.run(),
			task3.run(),
			task4.run(),
		)
		# app.create_background_task(task1.run())
		# app.create_background_task(task2.run())
		# await app.run_async()

	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print("\nAnimation stopped gracefully.")

simple_async_test()
