import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not isinstance(text, str):
        raise TypeError
    if not text:
        return ""
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace("ё", "е")
        text = text.replace("Ё", "Е")

    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def tokenize(text: str) -> list[str]:
    if not isinstance(text, str):
        raise TypeError
    if not text:
        return []
    word_pattern = r"\w+(?:-\w+)*"
    return re.findall(word_pattern, text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    if not isinstance(tokens, list):
        raise TypeError
    for token in tokens:
        if not isinstance(token, str):
            raise TypeError
    freq_dict = {}
    for token in tokens:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1

    return freq_dict


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not isinstance(freq, dict):
        raise TypeError
    for key in freq:
        if not isinstance(key, str):
            raise TypeError
        if not isinstance(freq[key], int):
            raise TypeError
    sorted_dict = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return sorted_dict[:n]
