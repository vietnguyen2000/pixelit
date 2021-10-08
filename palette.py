from PIL import ImageColor, Image
import cv2
import math

palette = [
    '#000000',
    '#222323',
    '#434549',
    '#626871',
    '#828b98',
    '#a6aeba',
    '#cdd2da',
    '#f5f7fa',
    '#625d54',
    '#857565',
    '#9e8c79',
    '#aea189',
    '#bbafa4',
    '#ccc3b1',
    '#eadbc9',
    '#fff3d6',
    '#583126',
    '#733d3b',
    '#885041',
    '#9a624c',
    '#ad6e51',
    '#d58d6b',
    '#fbaa84',
    '#ffce7f',
    '#002735',
    '#003850',
    '#004d5e',
    '#0b667f',
    '#006f89',
    '#328ca7',
    '#24aed6',
    '#88d6ff',
    '#662b29',
    '#94363a',
    '#b64d46',
    '#cd5e46',
    '#e37840',
    '#f99b4e',
    '#ffbc4e',
    '#ffe949',
    '#282b4a',
    '#3a4568',
    '#615f84',
    '#7a7799',
    '#8690b2',
    '#96b2d9',
    '#c7d6ff',
    '#c6ecff',
    '#002219',
    '#003221',
    '#174a1b',
    '#225918',
    '#2f690c',
    '#518822',
    '#7da42d',
    '#a6cc34',
    '#181f2f',
    '#23324d',
    '#25466b',
    '#366b8a',
    '#318eb8',
    '#41b2e3',
    '#52d2ff',
    '#74f5fd',
    '#1a332c',
    '#2f3f38',
    '#385140',
    '#325c40',
    '#417455',
    '#498960',
    '#55b67d',
    '#91daa1',
    '#5e0711',
    '#82211d',
    '#b63c35',
    '#e45c5f',
    '#ff7676',
    '#ff9ba8',
    '#ffbbc7',
    '#ffdbff',
    '#2d3136',
    '#48474d',
    '#5b5c69',
    '#73737f',
    '#848795',
    '#abaebe',
    '#bac7db',
    '#ebf0f6',
    '#3b303c',
    '#5a3c45',
    '#8a5258',
    '#ae6b60',
    '#c7826c',
    '#d89f75',
    '#ecc581',
    '#fffaab',
    '#31222a',
    '#4a353c',
    '#5e4646',
    '#725a51',
    '#7e6c54',
    '#9e8a6e',
    '#c0a588',
    '#ddbf9a',
    '#2e1026',
    '#49283d',
    '#663659',
    '#975475',
    '#b96d91',
    '#c178aa',
    '#db99bf',
    '#f8c6da',
    '#002e49',
    '#004051',
    '#005162',
    '#006b6d',
    '#008279',
    '#00a087',
    '#00bfa3',
    '#00deda',
    '#453125',
    '#614a3c',
    '#7e6144',
    '#997951',
    '#b29062',
    '#cca96e',
    '#e8cb82',
    '#fbeaa3',
    '#5f0926',
    '#6e2434',
    '#904647',
    '#a76057',
    '#bd7d64',
    '#ce9770',
    '#edb67c',
    '#edd493',
    '#323558',
    '#4a5280',
    '#64659d',
    '#7877c1',
    '#8e8ce2',
    '#9c9bef',
    '#b8aeff',
    '#dcd4ff',
    '#431729',
    '#712b3b',
    '#9f3b52',
    '#d94a69',
    '#f85d80',
    '#ff7daf',
    '#ffa6c5',
    '#ffcdff',
    '#49251c',
    '#633432',
    '#7c4b47',
    '#98595a',
    '#ac6f6e',
    '#c17e7a',
    '#d28d7a',
    '#e59a7c',
    '#202900',
    '#2f4f08',
    '#495d00',
    '#617308',
    '#7c831e',
    '#969a26',
    '#b4aa33',
    '#d0cc32',
    '#622a00',
    '#753b09',
    '#854f12',
    '#9e6520',
    '#ba882e',
    '#d1aa39',
    '#e8d24b',
    '#fff64f',
    '#26233d',
    '#3b3855',
    '#56506f',
    '#75686e',
    '#917a7b',
    '#b39783',
    '#cfaf8e',
    '#fedfb1',
    '#1d2c43',
    '#2e3d47',
    '#394d3c',
    '#4c5f33',
    '#58712c',
    '#6b842d',
    '#789e24',
    '#7fbd39',
    '#372423',
    '#53393a',
    '#784c49',
    '#945d4f',
    '#a96d58',
    '#bf7e63',
    '#d79374',
    '#f4a380',
    '#2d4b47',
    '#47655a',
    '#5b7b69',
    '#71957d',
    '#87ae8e',
    '#8ac196',
    '#a9d1c1',
    '#e0faeb',
    '#001b40',
    '#03315f',
    '#07487c',
    '#105da2',
    '#1476c0',
    '#4097ea',
    '#55b1f1',
    '#6dccff',
    '#554769',
    '#765d73',
    '#977488',
    '#b98c93',
    '#d5a39a',
    '#ebbd9d',
    '#ffd59b',
    '#fdf786',
    '#1d1d21',
    '#3c3151',
    '#584a7f',
    '#7964ba',
    '#9585f1',
    '#a996ec',
    '#baabf7',
    '#d1bdfe',
    '#262450',
    '#28335d',
    '#2d3d72',
    '#3d5083',
    '#5165ae',
    '#5274c5',
    '#6c82c4',
    '#8393c3',
    '#492129',
    '#5e414a',
    '#77535b',
    '#91606a',
    '#ad7984',
    '#b58b94',
    '#d4aeaa',
    '#ffe2cf',
    '#721c03',
    '#9c3327',
    '#bf5a3e',
    '#e98627',
    '#ffb108',
    '#ffcf05',
    '#fff02b',
    '#f7f4bf',
]


def colorDistance(a, b):
    d = 0
    for i in range(len(a)):
        d += (a[i]-b[i])**2
    return math.sqrt(d)


def getColorWithPalette(rgb):
    minDistance = 99999999999999999
    res = palette[0]
    for color in palette:
        c_rgb = ImageColor.getcolor(color, 'RGB')
        distance = colorDistance(rgb, c_rgb)
        if (distance < minDistance):
            minDistance = distance
            res = c_rgb
    return res


def rgbToHex(rgb):
    return '0x%02x%02x%02x' % rgb


img = Image.open('mannually.png', 'r')
w, h = img.size
pixels = img.load()


def printColor():
    for x in range(w):
        print('[', end='')
        for y in range(h):
            c = getColorWithPalette(pixels[y, x])
            print(rgbToHex(c), end='')
            if (y != h-1):
                print(',', end='')
        print(']', end='')
        if (x != w-1):
            print(',', end='')


def printSolution():
    for x in range(w):
        print('[', end='')
        for y in range(h):
            if (pixels[y, x] != (255, 255, 255)):
                print('1', end='')
            else:
                print('-1', end='')
            if (y != h-1):
                print(',', end='')
        print(']', end='')
        if (x != w-1):
            print(',', end='')


printColor()
