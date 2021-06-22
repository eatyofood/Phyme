import pandas as pd
from Phyme import Phyme
import pretty_errors

pd.set_option('display.max_colwidth',None)

ph   = Phyme()

def rhyme(word='',only_perfect=False,r_frame=False,return_output=True):
    '''
    TAKES:
        word : (str) enter a word you want to find rhymes. if left blank it will prompt input
        only_perfect  : (bool) if true will only return perfect rhymes
        r_frame       : (bool) if true will put results in a dataframe , otherwise it will print rhymes.
        return_output : (bool) if true will return a variable, with either a dictionary or dataframe 
                         depending on what output you set. 

    OUTPUT: 
        Rhymes yo! : prints em or returns em in the form of a dictionary or DataFrame depending
        on the options you set
    '''
    di   = {}
    
    # If No Word Input
    if word == '':
        word = str(input('Enter a word to rhyme:'))
        print('')


    # find perfect rhymes. DOG -> COG


    get_perfect_rhymes = ph.get_perfect_rhymes(word)#, num_sylls=None)
    di['perfect_rhymes'] = get_perfect_rhymes

    # find rhymes with the same vowels and consonants of the same type (fricative, plosive, etc) and voicing (voiced or unvoiced). FOB -> DOG


    get_family_rhymes = ph.get_family_rhymes(word)#, num_sylls=None)
    di['family_rhymes'] = get_family_rhymes

     # find rhymes with the same vowels and consonants of the same type, regardless of voicing. HAWK -> DOG


    get_partner_rhymes = ph.get_partner_rhymes(word)
    di['partner_rhymes'] = get_partner_rhymes

    # find rhymes with the same vowels and consonants, as well as any extra consonants. DUDES -> DUES


    get_additive_rhymes = ph.get_additive_rhymes(word)
    di['additive_rhymes'] = get_additive_rhymes

    # find rhymes with the same vowels and a subset of the same consonants. DUDE -> DO


    get_subtractive_rhymes = ph.get_subtractive_rhymes(word)  
    di['subtractive_rhymes'] = get_subtractive_rhymes
    
    # find rhymes with the same vowels and some of the same consonants, with some swapped out for other consonants. FACTOR -> FASTER


    get_substitution_rhymes = ph.get_substitution_rhymes(word) 
    di['substitution_rhymes'] = get_substitution_rhymes

    # find rhymes with the same vowels and arbitrary consonants. CASH -> CATS


    get_assonance_rhymes = ph.get_assonance_rhymes(word)
    di['assonance_rhymes'] = get_assonance_rhymes

    # find word that do not have the same vowels, but have the same consonants. CAT -> BOT


    get_consonant_rhymes = ph.get_consonant_rhymes(word)
    di['consonant_rhymes'] = get_consonant_rhymes
    
    if r_frame == True:

        # Turn Rhmes Into Data Frame
        df = pd.DataFrame([di])
        df = df.T
        df.index.name = 'Rhyme Type'
        df.rename(columns={0:word})
        if only_perfect:
            df = df.T[['perfect_rhymes']].T

        if return_output:
            return df
        else:
            print(df)
    else:
        if return_output:
            if only_perfect:
                di = di['perfect_rhymes']
            return di
        else:
            if only_perfect:
                print('perfect_rhymes: ')
                print('|======================|')
                print(get_perfect_rhymes)
                print('')
            else:
                print('perfect_rhymes: ')
                print('|======================|')
                print(get_perfect_rhymes)
                print('')
                print('family_rhymes: ')
                print('|======================|')
                print(get_family_rhymes)
                print('')
                print('partner_rhymes: ')
                print('|======================|')
                print(get_partner_rhymes)
                print('')
                print('additive_rhymes: ')
                print('|======================|')
                print(get_additive_rhymes)
                print('')
                print('subtractive_rhymes: ')
                print('|======================|')
                print(get_subtractive_rhymes)
                print('')
                print('substitution_rhymes: ')
                print('|======================|')
                print(get_substitution_rhymes)
                print('')
                print('assonance_rhymes: ')
                print('|======================|')
                print(get_assonance_rhymes)
                print('')
                print('consonant_rhymes:')
                print('|======================|')
                print(get_consonant_rhymes)


word_input = ''
'''! NOT USEFUL IN SHELL SCRIPT !'''
# DataFrame Option - 
#print('do you want output in a data frame format')
#want_frame = str(input('enter y/n:'))
r_frame    = False
#if 'y' in want_frame:
#    r_frame = True
''' ! end useless bullshit !'''



# Only Perfect Rhymes? 
print('do you want only perfect rhymes?')

perfect_rhyme = str(input('enter y/n:')).lower()
only_p        = False
if 'y' in perfect_rhyme:
    only_p    = True





while word_input.lower() != 'done!':
    print('=============[get ready to wrap]============')
    print('1) type a word to return rhymes ')
    print('2) type "done!" to exit the program')
    print('.............................................')
    print('')
    word_input = str(input('word:'))
    print('')
    print(f'+++++++++++++++++++{word_input}++++++++++++++++++++++++')
    try:
        print(rhyme(word_input,only_perfect=only_p,r_frame=r_frame ))
        print('')
    except BaseException as b:
        print('sorry that word is not in the dic, or somthing else broke. \n ... try again  ')
        print('Error:',b)
