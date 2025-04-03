"""Base class for all La Marzocco IoT devices."""

import asyncio
import logging
from abc import abstractmethod
from typing import Any

from bleak import BleakError

from pylamarzocco.legacy.clients.bluetooth import LaMarzoccoBluetoothClient
from pylamarzocco.legacy.clients.cloud import LaMarzoccoCloudClient
from pylamarzocco.legacy.clients.local import LaMarzoccoLocalClient
from pylamarzocco.legacy.const import FirmwareType
from pylamarzocco.legacy.exceptions import (
    AuthFail,
    BluetoothConnectionFailed,
    ClientNotInitialized,
    RequestNotSuccessful,
)
from pylamarzocco.legacy.helpers import parse_firmware
from pylamarzocco.legacy.models import (
    LaMarzoccoDeviceConfig,
    LaMarzoccoFirmware,
    LaMarzoccoStatistics,
)

_LOGGER = logging.getLogger(__name__)


class LaMarzoccoBaseDevice:
    """Base class for all La Marzocco devices"""

    _cloud_client: LaMarzoccoCloudClient | None

    def __init__(
        self,
        model: str,
        serial_number: str,
        name: str,
        cloud_client: LaMarzoccoCloudClient | None = None,
        local_client: LaMarzoccoLocalClient | None = None,
        bluetooth_client: LaMarzoccoBluetoothClient | None = None,
    ) -> None:
        """Initializes a new LaMarzoccoMachine instance"""

        self.model: str = model
        self.serial_number: str = serial_number
        self.name: str = name
        self.firmware: dict[FirmwareType, LaMarzoccoFirmware] = {}
        self.statistics: LaMarzoccoStatistics | None = None
        self.config: LaMarzoccoDeviceConfig = LaMarzoccoDeviceConfig(
            turned_on=False,
            doses={},
        )

        self._raw_config: dict[str, Any] | None = None
        self._cloud_client = cloud_client
        self._bluetooth_client = bluetooth_client
        self._local_client = local_client
        self._update_lock = asyncio.Lock()
        self._local_connection_down = False

    def parse_config(self, raw_config: dict[str, Any]) -> None:
        """Parse the config object."""

        self.firmware = parse_firmware(raw_config["firmwareVersions"], self.firmware)

    @property
    def cloud_client(self) -> LaMarzoccoCloudClient:
        """Ensure that the cloud client is initialized."""

        if self._cloud_client is None:
            raise ClientNotInitialized("Cloud client not initialized")
        return self._cloud_client

    @abstractmethod
    def parse_statistics(self, raw_statistics: list[dict[str, Any]]) -> None:
        """Parse the statistics object."""

    @property
    def full_model_name(self) -> str:
        """Return the full model name of the device."""
        return self.model

    async def get_config(
        self,
        local_api_retry_delay: int = 3,
    ) -> None:
        """Update the machine status."""

        raw_config: dict[str, Any] = {}

        async with self._update_lock:
            # first, try to update locally
            if self._local_client is not None:
                try:
                    raw_config = await self._local_client.get_config()
                except AuthFail as exc:
                    _LOGGER.debug(
                        "Got 403 from local API, sending token request to cloud"
                    )
                    # for some machines (GS3) we need to send a token request before local API works
                    if self._cloud_client is not None:
                        await self._cloud_client.token_command(self.serial_number)
                        await asyncio.sleep(local_api_retry_delay)
                        raw_config = await self._local_client.get_config()
                    else:
                        raise exc
                except RequestNotSuccessful as exc:
                    msg = (
                        "Could not connect to local API although initialized, "
                        "falling back to cloud."
                    )
                    if not self._local_connection_down:
                        _LOGGER.warning(msg)
                        self._local_connection_down = True
                    _LOGGER.debug(msg)
                    _LOGGER.debug(exc)
                    if self._cloud_client is None:
                        raise exc
                else:
                    if self._local_connection_down:
                        _LOGGER.warning("Local API connection restored.")
                        self._local_connection_down = False

            # if local update failed, try to update from cloud
            if self._cloud_client is not None and not raw_config:
                raw_config = await self._cloud_client.get_config(self.serial_number)

            self.parse_config(raw_config)

    async def get_statistics(self) -> None:
        """Update the statistics"""

        raw_statistics = await self.cloud_client.get_statistics(self.serial_number)
        self.parse_statistics(raw_statistics)

    async def get_firmware(self) -> None:
        """Update the firmware"""

        self.firmware = await self.cloud_client.get_firmware(self.serial_number)

    @abstractmethod
    async def update_firmware(self, component: FirmwareType) -> bool:
        """Update firmware"""

    async def _bluetooth_command_with_cloud_fallback(
        self,
        command: str,
        **kwargs,
    ) -> bool:
        """Send a command to the machine via Bluetooth, falling back to cloud if necessary."""

        # First, try with bluetooth
        if self._bluetooth_client is not None:
            func = getattr(self._bluetooth_client, command)
            try:
                _LOGGER.debug(
                    "Sending command %s over bluetooth with params %s",
                    command,
                    str(kwargs),
                )
                await func(**kwargs)
            except (BleakError, BluetoothConnectionFailed) as exc:
                msg = "Could not send command to bluetooth device, even though initalized."

                if self._cloud_client is None:
                    _LOGGER.error(
                        "%s Cloud client not initialized, cannot fallback. Full error %s",
                        msg,
                        exc,
                    )
                    return False

                _LOGGER.warning("%s Falling back to cloud", msg)
                _LOGGER.debug("Full error: %s", exc)
            else:
                return True

        # no bluetooth or failed, try with cloud
        if self._cloud_client is not None:
            _LOGGER.debug(
                "Sending command %s over cloud with params %s",
                command,
                str(kwargs),
            )
            func = getattr(self._cloud_client, command)
            kwargs["serial_number"] = self.serial_number
            if await func(**kwargs):
                return True
        return False

    def __str__(self) -> str:
        config = dict(vars(self.config).items())
        return str(config)
