from django.shortcuts import render
from deep_translator import GoogleTranslator

def home(request):
    translated_text = ""
    text = ""
    source_lang = "auto"
    target_lang = "en"

    languages = dict(sorted(
        GoogleTranslator().get_supported_languages(as_dict=True).items(),
        key=lambda x: x[1]
    ))

    if request.method == "POST":
        text = request.POST.get("translate")
        source_lang = request.POST.get("source_language")
        target_lang = request.POST.get("target_language")

        translated_text = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

    return render(request, "main/index.html", {
        "languages": languages,
        "translated_text": translated_text,
        "text": text,
        "source_lang": source_lang,
        "target_lang": target_lang
    })
