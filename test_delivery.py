import unittest
from delivery import FoodDeliverySystem

class TestFoodDeliverySystem(unittest.TestCase):
    def setUp(self):
        self.system = FoodDeliverySystem()

    # Task 2: Write tests for order success/failure scenarios
    def test_place_order_success(self):
        result = self.system.place_order("cust1", ["pizza"], "req1")
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["order"]["status"], "Placed")
        self.assertIn(result["order"]["order_id"], self.system.orders)

    def test_place_order_duplicate_failure(self):
        self.system.place_order("cust1", ["burger"], "req_dup")
        # Attempt to place same request_id again
        result = self.system.place_order("cust1", ["burger"], "req_dup")
        self.assertEqual(result["status"], "error")
        self.assertEqual(result["message"], "Duplicate request detected")

    def test_place_order_invalid_item(self):
        result = self.system.place_order("cust1", ["salad"], "req2")
        self.assertEqual(result["status"], "error")
        self.assertIn("not found", result["message"])

    def test_track_order_success(self):
        order_res = self.system.place_order("cust1", ["sushi"], "req3")
        order_id = order_res["order"]["order_id"]
        
        # Change status
        self.system.update_order_status(order_id, "Delivered")
        
        # Check status
        track_res = self.system.track_order(order_id)
        self.assertEqual(track_res["order_status"], "Delivered")

    def test_track_order_not_found(self):
        track_res = self.system.track_order("invalid_id")
        self.assertEqual(track_res["status"], "error")

if __name__ == '__main__':
    unittest.main()
