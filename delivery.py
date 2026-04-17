import uuid
from datetime import datetime

class FoodDeliverySystem:
    def __init__(self):
        # Store orders with unique order ID as key
        self.orders = {}
        # Simple menu for validation
        self.menu = {"pizza": 10.99, "burger": 5.99, "sushi": 15.00}
        # Tracker for incoming requests to prevent duplicates
        self.active_request_ids = set()

    def place_order(self, customer_id, items, request_id):
        """Places an order, prevents duplicates, and validates items."""
        # Task 1: Prevent Duplicate Orders (Idempotency)
        if request_id in self.active_request_ids:
            return {"status": "error", "message": "Duplicate request detected"}
        
        # Validate items
        for item in items:
            if item not in self.menu:
                return {"status": "error", "message": f"Item {item} not found"}

        # Generate unique order ID
        order_id = str(uuid.uuid4())[:8]
        
        # Calculate total
        total = sum(self.menu[item] for item in items)
        
        # Create Order Record
        order = {
            "order_id": order_id,
            "customer_id": customer_id,
            "items": items,
            "total": total,
            "status": "Placed",
            "timestamp": datetime.now()
        }
        
        # Process and Save
        self.orders[order_id] = order
        self.active_request_ids.add(request_id)
        print(f"Order {order_id} placed successfully for Customer {customer_id}.")
        return {"status": "success", "order": order}

    def track_order(self, order_id):
        """Tracks the status of a specific order."""
        # Task 1: Order Tracking
        order = self.orders.get(order_id)
        if order:
            return {"status": "success", "order_status": order["status"]}
        return {"status": "error", "message": "Order not found"}

    def update_order_status(self, order_id, new_status):
        """Simulates processing and delivery updates."""
        if order_id in self.orders:
            self.orders[order_id]["status"] = new_status
            return True
        return False

# Example Usage
if __name__ == "__main__":
    system = FoodDeliverySystem()
    
    # Place valid order
    order1 = system.place_order("cust123", ["pizza", "burger"], "req_1")
    
    # Try duplicate order
    duplicate_attempt = system.place_order("cust123", ["pizza"], "req_1")
    print(duplicate_attempt) # Output: {'status': 'error', 'message': 'Duplicate request detected'}
    
    # Track order
    if order1['status'] == 'success':
        order_id = order1['order']['order_id']
        print("Tracking:", system.track_order(order_id))
