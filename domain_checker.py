import requests
import time 

url = "https://www.iranserver.com/ajax/searchDomainWhoisChecker/"

with open("domains.txt", "r") as input_file:
    domains = input_file.readlines()

with open("azad.txt", "w") as output_file:
    for domain in domains:
        domain = domain.strip()  
        if domain:  
            data = {
                "domain": domain
            }
            
            response = requests.post(url, json=data)
            response_json = response.json()  
            print(response_json)

            res = response_json[0].get('available', False)

            if res == True:
                print(f"Domain {domain} is available.")
                output_file.write(f'{domain}\n')

            
            time.sleep(2)  

print("دامنه‌های آزاد در فایل azad.txt ذخیره شدند.")
