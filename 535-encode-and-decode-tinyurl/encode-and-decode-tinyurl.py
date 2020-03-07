# -*- coding:utf-8 -*-


# English:
# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
#
# 中文:
# TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl 时，它将返回一个简化的URL http://tinyurl.com/4e9iAk.
# 要求：设计一个 TinyURL 的加密 encode 和解密 decode 的方法。你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。


#
# @lc app=leetcode.cn id=535 lang=python
#
# [535] TinyURL 的加密与解密
#
# https://leetcode-cn.com/problems/encode-and-decode-tinyurl/description/
#
# algorithms
# Medium (78.33%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 4.2K
# Testcase Example:  '"https://leetcode.com/problems/design-tinyurl"'
#
# TinyURL是一种URL简化服务， 比如：当你输入一个URL https://leetcode.com/problems/design-tinyurl
# 时，它将返回一个简化的URL http://tinyurl.com/4e9iAk.
#
# 要求：设计一个 TinyURL 的加密 encode 和解密 decode
# 的方法。你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。
#
#

class Codec:
    cache = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        cache_key = hash(longUrl)
        self.cache[str(cache_key)] = longUrl
        return 'http://tinyurl.com/{}'.format(cache_key)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        x = shortUrl.split('/')[-1]
        if x in self.cache:
            return self.cache[x]
        return ''

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

if __name__ == "__main__":
    codec = Codec()
    s = codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))
    print(s)


