fix_map = {
    "Þ": "S",
    "þ": "s",
    "Ý": "i",
    "ý": "ı",
    "Ð": "g",
    "ð": "g"
}

with open("duzenlenecek_srt.txt", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

for wrong, correct in fix_map.items():
    text = text.replace(wrong, correct)

with open("duzeltilmis_srt.txt", "w", encoding="utf-8") as f:
    f.write(text)