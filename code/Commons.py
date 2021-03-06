headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'music.163.com',
    'Referer': 'https://music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/70.0.3538.110 Safari/537.36'
}

# 文件保存的根目录
DOWNLOAD_DIR = 'download/'

NETEASE = {
    # 网易云搜索 API 接口
    'SEARCH_URL': 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token',

    # 网易云专辑信息 API 接口
    'ALBUM_URL': 'http://music.163.com/api/album/{}',

    # 网易云播放地址 API 接口
    'SONG_URL': 'http://music.163.com/weapi/song/enhance/player/url?csrf_token=',

    # 网易云歌词 API 接口
    'LYRIC_URL': 'https://music.163.com/weapi/song/lyric?csrf_token='
}

# 下载的专辑上限
ALBUM_MAX_SIZE = 30

# 歌手
artists = [
    '李荣浩'
]

# MySql 配置

MYSQL = {
    'host': '',
    'port': 3306,
    'username': '',
    'password': '',
    'schema': 'infiniti'
}
