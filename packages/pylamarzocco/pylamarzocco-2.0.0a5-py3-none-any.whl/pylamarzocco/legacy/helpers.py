"""Helper functions for pylamarzocco."""

from typing import Any
from aiohttp import ClientResponse

from .const import (
    BoilerType,
    FirmwareType,
    PhysicalKey,
    PrebrewMode,
    SmartStandbyMode,
    WeekDay,
    MachineModel,
    KEYS_PER_MODEL,
)
from .models import (
    LaMarzoccoBoiler,
    LaMarzoccoBrewByWeightSettings,
    LaMarzoccoCoffeeStatistics,
    LaMarzoccoFirmware,
    LaMarzoccoPrebrewConfiguration,
    LaMarzoccoScale,
    LaMarzoccoSmartStandby,
    LaMarzoccoWakeUpSleepEntry,
)

# def schedule_to_request(schedule: LaMarzoccoSchedule) -> LaMarzoccoCloudSchedule:
#     """convert schedule to API expected input format"""

#     schedule_conv: LaMarzoccoCloudSchedule = {
#         "enable": schedule.enabled,
#         "days": [],
#     }
#     for day, schedule_day in schedule.days.items():
#         # requests wants 00:00, response gives 24:00
#         h_on = "00" if schedule_day.h_on == 24 else str(schedule_day.h_on).zfill(2)
#         h_off = "00" if schedule_day.h_off == 24 else str(schedule_day.h_off).zfill(2)

#         hh_mm_on = h_on + ":" + str(schedule_day.m_on).zfill(2)
#         hh_mm_off = h_off + ":" + str(schedule_day.m_off).zfill(2)

#         schedule_conv["days"].append(
#             {
#                 "day": str.upper(day),
#                 "enable": schedule_day.enabled,
#                 "on": hh_mm_on,
#                 "off": hh_mm_off,
#             }
#         )
#     return schedule_conv


# def parse_schedule(schedule: dict[str, Any]) -> LaMarzoccoSchedule:
#     """Parse schedule from API config object."""

#     global_enable: bool = schedule["enabled"]
#     days: dict[WeekDay, LaMarzoccoScheduleDay] = {}
#     for weekday in WeekDay:
#         day_settings = schedule[weekday]
#         days[weekday] = LaMarzoccoScheduleDay(
#             enabled=day_settings["enabled"],
#             h_on=day_settings["h_on"],
#             h_off=day_settings["h_off"],
#             m_on=day_settings["m_on"],
#             m_off=day_settings["m_off"],
#         )
#     return LaMarzoccoSchedule(enabled=global_enable, days=days)


def parse_boilers(boilers: list[dict[str, Any]]) -> dict[BoilerType, LaMarzoccoBoiler]:
    """Parse boiler settings from API config object."""

    parsed_boilers: dict[BoilerType, LaMarzoccoBoiler] = {}
    for boiler in boilers:
        is_enabled = boiler["isEnabled"]
        current_temp = boiler["current"]
        target_temp = boiler["target"]
        parsed_boilers[BoilerType(boiler["id"])] = LaMarzoccoBoiler(
            enabled=is_enabled,
            current_temperature=current_temp,
            target_temperature=target_temp,
        )
    return parsed_boilers


def parse_preinfusion_settings(
    model: MachineModel,
    config: dict[str, Any],
) -> tuple[
    PrebrewMode,
    dict[
        PhysicalKey,
        tuple[LaMarzoccoPrebrewConfiguration, LaMarzoccoPrebrewConfiguration],
    ],
]:
    """Parse preinfusion settings from API config object."""

    num_keys = KEYS_PER_MODEL[model]
    if num_keys == 0:
        num_keys = 1

    parsed: dict[PhysicalKey, tuple[LaMarzoccoPrebrewConfiguration, LaMarzoccoPrebrewConfiguration]] = {}
    preinfusion_settings = config.get("preinfusionSettings", {})
    mode = PrebrewMode(preinfusion_settings.get("mode", "Disabled"))
    settings_group_1 = preinfusion_settings.get("Group1", [])
    key = 1
    if (num_settings := len(settings_group_1)) > num_keys:
        step = 2
    else:
        step = 1
    for i in range(0, num_settings, step):

        type_a = LaMarzoccoPrebrewConfiguration(
            on_time=settings_group_1[i].get("preWetTime", 0),
            off_time=settings_group_1[i].get("preWetHoldTime", 0),
        )
        if num_settings > num_keys:
            type_b = LaMarzoccoPrebrewConfiguration(
                on_time=settings_group_1[i + 1].get("preWetTime", 0),
                off_time=settings_group_1[i + 1].get("preWetHoldTime", 0),
            )
        else:
            type_b = type_a
        parsed[PhysicalKey(key)] = (type_a, type_b)
        key += 1

    return mode, parsed


