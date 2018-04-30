import pytest
import retrie

# def test_empty_exception():
#     with pytest.raises(Exception):
#         rt = retrie.Retrie('')
#     with pytest.raises(Exception):
#         rt = retrie.Retrie()
#         rt.add('')
#     with pytest.raises(Exception):
#         rt = retrie.Retrie()
#         rt.regex()

def test_trivial():
    rt = retrie.Retrie('a')
    assert rt.regex().fullmatch('a')
    assert not rt.regex().fullmatch('')
    assert not rt.regex().fullmatch('aa')

def test_two_roots():
    rt = retrie.Retrie('a', 'b')
    assert rt.regex().fullmatch('a')
    assert rt.regex().fullmatch('b')
    assert not rt.regex().fullmatch('')
    assert not rt.regex().fullmatch('aa')
    assert not rt.regex().fullmatch('bb')
    assert not rt.regex().fullmatch('ab')
    assert not rt.regex().fullmatch('ba')

def test_aa_ab():
    rt = retrie.Retrie('aa', 'ab')
    assert rt.regex().fullmatch('aa')
    assert rt.regex().fullmatch('ab')
    assert not rt.regex().fullmatch('')
    assert not rt.regex().fullmatch('a')
    assert not rt.regex().fullmatch('b')
    assert not rt.regex().fullmatch('bb')
    assert not rt.regex().fullmatch('ba')
    assert not rt.regex().fullmatch('aaa')
    assert not rt.regex().fullmatch('aba')
    assert not rt.regex().fullmatch('aa ')
    assert not rt.regex().fullmatch('ab ')

def test_a_b_aa_bb():
    rt = retrie.Retrie('a', 'b', 'aa', 'bb')
    assert not rt.regex().fullmatch('')
    assert rt.regex().fullmatch('a')
    assert rt.regex().fullmatch('b')
    assert rt.regex().fullmatch('aa')
    assert rt.regex().fullmatch('bb')
    assert not rt.regex().fullmatch('ab')
    assert not rt.regex().fullmatch('aab')
    assert not rt.regex().fullmatch('ba')
    assert not rt.regex().fullmatch('bba')

def test_a_b_aaa_bbb():
    rt = retrie.Retrie('a', 'b', 'aaa', 'bbb')
    assert not rt.regex().fullmatch('')
    assert rt.regex().fullmatch('a')
    assert rt.regex().fullmatch('b')
    assert rt.regex().fullmatch('aaa')
    assert rt.regex().fullmatch('bbb')
    assert not rt.regex().fullmatch('aa')
    assert not rt.regex().fullmatch('bb')

def test_monkey():
    rt = retrie.Retrie('monkey')
    assert rt.regex_str() == 'monkey'
    rt.add('money')
    assert rt.regex_str() == 'mon(key|ey)'
    rt.add('monk')
    assert rt.regex_str() == 'mon(k(ey)?|ey)'
    rt.add('monks')
    assert rt.regex_str() == 'mon(k(ey|s)?|ey)'
    rt.add('monkeynut')
    assert rt.regex_str() == 'mon(k(ey(nut)?|s)?|ey)'
    rt.add('monkeyface')
    assert rt.regex_str() == 'mon(k(ey(nut|face)?|s)?|ey)'
    rt.add('monkery')
    assert rt.regex_str() == 'mon(k(e(y(nut|face)?|ry)|s)?|ey)'
    rt.add('ape')
    assert rt.regex_str() == 'mon(k(e(y(nut|face)?|ry)|s)?|ey)|ape'

def test_common_prefix():
    assert retrie.common_prefix('a', 'b') == ''
    assert retrie.common_prefix('a', 'a') == 'a'
    assert retrie.common_prefix('aa', 'aa') == 'aa'
    assert retrie.common_prefix('aab', 'aa') == 'aa'
    assert retrie.common_prefix('aa', 'aab') == 'aa'
    assert retrie.common_prefix('aaa', 'aab') == 'aa'
    assert retrie.common_prefix('aaa', 'aa') == 'aa'
