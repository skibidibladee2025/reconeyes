import tkinter as tk
from tkinter import messagebox
import threading
import webbrowser
import time
from srv import app, scrape_all_cams, FLASK_HOST, FLASK_PORT

class OpenEyesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OpenEyes - IP Camera Map")
        self.root.geometry("400x300")

        self.server_thread = None
        self.scraping_thread = None

        # Status label
        self.status_label = tk.Label(root, text="Status: Ready", font=("Arial", 12))
        self.status_label.pack(pady=10)

        # Start Server Button
        self.start_server_btn = tk.Button(root, text="Start Server", command=self.start_server, font=("Arial", 12))
        self.start_server_btn.pack(pady=10)

        # Scrape Cameras Button
        self.scrape_btn = tk.Button(root, text="Scrape Cameras", command=self.scrape_cameras, state=tk.DISABLED, font=("Arial", 12))
        self.scrape_btn.pack(pady=10)

        # Open Map Button
        self.open_map_btn = tk.Button(root, text="Open Map in Browser", command=self.open_map, state=tk.DISABLED, font=("Arial", 12))
        self.open_map_btn.pack(pady=10)

        # Progress label
        self.progress_label = tk.Label(root, text="", font=("Arial", 10))
        self.progress_label.pack(pady=10)

    def start_server(self):
        if self.server_thread and self.server_thread.is_alive():
            messagebox.showinfo("Info", "Server is already running.")
            return

        self.status_label.config(text="Status: Starting server...")
        self.server_thread = threading.Thread(target=self.run_server, daemon=True)
        self.server_thread.start()
        self.start_server_btn.config(state=tk.DISABLED)
        self.scrape_btn.config(state=tk.NORMAL)
        self.open_map_btn.config(state=tk.NORMAL)
        self.status_label.config(text="Status: Server running on http://{}:{}".format(FLASK_HOST, FLASK_PORT))

    def run_server(self):
        try:
            app.run(host=FLASK_HOST, port=FLASK_PORT, debug=False, threaded=True, use_reloader=False)
        except Exception as e:
            self.status_label.config(text="Status: Server error - " + str(e))

    def scrape_cameras(self):
        if self.scraping_thread and self.scraping_thread.is_alive():
            messagebox.showinfo("Info", "Scraping is already in progress.")
            return

        self.status_label.config(text="Status: Scraping cameras...")
        self.progress_label.config(text="This may take several minutes...")
        self.scraping_thread = threading.Thread(target=self.perform_scrape, daemon=True)
        self.scraping_thread.start()

    def perform_scrape(self):
        try:
            scrape_all_cams()
            self.status_label.config(text="Status: Scraping completed!")
            self.progress_label.config(text="")
            messagebox.showinfo("Success", "Camera scraping completed!")
        except Exception as e:
            self.status_label.config(text="Status: Scraping error - " + str(e))
            self.progress_label.config(text="")
            messagebox.showerror("Error", "Scraping failed: " + str(e))

    def open_map(self):
        url = "http://{}:{}".format(FLASK_HOST, FLASK_PORT)
        webbrowser.open(url)
        self.status_label.config(text="Status: Map opened in browser")

if __name__ == "__main__":
    root = tk.Tk()
    gui = OpenEyesGUI(root)
    root.mainloop()