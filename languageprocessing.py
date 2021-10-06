from nltk import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords


def remove_stopwords(text):
    '''
    Removing stopwords from string
    :param text: string from which stopwords have to be removed
    :returns string with stopwords removed
    '''
    stop_words = set(stopwords.words('english'))
    stop_words.add('please')
    tokens = word_tokenize(text)
    clean_tokens = [w for w in tokens if not w in stop_words]
    return ' '.join(clean_tokens)


def pos_tagger(nltk_tag):
    '''
    Part of Speech tagging for the string
    :param nltk_tag: pos tag given by WordNetLemmatizer
    :returns simpified pos tag from wordnet
    '''
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:          
        return None


def lemmatize(text):
    '''
    POS Tagged Lemmitization
    :param text: string that has to be lemmatized
    :returns string that is lemmatized
    '''
    lemmatizer = WordNetLemmatizer()
    pos_tagged = pos_tag(word_tokenize(text))
    wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged))
    
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            lemmatized_sentence.append(word)
        else:
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    
    return ' '.join(lemmatized_sentence)