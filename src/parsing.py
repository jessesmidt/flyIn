from typing import Any
import os

class Parser:
	def __init__(self, filename: str) -> None:
		self.filename: str = filename
		self.zones: dict {}
		self.connections: list = []
		self.nb_drones: int = 0

	def parse(self) -> "Graph":
		"""
		main parsing handler.
		"""
		if not os.path_exists(filename):
			raise FileNotFoundError("Configuration file '{filename}' was not found")

		with open(filename, 'r') as file:
			for line_num, line in enumerate(f, 1):
				line = line.strip()
			if not line or line.startswith('#'):
				continue

			if line.startswith('nb_drones'):
				self._parse_nb_drones(line, line_num)
			elif line.startswith('start_hub:'):
				self._parse_zone(line, line_num, 'start')
			elif line.startswith('hub:'):
				self._parse_zone(line, line_num, 'normal')
			elif line.startswith('end_hub:'):
				self._parse_zone(line, line_num, 'end')
			elif line.startswith('connection:'):
				self._parse_connection(line, line_num)
			else:
				raise ValueError(f"Line {line_num}: unknown syntax")
		return Graph(self.zones, self.connections, self.nb_drones)

	def _parse_zone(self, line: str, line_num: int) -> None:
		content = line.split(':', 1)[1].strip()
		if '[' in content:
			main, meta = content.split('[', 1)
			meta = meta.rstrip(']')
		else:
			main, meta = content, ''

		parts = main.split():
		name, x, y = parts[0], int(parts[1]), int(parts[2])
		for tag in meta.split():
			key, value = tag.split('=')

	def _parse_connection(self, line: str, line_num: int) -> None:
		pass