import telebot 
from Mystickertoken import token
from telebot import types
import random

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    # user_info = f'{message.from_user.first_name} {message.from_user.id}'
    # print(chat_id)
    # print(user_info)
    bot.send_message(chat_id,"Hello!!! I'm sticker bot")

@bot.message_handler(content_types=['sticker','text'])
def start_message(message):
    chat_id=message.chat.id
    # if message.text.lower() =='hello':
    stickers = ['CAACAgQAAxkBAAEBNoRghVy-ff-MV1qMT6eLYaZGBsHnEAACDgEAAmuuXgmEqpvy8hiGjR8E',
    'CAACAgQAAxkBAAEBNoFghVy7oNDd1-ylKA_-LKo31xDLCgACDwEAAmuuXglyouPHwS2MQB8E',
    'CAACAgQAAxkBAAEBNbhghUcnp1VxhzQJSRTH2oY3SY7wTAACPwEAAmuuXgm9uBqL7km33R8E',
    'CAACAgQAAxkBAAEBNopghV0mEBpp54ch4buKaYE-xnAP5wACCgEAAmuuXgkDg_-O9uHVcR8E',
    'CAACAgQAAxkBAAEBNqBghWrMDDSXunI3EAAByjLyk1j0x4wAAgQBAAJrrl4JZKxFj1ZaKq0fBA',
    'CAACAgIAAxkBAAEBNqNghWzgUfDI1BqFnZejnf91oEgXjQACYpEAAmOLRgx_AhT8gX512B8E',
    'CAACAgIAAxkBAAEBN5RghkSsfGjt1vBmC0h4UEyk2Ft4PAACdAEAAhAabSJqs0AMw8PSSR8E',
    'CAACAgUAAxkBAAEBN5pghkTXS5TCHIUhXd70n4-cSzuV3gACkQADcX38FLsHge7VdDoeHwQ',
    'CAACAgUAAxkBAAEBN51ghkTrmmOT0BJKVKPCbc18c9STEQACkgADcX38FOwRRhdJ4WRGHwQ',
    'CAACAgUAAxkBAAEBN6BghkT_VavcGIWdJMz2WVuToHzGtAACkwADcX38FOQ9JIMIFhnQHwQ',
    'CAACAgIAAxkBAAEBN6NghkUVaryTZL24KC5kZKjukPbMPgACnAkAAm8Odx2RJ6jdw_jHrB8E',
    'CAACAgIAAxkBAAEBN6ZghkUmanGv8DW0B6GQ9RRtZgZb8wACnwkAAm8Odx3Bk9TEObgUjR8E',
    'CAACAgIAAxkBAAEBN6lghkU6wHqhhUeFodWEoddEJL7wqAACYQADCvzCBab7fC31WjmuHwQ',
    'CAACAgIAAxkBAAEBN6xghkVIgd47AU_Fd_kS29OxiJMd9QACWQADCvzCBc5Tuxl8fnMbHwQ',
    'CAACAgIAAxkBAAEBN69ghkVg0bpfZAABSCAEuRughdu2wYUAAmAAAwr8wgW3G2YsI9wthh8E',
    'CAACAgIAAxkBAAEBN7JghkWWbbDdZapFnZEIEJhTlJUVZQACuAADwPsIAAFNkkmY37GUjh8E',
    'CAACAgIAAxkBAAEBN7VghkWy6pkn7uRAo1lknO122cmwTQACygADwPsIAAGJaMWA1FKexR8E',
    'CAACAgIAAxkBAAEBN7hghkXEc2ufu_GLo8SFAVAIIIQZ_AACEgADw4AGOHFT-VwUNO6OHwQ',
    'CAACAgIAAxkBAAEBN7tghkXcTCWj0mr6tREoKtveaoL4aAACAgADevByEtSUNlXOX4gqHwQ',
    'CAACAgIAAxkBAAEBN75ghkXrCEiA-jDN4Lt4qDwefWu7CQACAwADevByEi9G-dYCaDQuHwQ',
    'CAACAgIAAxkBAAEBN8FghkX99SQZV_SSPm_zhrZjCMw2MwACFAADevByEr_VXVcYTlO0HwQ',
    'CAACAgIAAxkBAAEBN8RghkYP0UBX2Mp67R8ry9IxZP2pHwACTQADwPY0BIhIR9qiDknIHwQ',
    'CAACAgIAAxkBAAEBN8dghkYg2OuPPfygbiChyXbgXX7TbwACbwADwPY0BI5qcszvsbfaHwQ',
    'CAACAgIAAxkBAAEBN8pghkY2g1-S2LUEH4a54t8vWFq5TwACAgADhTYNEP6Fbpaikww2HwQ',
    'CAACAgIAAxkBAAEBN81ghkg4jzjKPb4hQgkN-hlzTyzMKwACGAADhTYNEDQrieSio2jVHwQ',
    'CAACAgIAAxkBAAEBN9BghkiJCkt8Dq15n5hBo5ZvUpyAgQACfQADhTYNEMrbKkbvUpCWHwQ',
    'CAACAgIAAxkBAAEBN9Nghkih-39jcoWOy453M0UY6SVwmwACS8EBAAFji0YM9NCLBtiPubIfBA',
    'CAACAgIAAxkBAAEBN9Zghki-xUp9Q1n4ddX9-STkWywy3gACtAEAAkE7oBUYMxAVAhdELR8E',
    'CAACAgIAAxkBAAEBN9lghkjLcvYHUFa0T9wS6KeNIg_ftAACwAEAAkE7oBXSE8QyPghG3R8E',
    'CAACAgIAAxkBAAEBN9xghkjfJVbpsdUjCI7-J1H7q3GInAACwQEAAkE7oBXETGS2BPlobx8E',
    'CAACAgIAAxkBAAEBN99ghkkRPrSHKNaOBkE_EyaEDhxi3gACuAEAAkE7oBVXOuNnqOHL2x8E',
    'CAACAgIAAxkBAAEBN-JghkknmfoSeFRI5extpKHfd4lWTgACRwADI0MjBD6Sdj5I0_C2HwQ',
    'CAACAgIAAxkBAAEBN-Vghkk8Vc1T4MKEITDKlgAB6sJDjEoAAj0AAyNDIwScXIIedNs2cR8E',
    'CAACAgIAAxkBAAEBN-hghklt0Sz6_ghoyJ9WKnHydIQcSAACowEAAhAabSJHzsXzC9jXYx8E',
    'CAACAgIAAxkBAAEBN-tghkmClEwNbMtdrde35_IEyFE0lwACZwEAAhAabSKA4rHilXxE_R8E',
    'CAACAgIAAxkBAAEBN-5ghkmS934HRbX5vbg70iKKZHd5qAACYQEAAhAabSLviIx9qppNBx8E',
    'CAACAgIAAxkBAAEBN_FghkmjharKr-IzcJyXw-6I5uNSQAACawEAAhAabSJ2Qz3dblM7Ch8E',
    'AACAgIAAxkBAAEBN_RghkmzZN3FZxHoyf9GT73Ot5GJKgACbAEAAhAabSIpJJQxD9m3bB8E',
    'CAACAgIAAxkBAAEBN_dghknNrT0ENkM3e-2G9Wq1sYH0ZgACqwEAAhAabSJ4vr6RzFRsxx8E',
    'CAACAgIAAxkBAAEBN_pghkniXc6VqPTVdpwiT529O59uZgACKAEAAuCy8BEFOQ0wvAK4Wx8E',
    'CAACAgIAAxkBAAEBN_1ghkn4_YJyMqoie9TDN2_iCBp7jgAClAADBSknDa8yFLVh6XuvHwQ',
    'CAACAgIAAxkBAAEBOAABYIZKCJ579zIm1Q5yPOyo9tG2CM8AAjcAA0bBow4lF5BCTjqGrR8E',
    'CAACAgIAAxkBAAEBOANghkogU09ChPQcwROUw3a5QlKCaAACRQIAAs3ASBh4ysy-NFvbex8E',
    'CAACAgIAAxkBAAEBOAZghko4hIMSOM2j0rDwQfig813-pAACGAAD4LLwESBR01A234ZFHwQ',
    'CAACAgQAAxkBAAEBOAlghkpin-NrtSwghCBRtEvRAAGu3XUAAlwBAAJrrl4J4HxS03d1fGQfBA',
    'CAACAgQAAxkBAAEBOAxghkp0OspYQ51huSdn5hm-LQayyAACXQEAAmuuXgmViqZxmk3PLB8E',
    'CAACAgIAAxkBAAEBOA9ghkqHHzDGX64LLxgFlA45OGnVyQACaAsAAhaf9gpkTaicogiXLB8E',
    'CAACAgIAAxkBAAEBOBJghkqVRWo_JTTNAXYuFre5JV7emQACaQsAAhaf9gpKQeG2RhTbFh8E',
    'CAACAgIAAxkBAAEBOBVghkqr9uUQ4uUODI6PwQ_mbUUeiwACuwsAAhaf9gp5Ml6Sw0JA1B8E',
    'CAACAgIAAxkBAAEBOBhghkq-K9sKqk0Cq4fFPhRdCQ5bxwACvQsAAhaf9grfoOhz4N_-uB8E',
    'CAACAgQAAxkBAAEBOClghktclVRfrcah40I-curYeF1-XgACdwIAAgJ3rRFEjbKvOdI9xR8E',
    'CAACAgIAAxkBAAEBNaBghUT9VlneDx-EGbjbbC_zRCyd7gACVQADCvzCBcMC7l9e60fFHwQ']


    # bot.send_message(chat_id,'Hello dear!')
    # bot.send_sticker(chat_id,'CAACAgIAAxkBAAEBNaxghUXruOzRXgnftX3D6WmTQexaTAACvQADwPsIAAHn-Q6cy5HaKR8E')
    # bot.send_sticker(chat_id,'CAACAgIAAxkBAAEBNa9ghUX9jv7-iZ16vDFToJMJ77CuuQAC0gADwPsIAAG3BmZICbGCvx8E')
    
    bot.send_sticker(chat_id,random.choice(stickers))
bot.polling()