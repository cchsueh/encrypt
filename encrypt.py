# 使用 randint()
from random import randint


class Encrypt:
    def __init__(self):
        self.setCode()

    def __str__(self):
        return self.code

    def setCode(self):
        # 取得a、b值
        a = 0
        b = 0
        while a % 2 == 0:
            a = randint(0, 9)
            b = randint(0, 9)
            # 利用公式建立密碼表
            self.code = ''
            x = 'a'
            i = 0
            while i < 26:
                y = ord(x) * a + b
                m = y % 26
                self.code += chr(m + 97)
                x = chr(ord(x) + 1)
                i += 1

    def toEncode(self, ps):
        # 暫存編碼結果的字串
        result = ''
        # 利用迴圈走完參數字串的所有字元，若是英文小寫字母就進行編碼轉換
        for i in ps:
            if ord(i) >= 97 and ord(i) <= 122:
                m = ord(i) - 97
                result += self.code[m]
            else:
                result += i

        return result

        return ps

    def toDecode(self, ps):
        # 暫存編碼結果的字串
        result = ''

        # 逐一取得每一個字元
        i = 0
        while i < len(ps):
            # 判斷字元是否為英文小寫字母，若是小寫字母就進行編碼轉換
            if ord(ps[i]) >= 97 and ord(ps[i]) <= 122:
                # 第二層迴圈尋找該字元在密碼表中的索引值，加上 DIFF 就可轉換回原本的字元
                j = 0
                while j < len(self.code):
                    if ps[i] == self.code[j]:
                        result += chr(j + 97)
                    j += 1
            else:
                result += ps[i]
            i += 1
        return result


if __name__ == '__main__':
    e = Encrypt()
    print()
    print(e)
    s1 = 'There is no spoon.'
    s2 = e.toEncode(s1)
    print(s2)
    s3 = e.toDecode(s2)
    print(s3)