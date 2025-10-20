import os

base_config = {
    "WAKE_WORD": ["computer", "hey computer"],
    "TIMEOUT": 10,
    # longest amount of time the allow a phrase to continue before stopping the recording
    "PHRASE_TIME_LIMIT": 7,
    "USE_FASTER_WHISPER": False,
    "VISION_MODEL": "vlm",
    "LOCAL_MODEL": "gemma2:2b-instruct-q4_K_M",
    "RAG_MODEL": "gemma2:2b-instruct-q4_K_M",
    "STORE_CONVERSATIONS": True,  # to save in case we you want to analyze later
    "CONDENSE_MESSAGES": True,  # for faster response time
    # number of messages to keep in memory (odd #s work best)
    "TRAILING_MESSAGE_COUNT": 3,
    "SYSTEM_PROMPT": "You are Pi-Card, the Raspberry Pi AI assistant.",
}

config = {
    "SOUNDS_PATH": "/home/awes/pi-card/sounds/",
    "WHISPER_CPP_PATH": "/home/awes/whisper.cpp/build/bin/",
    "WHISPER_MODEL_PATH": "/home/awes/whisper.cpp/models/ggml-tiny.bin",
    "LLAMA_CPP_PATH": "../llama.cpp/",
    "VLM_MMPROJ_PATH": "../llama.cpp/mmproj-Qwen2-VL-2B-Instruct-f16.gguf",
    "VLM_MODEL_PATH": "../llama.cpp/Qwen2-VL-2B-Instruct-Q4_K_M.gguf",
}


docker_config = {
    "SOUNDS_PATH": "/app/src/sounds/",
    "WHISPER_CPP_PATH": "",
    "WHISPER_MODEL_PATH": "/app/whisper.cpp/models/ggml-tiny.bin",
    "LLAMA_CPP_PATH": "/app/llama.cpp/",
    "VLM_MMPROJ_PATH": "/app/llama.cpp/mmproj-Qwen2-VL-2B-Instruct-f16.gguf",
    "VLM_MODEL_PATH": "/app/llama.cpp/Qwen2-VL-2B-Instruct-Q4_K_M.gguf",
    # update the model names from docker-compose.yml
    "LOCAL_MODEL": os.getenv("OLLAMA_MODEL"),
    "RAG_MODEL": os.getenv("OLLAMA_MODEL"),
}

config.update(base_config)

docker_config.update(base_config)
