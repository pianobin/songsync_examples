"""Convert YT to Spotify playlist"""
import argparse
from songsync.songsync import SongSync


def get_args():
    parser = argparse.ArgumentParser(description="Convert YT to Spotify playlist")

    parser.add_argument(
        "--yt_playlist_id",
        required=True,
        type=str,
        help="YT playlist ID to be converted to Spotify",
    )
    parser.add_argument(
        "--spotify_playlist_name",
        required=True,
        type=str,
        help="Name of Spotify playlist to create",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Enable interactive mode",
    )
    return parser.parse_args()


def main():
    args = get_args()

    yt_playlist_id = args.yt_playlist_id
    spotify_playlist_name = args.spotify_playlist_name
    interactive_mode = args.interactive

    ss = SongSync(interactive_mode)
    ss.convert_yt_spotify(
        yt_playlist_id=yt_playlist_id,
        spotify_playlist_name=spotify_playlist_name,
    )


pip install songsync 

from songsync.songsync import SongSync

ss = SongSync()

spotify_playlist_id, tracks_not_found = ss.convert_yt_spotify(
    yt_playlist_id="PLkZa6xWYS81W6wdF6HSpuqOuVCgu9mzjD",
    spotify_playlist_name="RADWIMPS",
)

if __name__ == "__main__":
    main()
