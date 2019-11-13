import random

cat_names = {
    '보리': ('bori',4),
    '라쿤': ('raccoon',5),
    '': ('random',2),
}

base_url = 'https://yuigahama.moe/api/catbot/cat-image/'


def make_cat_image_url(utterance: str):
    # TODO URL 부분을 base_url로 고칠수 있도록 config.py 추가
    for name in cat_names:
        if name in utterance and name != '':
            return base_url + cat_names[name][0] + str(random.randint(1,cat_names[name][1]))
    return base_url + cat_names[''][0] + str(random.randint(1, cat_names[''][1]))
