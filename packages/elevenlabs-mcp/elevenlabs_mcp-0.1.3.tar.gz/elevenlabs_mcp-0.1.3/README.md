# Eleven Labs MCP Server

Official Eleven Labs Model Context Protocol (MCP) server that enables interaction with powerful text-to-speech and audio processing APIs. This server allows MCP clients like [Claude Desktop](https://www.anthropic.com/claude), [Cursor](https://www.cursor.so), [Windsurf](https://codeium.com/windsurf), [OpenAI Agents](https://github.com/openai/openai-agents-python) and others to generate speech, clone voices, transcribe audio, and more.

## Quick Start with Claude

1. Get your API key from [Eleven Labs](https://elevenlabs.io/). There is a generous free tier of 10k credits per month.
2. Install elevenlabs_mcp with `pip install elevenlabs_mcp` or `uv add elevenlabs_mcp`.
3. Install the MCP server by running `python -m elevenlabs_mcp --api-key={{PUT_YOUR_API_KEY_HERE}}`.
4. Restart Claude.

## Other MCP clients
For other clients like Cursor and Windsurf, run `python -m elevenlabs_mcp --api-key={{PUT_YOUR_API_KEY_HERE}} --print` to get the configuration. Paste it into appropriate configuration directory specified by your MCP client.


That's it! Your MCP client can now interact with Eleven Labs through these tools:

- `text_to_speech`: Convert text to speech using a specified voice
- `voice_clone`: Clone a voice using provided audio files
- `speech_to_text`: Transcribe speech from an audio file
- `text_to_sound_effects`: Generate sound effects from text descriptions
- `isolate_audio`: Isolate audio from a file
- `check_subscription`: Check your Eleven Labs subscription status
- `list_voices`: Get a list of all available voices
- `search_voices`: Search through your voice library for a specific voice
- `speech_to_speech`: Transform audio from one voice to another using provided audio files
- `text_to_voice`: Design a voice via a text prompt
- `create_voice_from_preview`: Using an ID from `text_to_voice`, save your generated to your library

## Example Usage

Try asking Claude:
- "Can you convert this text to speech using a British accent?"
- "What voices are available for text-to-speech?"
- "Can you transcribe this audio file for me?"
- "Generate some rain sound effects"

## Contributing

If you want to contribute or run from source:

1. Clone the repository:
```bash
git clone https://github.com/jacekduszenko/elevenlabs-mcp.git
cd elevenlabs-mcp
```

2. Create a virtual environment and install dependencies:
```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

3. Copy `.env.example` to `.env` and add your ElevenLabs API key:
```bash
cp .env.example .env
# Edit .env and add your API key
```

4. Install the mcp cli:
```bash
uv add "mcp[cli]"
```

6. Install the server in Claude Desktop: `mcp install server.py`.

7. Debug and test locally with MCP Inspector: `mcp dev server.py`

## Requirements

- Python 3.11 or higher
- Dependencies:
  - mcp>=0.1.0
  - fastapi==0.109.2
  - uvicorn==0.27.1
  - python-dotenv==1.0.1
  - pydantic>=2.6.1
  - httpx==0.28.1
  - elevenlabs>=1.56.0

## Troubleshooting

Logs when running with Claude Desktop can be found at:
- **Windows**: `%APPDATA%\Claude\logs\mcp-server-elevenlabs.log`
- **macOS**: `~/Library/Logs/Claude/mcp-server-elevenlabs.log`

### Timeouts when using certain tools

Certain ElevenLabs API operations like voice design and audio isolation can take a long time to resolve. When using the MCP inspector in dev mode you might get timeout errors, despite the tool completing its intended task.

This shouldn't occur when using a client like Claude.