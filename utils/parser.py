from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Dict


class ParserProtocol(ABC):

    @abstractmethod
    async def parse_sensors_json(self, text: str) -> Dict: ...


class Parser(ParserProtocol):
    async def parse_sensors_json(self, text: str) -> Dict:
        temps = defaultdict(list)

        for line in text.splitlines():
            line = line.strip()
            if ":" in line and "°C" in line:
                name, rest = line.split(":", 1)
                value = float(rest.split("°C")[0].replace("+", "").strip())
                temps[name].append(value)

        # если элемент в списке 1, превращение в число
        temps_clean = {k.lower(): v[0] if len(v) == 1 else v for k, v in temps.items()}

        # hotspot
        hotspot = max(v if isinstance(v, float) else max(v) for v in temps_clean.values())

        result = {
            "temperatures": temps_clean,
            "hotspot": hotspot
        }

        return result
