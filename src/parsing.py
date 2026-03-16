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
				if self.start_hub is not None:
					raise ValueError(f"Line {line_num}: duplicate start_hub")
				self._parse_zone(line, line_num, 'start')
			elif line.startswith('hub:'):
				self._parse_zone(line, line_num, 'normal')
			elif line.startswith('end_hub:'):
				if self.end_hub is not None:
					raise ValueError(f"Line {line_num}: duplicate end_hub")
				self._parse_zone(line, line_num, 'end')
			elif line.startswith('connection:'):
				self._parse_connection(line, line_num)
			else:
				raise ValueError(f"Line {line_num}: unknown syntax")

		self._validate(line_num)	
		return Graph(self.zones, self.connections, self.nb_drones)

	def _parse_nb_drones(self, line: str, line_num: int) -> None:
		"""

		"""
		if ':' not in line:
			raise ValueError(f"Line {line_num}: expected 'nb_drones: <number>'")

		content = line.split(':', 1)[1].strip()

		if not content:
			raise ValueError(f"Line {line_num}: nb_drones value is missing")
		try:
			self.nb_drones = int(content)
		except ValueError:
			raise ValueError(f"Line {line_num}: {key} must be an integer")

		if self.nb_drones <= 0:
			raise ValueError(f"Line {line_num}: {key} must be a positive integer")		

	def _parse_zone(self, line: str, line_num: int) -> None:
		"""

		"""
		content = line.split(':', 1)[1].strip()
		if '[' in content:
			main, meta = content.split('[', 1)
			meta = meta.rstrip(']')
		else:
			main, meta = content, ''

		parts = main.split():
		if len(parts) < 3:
			raise ValueError(f"Line {line_num}: expected name x y")

		name = parts[0]
		
		try:
			x, y = int(parts[1]), int(parts[2])
		except ValueError:
			raise ValueError(f"Line {line_num}: coordinates must be integers")
		if x < 0 or y < 0:
			raise ValueError(f"Line {line_num}: coordinates must be positive integers")
		if name in self.zones:
			raise ValueError(f"Line {line_num}: duplicate zone name  {name}")

		metadata = self._parse_metadata(meta, line_num)
		zone_type = metadata.get('zone', 'normal')
		color = metadata.get('color', None)
		max_drones = int(metadata.get('max_drones', 1))
		# self.zones[name] = Zone(name, x, y, zonetype, color, max_drones)
		self.zones[name] = {
			'x': x,
			'y': y,
			'zone_type': zone_type,
			'color': color,
			'max_drones': max_drones
		}

	def _parse_connection(self, line: str, line_num: int) -> None:
		"""

		"""
		content = line.split(':', 1)[1].strip()

		if '[' in content:
			main, meta = content.split('[', 1)
			meta = meta.rstrip(']')
		else:
			main, meta = content, ''

		parts = main.strip().split('-')
		if len(parts) != 2:
			raise ValueError(f"Line {line_num}: invalid connection format")

		zone1, zone2 = parts[0].strip(), parts[1].strip()
		if zone1 not in self.zones or zone2 not in self.zones:
			raise ValueError(f"Line {line_num}: unknown zone in connection")

		metadata = self._parse_metadata(meta, line_num)

		try:
			max_capacity = int(metadata.get('max_link_capacity', 1))
		except ValueError:
			raise ValueError(f"Line {line_num}: max_link_capacity must be an integer")

		if max_capacity <= 0:
			raise ValueError(f"Line {line_num}: max_link_capacity must be a positive integer")

		self.connection.append((zone1, zone2, max_capacity))

	def _parse_metadata(self, meta: str, line_num: int) -> dict:
		result = {}
		for tag in meta.split():
			if  '=' not in tag:
				raise ValueError(f"Line {line_num}: invalid metadata tag '{tag}'")
			key, value = tag.split('=', 1)
			result[key] = value
		return result

	def _validate(self, line_num: int) -> None:
		if self.nb_drones == 0:
			raise ValueError("nb_drones is missing or not defined")
		if self.start_zone is None:
			raise ValueError("Missing start_hub")
		if self.end_zone is None:
			raise ValueError("Missing end_hub")
		if len(self.zones) == 0:
			raise ValueError("No zones defined")
		if len(self.connections) == 0:
			raise ValueError("No connections defined")