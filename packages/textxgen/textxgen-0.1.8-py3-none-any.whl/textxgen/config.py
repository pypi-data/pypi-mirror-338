# textxgen/config.py


class Config:
    """
    Configuration class for TextxGen package.
    Stores API key, endpoints, and other configurations.
    """

    # Predefined API key for OpenRouter
    API_KEY = (
        "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"
    )

    # Base URL for OpenRouter API
    BASE_URL = "https://openrouter.ai/api/v1"

    # Supported models (actual model IDs)
    SUPPORTED_MODELS = {
        "llama3": "meta-llama/llama-3.1-8b-instruct:free",
        "phi3": "microsoft/phi-3-mini-128k-instruct:free",
        "deepseek": "deepseek/deepseek-chat:free",
        "qwen": "qwen/qwen2.5-vl-3b-instruct:free",
        "deepseek_v3": "deepseek/deepseek-chat-v3-0324:free",
        "gemma3_4b": "google/gemma-3-4b-it:free",
        "gemma3_1b": "google/gemma-3-1b-it:free",
    }

    # Default model
    DEFAULT_MODEL = SUPPORTED_MODELS["llama3"]

    # Headers for API requests
    HEADERS = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    @staticmethod
    def get_model_display_names() -> dict:
        """
        Returns a dictionary of model display names (without the `:free` suffix).

        Returns:
            dict: Model display names mapped to their keys.
        """
        return {
            "llama3": "LLaMA 3 (8B Instruct)",
            "phi3": "Phi-3 Mini (128K Instruct)",
            "deepseek": "DeepSeek Chat",
            "qwen": "Qwen 2.5 (3B Parameters)",
            "deepseek_v3": "Deepseek Chat V3",
            "gemma3_4b": "Google Gemma 3 (4B Parameters)",
            "gemma3_1b": "Google Gemma 3 (1B Parameters)",
        }
