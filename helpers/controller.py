class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def load_ticket_data(self, filepath):
        self.model.load_ticket_data(filepath)
        if self.model.ticket_data:
            self.view.ticketMassLoadFrame.file_name = self.model.ticket_data['filepath']
            self.view.ticketMassLoadFrame.order_number = self.model.ticket_data['order_number']
            self.view.ticketMassLoadFrame.ship_date = self.model.ticket_data['ship_date']
            self.view.ticketMassLoadFrame.customer_name = self.model.ticket_data['customer_name']
