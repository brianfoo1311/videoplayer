import tkinter as tk
import tkinter.messagebox


import video_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class UpdateVideo():
    def __init__(self, window):
        window.geometry("350x200")
        window.title("Update videos")
        window.configure(bg='#6495ED')

        enter_lbl = tk.Label(window, text="Enter Video Number", bg='#6495ED')
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        update_btn = tk.Button(window, text="Update", command=self.update_clicked)
        update_btn.grid(row=0, column=4, padx=10, pady=10)

        enter_new_rating_lbl = tk.Label(window, text="Enter new rating", bg='#6495ED')
        enter_new_rating_lbl.grid(row=1, column=1, padx=10, pady=10)

        self.input_rating = tk.Entry(window, width=3)
        self.input_rating.grid(row=1, column=2, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), bg='#6495ED')
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

    def update_clicked(self):
        key = self.input_txt.get()
        rating = self.input_rating.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}\n"
            tkinter.messagebox.showinfo("Updated video", video_details)
        else:
            tkinter.messagebox.showerror("Error", f"Video {key} not found")
            self.status_lbl.configure(text="Update button was clicked!")


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    UpdateVideo(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
