import MySQLdb
import seaborn as sns
import pandas as pd
import numpy as np
from collections import Counter

def dbConnect():
    """
    connect to MySQL database called p3

    Parameters
    ----------
    None

    Return
    ------
    connection object from MySQLdb.connect()

    """
    dsn_database = 'p3'
    dsn_uid = 'root'
    dsn_pwd = ''
    conn = MySQLdb.connect(user=dsn_uid, passwd=dsn_pwd, db=dsn_database)
    return conn

def dbTableToDataFrame(conn, table):
    """
    convert table from p3 database into a dataframe

    Parameters
    ----------
    1. connection object
    2. table name to select from in database p3

    Return
    ------
    dataframe with contents from table name passed
    
    """
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ' + table)
    result = []
    columns = tuple([item[0] for item in cursor.description])
    for row in cursor:
        result.append(dict(zip(columns, row)))
    result_df = pd.DataFrame(result)
    return result_df

class SchoolTools:
    def __init__(self):
        pass

    def remove_stopwords(self,institutions):
        '''
        Remove stopwords from a series of strings.

        Parameters
        ----------
        institutions : Series
            A series of institution names, not identified.
        '''
        stopwords = ['of','the','at','in','i','y','and','de','@']
        for word in stopwords:
            institutions = institutions.str.replace(' '+word+' ',' ')
            institutions = institutions.str.replace('\A'+word+' ','')
        return institutions
    
    def remove_punctuation(self,institutions):
        '''
        Remove punctuation from a series of strings.

        Parameters
        ----------
        institutions : Series
            A series of institution names, not identified.
        '''
        stoppunc = [',','\.',';',':','-','&','(',')','/']
        for punc in stoppunc:
            institutions = institutions.str.replace(punc,' ')
        return institutions.str.strip()
        

    def identify_schools(self,institutions):
        '''
        Process a series of school names to give more unique identifiers.

        Replace common stems with just the stem, delete other stems completely,
        and replace keywords and nicknames with common titles.

        Parameters
        ----------
        institutions : Series
            A series of institution names, not identified.
        '''
        institutions = institutions.str.split()
        for i in range(len(institutions)):
            institutions[i] = self._delete_stems(institutions[i])
            institutions[i] = self._reduce_to_stems(institutions[i])
            institutions[i] = self._replace_by_keyword(institutions[i])
            institutions[i] = self._replace_by_nickname(institutions[i])
        return institutions.str.join(' ')

    def _delete_stems(self,institution):
        '''Delete some common superfluous words in institution names.'''
        del_stems = ['univ','school','law','business']
        del_word_inds = []
        for word_i in range(len(institution)):
            for del_stem in del_stems:
                if institution[word_i][:len(del_stem)] == del_stem:
                    del_word_inds.append(word_i)
        for word_i in del_word_inds[::-1]:
            del(institution[word_i])
        return institution

    def _reduce_to_stems(self,institution):
        '''Replace words with their stem to increase names in common.'''
        stems = ['poly','tec','cal','inst','agri','coll']
        for word_i in range(len(institution)):
                for stem in stems:
                    if institution[word_i][:len(stem)]==stem:
                        institution[word_i]=stem
        return institution

    def _replace_by_keyword(self,institution):
        '''Identify a school by matching a keyword.'''
        keywords=['wharton','yale','harvard','mit','henley','berkeley','gurion',
                  'duke','babson','bentley','canberra','boulder','stanford',
                  'northwestern','usc','ucla','nyu','bowling green',
                  'baldwin wallace','boston coll','cal culinary',
                  'virginia commonwealth','virginia poly','stony brook',
                  'georgia tec','coll park']
        for name in keywords:
            match_counter = 0
            names = name.split()
            for word in names:
                if word in institution:
                    match_counter += 1
                if match_counter == len(names):
                    institution = names
        return institution

    def _replace_by_nickname(self,institution):
        '''Identify a school when its nickname is given.'''
        nicknames={'cal':'berkeley','pennsylvania':'penn','wharton':'penn',
                   'virginia poly':'virginia tec','chicago booth':'chicago',
                   'massachusetts inst tec':'mit','coll park':'maryland'}
        for name in nicknames:
            match_counter = 0
            names = name.split()
            for word in names:
                if word in institution:
                    match_counter +=1
                if match_counter == len(institution) and match_counter == len(names):
                    institution = [nicknames[name]]
                    return institution
        return institution

def company_vector(investor, companies):
    """ Return a company vecotr for the input investor in the context of the given companies
    
    Parameters
    ----------
    investor: iterable of companies
    companies: iterable of companies
    integer, size of the entire set of companies across all investors
    
    Return
    ------
    array
        An integer array, of length equal to len(companies), containing the count for each
        company in investor at its corresponding position in companies
    
    """
    
    #create dictionary of counts of each company in investor porfolios
    counter = Counter(investor)
    #intialize empty array
    counts = []
    #loop through vocab and add counts
    for let in companies:
        if let not in counter.keys():
            counts.append(0)
        else:
            counts.append(counter[let])
    counts = np.array(counts).astype(int)
    return(counts)
