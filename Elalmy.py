import time
import sys
import random

def elalmy_terminal_horror():
    # تأثير المصفوفة (Matrix Effect)
    chars = "0123456789ABCDEF@#$%"
    
    print("\033[91m") # لون أحمر للرعب
    print("!!! WARNING: ELALMY_DARK_CORE_ACTIVE !!!")
    print("!!! UNAUTHORIZED ACCESS DETECTED !!!")
    print("="*50 + "\033[0m")
    
    target = input(">> ENTER TARGET SYSTEM: ")
    
    print("\n\033[92m[*] INITIALIZING DEEP SCAN...\033[0m")
    
    # محاكاة البيانات المتدفقة بسرعة
    try:
        while True:
            # توليد بيانات عشوائية تبدو مثل "شفرات مخترقة"
            stream = "".join(random.choice(chars) for _ in range(60))
            print(f"\033[92m{stream}\033[0m")
            
            # كل فترة يظهر تحديث "مرعب"
            if random.random() > 0.9:
                print(f"\033[91m[!] BREACHING {target} - STATUS: ENCRYPTED DATA FOUND!\033[0m")
            
            time.sleep(0.08) # السرعة هنا تجعل المشهد يبدو حقيقياً
    except KeyboardInterrupt:
        print("\n\033[91m[!] SYSTEM SHUTDOWN. OPERATION LOGGED BY ELALMY.\033[0m")

if __name__ == "__main__":
    elalmy_terminal_horror()
