import os
import shutil
import subprocess
import threading
import tkinter as tk
from tkinter import ttk

import sv_ttk

valorant_dir = r""
haloinfinite_dir = r""
minecraft_dir = r"%appdata%\.minecraft"
valorant_dir = r""


class MyApp:
    def __init__(self, parent, games):
        self.parent = parent
        self.games = games
        self.buttons = []

        parent.title("polar")

        parent.geometry("400x300")

        sv_ttk.set_theme("dark")

        max_width = max(len(label) for label in games)

        style = ttk.Style()
        style.configure(
            "RoundedButton.TButton",
            borderwidth=0,
            relief="flat",
            background="#0077cc",
            foreground="white",
            font=("Arial", 12, "bold"),
            padding=10,
            borderradius=10,
        )

        for game in self.games:
            self.button = ttk.Button(
                parent,
                text=game,
                width=max_width,
                command=lambda g=game: self.button_clicked(g),
                style="RoundedButton.TButton",
            )
            self.button.pack()
            self.buttons.append(self.button)

    def button_clicked(self, game):
        if game == "Halo Infinite":
            # ZETALOADER
            # Check if user already has scoop
            result = subprocess.run("scoop info", capture_output=True)
            if (
                result.returncode == 0
                and b"Usage: scoop info <app> [--verbose]" in result.stdout
            ):
                pass
            else:
                scoop_installed = False
                os.system(
                    'powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser" && powershell -Command "irm get.scoop.sh | iex"'
                )
            # Git Install
            os.system("scoop install git")
            # Nim Install
            os.system("scoop install nim")
            # Winim Install
            os.system("nimble install winim -y")
            # Clone ZetaLoader
            os.system("git clone https://github.com/Aetopia/ZetaLoader.git")
            # CD into dir
            os.system("cd ZetaLoader && build.bat")
            shutil.move(
                "ZetaLoader\dinput8.dll",
                r"C:\Program Files (x86)\Steam\steamapps\common\Halo Infinite",
            )
            if scoop_installed == False:
                os.system("scoop uninstall scoop -y")
            shutil.rmtree("ZetaLoader")
            # GAME SETTINGS


if __name__ == "__main__":
    games = ["VALORANT", "Halo Infinite", "Minecraft"]
    root = tk.Tk()
    app = MyApp(root, games)
    root.mainloop()
