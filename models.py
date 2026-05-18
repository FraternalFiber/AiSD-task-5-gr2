class Item:
    def __init__(self, item_id, weight, value):
        self.id = item_id
        self.weight = weight
        self.value = value
        # Współczynnik opłacalności (wartość / rozmiar)
        self.ratio = value / weight if weight > 0 else 0

    def __repr__(self):
        return f"Item(id={self.id}, w={self.weight}, v={self.value})"