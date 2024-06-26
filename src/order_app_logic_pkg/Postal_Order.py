from datetime import datetime, timedelta

from .Order import Order


class Postal_Order(Order):
    VALID_STATES = ["Initiated", "Packed", "Shipped", "Delivered"]

    def __init__(self, customer):
        super().__init__(customer)

        # cannot estimate time yet - user must finish ordering process
        #
        # estimated_delivery_time=(datetime.now()+timedelta(seconds=22.5))
        # i was testing it for an error, so I used the try/except. Can delete.
        # try:
        # self.o_delivery_date=estimated_delivery_time
        # except AttributeError:
        #     print("Postal Order: Delivery date not set")

        self.past_states = []  # not a property
        self.current_state = 0  # current state is, "initiated", among past states

    @property
    def o_delivery_date(self) -> datetime:
        return self._o_delivery_date

    def set_delivery_date(self):
        current_date = datetime.now()
        new_date = current_date + timedelta(days=30)
        self._o_delivery_date = new_date

    @property
    def current_state(self) -> type[int]:
        return self._current_state

    @current_state.setter
    def current_state(self, new_state: type[int]):
        if Postal_Order.VALID_STATES[new_state] in Postal_Order.VALID_STATES:
            self.past_states.append(new_state)  # add new_state, assuming it is valid
            if self.has_partial_valid_state_sequence(
                self.past_states, Postal_Order.VALID_STATES
            ):
                self._current_state = new_state
            else:
                self.lower_the_status_by_a_level()  # not valid, so  undo new_state

    # Returns true if the 'states' parameter has a set of valid states. Returns False otherwise
    # Parameter valid_sequence has values ["Initiated", "Packed", "Shipped", "Delivered"]
    # A postal oders's valid partial state sequence can only have the following form:
    # []
    # ["initiated"],
    # ["Initiated", "Packed"]
    # ["Initiated", "Packed", "Shipped"],
    # ["Initiated", "Packed", "Shipped", "Delivered"]
    def has_partial_valid_state_sequence(
        self, states: type[list[int]], valid_sequence: list[type[str]]
    ) -> type[bool]:
        result = False
        if len(states) <= len(valid_sequence):
            in_valid_seq = True
            for i, state in enumerate(states):
                if state >= len(Postal_Order.VALID_STATES):
                    in_valid_seq = False
                    break
                if valid_sequence[state - i] != valid_sequence[0]:
                    in_valid_seq = False
                    break
                else:
                    valid_sequence = valid_sequence[1:]  # Remove the matched state
            if in_valid_seq:
                result = True
        return result

    # useful if the order status was wrongly raised
    def lower_the_status_by_a_level(self):
        self.past_states = self.past_states.pop()  # remove last

    # useful if the order status was wrongly lowered
    def raise_the_status_by_a_level(self):
        if len(self.past_states) < len(Postal_Order.VALID_STATES):
            self.past_states = len(self.past_states)

    """
    @property
    def past_states(self):
        return self.past_states
        
    """

    def __str__(self) -> type[str]:

        states = Postal_Order.VALID_STATES[: len(self.past_states)]
        star_line = "-" * 100 + "\n"
        postal_order_header_details = (
            "Additional details for Postal Order\n"
            + f"Estimated Delivery date: {datetime.now() + timedelta(seconds=60)}\n"
            + "Postal Order status: "
            + " ".join(map(str, states))
            + "\n"
        )
        base_order_details = super().__str__()
        print(datetime.now(), "__str__")
        return base_order_details + star_line + postal_order_header_details + star_line
