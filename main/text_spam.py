import tkinter as tk
import pyautogui
import time
import threading

# Enforce the global mouse failsafe
pyautogui.FAILSAFE = True 

def start_spamming(phrase_entry, amount_entry, status_label, speed_entry):
    phrase = phrase_entry.get()
    raw_amount = amount_entry.get()
    raw_speed = speed_entry.get() 
    
    if not raw_amount:
        return
        
    amount = int(raw_amount)
    speed = float(raw_speed) if raw_speed else 0.1

    status_label.config(text="Status: Starting in 5s... Prepare target!", fg="blue")
    time.sleep(5) 
    
    status_label.config(text="Status: Automating... (Slam mouse to top-left to STOP)", fg="red")

    try:
        for i in range(amount):
            pyautogui.typewrite(phrase)
            pyautogui.press("enter")
            time.sleep(speed)
            
        status_label.config(text="Status: Finished!", fg="green")
        
    except pyautogui.FailSafeException:
        status_label.config(text="Status: EMERGENCY STOPPED!", fg="darkred")

def main():
    root = tk.Tk()
    root.title("GUI Text Automation Utility")
    root.geometry("600x270")
    root.resizable(False, False)

    # Number validation engine
    def validate_numbers(P):
        if P == "" or P.isdigit():
            return True
        return False
    vcmd = (root.register(validate_numbers), '%P')

    # UI Widgets
    label_welcome = tk.Label(root, text="GUI Text Automation Utility", font=("Arial", 12, "bold"))
    label_welcome.grid(row=0, column=0, columnspan=2, pady=10)

    label_text = tk.Label(root, text="Enter the phrase to automate:")
    label_text.grid(row=1, column=0, padx=10, pady=5, sticky="e")

    get_text = tk.Entry(root, width=25)
    get_text.grid(row=1, column=1, padx=10, pady=5)

    label_amount = tk.Label(root, text="Repetition count:")
    label_amount.grid(row=2, column=0, padx=10, pady=5, sticky="e")

    get_amount = tk.Entry(root, width=25, validate="key", validatecommand=vcmd)
    get_amount.grid(row=2, column=1, padx=10, pady=5)

    label_speed = tk.Label(root, text="Interval in seconds (default 0.1s):")
    label_speed.grid(row=3, column=0, padx=10, pady=5, sticky="e")

    get_speed = tk.Entry(root, width=25)
    get_speed.grid(row=3, column=1, padx=10, pady=5)

    status_label = tk.Label(root, text="Status: Ready", font=("Arial", 10, "italic"))
    status_label.grid(row=4, column=0, columnspan=2, pady=5)

    start_btn = tk.Button(
        root, 
        text="Start", 
        width=25, 
        # Note the .start() appended at the very end!
        command=lambda: threading.Thread(
            target=start_spamming, 
            args=(get_text, get_amount, status_label, get_speed), 
            daemon=True
        ).start()
    )

    start_btn.grid(row=5, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()



