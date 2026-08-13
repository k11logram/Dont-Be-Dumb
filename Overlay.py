# Screen Overlay for Quishing Project

import os
import sys
import webview


class Overlay:
    def __init__(self):
        self.html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quishing-demo.html")

    def run(self):
        if not os.path.exists(self.html_file):
            raise FileNotFoundError(f"HTML file not found: {self.html_file}")

        webview.create_window(
            title="Overlay",
            url=self.html_file,
            fullscreen=True,
            frameless=True,
            easy_quit=True,
            draggable=False,
            maximized=True,
            on_top=True,
            transparent=False,
        )
        webview.start()


if __name__ == "__main__":
    Overlay().run()

    