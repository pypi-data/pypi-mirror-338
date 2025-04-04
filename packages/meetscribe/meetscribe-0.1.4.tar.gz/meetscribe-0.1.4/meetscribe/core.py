import os
import torch
import whisper
import torchaudio
import faiss
import threading
import logging

from pyannote.audio import Pipeline as PyannotePipeline
from pyannote.audio.pipelines.utils.hook import ProgressHook

from llama_index.core.node_parser import SentenceSplitter
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import Document as LangDoc

# === Logging ===
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def process_audio(wav_path, openai_key, hf_token, embedding_model="HuggingFace"):
    """
    Process an audio file and return a transcript and a LangChain QA chain.

    Parameters:
        wav_path (str): Path to the .wav audio file.
        openai_key (str): OpenAI API key for LLM usage.
        hf_token (str): HuggingFace token for loading PyAnnote and optional embeddings.
        embedding_model (str): 'HuggingFace' or 'OpenAI'. Controls which embedding model to use.

    Returns:
        transcript_text (str): Diarized transcript.
        qa_chain (ConversationalRetrievalChain): LangChain QA pipeline.
    """
    os.environ["OPENAI_API_KEY"] = openai_key

    whisper_result = {}
    diarization_result = {}

    logger.info("Starting transcription and diarization threads.")

    def transcribe():
        logger.info("Loading Whisper model...")
        model = whisper.load_model("large")
        whisper_result["data"] = model.transcribe(wav_path, verbose=False)
        logger.info("Transcription complete.")
        del model
        torch.cuda.empty_cache()

    def diarize():
        logger.info("Loading PyAnnote diarization model...")
        pipeline = PyannotePipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1", use_auth_token=hf_token
        )
        pipeline.to(torch.device("cuda:0" if torch.cuda.is_available() else "cpu"))
        waveform, sample_rate = torchaudio.load(wav_path)
        with ProgressHook():
            diarization_result["data"] = pipeline({
                "waveform": waveform, "sample_rate": sample_rate
            })
        logger.info("Diarization complete.")
        del pipeline
        torch.cuda.empty_cache()

    t1 = threading.Thread(target=transcribe)
    t2 = threading.Thread(target=diarize)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    whisper_segments = whisper_result["data"].get("segments", [])
    diarization = diarization_result["data"]

    transcript = []
    for seg in whisper_segments:
        speaker = "UNKNOWN"
        for turn, _, spk in diarization.itertracks(yield_label=True):
            if turn.start <= seg["start"] <= turn.end:
                speaker = spk
                break
        transcript.append(f"{speaker}: {seg['text'].strip()}")

    transcript_text = "\n".join(transcript)
    if not transcript_text.strip():
        raise ValueError("Transcript is empty")

    logger.info("Transcript generated. Creating vector store.")

    splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=100)
    chunks = splitter.split_text(transcript_text)
    metadata = [{"chunk_id": i} for i in range(len(chunks))]
    lang_docs = [LangDoc(page_content=chunk, metadata=meta) for chunk, meta in zip(chunks, metadata)]

    if embedding_model == "HuggingFace":
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            cache_folder=os.path.expanduser("~/.cache/huggingface"),
            model_kwargs={"use_auth_token": hf_token}
        )
        logger.info("Using HuggingFace embeddings.")
    else:
        embeddings = OpenAIEmbeddings()
        logger.info("Using OpenAI embeddings.")

    faiss_store = FAISS.from_documents(lang_docs, embeddings)

    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=faiss_store.as_retriever(search_kwargs={"k": 5}),
        memory=memory,
        return_source_documents=False
    )

    logger.info("QA chain ready.")
    return transcript_text, qa_chain


def ask_question(qa_chain, question):
    """
    Ask a question using the provided QA chain.

    Parameters:
        qa_chain (ConversationalRetrievalChain): The QA chain returned from process_audio.
        question (str): The question to ask.

    Returns:
        str: The answer from the language model.
    """
    if not question.strip():
        raise ValueError("Question is empty")
    logger.info(f"Asking: {question}")
    return qa_chain.run(question)
