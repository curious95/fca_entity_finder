import spacy
nlp = spacy.load('model/')

doc = nlp('Who is Nishanth?')
# Print entity labels and text
print("\n-------------------------------------------\nEntities found after training:")
for ent in doc.ents:
    if ent.label_=='MAN':
        print(ent.label_, ent.text)