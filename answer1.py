def ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        print("Invalid IP")
        return
    
    for x in parts:
        if not x.isdigit() or not (0 <= int(x) <= 255):
            print("Invalid IP")
            return
    
    fi_oc, sec_oc = int(parts[0]), int(parts[1])
    
    if (fi_oc == 10 or
        (fi_oc == 172 and 16 <= sec_oc <= 31) or
        (fi_oc == 192 and sec_oc == 168)):
        print("IP is in a private range.")
        return
    
    print(f"Valid IP: {ip}")

def gmail(email):
    if "@gmail.com" not in email:
        print("Invalid Gmail address ")
        return
    
    usr = email.split('@')[0]
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789._%+-"
    
    for char in usr:
        if char not in allowed_chars:
            print("Invalid Gmail address format.")
            return
    
    print(f"Valid Gmail address: {email}")

ip_input = input("Enter an IPaddress: ")
ip(ip_input)

email_input = input("Enter a Gmail address: ")
gmail(email_input)
