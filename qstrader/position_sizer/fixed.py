from .base import AbstractPositionSizer


class FixedPositionSizer(AbstractPositionSizer):
    def __init__(self, default_quantity=100):
        self.default_quantity = default_quantity

    def size_order(self, portfolio, initial_order):
        """
        This position sizer does nothing
        """
        #initial_order.quantity = self.default_quantity

        return initial_order
