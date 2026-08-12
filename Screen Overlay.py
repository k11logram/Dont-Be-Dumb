import tkinter as tk

class BreakReminder:
    def __init__(self, duration_seconds):
        self.root = tk.Tk()
        self.duration = duration_seconds
        
        # Configure the window to be full-screen
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        
        # Add a visible message and a way to exit safely
        self.label = tk.Label(
            self.root, 
            text=self.get_message(), 
            fg='white', 
            bg='black', 
            font=('Helvetica', 24)
        )
        self.label.pack(expand=True)
        
        # Start the countdown
        self.update_timer()
        
    def get_message(self):
        return f"Time for a break!\nRemaining: {self.duration} seconds\n\n(Press ESC to close safely)"

    def update_timer(self):
        if self.duration > 0:
            self.duration -= 1
            self.label.config(text=self.get_message())
            # Schedule the next second without blocking the application loop
            self.root.after(1000, self.update_timer)
        else:
            self.root.destroy()

# Example: A 10 second educational break overlay
if __name__ == "__main__":
    app = BreakReminder(10)
    
    # Allowing the user to override and close the window at any time using Escape
    app.root.bind('<Escape>', lambda e: app.root.destroy())
    
    app.root.mainloop()
