# Python GUI Automation Utility

> A multithreaded desktop automation utility built with Python and Tkinter. Features customizable execution intervals, a responsive GUI, and PyAutoGUI failsafe interrupts.

## 🎥 Demo
*(Note: A GIF demonstration of the application in action will be added here shortly!)*

---

## ⚙️ Features
* **Concurrent Execution:** Utilizes Python's `threading` module to ensure the Tkinter GUI remains completely responsive during long automation loops.
* **Emergency Failsafe:** Integrates `pyautogui.FAILSAFE`, allowing the user to instantly kill the automation by throwing the mouse cursor to the top-left corner of the screen.
* **Input Validation:** Prevents crashes with a custom Tkinter validation engine that only accepts numerical inputs for repetition counts.
* **Fallback Logic:** Safely defaults to a 0.1-second interval if the user leaves the speed configuration blank.
* **Fixed Window Geometry:** A clean, non-resizable 600x270 interface to maintain consistent UX.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `tkinter` (UI), `pyautogui` (OS Automation), `threading` (Concurrency), `time` (Interval Management)

---

## 🚀 How to Run Locally

### Prerequisites
Make sure you have Python installed on your machine. You will also need to install the required external libraries.

### Installation & Execution
1. Clone the repository:
```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
```

2. Navigate into the project directory:
```bash
cd your-repo-name
```


3. Install the required dependencies:
```bash
pip install -r requirements.txt
```


4. Run the application:
```bash
python text_spam.py
```

---

## 👨‍💻 Author

**Chyrus Miguel Macalla**

* GitHub: [@Migelitoz](https://github.com/Migelitoz)
