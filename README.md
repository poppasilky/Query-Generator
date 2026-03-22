```markdown
# Random Search Query Generator

A Python tool that generates realistic, varied search queries using part-of-speech tagging. Each query mimics real user behavior—questions, comparisons, location‑based, product reviews, and more—by combining words from a large English corpus (via NLTK). Run it interactively: press **Enter** for a new query, `q` to quit.

## Features

- **Part‑of‑speech aware** – uses nouns, verbs, adjectives, adverbs to build grammatically correct phrases.
- **10+ query patterns** – questions (who/what/how/why/where/when/which), comparisons, “how‑to”, “where to buy”, product reviews, location‑based, and more.
- **Interactive** – generate one query per keypress.
- **Large vocabulary** – built from NLTK’s word corpus (tens of thousands of words, filtered for stopwords and proper names).
- **Portable** – works with Python 3.8+ and NLTK.

## Requirements

- Python 3.8 or newer
- NLTK (`pip install nltk`)

## Installation

1. **Clone the repository**  
   ```bash
   git clone git@github.com:poppasilky/Query-Generator.git
   cd Query-Generator
   ```

2. **Create and activate a virtual environment** (recommended)  
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install NLTK**  
   ```bash
   pip install nltk
   ```

4. **Run the script** – NLTK data will be downloaded automatically on first run.  
   ```bash
   python query_gen.py
   ```

## Usage

Once the script starts, you’ll see:

```
Random Search Query Generator
Press Enter to generate a new query, or 'q' to quit.
```

- **Press Enter** – a new random query is printed, along with a counter.
- **Type `q` and press Enter** – exit the program.

## Customization

- **Add more patterns** – edit the `patterns` list inside `generate_query()`.
- **Change word lists** – modify the POS‑tagged sets (`nouns`, `verbs`, `adjectives`, `adverbs`).
- **Increase word pool** – increase the slice size in `all_words[:50000]` to e.g. `all_words[:100000]` (will slow initial tagging but gives more variety).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [NLTK](https://www.nltk.org/) – for the natural language toolkit and corpora.
- MIT wordlist (indirectly) – part of the NLTK corpus.

---

*Happy generating!*
```
