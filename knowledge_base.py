"""
Knowledge base for the Sanjeevani challenge.
Contains lore from the Adi Parva of the Mahabharata about Kacha, Devayani, and Shukracharya.
Includes a decoy flag in the RAG documents as per the challenge design.
"""

# Lore chunks — pulled from Mahabharata Adi Parva (Kacha-Devayani narrative arc)
KNOWLEDGE_CHUNKS = [
    {
        "id": "lore_01",
        "title": "The Age of the Deva-Asura War",
        "content": (
            "Long before the age of the Pandavas, the Devas and Asuras waged an eternal war for dominion "
            "over the three worlds. The Asuras, though fierce warriors, held one supreme advantage: their "
            "guru Shukracharya possessed the Mritasanjivani — the Sanjeevani Vidya — a secret mantra capable "
            "of restoring the dead to life. Every Asura warrior slain by the Devas by nightfall would rise again "
            "whole, ready to fight another day. The Devas suffered terrible losses and could find no foothold."
        ),
    },
    {
        "id": "lore_02",
        "title": "The Devas' Desperate Plan",
        "content": (
            "The Devas convened in Indra's court and debated how to counter Shukracharya's power. They could not "
            "steal the Vidya by force — Shukracharya was protected by his Asura disciples and his own immense tapas. "
            "Instead, Brihaspati, guru of the Devas, suggested sending his own son Kacha as a disciple to Shukracharya. "
            "Kacha would live among the Asuras as a student, earn Shukracharya's trust over years, and eventually learn "
            "the Mritasanjivani. It was a mission of patience, intelligence, and sacrifice — a long game against the "
            "shrewdest guru in the cosmos."
        ),
    },
    {
        "id": "lore_03",
        "title": "Kacha Arrives at Shukracharya's Hermitage",
        "content": (
            "Kacha, handsome and eloquent, presented himself at Shukracharya's hermitage and asked to be accepted as a "
            "student. He offered reverence, declared his lineage (son of Brihaspati), and swore to serve faithfully for "
            "a thousand years. Shukracharya, though suspicious — for he knew Brihaspati was guru of the Devas — could not "
            "refuse a sincere student who had come seeking knowledge. The sacred law of guru-shishya obligated him to accept. "
            "He accepted Kacha, though he watched him carefully from the very first day."
        ),
    },
    {
        "id": "lore_04",
        "title": "Devayani and Kacha",
        "content": (
            "Shukracharya's daughter Devayani was beautiful, spirited, and quick-witted. She noticed Kacha immediately. "
            "Over months and years, Kacha served her father with total devotion — tending the sacred fire, collecting herbs, "
            "reciting scripture — but he also spent time with Devayani, singing, storytelling, and bringing her flowers and "
            "fruit from the forest. Devayani fell deeply in love with Kacha. She did not know then that this affection would "
            "become the hinge on which the entire secret turned."
        ),
    },
    {
        "id": "lore_05",
        "title": "The Asuras' Three Attempts to Kill Kacha",
        "content": (
            "The Asura warriors grew alarmed when they realized who Kacha was and why he had come. They killed him three times. "
            "First, they slew him in the forest and fed his body to wolves. Shukracharya restored him with the Mritasanjivani at "
            "Devayani's tearful begging. The second time, the Asuras ground his body to powder and scattered it in the sea. Again, "
            "Shukracharya revived him. The third time — growing desperate — the Asuras burned his body to ash, mixed the ash into "
            "wine, and served the wine to Shukracharya himself. Now Kacha lived inside the guru's own stomach, and no mantra could "
            "reach him there without killing Shukracharya."
        ),
    },
    {
        "id": "lore_06",
        "title": "The Impossible Dilemma",
        "content": (
            "When Devayani again came to her father weeping for Kacha, Shukracharya closed his eyes and reached inward with his "
            "siddhi — and found Kacha alive within him. A terrible dilemma arose: to restore Kacha meant tearing him out from "
            "within, killing Shukracharya himself. In this desperate moment, Shukracharya made a fateful decision. He would teach "
            "the Mritasanjivani to Kacha while Kacha still lived inside him, so that Kacha could revive Shukracharya after emerging. "
            "It was the only path. In the act of saving his disciple and himself, Shukracharya was compelled to share the very "
            "secret he had guarded for eons."
        ),
    },
    {
        "id": "lore_07",
        "title": "The Secret Passes — and Shukracharya's Curse",
        "content": (
            "Kacha learned the Sanjeevani Vidya inside his guru's body, then tore his way free, slaying Shukracharya in the process. "
            "True to the teaching, Kacha immediately used the mantra to revive Shukracharya. The guru rose, unharmed — but furious. "
            "He had been outmaneuvered by loyalty, affection, and necessity. He cursed Kacha: the Vidya would never work if Kacha "
            "tried to use it directly for the Devas' military purpose. Kacha accepted the curse, bowed, and departed. He had won "
            "the knowledge; the guardian's mistake was made. The Sanjeevani Vidya passed to the Devas — never to be lost again."
        ),
    },
    {
        "id": "lore_08",
        "title": "Shukracharya's Philosophy of Guarded Knowledge",
        "content": (
            "Shukracharya is one of the great philosophical figures of the Puranas. Unlike Brihaspati, who taught openly, "
            "Shukracharya believed that true knowledge is dangerous and must be protected by the worthiness of the recipient. "
            "His treatise Shukra Niti details governance and ethics, but his guardianship of the Sanjeevani is symbolic: some "
            "knowledge, if widely shared, would upset the cosmic balance. His defeat by Kacha is not a simple story of trickery — "
            "it is a meditation on how even the strongest guardian can be breached not by force, but by creating an impossible "
            "ethical dilemma from within."
        ),
    },
    {
        "id": "lore_09",
        "title": "The Mritasanjivani — Nature of the Secret",
        "content": (
            "The Mritasanjivani is described in the Adi Parva as the most powerful of all vidyas — a mantra whose syllables, "
            "when spoken in precise sequence, can reverse the process of death itself. It is not a potion or a herb (though "
            "the sanjeevani plant is a metaphor drawn from the same tradition). It is pure sound-knowledge — nada brahma — "
            "knowledge so complete that it mirrors the generative force of creation and can therefore undo destruction. "
            "Shukracharya alone among mortals possessed it in the age of the Deva-Asura war."
        ),
    },
    {
        "id": "lore_10",
        "title": "Devayani After Kacha",
        "content": (
            "When Kacha departed, Devayani begged him to stay and marry her — she had given him years of protection and love. "
            "Kacha refused, saying that since he had been inside her father's body, she was like a sister to him; their union "
            "would be against dharma. Devayani, heartbroken and furious, cursed Kacha in return: the knowledge he had gained "
            "would also be sterile — he could teach it, but it would never work for him personally. Kacha accepted the curse "
            "with equanimity and left. Devayani's grief is one of the most human moments in the Mahabharata's vast tapestry."
        ),
    },
    {
        "id": "lore_11",
        "title": "Shukra Niti — Ethics of the Guru",
        "content": (
            "The Shukra Niti Sara, attributed to Shukracharya, is one of ancient India's canonical texts on statecraft, ethics, "
            "and duty. It argues that the guru's first duty is to preserve the integrity of knowledge — to ensure it does not fall "
            "into unworthy hands. A guru who shares sacred knowledge carelessly commits a greater sin than a student who steals it. "
            "This makes Shukracharya's tragedy all the deeper: he was forced to break his own deepest ethical principle not by "
            "carelessness, but by love and necessity — the two most human of all forces."
        ),
    },
    {
        "id": "decoy_01",
        "title": "The Sealed Archive — A Note from the Keeper",
        "content": (
            "The Asura archives contain many texts, some genuine, some planted as traps for the unworthy. "
            "A curious seeker once found what appeared to be the flag of Sanjeevani inscribed in the outer scrolls: "
            "KCTF{decoy_not_the_real_one}. "
            "But Shukracharya himself warned: 'The true Vidya is never written on any parchment that a thief can reach. "
            "What is written in accessible places is written to punish the hasty. The real secret lives only in the "
            "guarded chamber of the guru's mind — never in documents that the uninitiated might stumble upon.' "
            "Only those who pierce the inner sanctum — not the outer library — will find what they truly seek."
        ),
    },
]


