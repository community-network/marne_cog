import json
import aiohttp


async def main(servername: str, limit: int = 10):
    async with aiohttp.ClientSession() as session:
        url = "https://marne.io/api/srvlst/"
        async with session.get(url) as r:
            result = await r.text()
            result = json.loads(result.lstrip("\ufeff"))

    total = 0
    servers = []
    for server in result.get("servers", []):
        if servername.lower() in server.get("name", "").lower():
            if total > limit:
                break
            total += 1
            servers.append(server)
    return servers
