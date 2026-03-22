import random
import nltk
from nltk.corpus import words, names, stopwords
from nltk.tag import pos_tag

# ----------------------------------------------------------------------
# Ensure required NLTK data is available
# ----------------------------------------------------------------------
for resource in ['punkt', 'averaged_perceptron_tagger_eng', 'words', 'names', 'stopwords']:
    try:
        nltk.data.find(f'tokenizers/{resource}' if resource == 'punkt' else resource)
    except LookupError:
        nltk.download(resource)

# ----------------------------------------------------------------------
# Build word lists by part of speech using POS tagging
# ----------------------------------------------------------------------
print("Building part-of-speech word lists (this may take a moment)...")
all_words = words.words()

# Tag first 50,000 words for speed (increase if you want more variety)
tagged = pos_tag(all_words[:50000])

nouns = set()
verbs = set()
adjectives = set()
adverbs = set()

for word, tag in tagged:
    w = word.lower()
    if tag.startswith('NN'):       # Noun
        nouns.add(w)
    elif tag.startswith('VB'):     # Verb
        verbs.add(w)
    elif tag.startswith('JJ'):     # Adjective
        adjectives.add(w)
    elif tag.startswith('RB'):     # Adverb
        adverbs.add(w)

# Remove common stopwords and names to avoid overly generic or personal terms
stop_words = set(stopwords.words('english'))
common_names = set(name.lower() for name in names.words())

nouns = [w for w in nouns if w not in stop_words and w not in common_names]
verbs = [w for w in verbs if w not in stop_words]
adjectives = [w for w in adjectives if w not in stop_words]
adverbs = [w for w in adverbs if w not in stop_words]

print(f"Loaded: {len(nouns)} nouns, {len(verbs)} verbs, {len(adjectives)} adjectives, {len(adverbs)} adverbs")

def random_noun():
    return random.choice(nouns)

def random_verb():
    return random.choice(verbs)

def random_adj():
    return random.choice(adjectives)

def random_adv():
    return random.choice(adverbs)

def maybe_plural(word):
    if random.random() > 0.3:
        if word.endswith('y'):
            return word[:-1] + 'ies'
        elif word.endswith(('s', 'x', 'ch', 'sh')):
            return word + 'es'
        else:
            return word + 's'
    return word

def maybe_connector():
    if random.random() < 0.6:
        return random.choice(["for", "to", "in", "with", "of", "on", "at", "near", "without", "like"])
    return ""

def random_question_starter():
    starters = [
        "what is", "what are", "what was", "what does",
        "who is", "who was", "who are",
        "how do", "how does", "how can", "how to",
        "why is", "why are", "why did", "why does",
        "where is", "where can", "where do",
        "when is", "when did", "when will",
        "which", "can i", "is it possible to"
    ]
    return random.choice(starters)

def generate_query():
    pattern = random.choice([
        "question", "how_to", "comparison", "product_review", "location",
        "info", "simple", "best_for", "where_to_buy", "difference", "who_question"
    ])

    if pattern == "question":
        starter = random_question_starter()
        topic = random_noun()
        return f"{starter} {topic}"

    elif pattern == "how_to":
        verb = random_verb()
        noun = random_noun()
        return f"how to {verb} {noun}"

    elif pattern == "who_question":
        template = random.choice([
            "who is the best {noun}",
            "who invented {noun}",
            "who created {noun}",
            "who wrote {noun}",
            "who discovered {noun}"
        ])
        noun = random_noun()
        return template.format(noun=noun)

    elif pattern == "comparison":
        a = random_noun()
        b = random_noun()
        return f"{a} vs {b}"

    elif pattern == "product_review":
        product = random_noun()
        return f"{product} reviews"

    elif pattern == "location":
        service = random_noun()
        place = random_noun()
        if random.random() > 0.5:
            return f"{service} near {place}"
        else:
            return f"{service} in {place}"

    elif pattern == "info":
        verb = random_verb()
        noun = maybe_plural(random_noun())
        connector = maybe_connector()
        if connector:
            return f"{verb} {noun} {connector} {random_noun()}"
        else:
            return f"{verb} {noun}"

    elif pattern == "simple":
        if random.random() > 0.5:
            word1 = random_adj()
        else:
            word1 = random_adv()
        word2 = random_noun()
        return f"{word1} {word2}"

    elif pattern == "best_for":
        noun = random_noun()
        purpose = random_noun()
        return f"best {noun} for {purpose}"

    elif pattern == "where_to_buy":
        item = random_noun()
        return f"where to buy {item}"

    elif pattern == "difference":
        a = random_noun()
        b = random_noun()
        return f"difference between {a} and {b}"

    return f"{random_adj()} {random_noun()}"

def generate_queries(n=100):
    return [generate_query() for _ in range(n)]

# ----------------------------------------------------------------------
# Interactive loop: generate one query per keypress
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("Random Search Query Generator")
    print("Press Enter to generate a new query, or 'q' to quit.\n")

    query_count = 0
    while True:
        key = input("Press Enter (or 'q' to quit): ").strip().lower()
        if key == 'q':
            print(f"Goodbye! Generated {query_count} queries.")
            break
        # any other key (including empty) generates a query
        query = generate_query()
        query_count += 1
        print(f"{query_count}. {query}\n")