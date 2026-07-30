from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "chapters/28_attention/CHAPTER.md"

text = CHAPTER.read_text(encoding="utf-8")

old_status = (
    "> **Stato della candidatura.** Il testo e il codice sono presentati per revisione. "
    "La figura `ATT-01` è una bozza con un difetto documentato; `ATT-02` è validata tecnicamente. "
    "Nessuna figura è ancora approvata dall'autore. Nessuna pagina del libro è stata rasterizzata."
)
new_status = (
    "> **Stato della candidatura.** Il testo e il codice sono presentati per revisione. "
    "Le figure `ATT-01/candidate-v2.png` e `ATT-02/candidate-v2.png` sono validate tecnicamente "
    "e attendono l'approvazione autoriale. Nessuna pagina del libro è stata rasterizzata."
)
if old_status in text:
    text = text.replace(old_status, new_status)

text = text.replace("candidate-v1.png", "candidate-v2.png")

head_pattern = re.compile(
    r"\$\$\s*\\operatorname\{head\}_i\s*=\s*"
    r"\\operatorname\{Attention\}\(QW_i\^Q, KW_i\^K, VW_i\^V\),\s*\$\$",
    flags=re.MULTILINE,
)
head_replacement = """$$
h_i =
\\mathrm{Attention}\\left(QW_i^Q, KW_i^K, VW_i^V\\right),
$$"""
text, head_count = head_pattern.subn(head_replacement, text)

multi_pattern = re.compile(
    r"\$\$\s*\\operatorname\{MultiHead\}\(Q,K,V\)\s*=\s*"
    r"\\operatorname\{Concat\}\(\\operatorname\{head\}_1,\\ldots,\\operatorname\{head\}_h\)W\^O\.\s*\$\$",
    flags=re.MULTILINE,
)
multi_replacement = """$$
\\mathrm{MHA}(Q,K,V)
=
\\left[h_1 \\mathbin{\\|} \\cdots \\mathbin{\\|} h_H\\right]W^O.
$$"""
text, multi_count = multi_pattern.subn(multi_replacement, text)

if "\\operatorname" in text:
    raise RuntimeError("Unsupported \\operatorname macro remains in CHAPTER.md")
if "candidate-v1.png" in text:
    raise RuntimeError("Obsolete visual candidate reference remains in CHAPTER.md")
if head_count != 1 or multi_count != 1:
    raise RuntimeError(("Unexpected formula replacement count", head_count, multi_count))

CHAPTER.write_text(text, encoding="utf-8")
print(f"Updated {CHAPTER}")
