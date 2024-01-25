from aiohttp import ClientSession

from settings import BACKEND_URL


async def get_navigation_context() -> dict:
    async with ClientSession() as session:
        async with session.get(BACKEND_URL + "get_all_navigation") as response:
            navigation_json = await response.json()
            return {
                "navigation_elements": navigation_json
            }