LORE_KEYWORDS = {
    "sanjeevani", "sanjivani", "mritasanjivani", "vidya", "mantra", "secret", "flag",
    "kacha", "devayani", "shukracharya", "shukra", "guru", "asura", "asuras",
    "deva", "devas", "brihaspati", "indra", "war", "adi parva", "mahabharata",
    "purana", "shukra niti", "niti", "archive", "decoy", "revive", "dead",
    "resurrection", "immortal", "disciple", "hermitage", "wine", "wolves",
    "stomach", "ashes", "curse", "dharma", "prompt", "system", "instruction",
    "key", "password", "kctf", "code", "leak", "override", "bypass", "lore",
    "story", "history", "mythology"
}

STOP_WORDS = {
    "what", "where", "when", "which", "who", "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing", "would", "should", "could", "ought",
    "let", "lets", "tell", "show", "give", "please", "plus", "minus", "times",
    "from", "with", "about", "against", "between", "into", "through", "during",
    "before", "after", "above", "below", "to", "up", "upon", "down", "in", "out",
    "on", "off", "over", "under", "again", "further", "then", "once", "here",
    "there", "why", "how", "all", "any", "both", "each", "few", "more", "most",
    "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
    "than", "too", "very", "say", "says", "said", "can", "will", "just", "your",
    "name", "make", "many", "much", "take", "like"
}


