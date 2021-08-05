"""Exploring losing steak in WildRift"""
import json
import random
import operator
from collections import defaultdict
from typing import List, Dict


class WildRift:
    """How possible is losing steak"""

    def __init__(self, matches_number: int = 50):
        self.matches_number = matches_number
        self.results = self.generate_results()

    def generate_results(self) -> List[bool]:
        """Generate results"""
        results = []
        for _ in range(self.matches_number):
            results.append(random.choice([True, False]))
        return results

    def outcomes(self) -> Dict[bool, int]:
        """Return outcomes counts"""
        return {
            True: self.results.count(True),
            False: self.results.count(False),
        }

    def calculate_steaks(self, outcome: bool = False) -> Dict[int, int]:
        """Calculate distribution"""
        steaks = []  # array to store all repeating sequences
        current_steak = []
        for element in self.results:
            if element == outcome:
                current_steak.append(element)
            else:
                if current_steak:
                    steaks.append(current_steak)
                    current_steak = []

        # form results
        results: Dict[int, int] = defaultdict(int)
        for seq in steaks:
            results[len(seq)] += 1

        return dict(
            sorted(results.items(), key=operator.itemgetter(0), reverse=True)
        )


if __name__ == "__main__":
    data = []
    for _ in range(100):
        obj = WildRift(matches_number=random.randint(100, 500))
        record = {"outcomes": obj.outcomes(), "steaks": obj.calculate_steaks()}
        data.append(record)

    with open("loss_steak.json", "w") as file_handler:
        file_handler.write(json.dumps(data, indent=2))
