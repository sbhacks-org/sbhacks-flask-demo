import random

def find_zodiac_sign(day, month):
    if month == 12:
        astro_sign = 'Sagittarius' if day < 22 else 'Capricorn'
    elif month == 1:
        astro_sign = 'Capricorn' if day < 20 else 'Aquarius'
    elif month == 2:
        astro_sign = 'Aquarius' if day < 19 else 'Pisces'
    elif month == 3:
        astro_sign = 'Pisces' if day < 21 else 'Aries'
    elif month == 4:
        astro_sign = 'Aries' if day < 20 else 'Taurus'
    elif month == 5:
        astro_sign = 'Taurus' if day < 21 else 'Gemini'
    elif month == 6:
        astro_sign = 'Gemini' if day < 21 else 'Cancer'
    elif month == 7:
        astro_sign = 'Cancer' if day < 23 else 'Leo'
    elif month == 8:
        astro_sign = 'Leo' if day < 23 else 'Virgo'
    elif month == 9:
        astro_sign = 'Virgo' if day < 23 else 'Libra'
    elif month == 10:
        astro_sign = 'Libra' if day < 23 else 'Scorpio'
    elif month == 11:
        astro_sign = 'Scorpio' if day < 22 else 'Sagittarius'
    return astro_sign

def get_magic_8_ball_response():
    responses = ['As I see it, yes.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Don’t count on it.', 'It is certain.', 'It is decidedly so.', 'Most likely.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Outlook good.', 'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.', 'Without a doubt.', 'Yes.', 'Yes – definitely.', 'You may rely on it.']
    return random.choice(responses)