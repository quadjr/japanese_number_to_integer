#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re

def japanese_number_to_integer(num):
    # 数字定義
    digits = {'':0, '〇':0, '一':1, '二':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9,
        '零':0, '壹':1, '壱':1, '弌':1, '弐':2, '弍':2, '貳':2, '貮':2, '参':3, '參':3, '泗':4, '肆':4, '伍':5, '陸':6, 
        '漆':7, '質':7, '捌':8, '玖':9}
    digits_base = [
        ['', 1],
        ['万', 10**4],
        ['萬', 10**4],
        ['億', 10**8],
        ['兆', 10**12],
        ['京', 10**16],
        ['垓', 10**20],
        ['𥝱', 10**24],
        ['穣', 10**28],
        ['溝', 10**32],
        ['澗', 10**36],
        ['正', 10**40],
        ['載', 10**44],
        ['極', 10**48],
        ['恒河沙', 10**52],
        ['阿僧祇', 10**56],
        ['那由他', 10**60],
        ['不可思議', 10**64],
        ['無量大数', 10**68],
    ]
    digits_sub_base = [
        ['', 1],
        ['十拾什', 10],
        ['百陌佰', 100],
        ['千仟阡', 1000],
    ]

    # 正規表現文字列の生成
    match_str = ''
    digits_join = ''.join(digits.keys())
    for base, _ in digits_base:
        for sub_base, _ in digits_sub_base:
            if sub_base == '':
                match_str +=  '(' + base[::-1] + ')?' if base != '' else ''
                match_str += '(?P<d' + sub_base + base + '>[' + digits_join + ']?)'
            else:
                match_str += '(?P<b' + sub_base + base + '>[' + sub_base + ']?)(?P<d' + sub_base + base + '>[' + digits_join + ']?)'

    # 正規表現処理（漢数字文字列を逆順にしてマッチング処理）
    match = re.fullmatch(match_str, num[::-1])
    if match is None:
        raise ValueError

    # 数値算出
    res = 0
    for base, base_value in digits_base:
        for sub_base, sub_value in digits_sub_base:
            d = match.group('d' + sub_base + base)
            res += digits[d] * sub_value * base_value
            if sub_base != '' and base != '':
                res += sub_value * base_value if d == '' and match.group('b' + sub_base + base) != '' else 0

    return res

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(japanese_number_to_integer(sys.argv[1]))
    else:
        print(sys.argv[0] + ' 漢数字')
