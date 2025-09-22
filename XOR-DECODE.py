import base64

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

def decode_string(encoded_str, key="UTF-8"):
    """Base64 decode + XOR with key (UTF-8)"""
    try:
        byte_array = bytearray(base64.b64decode(encoded_str))
    except Exception:
        return f"{RED}Invalid Base64{RESET}"

    key_len = len(key)
    for i in range(len(byte_array)):
        byte_array[i] ^= ord(key[i % key_len])
    try:
        return f"{GREEN}{byte_array.decode('utf-8')}{RESET}"
    except Exception:
        return f"{RED}Cannot decode bytes to UTF-8{RESET}"

# Axe art in green
print(f'''
{GREEN}  /:\\      /:.
 //  \\_()_/  \\
||   |    |   ||
||   | $  |   ||
||   |____|   ||
  \\  / || \\  //
  `:/  ||  \\;'
       ||
       ||
       XX
       XX
       XX
       XX
       OO
       ππ    Version 1.0.0{RESET}
''')

print("   • Interactive Base64+XOR decoder (type 'exit' to quit! [Copyright Shauryadeep ])\n")

while True:
    encoded_input = input(f"{YELLOW}Enter encoded string: {RESET}").strip()
    if encoded_input.lower() == "exit":
        print(f"{RED}Exiting...{RESET}")
        break
    decoded_output = decode_string(encoded_input)
    print(f"Decoded: {decoded_output}\n")
