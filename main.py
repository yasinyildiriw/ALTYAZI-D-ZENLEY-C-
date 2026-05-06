fix_map = {
    "Þ": "Ş",
    "þ": "ş",
    "Ý": "İ",
    "ý": "ı",
    "Ð": "Ğ",
    "ð": "ğ"
}

with open("duzenlenecek_srt.txt", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

for wrong, correct in fix_map.items():
    text = text.replace(wrong, correct)

with open("duzeltilmis_srt.txt", "w", encoding="utf-8") as f:
    f.write(text)
