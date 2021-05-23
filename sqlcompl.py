import os
import sys
import argparse


# Funkcija atslegvardu skaita noteiksanai
# kw_list - atslegvardu saraksts
# in_list - pec atstarpem sadalits SQL vaicajums
def list_count(kw_list, in_list):
    cnt = 0
    for el in in_list:
        if el in kw_list:
            cnt += 1
    return cnt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--targetfile', help='Specify the SPARQL queries file',
                        metavar='FILE', required=True)
    args = parser.parse_args()
    infile = ''

    if os.path.isabs(args.targetfile):
        infile = args.targetfile
    else:
        infile = os.path.join(sys.path[0], args.targetfile)

    # Ielasam atslegvardu sarakstu
    fkeywords = open('./keywords.csv', 'r', encoding='utf_8')
    keywords = fkeywords.read().split(',')

    # Ielasam SQL vaicajumus
    f = open(infile, 'r', encoding='utf_8')
    text_in = f.read()

    # Atdalam vaicajumus
    # translated - Ontop tulkotais vaicajums
    # optimized - tulkojuma optimizetais variants
    # manual - manuali rakstits vaicajums
    # previous - Ontop tulkots vaicajums no iepriekseja gada magistra darba
    text_split = text_in.split('###')
    translated = text_split[0]
    optimized = text_split[1]
    manual = text_split[2]
    previous = text_split[3]

    # Sadalam vaicajumus pa vardiem pec atstarpem vai jaunas rindas simboliem
    translated_split = translated.split()
    optimized_split = optimized.split()
    manual_split = manual.split()
    prev_split = previous.split()

    # Iegustam katra vaicajuma atslegvardu skaitu
    t_count = list_count(keywords, translated_split)
    o_count = list_count(keywords, optimized_split)
    m_count = list_count(keywords, manual_split)
    prev_count = list_count(keywords, prev_split)

    print('Translated query complexity: {}'.format(t_count))
    print('Optimized query complexity: {}'.format(o_count))
    print('Manual query complexity: {}'.format(m_count))
    print('Previous query complexity: {}'.format(prev_count))

    f.close()
    fkeywords.close()
