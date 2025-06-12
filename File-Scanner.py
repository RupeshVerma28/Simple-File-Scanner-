import customtkinter as ctk
from tkinter import filedialog, messagebox
from reportlab.pdfgen import canvas
import os
import mimetypes
import hashlib

# Configure appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Simple File Scanner Tool")
app.geometry("600x550")

file_path = ""
scan_result = {}

# Utility functions
def get_file_info(path):
    file_stat = os.stat(path)
    file_type, _ = mimetypes.guess_type(path)
    file_type = file_type or "Unknown"
    file_size = file_stat.st_size
    file_ext = os.path.splitext(path)[-1].lower()
    is_exe = file_ext in ['.exe', '.bat', '.sh', '.js', '.jar', '.vbs', '.ps1']

    # Hashing
    with open(path, 'rb') as f:
        content = f.read()
        file_hash = hashlib.sha256(content).hexdigest()

    suspicious_keywords = [b"eval", b"os.system", b"subprocess", b"powershell"]
    found_keywords = [kw.decode() for kw in suspicious_keywords if kw in content]

    return {
        "File Name": os.path.basename(path),
        "File Type": file_type,
        "Extension": file_ext,
        "Size (bytes)": file_size,
        "Executable": "Yes" if is_exe else "No",
        "SHA-256": file_hash,
        "Suspicious Code": ", ".join(found_keywords) if found_keywords else "None",
        "Safe": "No" if is_exe or found_keywords else "Yes"
    }

# GUI Functions
def browse_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        path_label.configure(text=f"Selected: {os.path.basename(file_path)}")

def scan_file():
    global scan_result
    if not file_path:
        messagebox.showerror("Error", "Please select a file first.")
        return
    scan_result = get_file_info(file_path)
    result_box.configure(state="normal")
    result_box.delete("1.0", ctk.END)
    for k, v in scan_result.items():
        result_box.insert(ctk.END, f"{k}: {v}\n")
    result_box.configure(state="disabled")

def download_report():
    if not scan_result:
        messagebox.showerror("Error", "No report to download.")
        return
    c = canvas.Canvas("file_scan_report.pdf")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "🛡️ File Scan Report")
    c.setFont("Helvetica", 12)
    y = 760
    for k, v in scan_result.items():
        c.drawString(80, y, f"{k}: {v}")
        y -= 25
    c.save()
    messagebox.showinfo("Success", "Report downloaded as file_scan_report.pdf")

# GUI Layout
ctk.CTkLabel(app, text="🔍 Simple File Scanner", font=("Arial", 20, "bold")).pack(pady=20)

ctk.CTkButton(app, text="Select File", command=browse_file).pack(pady=10)
path_label = ctk.CTkLabel(app, text="No file selected", wraplength=500)
path_label.pack()

ctk.CTkButton(app, text="Scan File", command=scan_file).pack(pady=10)

result_box = ctk.CTkTextbox(app, height=200, width=500)
result_box.pack(pady=10)
result_box.configure(state="disabled")

ctk.CTkButton(app, text="Download Report", command=download_report).pack(pady=10)

app.mainloop()
