import MySQLdb
import seaborn as sns
import pandas as pd

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

class SchoolID:
    def __init__(self):
        pass

    def identify_school(self,institutions,i):
        '''
        Process a school name to give a more unique identifier.

        Replace common stems with just the stem, delete others, and replace
        keywords and nicknames with a common title.

        Parameters
        ----------
        institutions : Series
            A series of institution names, not identified.
        i : int
            The index of the school to be identified in institutions
        '''
        institutions[i] = self._delete_stems(institutions[i])
        institutions[i] = self._reduce_to_stems(institutions[i])
        institutions[i] = self._replace_by_keyword(institutions[i])
        institutions[i] = self._replace_by_nickname(institutions[i])

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
                    institutions = names
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
