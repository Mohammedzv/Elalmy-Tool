import time
import sys
import random

def elalmy_long_search():
    R = '\033[31m'
    G = '\033[92m'
    W = '\033[97m'
    END = '\033[0m'

    print(f"{R}--- ELALMY_CYBER_CORE_V.4.0 ---{END}")
    print(f"{G}[!] SYSTEM: STARTING DEEP SEARCH [DURATION: 5 MINS]{END}\n")
    
    target = input(f"{W}[?] TARGET DOMAIN: {END}")
    
    # الـ 5 دقائق (300 ثانية)
    duration = 300 
    start_time = time.time()
    
    print(f"{G}[*] SCANNING STARTED... PLEASE WAIT.{END}")
    
    while time.time() - start_time < duration:
        # محاكاة البحث
        sys.stdout.write(f"\r{W}[*] SEARCHING... SECONDS ELAPSED: {int(time.time() - start_time)}  {END}")
        sys.stdout.flush()
        time.sleep(1) # تحديث كل ثانية
        
    print(f"\n\n{G}[+] SEARCH COMPLETE!{END}")
    print(f"{G}[+] RESULTS FOUND:{END}\n")
    
    # عرض الحسابات العشوائية الوهمية في النهاية
    for i in range(1, 4):
        fake_acc = f"elalmy_user{random.randint(100,999)}@example.com:pass_{random.randint(100000,999999)}"
        print(f"{R} >> FOUND: {fake_acc}{END}")
        time.sleep(1)

    print(f"\n{R}--- OPERATION TERMINATED BY ELALMY ---{END}")

if __name__ == "__main__":
    elalmy_long_search()
