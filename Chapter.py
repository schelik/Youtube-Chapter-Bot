from tracemalloc import start


class Chapter:
    title = ""
    description = ""
    video_file_name = ""
    thumnail_image_file_name = ""
    thumbnail_file_name = ""
    start_time = 0

    def __init__(self) -> None:
        pass

    def __init__(self, title, video_file_name, start_time, thumbnail_file_name) -> None:
        self.title = title
        self.video_file_name = video_file_name
        self.start_time = start_time
        self.thumbnail_file_name = thumbnail_file_name
