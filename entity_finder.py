import spacy
from spacy import displacy
from collections import Counter
import pprint
import re
import en_core_web_sm


def find_fac_entities(text_corpus: str):
    response_dict = {}
    nlp = en_core_web_sm.load()
    text_corpus = re.sub('[^A-Za-z ]+', '', text_corpus)
    print(text_corpus)
    doc = nlp(text_corpus)
    for x in doc.ents:
        response_dict[x.text] = x.label_
    return response_dict


# def main():
#
#     resp_dict = find_fac_entities('Land Use Ordinance Lawrence Township, Mercer County §412 105 16.Beauty parlors/barber shops. 17.Child care center. [Ord. 2350-19, 12/17/19]. 18.Funeral home. C.Accessory Uses Permitted.  Any of the following uses may be permitted when used in conjunction with a principal use: 1.Playgrounds. 2.Conservation areas. 3.Parks and public purpose uses. 4.Tennis courts and other usual recreational facilities. 5.Commercial swimming pools for the use of residents. 6.Off street parking, including automobile sheds and grouped private parking. 7.Fences, walls, gazebos, mail kiosks and other street furniture Maintenance building Signs Home occupation Yorkshire Village.  [Ord. 1585-99, 9/7/1999]a.Private residential swimming pool. Private residential tool shed. Fences and walls. Deck/patio. 12.Accessory uses customarily incidental to a principal use.re :)')
#     print(resp_dict)
#
# if __name__ == '__main__':
#     main()
