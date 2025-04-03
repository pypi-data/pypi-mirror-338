"""
lrc.py
Generates lrc files for songs using OpenAI's Whisper model.

Credits:
https://github.com/openai/whisper
https://openai.com/index/whisper/
Thanks the for inspiration:
https://www.lrcgenerator.com/
https://github.com/openai/whisper
"""

from dataclasses import dataclass
from pathlib import Path

import whisper
from rich.console import Console

console = Console()


@dataclass
class RetrievedMusicFiles:
    """
    Data class to store information about retrieved music files.

    Attributes:
        all_files (list[Path]): A list of all music file paths found.
        with_lrc (list[Path]): A list of music file paths that already have corresponding LRC files.
        without_lrc (list[Path]): A list of music file paths that do not have corresponding LRC files.
    """

    all_files: list[Path]
    with_lrc: list[Path]
    without_lrc: list[Path]


def seconds_to_lrc_timestamp(seconds: float) -> str:
    """
    Converts seconds to a valid lrc timestamp.
    The format is `mm:ss:ms`.

    Args:
        seconds (float): The number of seconds.

    Examples:
        >>> seconds_to_lrc_timestamp(84)
        01:24.00
        >>> seconds_to_lrc_timestamp(583.78)
        09:43.78
        >>> seconds_to_lrc_timestamp(84.123)
        01:24.12
    """
    minutes, seconds = divmod(seconds, 60)
    milliseconds = int(round((seconds - int(seconds)) * 100))
    return f"{int(minutes):02}:{int(seconds):02}.{milliseconds:02}"


def generate_lrc(audio_path: str, model: whisper.Whisper) -> str:
    """
    Converts audio to `lrc` format.

    Args:
        audio_path (str): The path of the audio file.
        model (whisper.Whisper): The openai whisper model to be used to process the audio to text.
    """
    result = model.transcribe(audio_path)

    segments = result.get("segments")

    if not isinstance(segments, list):
        raise TypeError(
            "Expected result to have segments,"
            "try using a different model or use a different version of whisper"
        )

    lrc_result: list[str] = []

    for segment in segments:
        lrc_timestamp: str = seconds_to_lrc_timestamp(segment["start"])
        text: str = segment["text"]
        text = text.strip()

        lrc_result.append(f"[{lrc_timestamp}]{text}")

    return "\n".join(lrc_result)


def get_music_files(music_path: Path) -> RetrievedMusicFiles:
    """
    Returns a list of valid music file paths found within a directory and its subdirectories.

    Args:
        music_path (pathlib.Path): The file path of the directory to search.

    Returns:
        List of Path objects that contain file paths of valid music files.
    """
    valid_files: list[Path] = []
    valid_audio_extensions: list[str] = [".mp3", ".wav", ".flac"]

    retrieved_music_files = RetrievedMusicFiles([], [], [])

    for root, _, files in music_path.walk():
        for file in files:
            path = Path(file)

            extension: str = path.suffix

            if extension in valid_audio_extensions:
                full_path: Path = root / file

                retrieved_music_files.all_files.append(full_path)

                if full_path.with_suffix(".lrc").exists():
                    retrieved_music_files.with_lrc.append(full_path)
                else:
                    retrieved_music_files.without_lrc.append(full_path)

                valid_files.append(full_path)

    return retrieved_music_files


def generate_lrc_at_song(song_path: str | Path, model: whisper.Whisper) -> None:
    """Generates a lrc file at the location of the provided song location.

    Args:
        song_path (str | pathlib.Path): The path/location where the song file is located.
        model (whisper.Whisper): Whisper model to use to generate the lyrics for the lrc file.q

    Raises:
        FileNotFoundError: If the song path doesn't exist.
        FileExistsError: If an LRC file already exits for the song.
    """
    song_path = Path(song_path)

    if not song_path.exists():
        raise FileNotFoundError(f"No file called '{song_path}' exists.")

    song_dir: Path = song_path.parent
    lrc_path: Path = song_path.with_suffix(".lrc")

    if lrc_path.exists():
        raise FileExistsError(f"lrc file for '{song_dir}' already exists.")

    lrc_data: str = generate_lrc(str(song_path), model)

    lrc_path.write_text(lrc_data, encoding="utf-8")


def generate_lrc_for_album(album_path: str | Path, model: whisper.Whisper) -> None:
    """
    Generates `lrc` files for each song in a album. (The lrc files go into the album folder)
    The `lrc` file is the same name as the songs file name with its extension replaced with `lrc`.

    Args:
        album_path (str): The file path of the album.
        model (whisper.Whisper): The openai whisper model to be used to process the audio to text.

    Raises:
        FileNotFoundError: If the path to the album doesn't exist.
    """
    album_path = Path(album_path)

    if not album_path.exists():
        raise FileNotFoundError(f"No file called '{album_path}' exists.")

    status_message = "[bold green]Generating lrc files {}/{} ..."

    music_file_paths: RetrievedMusicFiles = get_music_files(album_path)
    total_files: int = len(music_file_paths.all_files)

    console.log(
        f"Found {total_files} songs!"
        f" {len(music_file_paths.without_lrc)} songs dont have an LRC file."
        f" {len(music_file_paths.with_lrc)} do have an LRC file, skipping them."
    )

    with console.status(status_message.format(0, total_files)) as status:
        for file_num, song_path in enumerate(music_file_paths.without_lrc, 1):
            song_name: str = song_path.stem

            console.log(f"Processing song: [blue]{song_name}")
            try:
                generate_lrc_at_song(song_path, model)
            except FileExistsError:
                console.log(
                    f"[bold yellow]Skipping song: [blue]{song_name}[bold yellow],"
                    "cause a lrc file already exists."
                )

            status.update(status_message.format(file_num, total_files))
