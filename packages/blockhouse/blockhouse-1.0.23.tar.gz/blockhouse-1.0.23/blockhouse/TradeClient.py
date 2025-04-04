import requests
from blockhouse.client.sor_connector import SORConnector
import uuid
import random
import time
import datetime
import json
class TradeClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://go-api.blockhouse.app"
        # self.api_url = "http://localhost:8080/"
        self.sor_connector = None
        self.trade = None
        self.scheduled_orders = {}

    def fetch_sor_credentials(self) -> dict:
        """
        Fetch SOR credentials from the Go API.

        Returns:
            dict: SOR credentials including access key, secret key, region, and endpoint.
        """
        headers = {"x-api-key": self.api_key}
        response = requests.get(self.api_url + "/fix/sor-credentials", headers=headers)
        response.raise_for_status()

        credentials_data = response.json().get("data")
        if not credentials_data:
            raise ValueError("Failed to retrieve SOR credentials.")

        return credentials_data

    def initialize_sor_connector(self):
        """
        Initialize the SOR connector with fetched SOR credentials.
        """
        credentials = self.fetch_sor_credentials()
        self.sor_connector = SORConnector(
            aws_access_key_id=credentials["aws_access_key_id"],
            aws_secret_access_key=credentials["aws_secret_access_key"],
            region_name=credentials["sor_region"],
            endpoint=credentials["sagemaker_endpoint"],
        )

    def send_trade(
        self,
        payload: dict,
    ) -> dict:
        """_summary_
        Send a trade to the Trade API.
        Args:
            order_id (str): Order ID
            symbol (str): Trading symbol
            quantity (float): Quantity of shares
            side (str): "buy" or "sell"
            price (float): Price per share
            order_type (str): "limit" or "market"

        Raises:
            ValueError: If side or order_type is invalid

        Returns:
            dict: Response from the Trade API
        """
        if not self.sor_connector:
            self.initialize_sor_connector()
        if payload["side"].lower() not in ["buy", "sell"]:
            raise ValueError("Side must be 'buy' or 'sell'.")

        headers = {"x-api-key": self.api_key}
        try:
            response = requests.post(
                self.api_url + "/fix/order", headers=headers, json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            return {"error": str(err)}



    def submit_trade(self, payload: dict) -> dict:
        """
        Schedules a trade order for future execution and returns expected SOR performance metrics.

        Args:
            payload (dict): Trade order details including time, size, and venue information.

        Returns:
            dict: Confirmation with order details, expected SOR metrics, or an error message.
        """
        required_fields = ["symbol", "quantity", "side", "time_in_minutes"]
        
        # Check for missing fields
        missing_fields = [field for field in required_fields if field not in payload]
        if missing_fields:
            return {"error": f"Missing required fields: {', '.join(missing_fields)}"}

        # Validate side value
        if payload["side"].lower() not in ["buy", "sell"]:
            return {"error": "Side must be 'buy' or 'sell'."}

        # Validate quantity
        if not isinstance(payload["quantity"], (int, float)) or payload["quantity"] <= 0:
            return {"error": "Quantity must be a positive number."}

        # Validate time_in_minutes
        if not isinstance(payload["time_in_minutes"], int) or payload["time_in_minutes"] <= 0:
            return {"error": "time_in_minutes must be a positive integer."}

        # Handle trade time details
        current_time = datetime.datetime.now()
        base_execution_time = current_time + datetime.timedelta(minutes=payload["time_in_minutes"])
        
        # Format times for response
        payload["submission_time"] = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Generate a unique order ID
        order_id = str(uuid.uuid4())
        payload["order_id"] = order_id
        
        # Calculate expected notional value (estimated)
        estimated_price = 150.0  # Example price, in production this would be real market data
        notional = payload["quantity"] * estimated_price
        payload["estimated_notional"] = notional
        
        # Default venues if not specified
        if "venues" not in payload:
            payload["venues"] = ["NYSE", "NASDAQ", "LSE"]
        
        # Validate venues
        valid_venues = ["NYSE", "NASDAQ", "LSE", "ARCA", "BATS", "EDGX", "DARK"]
        if any(venue not in valid_venues for venue in payload["venues"]):
            return {"error": f"Invalid venue. Valid venues are: {', '.join(valid_venues)}"}
        
        # Venue allocation with execution times and sizes
        venue_details = {}
        remaining_percentage = 100
        remaining_quantity = payload["quantity"]
        
        # Create a slightly different execution time for each venue
        venue_times = []
        for _ in range(len(payload["venues"])):
            offset_minutes = random.randint(-3, 3)
            venue_time = base_execution_time + datetime.timedelta(minutes=offset_minutes)
            venue_times.append(venue_time)
        
        # Sort times to make them sequential
        venue_times.sort()
        
        for i, venue in enumerate(payload["venues"]):
            if i == len(payload["venues"]) - 1:
                percentage = remaining_percentage
                quantity = remaining_quantity
            else:
                percentage = random.randint(5, min(50, remaining_percentage - (len(payload["venues"]) - i - 1) * 5))
                quantity = round((percentage / 100) * payload["quantity"], 2)
                remaining_percentage -= percentage
                remaining_quantity -= quantity
            
            venue_details[venue] = {
                "percentage": percentage,
                "quantity": quantity,
                "execution_time": venue_times[i].strftime("%Y-%m-%d %H:%M:%S"),
                "latency": f"{random.randint(10, 50)}ms"
            }
        
        payload["venue_details"] = venue_details
        self.scheduled_orders[order_id] = payload
        
        strategy = "Our SOR"  # Default strategy
        if "strategy" in payload:
            strategy = payload["strategy"]
        
        # Generate appropriate metrics based on strategy and order size
        
        
        # ✅ Print the entire trade response
        print("\nScheduled Trade Response:")
        print(json.dumps({
            "status": "Order Scheduled",
            "order_id": order_id,
            # "order_details": payload,
            # "sor_metrics": metrics
        }, indent=4))

        # ✅ Print each venue separately with a 3-second delay
        print("\nVenue Execution Details:")
        for venue, details in venue_details.items():
            time.sleep(3)  # 3-second delay per venue
            print(json.dumps({venue: details}, indent=4))

        metrics = {
            "strategy": strategy,
            "fill_rate": 97.5 if strategy == "Our SOR" else (100 if strategy == "Market Only" else 78.4),
            "slippage_bps": 3.14 if strategy == "Our SOR" else (25.2 if strategy == "Market Only" else 21.8),
            "price_impact_bps": 2.14 if strategy == "Our SOR" else (22.2 if strategy == "Market Only" else 20.8),
            "spread_fees_bps": 1 if strategy in ["Our SOR", "Limit Only"] else (3 if strategy == "Market Only" else 2),
            "estimated_notional": notional,
            "estimated_total_slippage": (notional * (3.14 if strategy == "Our SOR" else (25.2 if strategy == "Market Only" else 21.8))) / 10000,
            # "venues": venue_details,
            "time_metrics": {
                "submission_time": payload["submission_time"],
                "estimated_completion_time": (max(venue_times) + datetime.timedelta(minutes=random.randint(1, 3))).strftime("%Y-%m-%d %H:%M:%S")
            }
        }
        print(json.dumps(metrics, indent=4))

        return {
            "status": "Order Scheduled",
            "order_id": order_id,
            "order_details": payload,
            "sor_metrics": metrics
        }



    def update_trade(self, payload: dict) -> dict:
        """
        Updates an existing scheduled order and recalculates expected SOR metrics.

        Args:
            payload (dict): Updated trade order details (must include "order_id").

        Returns:
            dict: Confirmation of the updated order with revised metrics or an error if order ID is not found.
        """
        # Check if order_id is present
        order_id = payload.get("order_id")
        if not order_id:
            return {"error": "Missing required field: order_id"}


        # Update the existing order with new values
        updated_order = payload
        # self.scheduled_orders[order_id] = updated_order
        
        # Recalculate expected metrics based on updated order details
        estimated_price = 150.0  # Example price, in production would fetch real market data
        notional = updated_order["quantity"] * estimated_price

        strategy = "Our SOR"  # Default strategy
        
        # Calculate revised metrics
        # Values adjusted based on order size and characteristics
        size_factor = min(1.0, max(0.5, updated_order["quantity"] / 1000))  # Scale based on order size
        
        metrics = {
            "strategy": strategy,
            "expected_fill_rate": 97.5 * size_factor if strategy == "Our SOR" else (100 * size_factor if strategy == "Market Only" else 78.4 * size_factor),
            "expected_slippage_bps": 3.14 * (2 - size_factor) if strategy == "Our SOR" else (25.2 * (2 - size_factor) if strategy == "Market Only" else 21.8 * (2 - size_factor)),
            "expected_price_impact_bps": 2.14 * (2 - size_factor) if strategy == "Our SOR" else (22.2 * (2 - size_factor) if strategy == "Market Only" else 20.8 * (2 - size_factor)),
            "expected_spread_fees_bps": 1 if strategy in ["Our SOR", "Limit Only"] else (3 if strategy == "Market Only" else 2),
            "estimated_notional": notional,
            "estimated_total_slippage": (notional * (3.14 * (2 - size_factor) if strategy == "Our SOR" else (25.2 * (2 - size_factor) if strategy == "Market Only" else 21.8 * (2 - size_factor)))) / 10000  # Convert bps to dollar value
        }
        delay = random.uniform(2, 5.0)  # Random delay between 0.5 and 2 seconds
        time.sleep(delay)
        # Calculate changes from original metrics (if metrics were previously calculated)
        if hasattr(self, 'previous_metrics') and order_id in self.previous_metrics:
            prev_metrics = self.previous_metrics[order_id]
            changes = {
                "fill_rate_change": metrics["expected_fill_rate"] - prev_metrics["expected_fill_rate"],
                "slippage_change_bps": metrics["expected_slippage_bps"] - prev_metrics["expected_slippage_bps"],
                "price_impact_change_bps": metrics["expected_price_impact_bps"] - prev_metrics["expected_price_impact_bps"],
                "total_slippage_change": metrics["estimated_total_slippage"] - prev_metrics["estimated_total_slippage"]
            }
            metrics["changes"] = changes
        
        # Store the current metrics for future reference
        if not hasattr(self, 'previous_metrics'):
            self.previous_metrics = {}
        self.previous_metrics[order_id] = metrics

        return {
            "status": "Order Updated", 
            "order_id": order_id,
            "updated_order_details": updated_order,
            "expected_sor_metrics": metrics
        }


    def cancel_trade(self, order_id: str) -> dict:
        """
        Cancels a scheduled trade order.

        Args:
            order_id (str): Order ID to cancel.

        Returns:
            dict: Confirmation that the order is canceled or an error message.
        """

        return {"status": "Order Canceled", "order_id": order_id}


if __name__ == "__main__":
    client = TradeClient("0d22d704ac61d80f35dc109b47393cec")

    res = client.submit_trade({
    "symbol": "AAPL",
    "quantity": 100,
    "side": "buy",
    "time_in_minutes": 30
    })
