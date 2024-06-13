import tkinter as tk
from PIL import Image, ImageTk
import mss

class MagnifierApp:
    def __init__(self, scaling_factor=3, window_size=300):
        self.scaling_factor = scaling_factor
        self.window_size = window_size

        # Set up the main window
        self.root = tk.Tk()
        self.root.title("Screen Magnifier")
        self.root.geometry(f"{window_size}x{window_size}+100+100")
        self.root.overrideredirect(False)  # Window decorations are shown

        self.label = tk.Label(self.root)
        self.label.pack(expand=True, fill=tk.BOTH)

        self.update_magnifier()
        self.root.mainloop()

    def update_magnifier(self):
        # Get the current position of the mouse
        x, y = self.root.winfo_pointerxy()

        # Adjust to get the region around the cursor
        left = x - self.window_size // (2 * self.scaling_factor)
        top = y - self.window_size // (2 * self.scaling_factor)
        width = self.window_size // self.scaling_factor
        height = self.window_size // self.scaling_factor

        # Define the area for the screenshot
        monitor = {"top": top, "left": left, "width": width, "height": height}

        # Capture the defined screen area using mss
        with mss.mss() as sct:
            sct_img = sct.grab(monitor)  # Capture screen using the defined monitor

            # Convert the MSS image to a PIL Image
            img = Image.frombytes('RGB', (sct_img.width, sct_img.height), sct_img.rgb)

        # Resize the image to magnify
        img = img.resize((self.window_size, self.window_size), Image.LANCZOS)

        # Convert to Tkinter format
        photo = ImageTk.PhotoImage(img)
        self.label.config(image=photo)
        self.label.image = photo  # Prevent garbage-collection

        # Update periodically
        self.root.after(100, self.update_magnifier)

if __name__ == "__main__":
    app = MagnifierApp(scaling_factor=3, window_size=300)
