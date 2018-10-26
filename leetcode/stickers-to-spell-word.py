import collections
class Solution:
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]   1 <= len(stickers) <= 50
        :type target: str           1 <= len(target) <= 15
        :rtype: int

        M(i, target): the minimum steps to compose target by using words
                      from sticker[1 ... i]
        """

        def uniformWords(word, target):
            new = ''
            for char in word:
                if char in target:
                    new += char
            return new

        def hasWord(word, letters, times):
            flag = False
            for char in word:
                if letters[ord(char)-ord('a')] != 0:
                    flag = True
                    if letters[ord(char)-ord('a')] < times:
                        return False
            return flag & True

        def useWord(word, letters, times):
            tmp = letters.copy()
            for char in word:
                if tmp[ord(char)-ord('a')] != 0:
                    tmp[ord(char)-ord('a')] -= times
            return tmp

        def unUseWord(word, letters):
            for char in word:
                letters[ord(char)-ord('a')] += 1
            return letters

        def toWord(letters):
            strs = ''
            for i, v in enumerate(letters):
                if v > 0:
                    strs += chr(ord('a')+i)*v
            return strs

        def dfs(letters, stickers, dp, opt):
            if not letters:
                return 0
            if len(stickers) == 0:
                return 2 ** 10

            case = 2 ** 10
            word = collections.Counter(stickers[0])
            times = 0
            if letters & word:
                times = (letters&word).most_common()[-1][1]
            tmp = word
            for i in range(times-1):
                tmp += word
            while times > 0:
                if times > opt:
                    continue
                case = min(case, times+dfs(letters-tmp, stickers[1:], dp, case))
                times -= 1
                tmp -= word
            case = min(case, dfs(letters, stickers[1:], dp, case))
            # print(toWord(letters), stickers, case)
            return case


        # letters = [0] * 26
        # letters = unUseWord(target, letters)
        letters = collections.Counter(target)

        # Remove all irrelevant chars in stickers
        newStickers = []
        for sticker in stickers:
            newSticker = uniformWords(sticker, target)
            if newSticker:
                newStickers.append(newSticker)

        # Sort the stickers by the len, which comes first means
        # it shares more common words with target
        newStickers.sort(key = lambda s: len(s), reverse=True)

        # print(letters)
        ret = dfs(letters, newStickers, {}, 2**10)
        return ret if ret != 2**10 else -1 


print(Solution().minStickers(["with", "example", "science"], "thehat"))
print(Solution().minStickers(["notice", "possible"], "basicbasic"))
# print(Solution().minStickers(["notice", "possible"], "basicbasic"))
# print(Solution().minStickers(["ttttt", "ttta", "aatt"], "tttaaatt"))
# print(Solution().minStickers(["travel","quotient","nose","wrote","any"], "lastwest"))
# print(Solution().minStickers(["all","chord","doctor","dance","drive","ready","phrase","skill","dress","select","if","develop","space","broad","lone","was","fight","how","window","place","has","plural","star","complete","though","rub","practice","here","nation","dark","job","observe","key","hole","short","last","neck","oh","science","industry","work","gun","rule","magnet","stead","many","push","tall","soft","road"], "thosecontinent"))

# with open('/Users/Jim/Downloads/1000comomms.txt') as f:
#     lines = f.read().splitlines()
# import random
# stickers = random.sample(lines, 10)
# target = ''.join(random.sample(stickers,2))
# print(stickers, target)
        