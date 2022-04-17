import tkinter as tk
import tkinter.scrolledtext as tkst


import video_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

def set_text2(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class CreateVideoList():
    def __init__(self, window):
        window.geometry("700x400")
        window.title("Create Video List")
        window.configure(bg='#6495ED')

        enter_lbl = tk.Label(window, text="Enter Video Number", bg='#6495ED')
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        add_to_playlist_btn = tk.Button(window, text="Add to Playlist", command=self.add_to_playlist_clicked)
        add_to_playlist_btn.grid(row=0, column=4, padx=10, pady=10)

        play_the_playlist_btn = tk.Button(window, text="Play the Playlist", command=self.play_playlist_clicked)
        play_the_playlist_btn.grid(row=1, column=4, padx=10, pady=10)

        reset_the_playlist_btn = tk.Button(window, text="Reset the Playlist", command=self.reset_the_playlist_clicked)
        reset_the_playlist_btn.grid(row=2, column=4, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        playing_lbl = tk.Label(window, text="Now Playing", bg='#6495ED')
        playing_lbl.place(x=15, y=320)

        self.list_txt2 = tk.Text(window, width=48, height=1, wrap="none")
        self.list_txt2.place(x=16, y=350)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), bg='#6495ED')
        self.status_lbl.place(x=15, y=290)

    def add_to_playlist_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            video_details = f"{name}\n"
            self.list_txt.insert(1.0, video_details)
        else:
            set_text(self.list_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Add to Playlist button was clicked!")

    def play_playlist_clicked(self):
        key = self.input_txt.get()
        count = lib.get_play_count(key)
        if count is not None:
            videoname = lib.get_name(key)
            play_count = lib.increment_play_count(key)
            video_details = f"{videoname}: {count}"
            set_text2(self.list_txt2, video_details)
        else:
            set_text(self.list_txt, f"Video {key} not found")
        self.status_lbl.configure(
            text="Play the Playlist button was clicked!")

    def reset_the_playlist_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            self.list_txt.delete("1.0", tk.END)
            self.list_txt2.delete("1.0", tk.END)
            lib.library["01"].play_count = 0
            lib.library["02"].play_count = 0
            lib.library["03"].play_count = 0
            lib.library["04"].play_count = 0
            lib.library["05"].play_count = 0
        else:
            self.status_lbl.configure(text="Reset button was clicked")



if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CreateVideoList(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
