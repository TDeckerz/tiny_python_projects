#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = '.\crowsnest.py'


consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
template = 'Ahoy, Captain, {} {} off the larboard bow!'
side_check = 'Ahoy, Captain, {} {} off the {} bow!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word)


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('a', word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word)


# --------------------------------------------------
def test_vowel_upper():
    """OCTOPUS -> an OCTOPUS"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.upper()}')
        assert out.strip() == template.format('an', word.upper())


# --------------------------------------------------
def test_consonant_case():
    """Octopus -> An Octopus"""

    case_flag = '-c'
    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()} {case_flag}')
        assert out.strip() == template.format('A', word.title())


# --------------------------------------------------
def test_vowel_case():
    """Octopus -> An Octopus"""

    case_flag = '-c'
    for word in vowel_words:
        out = getoutput(f'{prg} {word.title()} {case_flag}')
        assert out.strip() == template.format('An', word.title())


# --------------------------------------------------
def test_starboard_case():
    """larboard -> starboard"""

    for word in consonant_words:
        for f in ['-s', '--starboard']:
            out = getoutput(f'{prg} {word} {f}')
            assert out.strip() == side_check.format('a', word, 'starboard')