from dataclasses import dataclass, field


@dataclass
class ACSystem:
    """Class that defines ACSystem."""

    type: str
    serial: str
    description: str

    @staticmethod
    def extract_ac_systems(json_data: dict) -> "list[ACSystem]":
        ac_systems_data = json_data.get("_embedded", {}).get("ac-system", [])
        return [
            ACSystem(
                type=ac_system.get("type", ""),
                serial=ac_system.get("serial", ""),
                description=ac_system.get("description", ""),
            )
            for ac_system in ac_systems_data
        ]


@dataclass
class ZoneInfo:
    """Class that defines zone information."""

    CanOperate: bool
    CommonZone: bool
    LiveHumidity_pc: float
    LiveTemp_oC: float
    NV_Exists: bool
    NV_Title: str
    AirflowControlEnabled: bool
    AirflowControlLocked: bool
    LastZoneProtection: bool
    ZonePosition: int
    NV_ITC: bool
    NV_ITD: bool
    NV_IHD: bool

    @staticmethod
    def extract_zone_info(zone: dict) -> "ZoneInfo":
        return ZoneInfo(
            CanOperate=zone.get("CanOperate", False),
            CommonZone=zone.get("CommonZone", False),
            LiveHumidity_pc=zone.get("LiveHumidity_pc", 0.0),
            LiveTemp_oC=zone.get("LiveTemp_oC", 0.0),
            NV_Exists=zone.get("NV_Exists", False),
            NV_Title=zone.get("NV_Title", ""),
            AirflowControlEnabled=zone.get("AirflowControlEnabled", False),
            AirflowControlLocked=zone.get("AirflowControlLocked", False),
            LastZoneProtection=zone.get("LastZoneProtection", False),
            ZonePosition=zone.get("ZonePosition", 0),
            NV_ITC=zone.get("NV_ITC", False),
            NV_IHD=zone.get("NV_IHD", False),
            NV_ITD=zone.get("NV_ITD", False)
        )


@dataclass
class SystemStatus:
    """Class that defines an actron air ac system status."""

    SystemName: str
    MasterSerial: str
    LiveTemp_oC: float
    LiveHumidity_pc: float
    IsOnline: bool
    IsOn: bool
    Mode: str
    FanMode: str
    TemprSetPoint_Cool: float
    TemprSetPoint_Heat: float
    SetCool_Min: float
    SetCool_Max: float
    SetHeat_Min: float
    SetHeat_Max: float
    RemoteZoneInfo: list[ZoneInfo] = field(default_factory=list)
    EnabledZones: list[bool] = field(default_factory=list)

    @staticmethod
    def extract_system_status(data: dict) -> "SystemStatus":
        if data is None:
            return SystemStatus(
                SystemName="",
                MasterSerial="",
                LiveTemp_oC=0.0,
                LiveHumidity_pc=0.0,
                IsOnline=False,
                IsOn=False,
                Mode="",
                FanMode="",
                TemprSetPoint_Cool=23.0,
                TemprSetPoint_Heat=23.0,
                SetCool_Min=0.0,
                SetCool_Max=0.0,
                SetHeat_Min=0.0,
                SetHeat_Max=0.0,
                RemoteZoneInfo=[],
                EnabledZones=[]
            )        

        IsOnline = data.get("isOnline", False)
        data = data.get("lastKnownState", {})
        return SystemStatus(
            SystemName=data.get("NV_SystemSettings", {}).get("SystemName", ""),
            MasterSerial=data.get("AirconSystem", {}).get("MasterSerial", ""),
            LiveTemp_oC=data.get("MasterInfo", {}).get("LiveTemp_oC", 0.0),
            LiveHumidity_pc=data.get("MasterInfo", {}).get("LiveHumidity_pc", 0.0),
            IsOnline=IsOnline,
            IsOn=data.get("UserAirconSettings", {}).get("isOn", False),
            Mode=data.get("UserAirconSettings", {}).get("Mode", ""),
            FanMode=data.get("UserAirconSettings", {}).get("FanMode", ""),
            TemprSetPoint_Cool=data.get("UserAirconSettings", {}).get(
                "TemperatureSetpoint_Cool_oC", "23.0"
            ),
            TemprSetPoint_Heat=data.get("UserAirconSettings", {}).get(
                "TemperatureSetpoint_Heat_oC", "23.0"
            ),
            SetCool_Min=data.get("NV_Limits", {})
            .get("UserSetpoint_oC", {})
            .get("setCool_Min", 0.0),
            SetCool_Max=data.get("NV_Limits", {})
            .get("UserSetpoint_oC", {})
            .get("setCool_Max", 0.0),
            SetHeat_Min=data.get("NV_Limits", {})
            .get("UserSetpoint_oC", {})
            .get("setHeat_Min", 0.0),
            SetHeat_Max=data.get("NV_Limits", {})
            .get("UserSetpoint_oC", {})
            .get("setHeat_Max", 0.0),
            RemoteZoneInfo=[
                ZoneInfo.extract_zone_info(zone)
                for zone in data.get("RemoteZoneInfo", [])
            ],
            EnabledZones=data.get("UserAirconSettings", {}).get("EnabledZones", []),
        )


@dataclass
class CommandResponse:
    """Class that defines a response to a command issued to actron air ac system."""

    CorrelationId: str
    Type: str
    Value: dict
    MWCResponseTime: str

    @staticmethod
    def extract_command_response(data: dict) -> "CommandResponse":
        return CommandResponse(
            CorrelationId=data.get("correlationId", ""),
            Type=data.get("type", ""),
            Value=data.get("value", ""),
            MWCResponseTime=data.get("mwcResponseTime", ""),
        )
