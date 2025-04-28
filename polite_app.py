import subprocess
import tkinter as tk
from tkinter import ttk

# Colors and styling
BG_GRADIENT_LEFT = "#dbeafe"  # light blue
BG_GRADIENT_RIGHT = "#fce7f3"  # light pink
CARD_BG = "#ffffff"
ACCENT = "#111827"
FONT_LARGE = ("Helvetica", 18, "bold")
FONT_MEDIUM = ("Helvetica", 13)
FONT_LABEL = ("Helvetica", 11, "bold")


def make_polite(text):
    system_prompt = (
        "You are a text rewriting assistant. Your only job is to rephrase short blunt messages "
        "into calm, polite, and professional versions. Do not add new information. "
        "Do not reference anything that isn't mentioned. Return only a single rewritten version.\n\n"
        f"Original: {text}\nPolite:"
    )

    try:
        result = subprocess.run(
            ['ollama', 'run', 'llama3.2:3b'],
            input=system_prompt.encode(),
            capture_output=True,
            timeout=30
        )
        output = result.stdout.decode().strip()

        if "Polite:" in output:
            output = output.split("Polite:")[-1].strip()

        output = output.strip('"').strip("'")

        lines = output.splitlines()
        cleaned_lines = [
            line for line in lines
            if text.lower() in line.lower() or len(line) > 20
        ]
        cleaned_output = cleaned_lines[0] if cleaned_lines else output
        return cleaned_output.strip() if cleaned_output else "⚠️ No useful response."

    except Exception as e:
        return f"⚠️ Error: {e}"

def run_rephraser():
    rude_text = input_entry.get("1.0", "end").strip()
    if not rude_text:
        output_box.config(state="normal")
        output_box.delete("1.0", "end")
        output_box.insert("1.0", "⚠️ Please enter a sentence.")
        output_box.config(state="disabled")
        return
    polite = make_polite(rude_text)
    output_box.config(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("1.0", polite)
    output_box.config(state="disabled")

# GUI Setup
root = tk.Tk()
root.title("Polite Rephraser")
root.geometry("600x620")
root.configure(bg=BG_GRADIENT_LEFT)

# Create a gradient-like background by faking it
canvas = tk.Canvas(root, bg=BG_GRADIENT_LEFT, highlightthickness=0)
canvas.pack(fill="both", expand=True)

card = tk.Frame(canvas, bg=CARD_BG, bd=0, relief="flat")
card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=540)

# Title
tk.Label(card, text="Polite Rephraser", font=FONT_LARGE, fg=ACCENT, bg=CARD_BG).pack(pady=(20, 10))

# Blunt Sentence Label
tk.Label(card, text="Blunt Sentence", font=FONT_LABEL, fg=ACCENT, bg=CARD_BG).pack(anchor="w", padx=20)

input_entry = tk.Text(card, height=4, font=FONT_MEDIUM, bg="#f3f4f6", relief="flat", highlightthickness=1, wrap="word", bd=1)
input_entry.pack(fill="both", padx=20, pady=(2, 15), ipady=10)

# Button
style = ttk.Style()
style.configure("Custom.TButton", font=FONT_MEDIUM, padding=6)
ttkn = ttk.Button(card, text="Make It Polite", command=run_rephraser, style="Custom.TButton")
ttkn.pack(pady=(0, 15))

# Output Label
tk.Label(card, text="Polite Version", font=FONT_LABEL, fg=ACCENT, bg=CARD_BG).pack(anchor="w", padx=20)

output_box = tk.Text(card, height=4, font=FONT_MEDIUM, bg="#f3f4f6", relief="flat", highlightthickness=1, wrap="word", bd=1, state="disabled")
output_box.pack(fill="both", expand=True, padx=20, pady=(2, 15), ipady=10)

root.mainloop()