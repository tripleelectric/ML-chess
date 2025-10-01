class Statistics:

    def __init__(self) -> None:
        pass

    @staticmethod
    def mean(vector):
        """
        For intuition: mean sometimes is called the "expectation"
        """
        return sum(vector) / len(vector)

    @staticmethod
    def median(vector):
        if len(vector) % 2 == 0:
            index_one = int(len(vector) / 2)
            index_two = index_one - 1
            return (vector[index_one] + vector[index_two]) / 2

    @staticmethod
    def variance(vector):
        mean = Statistics.mean(vector)
        n = len(vector)
        return sum([vi - mean for vi in vector]) / n


v = [1, 1, 2, 3, 4, 5]
print(Statistics.median(v))
