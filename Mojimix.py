import random

hiragana = ['あ', 'ぁ', 'い', 'ぃ', 'う', 'ぅ', 'え', 'ぇ', 'お', 'ぉ', 'か', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ', 'ご', 'さ', 'ざ', 'し', 'じ', 'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ', 'た', 'だ', 'ち', 'ぢ', 'つ', 'づ', 'て', 'で', 'と', 'ど', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ば', 'ぱ', 'ひ', 'び', 'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゃ', 'ゆ', 'ゅ', 'よ', 'ょ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん']
katakana = ['ア', 'ァ', 'イ', 'ィ', 'ウ', 'ゥ', 'エ', 'ェ', 'オ', 'ォ', 'カ', 'ガ', 'キ', 'ギ', 'ク', 'グ', 'ケ', 'ゲ', 'コ', 'ゴ', 'サ', 'ザ', 'シ', 'ジ', 'ス', 'ズ', 'セ', 'ゼ', 'ソ', 'ゾ', 'タ', 'ダ', 'チ', 'ヂ', 'ツ', 'ヅ', 'テ', 'デ', 'ト', 'ド', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'バ', 'パ', 'ヒ', 'ビ', 'ピ', 'フ', 'ブ', 'プ', 'ヘ', 'ベ', 'ペ', 'ホ', 'ボ', 'ポ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ャ', 'ユ', 'ュ', 'ヨ', 'ョ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン']
en_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
en_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
en_upper_zen = ['Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ', 'Ｖ', 'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ']
en_lower_zen = ['ａ', 'ｂ', 'ｃ', 'ｄ', 'ｅ', 'ｆ', 'ｇ', 'ｈ', 'ｉ', 'ｊ', 'ｋ', 'ｌ', 'ｍ', 'ｎ', 'ｏ', 'ｐ', 'ｑ', 'ｒ', 'ｓ', 'ｔ', 'ｕ', 'ｖ', 'ｗ', 'ｘ', 'ｙ', 'ｚ']



def randomizer(moji, hira=True, kata=True, lower=True, upper=True, lower_zen=True, upper_zen=True):
    text = ""

    for i in moji:
        x = random.randint(0,1)

        if i in hiragana and hira == True and x >= 1:
            place = hiragana.index(i)
            text += katakana[place]

        elif i in katakana and kata == True and x >=1:
            place = katakana.index(i)
            text += hiragana[place]

        elif i in en_upper and upper == True and x >=1:
            place = en_upper.index(i)
            text += en_upper_zen[place]

        elif i in en_lower and lower == True and x >=1:
            place = en_lower.index(i)
            text += en_lower_zen[place]

        elif i in en_upper_zen and upper_zen == True and x >=1:
            place = en_upper_zen.index(i)
            text += en_upper[place]
        
        elif i in en_lower_zen and lower_zen == True and x >=1:
            place = en_lower_zen.index(i)
            text += en_lower[place]

        else:
            text += i

    return text