def parse_settings(config_lines):
    result_dictionary={}
    for line in config_lines:
        try:
            list_of_line= line.split(":")
            if len(list_of_line)!=2:
                raise IndexError
            name, value= list_of_line
            value= int(value)
            if value<0 or value>100:
                raise ValueError("Out of range")
            result_dictionary[name]=value
        except IndexError as e:
            print(f"Format error in: {line}")
        except ValueError as e:
            print(f"Invalid value in: {line} ({e})")
    return result_dictionary
configs = [
    "volume:80",          # Valid
    "brightness:120",     # Invalid Range
    "difficulty:hard",    # Invalid Type
    "mute",               # Invalid Format (no colon)
    "contrast:50"         # Valid
]
settings = parse_settings(configs)
print(f"Loaded Settings: {settings}")


        
            