"""
Prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.
"""
import emoji

emo = input("Input: ")
print(emoji.emojize(f"Output: {emo}", language="alias"))