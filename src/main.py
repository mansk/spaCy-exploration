import spacy
import tarfile

nlp = spacy.load("en_core_web_sm")


def content_gen(tar_data):
    for member in tar_data.getmembers():
        if member.isfile() and member.name.endswith(".txt"):
            file = tar_data.extractfile(member).read()
            text = file.decode("utf_8")
            filename = member.name.split("/")[-1]
            president, speech_number = filename.rstrip(".txt").split("_speeches_")

            yield (text, {"president": president, "speech_number": int(speech_number)})


with tarfile.open("data.tar.gz", mode="r:gz") as tar_data:
    docs_gen = nlp.pipe(content_gen(tar_data), as_tuples=True)

    for doc, context in docs_gen:
        print(f"President: {context["president"]}, Speech: {context["speech_number"]}")
