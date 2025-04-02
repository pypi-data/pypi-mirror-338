import aiohttp

from flespi_sdk.modules.subsystem import Module


class Metadata(Module):
    def __init__(self, session: aiohttp.ClientSession, cid: int | None = None):
        super().__init__(session, cid)

    async def get(self) -> dict:
        """
        Get metadata for the current account.
        :return: Metadata as a dictionary.
        """
        params = {"fields": "metadata"}
        async with self.session.get(
            "platform/customer", params=params, headers=self.get_headers()
        ) as response:
            result = await self.get_result(response)
            return result[0]["metadata"]

    async def set(self, metadata: dict) -> None:
        """ "
        "Set metadata for the current account.
        :param metadata: Metadata as a dictionary.
        """
        async with self.session.put(
            "platform/customer",
            json={"metadata": metadata},
            headers=self.get_headers(),
        ) as response:
            await self.get_result(response)

    async def get_value(self, key_path: str):
        """
        Get a specific value from the metadata.
        :param key_path: The key path to the value in the metadata.
        :return: The value from the metadata.
        """
        metadata = await self.get()
        keys = key_path.split(".")
        value = metadata
        for key in keys:
            if key in value:
                value = value[key]
            else:
                return None
        return value

    async def set_value(self, key_path: str, value) -> None:
        """
        Set a specific value in the metadata.
        :param key_path: The key path to the value in the metadata.
        :param value: The value to set.
        """
        metadata = await self.get()
        keys = key_path.split(".")
        d = metadata
        for key in keys[:-1]:
            if key not in d:
                d[key] = {}
            d = d[key]
        d[keys[-1]] = value
        await self.set(metadata)

    async def delete_value(self, key_path: str) -> None:
        """
        Delete a specific key from the metadata.
        :param key_path: The key path to the value in the metadata.
        """
        metadata = await self.get()
        keys = key_path.split(".")
        value = metadata
        for key in keys[:-1]:
            if key in value:
                value = value[key]
            else:
                return None
        del value[keys[-1]]
        await self.set(metadata)
