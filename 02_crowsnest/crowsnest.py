#!/usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2022-01-20
Purpose: Crows Nest mini project
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='The thing we see')

    # Flag to determine whether article and object case match
    parser.add_argument('-c',
                        '--case',
                        help='Article case matches object case',
                        action='store_true')

    parser.add_argument('-s',
                        '--starboard',
                        help='Notifes starboard side',
                        action='store_true')
                        
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    object_spotted = args.word
    match_case = args.case
    side_flag = args.starboard
    side = 'larboard'
    
    # Single line which reduces opportunity for mistakes.
    article = 'an' if object_spotted[0].lower() in 'aeiou' else 'a'

    # If the case flag was passed in, check and then match the object case
    if match_case:
        if object_spotted == object_spotted.title():
            article = article.title()

    if side_flag:
        side = 'starboard'
    # Several ways of outputting the string
    # The first uses string concatenation. The second makes use of placeholders.
    # The last uses placeholders with f string
    # print('Ahoy, Captain, ' + article + ' ' + object_spotted + ' off the larboard bow!')
    # print('Ahoy, Captain, {} {} off the larboard bow!'.format(article, object_spotted))
    print(f'Ahoy, Captain, {article} {object_spotted} off the {side} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
