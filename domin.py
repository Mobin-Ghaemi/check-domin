import socket

def check_ir_domain(domain: str):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect(("whois.nic.ir", 43))
            s.sendall((domain + "\r\n").encode())

            response = b""
            while True:
                data = s.recv(4096)
                if not data:
                    break
                response += data

        result = response.decode("utf-8").lower()

        if "no entries found" in result:
            return True  
        else:
            return False 
    except Exception as e:
        print(f"⚠️ Error checking domain: {e}")
        return False

def check_domains():
    available_domains = []

    try:
        with open("domains.txt", "r") as file:
            domains = file.readlines()
    except FileNotFoundError:
        print("⚠️ File 'domains.txt' not found.")
        return
    
    for domain in domains:
        print('dddd',domain)
        domain = domain.strip()  
        if check_ir_domain(domain):
            available_domains.append(domain)

    with open("free.txt", "w") as f:
        for domain in available_domains:
            f.write(domain + "\n")

    print("Done! Available domains are saved in 'free.txt'.")

check_domains()
