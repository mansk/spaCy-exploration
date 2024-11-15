import spacy
import tarfile

nlp = spacy.load("en_core_web_sm")


def content_gen(tar_data):
    for member in tar_data.getmembers():
        if member.isfile() and member.name.endswith(".txt"):
            file = tar_data.extractfile(member).read()
            text = file.decode("utf_8")

            yield text


with tarfile.open("data.tar.gz", mode="r:gz") as tar_data:
    docs_gen = nlp.pipe(content_gen(tar_data), batch_size=1000)
