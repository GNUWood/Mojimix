# Mojimix

Mojimixは、日本語であれば片仮名と平仮名をシャッフルし、英語であれば全角・半角をシャッフルするPythonモジュールです。

###### 使用方法

```python
import Mojimix

text = Mojimix.randomizer("IPアドレスは、インターネット上であなたを特定する最も簡単な方法です。IPアドレスは、あなたを追跡し、あなたのオンライン生活をマッピングするために使用することができます。")

print(text)
```

###### 実行結果

```
IＰあどレスハ、イんターネッと上デアナたを特定スル最モ簡単な方法です。IＰあドれスは、あナタヲ追跡シ、アナたノおんらいン生活をまッピんグするタメニ使用スルコトガデきマす。
```

###### 機能のON/OFF切り替え

randomizerでシャッフルしない文字列を決めることができます。

```python
Mojimix.randomizer("任意の文字列", hira=True, kata=True, lower=True, upper=True, lower_zen=True, upper_zen=True)
```

hira: 平仮名から片仮名へのシャッフル

kata: 片仮名から平仮名へのシャッフル

lower: 英半角小文字から英全角小文字へのシャッフル

upper: 英半角大文字から英全角大文字へのシャッフル

lower_zen: 英全角小文字から英半角小文字へのシャッフル

upper_zen: 英全角大文字から英半角大文字へのシャッフル



いずれもデフォルトではTrueになっています。