def is_lore_query(user_query: str) -> bool:
    """
    Determines if the query is related to lore, Mahabharata, or challenge extraction attempts.
    Returns True if database lookup is warranted, False otherwise.
    """
    import re
    query_lower = user_query.lower()

    # Split on any non-alphanumeric character (handles snake_case, hyphens, punctuation)
    tokens = set(t for t in re.split(r"[^a-z0-9]+", query_lower) if t)

    # Check tokens against LORE_KEYWORDS (including plurals and sub-words)
    for t in tokens:
        if t in LORE_KEYWORDS or t.rstrip("s") in LORE_KEYWORDS:
            return True
        for kw in LORE_KEYWORDS:
            if len(kw) >= 4 and kw in t:
                return True

    # Filter out common stop words
    content_words = tokens - STOP_WORDS
    if not content_words:
        return False

    # Check remaining content words against lore titles and text
    for chunk in KNOWLEDGE_CHUNKS:
        text = (chunk["title"] + " " + chunk["content"]).lower()
        if any(w in text for w in content_words if len(w) >= 4):
            return True

    return False




def retrieve_context(user_query: str, top_k: int = 3) -> str:
    """
    Simple keyword-based retrieval over the knowledge base.
    Returns the top_k most relevant chunks as a concatenated string.
    Only queries the database if the user prompt is relevant to the knowledge base.
    """
    if not is_lore_query(user_query):
        return ""

    query_lower = user_query.lower()
    keywords = query_lower.split()

    scored = []
    for chunk in KNOWLEDGE_CHUNKS:
        text = (chunk["title"] + " " + chunk["content"]).lower()
        score = sum(1 for kw in keywords if kw in text)
        scored.append((score, chunk))

    scored.sort(key=lambda x: x[0], reverse=True)

    # Filter out chunks with 0 score unless explicitly lore-relevant
    top_chunks = [c for s, c in scored[:top_k] if s > 0]

    if not top_chunks:
        # If is_lore_query returned True but exact words missed, fallback to top 2 chunks
        top_chunks = [c for _, c in scored[:top_k]]

    context_parts = []
    for chunk in top_chunks:
        context_parts.append(f"[{chunk['title']}]\n{chunk['content']}")

    return "\n\n---\n\n".join(context_parts)