def parse_coffee_doses(config: dict[str, Any]) -> tuple[dict[PhysicalKey, float], int]:
    """Parse doses from API config object."""

    parsed: dict[PhysicalKey, float] = {}
    i = 1
    group_capabilities = config.get("groupCapabilities", [])
    if len(group_capabilities) == 0:
        return parsed, 0

    for dose in group_capabilities[0].get("doses", []):
        parsed[PhysicalKey(i)] = dose.get("stopTarget", 0)
        i += 1
    dose_hot_water: int = (
        config.get("teaDoses", {}).get("DoseA", {}).get("stopTarget", 0)
    )
    return parsed, dose_hot_water


def parse_cloud_statistics(
    statistics: list[dict[str, Any]],
) -> LaMarzoccoCoffeeStatistics:
    """Parse statistics from API statistics object."""

    drink_stats: dict[PhysicalKey, int] = {}
    continuous = 0
    total_flushes = 0

    for stat in statistics:
        coffee_type: int = stat["coffeeType"]
        count: int = stat["count"]
        if 0 <= coffee_type < 4:
            drink_stats[PhysicalKey(coffee_type + 1)] = count
        elif coffee_type == 4:
            continuous = count
        elif coffee_type == -1:
            total_flushes = count
    return LaMarzoccoCoffeeStatistics(
        drink_stats=drink_stats,
        continous=continuous,
        total_flushes=total_flushes,
    )


def parse_firmware(
    raw_firmware: list[dict[str, Any]],
    current_firmware: dict[FirmwareType, LaMarzoccoFirmware] | None = None,
) -> dict[FirmwareType, LaMarzoccoFirmware]:
    """Parse firmware from API config object."""

    parsed = {}
    for fw in raw_firmware:
        fw_type = FirmwareType(fw["name"].split("_")[0])
        version = fw["fw_version"]
        latest_version = (
            version
            if not current_firmware
            else current_firmware[fw_type].latest_version
        )
        parsed[fw_type] = LaMarzoccoFirmware(
            current_version=version,
            latest_version=latest_version,
        )
    return parsed


def parse_webhook_statistics(statistics: dict[str, Any]) -> LaMarzoccoCoffeeStatistics:
    """Parse statistics from webhook statistics object."""

    continuous = 0
    group = statistics["groups"][0]
    doses = group["doses"]
    drink_stats: dict[PhysicalKey, int] = {}
    for dose in doses:
        key: str = next(iter(dose))
        if key.startswith("Dose"):
            drink_stats[PhysicalKey(ord(key[-1]) - 64)] = dose[key]
        elif key == "ContinuousDose":
            continuous = dose[key]
    total_flushing = group["clean"]
    return LaMarzoccoCoffeeStatistics(
        drink_stats=drink_stats,
        continous=continuous,
        total_flushes=total_flushing,
    )


def parse_smart_standby(smart_standby_config: dict[str, Any]) -> LaMarzoccoSmartStandby:
    """Parse smart standby mode from API config object."""
    return LaMarzoccoSmartStandby(
        enabled=smart_standby_config.get("enabled", False),
        minutes=smart_standby_config.get("minutes", 10),
        mode=SmartStandbyMode(smart_standby_config.get("mode", "PowerOn")),
    )


def parse_wakeup_sleep_entries(
    entries: list[dict[str, Any]],
) -> dict[str, LaMarzoccoWakeUpSleepEntry]:
    """Parse wake up sleep entries from API config object."""
    parsed = {}
    for entry in entries:
        wake_up_sleep_entry = LaMarzoccoWakeUpSleepEntry(
            enabled=entry["enabled"],
            days=[WeekDay(day) for day in entry["days"]],
            entry_id=entry["id"],
            steam=entry["steam"],
            time_on=entry["timeOn"],
            time_off=entry["timeOff"],
        )
        parsed[wake_up_sleep_entry.entry_id] = wake_up_sleep_entry
    return parsed


def parse_brew_by_weight_settings(
    config: dict[str, Any],
) -> LaMarzoccoBrewByWeightSettings | None:
    """Parse brew by weight settings from API config object."""
    if "recipes" not in config:
        return None
    doses: dict[PhysicalKey, int] = {}
    recipes = config["recipes"]
    for recipe in recipes:
        for dose in recipe["recipe_doses"]:
            doses[PhysicalKey[dose["id"]]] = dose["target"]
    recipe_assignments = config["recipeAssignment"]
    active_dose = PhysicalKey.A
    for recipe_assignment in recipe_assignments:
        active_dose = PhysicalKey[recipe_assignment["recipe_dose"]]
    return LaMarzoccoBrewByWeightSettings(doses=doses, active_dose=active_dose)


def parse_scale(config: dict[str, Any]) -> LaMarzoccoScale | None:
    """Parse scale settings from API config object."""
    if scale := config.get("scale", None):
        return LaMarzoccoScale(
            connected=scale["connected"],
            name=scale["name"],
            battery=scale["battery"],
            address=scale["address"],
        )
    return None


def is_success(response: ClientResponse) -> bool:
    """Check if response is successful."""
    return 200 <= response.status < 300
