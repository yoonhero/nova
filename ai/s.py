def lengthOfLongestSubstring(s):
    result = 0

    for offset in range(len(s)):
        length = 0
        already = []
        for i in range(offset, len(s)):
            if s[i] not in already:
                print(already, s[i], offset)
                length += 1
                already.append(s[i])
            else:
                break
        result = length if length > result else result

    return result


print(lengthOfLongestSubstring("pwwkew"))
