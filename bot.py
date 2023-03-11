import pyrogram
from pyrogram import Client, filters
from shazamapi import Shazam

# Create a new Pyrogram client with your bot token
app = Client(
    "my_bot",
    bot_token="5566721946:AAE_rHjVUIFFIPStYdcLlBF1EIgdGsIj1hw"
)

# Define a command handler for the /song command
@app.on_message(filters.command("song"))
def send_song(client, message):
    # Get the song name from the user message
    song_name = message.text.split(" ", maxsplit=1)[1]
    
    # Search for the song using Shazam API
    shazam = Shazam()
    track = shazam.search(song_name)
    
    # Get the audio file of the song and send it to the user
    audio_file = client.send_audio(
        chat_id=message.chat.id,
        audio=track.url,
        title=track.title,
        performer=track.subtitle
    )

# Run the Pyrogram client
app.run()

