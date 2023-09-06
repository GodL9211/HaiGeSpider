#! -*-conding=: UTF-8 -*-
# 2023/9/6 15:32
# 防盗链处理

import requests

# 播放页面
url = "https://www.pearvideo.com/video_1707809"

cont_id = url.split("_")[1]
print(cont_id)

"""
通过分析网页源代码和加载后渲染的网页，需要构造成实际的播放地址为：
https://video.pearvideo.com/mp4/short/20201217/cont-1707809-15534149-hd.mp4
"""

# 视频中间层链接
video_url = f"https://www.pearvideo.com/videoStatus.jsp?contId={cont_id}&mrd=mrd=0.03351383962889121"

"""
{
  "resultCode": "1",
  "resultMsg": "success",
  "reqId": "1be70e8a-74bd-4a53-b6ed-c21e2f1d2ae6",
  "systemTime": "1693987311304",
  "videoInfo": {
    "playSta": "1",
    "video_image": "https://image.pearvideo.com/cont/20201217/cont-1707809-12525909.jpg",
    "videos": {
      "hdUrl": "",
      "hdflvUrl": "",
      "sdUrl": "",
      "sdflvUrl": "",
      "srcUrl": "https://video.pearvideo.com/mp4/short/20201217/1693987311304-15534149-hd.mp4"
    }
  }
}
"""

# 通过srcUrl构造真实的url

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    # 防盗链,溯源：当前请求的上一级
    "Referer": url
}

rsp = requests.get(video_url, headers=headers).json()
print(rsp)

"""
https://www.pearvideo.com/videoStatus.jsp?contId=1707809&mrd=0.7478015643860954

"""

systemTime = rsp["systemTime"]
RealsrcUrl = rsp["videoInfo"]["videos"]["srcUrl"].replace(systemTime, f"cont-{cont_id}")


# 下载视频
with open("a.mp4", mode="wb") as f:
    f.write(requests.get(RealsrcUrl).content)

if __name__ == '__main__':
    pass
