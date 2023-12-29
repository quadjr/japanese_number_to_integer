# 漢数字文字列変換
漢数字文字列を整数変数に変換するPython関数です。  
法令等の漢数字を変換する際にご活用ください。  
  
無駄に無量大数までサポートしています。

## 使い方
引数に漢数字文字列を指定して実行すると整数が表示されます  
importして関数を直接呼ぶことも出来ます。

#### コマンド例
```
python3 japanese_number_to_integer.py 三万五千一
```
結果表示
```
35001
```
---
#### コマンド例
```
python3 japanese_number_to_integer.py 30000百万
```
結果表示
```
30000000000
```
---
#### コマンド例
```
python3 japanese_number_to_integer.py 七十無量大数七百不可思議五千那由他一阿僧祇七千三百三十三恒河沙
```
結果表示
```
7007005000000173330000000000000000000000000000000000000000000000000000
```
---
#### 関数使用例
```
from japanese_number_to_integer import japanese_number_to_integer
print(japanese_number_to_integer('三万五千一'))
```
結果表示
```
35001
```
