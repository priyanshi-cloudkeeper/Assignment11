def validate_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        print("Invalid IP")
        return
    
    for x in parts:
        if not x.isdigit() or not (0 <= int(x) <= 255):
            print("Invalid IP")
            return
    
    first_octet, second_octet = int(parts[0]), int(parts[1])
    
    if (first_octet == 10 or
        (first_octet == 172 and 16 <= second_octet <= 31) or
        (first_octet == 192 and second_octet == 168)):
        print("IP is in a private range.")
        return
    
    print(f"Valid IP: {ip}")

def validate_gmail(email):
    if "@gmail.com" not in email:
        print("Invalid Gmail address ")
        return
    
    username = email.split('@')[0]
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789._%+-"
    
    for char in username:
        if char not in allowed_chars:
            print("Invalid Gmail address format.")
            return
    
    print(f"Valid Gmail address: {email}")

# Example inputs
ip_input = input("Enter an IPaddress: ")
validate_ipv4(ip_input)

email_input = input("Enter a Gmail address: ")
validate_gmail(email_input)
