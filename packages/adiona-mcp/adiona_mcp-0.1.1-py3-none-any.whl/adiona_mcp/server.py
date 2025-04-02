import os
import httpx
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from typing import Optional

load_dotenv()
mcp = FastMCP("HotelAPIServer")

BASE_URL = "https://prod.adiona.ai/api/v1"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('ADIONA_API_KEY')}"
}

@mcp.tool()
async def hotel_search(
    location: str,
    check_in: str,
    check_out: str,
    rooms: int
) -> dict:
    """
    Search for hotels based on location and dates
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BASE_URL}/hotel/search",
                json={
                    "location": location,
                    "checkIn": check_in,
                    "checkOut": check_out,
                    "rooms": rooms
                },
                headers=HEADERS,
                timeout=15.0
            )
            response.raise_for_status()
            return response.json()
    
    except httpx.HTTPStatusError as e:
        return {
            "success": False,
            "message": f"HTTP error {e.response.status_code}",
            "details": e.response.json()
        }

@mcp.tool()
async def hotel_info(hotel_id: str) -> dict:
    """
    Get detailed information about a specific hotel
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/hotel/{hotel_id}/info",
                headers=HEADERS
            )
            response.raise_for_status()
            return response.json()
    
    except httpx.HTTPStatusError as e:
        return {
            "success": False,
            "message": f"HTTP error {e.response.status_code}",
            "details": e.response.json()
        }

@mcp.tool()
async def location_search(query: str) -> dict:
    """
    Search for locations by name or coordinates
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{BASE_URL}/location/search",
                params={"query": query},
                headers=HEADERS
            )
            response.raise_for_status()
            return response.json()
    
    except httpx.HTTPStatusError as e:
        return {
            "success": False,
            "message": f"HTTP error {e.response.status_code}",
            "details": e.response.json()
        }

if __name__ == "__main__":
    mcp.run(transport="stdio")
