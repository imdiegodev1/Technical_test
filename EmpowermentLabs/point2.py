import pandas as pd
import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords

#nltk.download('stopwords')


def main():
    df = the_function(5, 'bbc_news.csv')

    return df

def the_function(n_words = int, file_name = str):

    ##Read csv file
    df = pd.read_csv(f'./{file_name}')

    ##conatenate text from description field
    text = ' '.join(df.description)

    ##Use personalized tokenization function
    tm = _tokenization_freq(n_words, text)

    ##convert list of touples in a dataframe
    df_f = pd.DataFrame(tm, columns=['word', 'freq'])
    

    return df_f

def _tokenization_freq (n, text):

    ##special characters
    punctuations = '''+!()-[]{};:'"\,<>'./’?@#$%^&*_~1234567890“â€™Ã©º'''

    ##lower all words and split them in a list
    words = text.lower().strip(punctuations)

    ##Tokenization
    pattern = r'''(?x)                  # Flag para iniciar el modo verbose
              (?:[A-Z]\.)+            # Hace match con abreviaciones como U.S.A.
              | \w+(?:-\w+)*         # Hace match con palabras que pueden tener un guión interno
              | \$?\d+(?:\.\d+)?%?  # Hace match con dinero o porcentajes como $15.5 o 100%
              | \.\.\.              # Hace match con puntos suspensivos
              | [][.,;"'?():-_`]    # Hace match con signos de puntuación
    '''
    tokenization = list(nltk.regexp_tokenize(words,pattern))

    ##remove common words
    common_words = stopwords.words('english')
    
    clean_tokens = [x for x in tokenization if x not in common_words and len(x) > 2]

    ##Generate frequency chart
    fdist = FreqDist(clean_tokens)
    common_words = fdist.most_common(n)
    
    return common_words

if __name__ == '__main__':
    df = main()

    print(df)