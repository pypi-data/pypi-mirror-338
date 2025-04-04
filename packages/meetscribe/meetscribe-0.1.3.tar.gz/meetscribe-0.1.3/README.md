# MeetScribe

**MeetScribe** is an intelligent AI-powered tool that converts spoken meeting audio into accurate, speaker-labeled transcripts and allows users to chat with those transcripts using powerful LLMs like GPT-4o.

Powered by OpenAI Whisper, PyAnnote for speaker diarization, and LangChain RAG pipelines.

---

## Features

- 🎙️ **Speaker Diarization** using [PyAnnote](https://github.com/pyannote/pyannote-audio)
- ✍️ **Transcription** using OpenAI's [Whisper](https://github.com/openai/whisper)
- 🧠 **Question Answering** using GPT-4o (or any OpenAI model)
- 🔍 **Customizable Embeddings** – Use HuggingFace or OpenAI Embeddings
- 📜 **Chat History** – Multi-turn conversation memory
- 🖥️ **Streamlit UI** – Easy-to-use local or web-based interface

---

## Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/jagadale1234/meetscribe.git
cd meetscribe
pip install -e .
```
## Requirements
- Hugging Face token (for PyAnnote)

- OpenAI API key (for embeddings + LLM)

## Usage (CLI)

```bash
meetscribe \
  --audio path/to/meeting.wav \
  --openai-key sk-xxx \
  --hf-token hf_yyy
```

## Usage (scripts and notebooks)
```python
from meetscribe import process_audio, ask_question

transcript, qa_chain = process_audio(
    wav_path="meeting.wav",
    openai_key="sk-xxx",
    hf_token="hf-yyy",
    embedding_model="OpenAI"
)

print(transcript)

answer = ask_question(qa_chain, "What was the deadline for the new design?")
print("Answer:", answer)
```


