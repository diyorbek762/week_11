def process_commands(device_db, command_list):
    for command in command_list:
        command_seperated=command.split(":")
        try:
            command_seperated=command.split(":")
            if len(command_seperated)!=3:
                raise ValueError("Invalid command format")
            if command_seperated[0] not in device_db:
                raise KeyError ("Unknown device")
            if command_seperated[1].upper() !="SET":
                raise ValueError ("Unsupported action")
            # command_int=int(command_seperated[2])
            try:
                command_int = int(command_seperated[2])
            except ValueError:
                raise ValueError(f"Value '{command_seperated[2]}' must be an integer")
            specific_req= device_db.get(command_seperated[0])
            min, max= specific_req.get("range")
            if command_int<min or command_int>max:
                raise ValueError("Value out of range")
        except ValueError as e:
            print(f"Skipping command '{command_seperated[0]}': {e}")
        except KeyError as e:
            print(f"Skipping command '{command_seperated[0]}': {e}")
        else:
            print(f"Updated {command_seperated[0]} to {int(command_seperated[2])}")
            device_db[command_seperated[0]]["value"]=int(command_seperated[2])
            

    print(f"Final: {device_db}")
devices = {
    "LIGHT_LIVING": {"type": "dimmer", "value": 50, "range": (0, 100)},
    "THERMOSTAT":   {"type": "temp",   "value": 22, "range": (15, 30)},
    "DOOR_LOCK":    {"type": "binary", "value": 0,  "range": (0, 1)} # 0=Locked, 1=Unlocked
}           

cmds = [
    "LIGHT_LIVING:SET:100",    # Valid
    "LIGHT_LIVING:SET:200",    # Out of range
    "THERMOSTAT:COOL:20",      # Invalid Action
    "GARAGE_DOOR:SET:1",       # Unknown Device
    "DOOR_LOCK:SET:OPEN",      # Invalid Value Type
    "bad_format_command"       # Bad Format
]
process_commands(devices, cmds)
devices = {"LIGHT_LIVING": {"type": "dimmer", "value": 50, "range": (0, 100)}}
cmds = ["LIGHT_LIVING:SET:100"]

process_commands(devices, cmds)

