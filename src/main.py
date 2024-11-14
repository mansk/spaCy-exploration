import spacy
import tarfile

nlp = spacy.load("en_core_web_sm")

with tarfile.open("data.tar.gz", mode="r:gz") as tar_data:
    for member in tar_data.getmembers():
        if member.isfile() and member.name.endswith(".txt"):
            file = tar_data.extractfile(member).read()
            doc = nlp(file.decode("utf_8"))

            print(f"{sum(1 for _ in doc.sents)} sentences found in {member.name}")
