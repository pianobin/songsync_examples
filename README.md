# songsync_examples

Examples of songsync https://github.com/pianobin/songsync

Run the shell script and set `yt_playlist_id` and `spotify_playlist_name` to your YouTube playlist ID and what you'd like to name the Spotify playlist.

Example with shell script:

```
./songsync_cmd.sh --yt_playlist_id PLkZa6xWYS81W6wdF6HSpuqOuVCgu9mzjD --spotify_playlist_name "My Playlist"
```

For interactive mode, include the `--interactive` flag.

Example with interactive mode:

```
./songsync_cmd.sh --yt_playlist_id PLkZa6xWYS81W6wdF6HSpuqOuVCgu9mzjD --spotify_playlist_name "My Playlist" --interactive
```

In interactive mode, if the script cannot find the YouTube track on Spotify you will be prompted to manually enter a title and artist. Enter it as it would appear in your country. You can enter blank in the prompt to skip.
