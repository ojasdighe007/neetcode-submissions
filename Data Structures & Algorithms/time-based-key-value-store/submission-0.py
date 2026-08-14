from sortedcontainers import SortedSet
class TimeMap:

    def __init__(self):
        self.mapKeyToSortedTimestamps: dict[str, SortedSet] = {}
        self.mapKeyTimestampPairToValue: dict[(str, int), int] = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.mapKeyToSortedTimestamps.get(key) is None:
            self.mapKeyToSortedTimestamps[key] = SortedSet()
        self.mapKeyToSortedTimestamps[key].add(timestamp)

        self.mapKeyTimestampPairToValue[(key,timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if self.mapKeyToSortedTimestamps.get(key) is not None:
            idx = self.mapKeyToSortedTimestamps[key].bisect_right(timestamp) - 1
        else:
            return ""

        if idx >= 0:
            timestamp_prev = self.mapKeyToSortedTimestamps[key][idx]
            return self.mapKeyTimestampPairToValue[(key,timestamp_prev)]

        return ""