import random

EMO_POOL = [
    '๐', '๐', '๐ค', '๐', '๐ณ', 
    '๐ช', '๐', '๐', '๐น',' โก', 
    '๐ฆ', '๐คช', '๐ฅต', '๐ก', '๐', 
    '๐ต', '๐ฅ'
]

GAN_POOL = [
    ' skrskr๐ค๐ค ', ' ๅพๅฒๅฎณๆฌธ๐๐ ', ' peace ', 
    ' ็ฌๆญป๐๐ ', ' ๅๅๆฏๆๅฆ ', ' ๅฅฝๅฑ๐ๅ ', 
    ' ๅฏไปฅ้คๅ๐ณ๐ณ ', ' ๅฅฝๅๆฒๆ่ฎ๐๐ ', ' 666่ตทไพ ', 
    ' ๆๆฏDJ~5555 ', ' ๆฌธๆฌธAAAA ', ' ็้ผ๐๐ ', 
    ' ใใ ', ' ๆฌธๅนน็ฉฟๅฑฑ็ฒๆฌธ๐คฉ๐คฉ ', ' ไฝ ๆ้ ญ็ทๅ๐ฐ๐ฐ '
]

FULL_COMMA = '๏ผ'
FULL_PERIOD = 'ใ'
FULL_EXCLAMATION = '๏ผ'
HALF_COMMA = ','
HALF_PERIOD = '.'
HALF_EXCLAMATION = '!'
END_OF_LINE = '[[endl]]'

PUNCTUATION_POOL = [
    FULL_COMMA, FULL_PERIOD, FULL_EXCLAMATION, 
    HALF_COMMA, HALF_EXCLAMATION,
    END_OF_LINE
] 

def generate_random_emoji_sequence() -> str:
    emo = random.sample(EMO_POOL, 2) * 2
    emo[1], emo[2] = emo[2], emo[1]
    return ' ' + ''.join(emo) + ' '

def generate_random_gan_text() -> str:
    return random.choice(GAN_POOL)

def convert(string: str) -> str:
    while string.count('[[endl]][[endl]]') > 0:
        string = string.replace('[[endl]][[endl]]', '[[endl]]')
    for punctuation in PUNCTUATION_POOL:
        punctuation_cnt = string.count(punctuation)
        for _ in range(punctuation_cnt):
            additive_gen = random.choice([generate_random_emoji_sequence, generate_random_gan_text])
            string = string.replace(punctuation, additive_gen(), 1)
    return string
