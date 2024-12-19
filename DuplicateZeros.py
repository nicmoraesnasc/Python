from collections.abc import Iterable

class DuplicateZeros:

    numbers = []

    def set_numbers(self, numbers):
        self.numbers = numbers
        
    def get_duplicate_zeros(self) -> Iterable:
        for i in self.numbers:
            if i == 0:
                return self.numbers.append(0)

duplicate_zeros = DuplicateZeros()

duplicate_zeros.set_numbers([1, 0, 2, 3, 0, 4, 5, 0])

print(list(duplicate_zeros.get_duplicate_zeros()))