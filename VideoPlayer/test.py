from library_item import LibraryItem

def test(capsys):
    video = LibraryItem("Tom and Jerry", "Fred Quimby", 4)

    assert video.name == "Tom and Jerry"
    assert video.director == "Fred Quimby"
    assert video.rating == 4

    assert video.stars()
    assert video.info() == "Tom and Jerry - Fred Quimby ****"

    with capsys.disabled():
        print()
        print(f"tested {video.__class__.__name__} successfully")

