SYSTEM_STATUS_RESPONSE = {
    "isOnline": False,
    "timeSinceLastContact": "2.10:26:15.3597948",
    "lastStatusUpdate": "2025-01-19T01:36:31+00:00",
    "lastKnownState": {
        "<22B02562>": {
            "Cloud": {
                "ConnectionState": "Connected",
                "FailedSentPackets": 0,
                "ReceivedPackets": 5473,
                "SentPackets": 3952,
                "Connection": {
                    "UpTime": {
                        "SinceLastMCUReset_s": 33464,
                        "CurrentSession_s": 33464
                    },
                    "SessionCount": {
                        "SinceLastMCUReset": 0,
                        "PriorToLastMCUReset": 0
                    },
                    "ErrorCount": {
                        "AbortedSockets": 0,
                        "LoopbackError": 0,
                        "DNSFailures": 0
                    }
                }
            },
            "Modbus": {
                "LinkPort": "Demo"
            },
            "NV_SystemSettings_Local": {
                "OTA": {
                    "Mode": 2,
                    "CheckInterval": {
                        "Mode1_Period_min": 1440,
                        "Mode2_TimeOfDay": "T02:00:00"
                    },
                    "LastCheck": {
                        "Trigger": "",
                        "Time": "2020-01-01T00:00:16",
                        "Result": "",
                        "Images": [
                            0
                        ]
                    },
                    "NextCheck": {
                        "Time": "2025-01-20T02:06:08"
                    }
                }
            },
            "SystemState": {
                "CpuId": "0x002D003C3039510537343535",
                "LastShutdownReason": "Power On",
                "MCUResetCountSincePOR": {
                    "Total": 0,
                    "Remote": 0
                },
                "HardFaultDebug": {
                    "Type": "0",
                    "IncidentCount": 0,
                    "LastIncidentTime": "NA",
                    "CoreRegisterDump": {
                        "R0": "0x00000000",
                        "R1": "0x00000000",
                        "R2": "0x00000000",
                        "R3": "0x00000000",
                        "R12": "0x00000000",
                        "LR": "0x00000000",
                        "PC": "0x00000000",
                        "PSR": "0x00000000"
                    }
                },
                "RTOS": {
                    "BlockingTaskMonitor": {
                        "Id": 0,
                        "TimeStamp": "NA",
                        "Parameters": [
                            0
                        ],
                        "StackDump": [
                            0
                        ]
                    }
                },
                "WCFirmwareVersion": "NEO v2.1.6.1, Jan  3 2025 16:39:19",
                "WCBootloaderVersion": "1.0.2.0",
                "ExternalFlash": {
                    "GFXAssets": {
                        "Primary": {
                            "Version": {
                                "Installed": "1.1.0.2",
                                "Required": "1.1.0.2"
                            },
                            "CRC": "OK"
                        },
                        "Secondary": {
                            "Version": {
                                "Installed": "1.0.4.2",
                                "Required": "1.0.4.2"
                            },
                            "CRC": "OK"
                        }
                    },
                    "FirmwareImages": {
                        "STM32_NEO": "",
                        "PIC24_ODU": "No Image",
                        "PIC24_Inzone": "3.30",
                        "PIC24_CMI": "0.0",
                        "NRF52_BLECentral": "1.1.0.0",
                        "NRF52_BLEPeripheral1": "1.1.4.2",
                        "NRF52_BLEPeripheral2": "No Image",
                        "WINC1500": "No Image"
                    }
                }
            },
            "SystemStatus_Local": {
                "Uptime_s": 33485,
                "WifiStrength_of3": -59,
                "SensorInputs": {
                    "SHTC1": {
                        "RelativeHumidity_pc": 69.3,
                        "Temperature_oC": 24.8
                    },
                    "RS485": {
                        "AInput_Voltage": 3.1,
                        "BInput_Voltage": 0.2,
                        "Current": 3.0
                    },
                    "PSU_Voltage": 12.0,
                    "AmbientLight": 7.0,
                    "Thermistors": {
                        "NearAmbient_oC": 25.6,
                        "WiFi_oC": 33.1,
                        "MainPCB_oC": 36.5,
                        "RoomAmbient_oC": 23.8
                    },
                    "TOF": {
                        "Enabled": True,
                        "Range_mm": 1154.0
                    }
                },
                "WiFi": {
                    "FirmwareVersion": "19.6.1",
                    "DriverVersion": "19.3.0",
                    "ModuleMACAddress": "F8:F0:05:7C:C0:D2",
                    "ApSSID": "Chandu_2G",
                    "ApBSSID": "E4:DA:DF:7F:F3:B9",
                    "RFChannel": 10,
                    "ConnectionCount": 1,
                    "DisconnectCount": 0,
                    "DeinitCount": 0,
                    "HardwareErrorCount": 0
                },
                "TouchScreen": {
                    "LastTouchTime": "NA",
                    "State": 0,
                    "XCoordinate": 0,
                    "YCoordinate": 0,
                    "I2CErrorCount": 0,
                    "ControllerModel": "FocalTech FT5426"
                },
                "TouchButton": {
                    "State": 0,
                    "I2CErrorCount": 0
                },
                "GUI": {
                    "ActiveScreen": "DISPLAY OFF"
                },
                "BTLE": {
                    "Central": {
                        "Mode": "NEO2 BTLE",
                        "FirmwareVersion": "1.1.0.0"
                    }
                }
            }
        },
        "AirconSystem": {
            "MasterWCModel": "NTB-1000",
            "MasterSerial": "22B02562",
            "MasterWCFirmwareVersion": "2.1.6.1",
            "IndoorUnit": {
                "Battery_Backup_Voltage": 0.0,
                "NV_ModelNumber": "0",
                "SerialNumber": "0",
                "IndoorFW": "3.99",
                "NV_SupportedFanModes": 4,
                "NV_AutoFanEnabled": True
            },
            "OutdoorUnit": {
                "Family": "Inverter: Advance Series I Single Phase",
                "Capacity_kW": 14,
                "ModelNumber": "0",
                "SerialNumber": "0",
                "SoftwareVersion": "3.99",
                "CtrlBoardType": "Type 150: Uno (PIC24FJ128GA308)"
            },
            "WallControllers": [
                {
                    "Address": "C1",
                    "Type": "NEO",
                    "FirmwareVersion": "0.0.0.0"
                },
                {
                    "Address": "C2",
                    "Type": "LR7",
                    "FirmwareVersion": "0.0"
                },
                {
                    "Address": "C3",
                    "Type": "LC7",
                    "FirmwareVersion": "0.0"
                }
            ],
            "Sensors": [
                {
                    "Designator": "C1",
                    "Detected": True,
                    "Enabled": True,
                    "Temperature_oC": 23.7,
                    "TemperatureOffset_oC": 0.0
                },
                {
                    "Designator": "C2",
                    "Detected": True,
                    "Enabled": True,
                    "Temperature_oC": 24.6,
                    "TemperatureOffset_oC": 0.0
                },
                {
                    "Designator": "C3",
                    "Detected": True,
                    "Enabled": True,
                    "Temperature_oC": 24.1,
                    "TemperatureOffset_oC": 0.0
                },
                {
                    "Designator": "RS1",
                    "Detected": True,
                    "Enabled": True,
                    "Temperature_oC": 24.3,
                    "TemperatureOffset_oC": 0.0
                },
                {
                    "Designator": "RS2",
                    "Detected": True,
                    "Enabled": True,
                    "Temperature_oC": 25.2,
                    "TemperatureOffset_oC": 0.0
                },
                {
                    "Designator": "RS3",
                    "Detected": True,
                    "Enabled": True,
                    "Temperature_oC": 24.3,
                    "TemperatureOffset_oC": 0.0
                }
            ],
            "Peripherals": [
                {
                    "LogicalAddress": 1,
                    "DeviceType": "Zone Controller",
                    "SerialNumber": "22G08389",
                    "MACAddress": "BC:89:83:1C:22:CB",
                    "ZoneAssignment": [
                        0
                    ],
                    "ConnectionState": "Disconnected",
                    "Firmware": {
                        "InstalledVersion": {
                            "NRF52": "0.0.0.0",
                            "EFM8": "NA"
                        },
                        "Update": {
                            "CurrentState": "Idle",
                            "CurrentInstallProgress_pc": -1,
                            "Events": {
                                "LastStartTime": "NA",
                                "LastCompleteTime": "NA",
                                "LastFailureTime": "NA",
                                "LastFailureStep": "Idle"
                            },
                            "RunCount": 0,
                            "FailureCount": 0
                        }
                    },
                    "LastConnectionTime": "NA",
                    "ConnectionEventCounts": 0,
                    "RSSI": {
                        "Local": 0,
                        "Remote": "NA"
                    },
                    "RemainingBatteryCapacity_pc": 0,
                    "SensorInputs": {
                        "BatteyLevels": {
                            "B1V5": 0.0,
                            "B3V3": 0.0,
                            "B4V5": 0.0
                        },
                        "RS485": {
                            "PSU_Voltage": "NA"
                        },
                        "SHTC1": {
                            "RelativeHumidity_pc": 0,
                            "Temperature_oC": 0.0
                        },
                        "Thermistors": {
                            "Ambient_oC": 0.0,
                            "Wall_oC": 0.0
                        }
                    }
                }
            ]
        },
        "Alerts": {
            "CleanFilter": False,
            "Defrosting": False
        },
        "AwayModeSavedState": {
            "Master": {
                "TemperatureSetpoint_Cool_oC": 0.0,
                "TemperatureSetpoint_Heat_oC": 0.0
            }
        },
        "LiveAircon": {
            "AmRunningFan": False,
            "CoilInlet": 20.7,
            "CompressorCapacity": 0,
            "CompressorChasingTemperature": 23.0,
            "CompressorLiveTemperature": 23.7,
            "CompressorMode": "OFF",
            "DRM": False,
            "Defrost": False,
            "ErrCode": 0,
            "FanPWM": 0,
            "FanRPM": 0,
            "IndoorUnitTemp": 0,
            "OutdoorUnit": {
                "AmbTemp": 25.3,
                "AmbientSensErr": False,
                "CoilSenseErr": False,
                "CoilTemp": 23.3,
                "CompPower": 0,
                "CompRunningPWM": 0,
                "CompSpeed": 0.0,
                "CompressorMode": 0,
                "CompressorOn": False,
                "CompressorSetSpeed": 0,
                "CondPc": 15.3,
                "DRM": 0,
                "DefrostMode": 0,
                "DischargeTemp": 23.1,
                "EEV": {
                    "Opening_pc": 0,
                    "SuperHeat": 0.0,
                    "SuperHeatRef": 0,
                    "Type": "UKV-SE"
                },
                "EXV": False,
                "ErrCode_1": 0,
                "ErrCode_2": 0,
                "ErrCode_3": 0,
                "ErrCode_4": 0,
                "ErrCode_5": 0,
                "OilReturn": False,
                "OilReturnEnable": False,
                "RemoteOnOff": False,
                "RoomTemp": 23.7,
                "RoomTempODU": 23.7,
                "RoomTempSet": 23.7,
                "SuctP0": 15.3,
                "SuctTemp": 23.0,
                "EnvelopeProtection": False,
                "ReverseValvePosition": "Cool",
                "OverheatProtection": False,
                "SupplyVoltage_Vac": 0.0,
                "SuppyCurrentRMS_A": 0.0,
                "SuppyPowerRMS_W": 0.0,
                "DriveTemp": 0.0,
                "LPErr": False,
                "HPErr": False,
                "OHP": {
                    "TargetLine": 0,
                    "TargetCondTemp_oC": 0.0,
                    "StartTemp_oC": 0.0
                }
            },
            "SystemOn": False
        },
        "MasterInfo": {
            "LiveHumidity_pc": 69.3,
            "LiveOutdoorTemp_oC": 25.3,
            "LiveTempHysteresis_oC": 23.7,
            "LiveTemp_oC": 23.7,
            "RemoteHumidity_pc": {
                "22B02562": 69.3
            }
        },
        "NV_Limits": {
            "UserSetpoint_oC": {
                "MinGap": 0.0,
                "VarianceAboveMasterCool": 0.0,
                "VarianceAboveMasterHeat": 0.0,
                "VarianceBelowMasterCool": 0.0,
                "VarianceBelowMasterHeat": 0.0,
                "setCool_Max": 30.0,
                "setCool_Min": 16.0,
                "setHeat_Max": 30.0,
                "setHeat_Min": 16.0
            }
        },
        "NV_QuickTimer": {
            "Master": [
                {
                    "OriginalTime": "01:00",
                    "Status": "Stopped",
                    "Mode": "Timer",
                    "Time": "00:00:00",
                    "Zones": [
                        True,
                        True,
                        True,
                        True,
                        True,
                        True,
                        True,
                        True
                    ]
                }
            ]
        },
        "NV_Schedule": {
            "Enabled": True,
            "Events": [
                {
                    "ID": 0,
                    "Name": "fanschedule",
                    "StartTime": "T21:00",
                    "EndTime": "T22:00",
                    "DaysOfOperation": [
                        "TUE",
                        "WED"
                    ],
                    "Enabled": True,
                    "EnabledZones": [
                        False,
                        False,
                        False,
                        False,
                        True,
                        False,
                        False,
                        False
                    ],
                    "Mode": "FAN",
                    "FanMode": "AUTO",
                    "TemperatureSetpoint_Cool_oC": 21.0,
                    "TemperatureSetpoint_Heat_oC": 21.0
                },
                {
                    "ID": 1,
                    "Name": "coolsheu.e",
                    "StartTime": "T22:00",
                    "EndTime": "T23:00",
                    "DaysOfOperation": [
                        "MON",
                        "WED",
                        "THU"
                    ],
                    "Enabled": True,
                    "EnabledZones": [
                        True,
                        False,
                        False,
                        False,
                        False,
                        False,
                        False,
                        False
                    ],
                    "Mode": "COOL",
                    "FanMode": "LOW",
                    "TemperatureSetpoint_Cool_oC": 17.0,
                    "TemperatureSetpoint_Heat_oC": 17.0
                },
                {
                    "ID": 2,
                    "Name": "heatschedule",
                    "StartTime": "T22:00",
                    "EndTime": "T23:00",
                    "DaysOfOperation": [
                        "MON"
                    ],
                    "Enabled": False,
                    "EnabledZones": [
                        False,
                        False,
                        True,
                        False,
                        False,
                        False,
                        False,
                        False
                    ],
                    "Mode": "HEAT",
                    "FanMode": "MED",
                    "TemperatureSetpoint_Cool_oC": 24.0,
                    "TemperatureSetpoint_Heat_oC": 24.0
                },
                {
                    "ID": 3,
                    "Name": "autoshedule",
                    "StartTime": "T19:00",
                    "EndTime": "T20:00",
                    "DaysOfOperation": [
                        "MON",
                        "WED"
                    ],
                    "Enabled": False,
                    "EnabledZones": [
                        True,
                        False,
                        False,
                        False,
                        False,
                        False,
                        False,
                        False
                    ],
                    "Mode": "AUTO",
                    "FanMode": "HIGH",
                    "TemperatureSetpoint_Cool_oC": 22.0,
                    "TemperatureSetpoint_Heat_oC": 22.0
                }
            ]
        },
        "NV_SystemSettings": {
            "AwayMode": {
                "TemperatureSetpoint_Cool_oC": 0.0,
                "TemperatureSetpoint_Heat_oC": 0.0,
                "TemperatureMinLimit_Cool_oC": 26.0,
                "TemperatureMaxLimit_Cool_oC": 36.0,
                "TemperatureMinLimit_Heat_oC": 10.0,
                "TemperatureMaxLimit_Heat_oC": 20.0
            },
            "Logs": {
                "snapshotTime_ms": 900000
            },
            "Display": {
                "HomeScreen": {
                    "BackgroundColour": "Black",
                    "Brightness": 50
                },
                "ScreenSaver": {
                    "Enabled": True,
                    "Timeout_s": 60,
                    "Brightness": 30
                },
                "ScreenOff": {
                    "Enabled": True,
                    "Timeout_s": 60
                }
            },
            "ProxmitySensor": {
                "Enabled": True,
                "Range_cm": 60
            },
            "LEDIndicators": {
                "WallGlow": {
                    "Enabled": True
                },
                "OnOffButton": {
                    "Enabled": True
                }
            },
            "Locks": {
                "PIN": "",
                "RentryTimeout_s": 0,
                "HomeScreen": {
                    "ModeSelector": False,
                    "TemperatureSetpoint": False,
                    "FanSpeed": False,
                    "OnOffButton": False
                },
                "MenuSystem": {
                    "OptionsButton": False,
                    "Timer": False,
                    "Schedule": False,
                    "WiFiAccount": False,
                    "SystemSettings": False
                }
            },
            "SystemName": "NEO_22B02562",
            "Time": {
                "SetAutomatically": True,
                "TimeMode24h": True,
                "Timezone": "Australia/Sydney",
                "Timezone_Readable": "NSW, Australia"
            },
            "UpdateTime": "T02:00:00",
            "UserACSettings": {
                "ControlParameters": {
                    "Compressor": {
                        "CutIn": {
                            "Cool_degC": 0.2,
                            "Heat_degC": 0.2
                        },
                        "CutOut": {
                            "Cool_degC": -0.5,
                            "Heat_degC": -0.5
                        },
                        "LowDemand": {
                            "Heat": {
                                "Supported": True,
                                "Enabled": False,
                                "Trigger_pc": 0,
                                "RunTime_m": 0
                            },
                            "Cool": {
                                "Supported": True,
                                "Enabled": False,
                                "Trigger_pc": 0,
                                "RunTime_m": 0
                            }
                        },
                        "MinimumDemand": {
                            "Heat": {
                                "Supported": True,
                                "Enabled": False,
                                "Demand_pc": 0
                            },
                            "Cool": {
                                "Supported": True,
                                "Enabled": False,
                                "Demand_pc": 0
                            }
                        },
                        "MaximumDemand": {
                            "Heat": {
                                "Supported": True,
                                "Demand_pc": 0
                            },
                            "Cool": {
                                "Supported": True,
                                "Demand_pc": 0
                            }
                        },
                        "ProtectionLimits": {
                            "Antifreeze": {
                                "EndTemperature_degC": 0.0,
                                "TargetTemperature_degC": 0.0,
                                "TriggerTemperature_degC": 0.0
                            },
                            "Overheat": {
                                "TriggerTemperature_degC": 55.0
                            }
                        },
                        "Deadband_degC": 1.5,
                        "Proportional": 0.0
                    }
                },
                "DraftReduction": {
                    "HotStart": {
                        "Enabled": False,
                        "Temperature_degC": 25.0,
                        "Time_s": 0
                    },
                    "MinimumAirflow": {
                        "Supported": True,
                        "Enabled": False,
                        "Level": 0
                    }
                },
                "FanAlertTime_h": 200,
                "Fanspeed": {
                    "High": 85,
                    "HighDefault": 85,
                    "HighRPM": 1500,
                    "Low": 42,
                    "LowDefault": 42,
                    "LowRPM": 1150,
                    "Med": 56,
                    "MedDefault": 56,
                    "MedRPM": 1290,
                    "DefrostFanPWM": 10,
                    "PowerOnTestRPM": 0,
                    "NumberOfPoles": 0,
                    "RPMErrorCheckEnabled": True
                },
                "enableFastHeat": False,
                "restoreSettingsOnPowerUp": False
            }
        },
        "RemoteZoneInfo": [
            {
                "CanOperate": True,
                "CommonZone": False,
                "LiveHumidity_pc": 69.3,
                "LiveTempHysteresis_oC": 23.7,
                "LiveTemp_oC": 23.7,
                "NV_Exists": True,
                "NV_Title": "Zone 1",
                "NV_VAV": False,
                "NV_ITC": False,
                "NV_ITD": False,
                "NV_IHD": True,
                "NV_IAC": False,
                "AirflowControlEnabled": False,
                "AirflowControlLocked": False,
                "NV_amSetup": True,
                "LastZoneProtection": True,
                "Sensors": {
                    "22B02562": {
                        "Connected": False,
                        "NV_Kind": "C1",
                        "NV_isPaired": False,
                        "NV_isViaRepeater": False,
                        "Signal_of3": "NA",
                        "TX_Power": 0,
                        "lastRssi": "NA"
                    }
                },
                "TemperatureSetpoint_Cool_oC": 23.0,
                "TemperatureSetpoint_Heat_oC": 21.0,
                "AirflowSetpoint": 0,
                "ZonePosition": 20
            },
            {
                "CanOperate": True,
                "CommonZone": False,
                "LiveHumidity_pc": 69.3,
                "LiveTempHysteresis_oC": 23.7,
                "LiveTemp_oC": 23.7,
                "NV_Exists": True,
                "NV_Title": "Zone 2",
                "NV_VAV": False,
                "NV_ITC": False,
                "NV_ITD": False,
                "NV_IHD": True,
                "NV_IAC": False,
                "AirflowControlEnabled": False,
                "AirflowControlLocked": False,
                "NV_amSetup": True,
                "LastZoneProtection": False,
                "Sensors": {
                    "22B02562": {
                        "Connected": False,
                        "NV_Kind": "C1",
                        "NV_isPaired": False,
                        "NV_isViaRepeater": False,
                        "Signal_of3": "NA",
                        "TX_Power": 0,
                        "lastRssi": "NA"
                    }
                },
                "TemperatureSetpoint_Cool_oC": 23.0,
                "TemperatureSetpoint_Heat_oC": 21.0,
                "AirflowSetpoint": 0,
                "ZonePosition": 20
            },
            {
                "CanOperate": True,
                "CommonZone": False,
                "LiveHumidity_pc": 69.3,
                "LiveTempHysteresis_oC": 23.7,
                "LiveTemp_oC": 23.7,
                "NV_Exists": True,
                "NV_Title": "Zone 3",
                "NV_VAV": False,
                "NV_ITC": False,
                "NV_ITD": False,
                "NV_IHD": True,
                "NV_IAC": False,
                "AirflowControlEnabled": False,
                "AirflowControlLocked": False,
                "NV_amSetup": True,
                "LastZoneProtection": False,
                "Sensors": {
                    "22B02562": {
                        "Connected": False,
                        "NV_Kind": "C1",
                        "NV_isPaired": False,
                        "NV_isViaRepeater": False,
                        "Signal_of3": "NA",
                        "TX_Power": 0,
                        "lastRssi": "NA"
                    }
                },
                "TemperatureSetpoint_Cool_oC": 23.0,
                "TemperatureSetpoint_Heat_oC": 21.0,
                "AirflowSetpoint": 0,
                "ZonePosition": 0
            },
            {
                "CanOperate": True,
                "CommonZone": False,
                "LiveHumidity_pc": 69.3,
                "LiveTempHysteresis_oC": 23.7,
                "LiveTemp_oC": 23.7,
                "NV_Exists": True,
                "NV_Title": "Zone 4",
                "NV_VAV": False,
                "NV_ITC": False,
                "NV_ITD": False,
                "NV_IHD": True,
                "NV_IAC": False,
                "AirflowControlEnabled": False,
                "AirflowControlLocked": False,
                "NV_amSetup": True,
                "LastZoneProtection": False,
                "Sensors": {
                    "22B02562": {
                        "Connected": False,
                        "NV_Kind": "C1",
                        "NV_isPaired": False,
                        "NV_isViaRepeater": False,
                        "Signal_of3": "NA",
                        "TX_Power": 0,
                        "lastRssi": "NA"
                    }
                },
                "TemperatureSetpoint_Cool_oC": 23.0,
                "TemperatureSetpoint_Heat_oC": 21.0,
                "AirflowSetpoint": 0,
                "ZonePosition": 0
            },
            {
                "CanOperate": True,
                "CommonZone": False,
                "LiveHumidity_pc": 69.3,
                "LiveTempHysteresis_oC": 23.7,
                "LiveTemp_oC": 23.7,
                "NV_Exists": True,
                "NV_Title": "Zone 5",
                "NV_VAV": False,
                "NV_ITC": False,
                "NV_ITD": False,
                "NV_IHD": True,
                "NV_IAC": False,
                "AirflowControlEnabled": False,
                "AirflowControlLocked": False,
                "NV_amSetup": True,
                "LastZoneProtection": False,
                "Sensors": {
                    "22B02562": {
                        "Connected": False,
                        "NV_Kind": "C1",
                        "NV_isPaired": False,
                        "NV_isViaRepeater": False,
                        "Signal_of3": "NA",
                        "TX_Power": 0,
                        "lastRssi": "NA"
                    }
                },
                "TemperatureSetpoint_Cool_oC": 23.0,
                "TemperatureSetpoint_Heat_oC": 21.0,
                "AirflowSetpoint": 0,
                "ZonePosition": 0
            },
            {
                "CanOperate": True,
                "CommonZone": False,
                "LiveHumidity_pc": 69.3,
                "LiveTempHysteresis_oC": 23.7,
                "LiveTemp_oC": 23.7,
                "NV_Exists": True,
                "NV_Title": "Zone 6",
                "NV_VAV": False,
                "NV_ITC": False,
                "NV_ITD": False,
                "NV_IHD": True,
                "NV_IAC": False,
                "AirflowControlEnabled": False,
                "AirflowControlLocked": False,
                "NV_amSetup": True,
                "LastZoneProtection": False,
                "Sensors": {
                    "22B02562": {
                        "Connected": False,
                        "NV_Kind": "C1",
                        "NV_isPaired": False,
                        "NV_isViaRepeater": False,
                        "Signal_of3": "NA",
                        "TX_Power": 0,
                        "lastRssi": "NA"
                    }
                },
                "TemperatureSetpoint_Cool_oC": 23.0,
                "TemperatureSetpoint_Heat_oC": 21.0,
                "AirflowSetpoint": 0,
                "ZonePosition": 0
            },
            {
                "CanOperate": True,
                "CommonZone": False,
                "LiveHumidity_pc": 69.3,
                "LiveTempHysteresis_oC": 23.7,
                "LiveTemp_oC": 23.7,
                "NV_Exists": True,
                "NV_Title": "Zone 7",
                "NV_VAV": False,
                "NV_ITC": False,
                "NV_ITD": False,
                "NV_IHD": True,
                "NV_IAC": False,
                "AirflowControlEnabled": False,
                "AirflowControlLocked": False,
                "NV_amSetup": True,
                "LastZoneProtection": False,
                "Sensors": {
                    "22B02562": {
                        "Connected": False,
                        "NV_Kind": "C1",
                        "NV_isPaired": False,
                        "NV_isViaRepeater": False,
                        "Signal_of3": "NA",
                        "TX_Power": 0,
                        "lastRssi": "NA"
                    }
                },
                "TemperatureSetpoint_Cool_oC": 23.0,
                "TemperatureSetpoint_Heat_oC": 21.0,
                "AirflowSetpoint": 0,
                "ZonePosition": 0
            },
            {
                "CanOperate": True,
                "CommonZone": False,
                "LiveHumidity_pc": 69.3,
                "LiveTempHysteresis_oC": 23.7,
                "LiveTemp_oC": 23.7,
                "NV_Exists": True,
                "NV_Title": "Zone 8",
                "NV_VAV": False,
                "NV_ITC": False,
                "NV_ITD": False,
                "NV_IHD": True,
                "NV_IAC": False,
                "AirflowControlEnabled": False,
                "AirflowControlLocked": False,
                "NV_amSetup": True,
                "LastZoneProtection": False,
                "Sensors": {
                    "22B02562": {
                        "Connected": False,
                        "NV_Kind": "C1",
                        "NV_isPaired": False,
                        "NV_isViaRepeater": False,
                        "Signal_of3": "NA",
                        "TX_Power": 0,
                        "lastRssi": "NA"
                    }
                },
                "TemperatureSetpoint_Cool_oC": 23.0,
                "TemperatureSetpoint_Heat_oC": 21.0,
                "AirflowSetpoint": 0,
                "ZonePosition": 0
            }
        ],
        "Servicing": {
            "NV_ErrorHistory": [],
            "NV_AC_EventHistory": [
                {
                    "Id": 0,
                    "Task": "MODBUS",
                    "TimeStamp": "2020-01-01T00:00:05",
                    "Event": "Modbus State Change",
                    "Parameters": [
                        "Demo Mode"
                    ]
                },
                {
                    "Id": 1,
                    "Task": "MODBUS",
                    "TimeStamp": "2020-01-01T00:00:05",
                    "Event": "Modbus State Change",
                    "Parameters": [
                        "Error Comms Loss"
                    ]
                }
            ],
            "NV_WC_EventHistory": [
                {
                    "Id": 0,
                    "Task": "WiFi",
                    "TimeStamp": "2020-01-01T00:00:16",
                    "Event": "AP Connect (DHCP IP)",
                    "Parameters": [
                        0
                    ]
                },
                {
                    "Id": 1,
                    "Task": "Touch Button Controller",
                    "TimeStamp": "2020-01-01T00:00:00",
                    "Event": "Cap Touch Button Event",
                    "Parameters": [
                        {
                            "State": "0"
                        }
                    ]
                }
            ]
        },
        "Installer": {
            "Id": "",
            "Name": "",
            "Email": "",
            "Phone": ""
        },
        "UserAirconSettings": {
            "AfterHours": {
                "Enabled": False,
                "Duration": 120
            },
            "ApplicationMode": "Residential",
            "AwayMode": False,
            "EnabledZones": [
                True,
                True,
                False,
                False,
                False,
                False,
                False,
                False
            ],
            "FanMode": "MED",
            "Mode": "AUTO",
            "NV_SavedZoneState": [
                True,
                True,
                False,
                False,
                False,
                False,
                False,
                False
            ],
            "QuietMode": False,
            "QuietModeEnabled": False,
            "QuietModeActive": False,
            "ServiceReminder": {
                "Enabled": False,
                "Time": "NA"
            },
            "VFT": {
                "Airflow": 0.0,
                "StaticPressure": 0.0,
                "Supported": True,
                "Enabled": True,
                "SelfLearn": {
                    "LastRunTime": "NA",
                    "CurrentState": "Idle",
                    "LastResult": "Idle",
                    "MaxStaticPressure": 0
                }
            },
            "TurboMode": {
                "Supported": True,
                "Enabled": False
            },
            "TemperatureSetpoint_Cool_oC": 23.0,
            "TemperatureSetpoint_Heat_oC": 23.0,
            "ZoneTemperatureSetpointVariance_oC": 2.0,
            "isFastHeating": False,
            "isOn": False,
            "ChangeSrc": {
                "Mode": "None",
                "isOn": "None"
            }
        },
        "type": "full-status-broadcast",
        "@metadata": {
            "connectionId": "",
            "server": "pd0sdwk0003Q8/5288"
        }
    }
}