import argparse
from .core import process_audio, ask_question

def main():
    parser = argparse.ArgumentParser(description="Run diarization + transcript QA on a .wav file.")
    parser.add_argument('--audio', required=True, help='Path to the input .wav audio file')
    parser.add_argument('--openai-key', required=True, help='OpenAI API Key')
    parser.add_argument('--hf-token', required=True, help='Hugging Face API Token')
    parser.add_argument('--embedding-model', choices=['HuggingFace', 'OpenAI'], default='HuggingFace', help='Embedding model to use (default: HuggingFace)')
    
    args = parser.parse_args()

    print(f"\nProcessing audio: {args.audio}\nUsing embedding model: {args.embedding_model}")

    transcript, qa_chain = process_audio(args.audio, args.openai_key, args.hf_token, args.embedding_model)

    print("\nTranscript:\n" + "-" * 30)
    print(transcript)

    while True:
        try:
            question = input("\nAsk a question (or type 'exit'): ")
            if question.lower() == "exit":
                break
            answer = ask_question(qa_chain, question)
            print("Answer:", answer)
        except KeyboardInterrupt:
            break
