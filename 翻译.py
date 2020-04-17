from googletrans import Translator
import time
import random
def init():
    global txt
    global times
    global language
    global translator
    translator = Translator(service_urls = ['translate.google.cn'])
def OneRound(s, src, dest):
    s = translator.translate(s, src = src, dest = dest).text
    time.sleep(random.randint(50, 300) / 100)
    s = translator.translate(s, src = dest, dest = src).text
    return s
def OverRound(s, times, src, dest):
    ss = []
    for i in range(times):
        s = OneRound(s, src, dest)
        time.sleep(random.randint(100, 500) / 100)
        ss.append(s)
        print('第' + str(i + 1) + '次：' + s)
        if i > 0 and ss[i - 1] == ss[i]:
            return s
        if i > 2 and ss[i - 2] == ss[i] and ss[i - 1] == ss[i - 3]:
            return s
        return s
def main():
    init()
    for i in range(len(txt)):
        print('')
        print('原 文：' + txt[i])
        print('[最终结果]\n' + OverRound(txt[i], times, language[0], language[1]))
        print('')
        time.sleep(random.randint(5, 12))
if __name__ == '__main__':
    txt = ['放逐这个世界',]
    times = 20
    language = ['zh-CN', 'en']
    main()