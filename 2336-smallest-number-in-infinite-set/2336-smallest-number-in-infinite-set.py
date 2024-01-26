# 


class SmallestInfiniteSet:

    def __init__(self):
        self.min = 1
        self.added = set()

    def popSmallest(self) -> int:
        to_pop = self.min
        if len(self.added) > 0:
            to_pop = min(min(self.added), to_pop)

        self.added.discard(to_pop)
        if to_pop == self.min:
            self.min += 1

        return to_pop

    def addBack(self, num: int) -> None:
        if num < self.min:
            self.added.add(num)