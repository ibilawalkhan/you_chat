from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled


def get_transcript(video_id: str) -> str:
    try:
        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id, languages=["en"])

        return " ".join(snippet.text for snippet in transcript)

    except TranscriptsDisabled:
        raise RuntimeError(f"Transcripts are disabled for video {video_id}")
