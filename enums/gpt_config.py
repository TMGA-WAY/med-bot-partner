from enum import Enum


class GptConfig(Enum):
    CREATIVE = "creative"
    BALANCED = "balanced"
    FOCUS = "focused"

    mode = {
        CREATIVE: {
            "temperature": 0.9,   # High randomness, more creative responses
            "top_p": 0.95,        # Higher chance of picking diverse words
            "frequency_penalty": 0.2,
            "presence_penalty": 0.6
        },
        BALANCED: {
            # Medium randomness, balanced creativity and accuracy
            "temperature": 0.7,
            "top_p": 0.9,
            "frequency_penalty": 0.1,
            "presence_penalty": 0.4
        },
        FOCUS: {
            # Low randomness, more focused and deterministic responses
            "temperature": 0.3,
            "top_p": 0.85,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.2
        }
    }
