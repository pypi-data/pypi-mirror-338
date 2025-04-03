from collections import Counter
import re


class Analyser:
    def print_results(self, your_results):
        """Print results and their unique item counts."""
        print("Results:", your_results)

        unique_counts = Counter(your_results)
        print("Unique Item Counts:", dict(unique_counts))

    def matches_any(self, card, pattern):
        """
        Check if the card matches a pattern using regular expressions.
        :param card: The card string (e.g., "AS").
        :param pattern: The pattern to match (e.g., "A*" to match "AS", "AH", etc.).
        :return: True if the card matches the pattern.
        """
        regex_pattern = re.sub(r'\*', '.*', pattern)
        regex_pattern = re.sub(r'\s*\|\s*', '|', regex_pattern)
        return re.fullmatch(regex_pattern, card) is not None

    def count(self, your_results, items):
        """
        Count the occurrences of each item in the provided list within `your_results`, allowing regex patterns.

        :param your_results: List of observed results.
        :param items: List of items (or patterns) to count in `your_results`.
        :return: A list of counts corresponding to each item in `items`.
        """
        return [sum(1 for result in your_results if self.matches_any(result, item)) for item in items]

    def has(self, your_results, sequence, consecutive=False, ordered=False):
        """
        Check if a given sequence exists in the your results.

        :param sequence: List of values to check for in results.
        :param consecutive: If True, requires the sequence to appear consecutively.
        :param ordered: If True, requires the sequence to appear in order but allows gaps.
        :return: True if the sequence is found according to the given conditions, otherwise False.
        """
        if not sequence:
            return False

        seq_len = len(sequence)

        # If sequence length is greater than results length, return False
        if seq_len > len(your_results):
            return False

        # Default check (unordered, not consecutive)
        if not consecutive and not ordered:
            result_count = Counter(your_results)
            sequence_count = Counter(sequence)
            for item in sequence:
                matches = any(self.matches_any(res, item)
                              for res in your_results)
                if not matches:
                    return False
            return True

        # Ordered but not consecutive (find indices in order)
        if ordered and not consecutive:
            index = 0
            for res in your_results:
                if index < seq_len and self.matches_any(res, sequence[index]):
                    index += 1
                if index == seq_len:
                    return True
            return False

        # Consecutive but not ordered check
        if consecutive and not ordered:
            for i in range(len(your_results) - seq_len + 1):
                window = your_results[i:i + seq_len]
                if all(any(self.matches_any(w, s) for w in window) for s in sequence):
                    return True
            return False

        # Consecutive and ordered check
        if consecutive:
            for i in range(len(your_results) - seq_len + 1):
                if all(self.matches_any(res, item) for res, item in zip(your_results[i:i + seq_len], sequence)):
                    return True
            return False

        return False
