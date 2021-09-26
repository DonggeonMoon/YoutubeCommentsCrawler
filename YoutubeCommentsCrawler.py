# 동영상 데이터: 숫자, 동영상 제목(title), 동영상 작성자(channelTitle), 날짜(publishedAt),
# 댓글 데이터: 아이디(authorDisplayName), 댓글내용(textOriginal), 작성시간(updatedAt), 좋아요(likeCount), 조회 시간

import requests
import openpyxl

DEVELOPER_KEY = ""  # Youtube data api key를 입력하세요.


def get_comments(video_id, key):
    url = "https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id={videoId}&key={key}"
    data = requests.get(url.format(key=key, videoId=video_id)).json()

    title = data['items'][0]['snippet']['title']
    channel_title = data['items'][0]['snippet']['channelTitle']
    published_at = data['items'][0]['snippet']['publishedAt']

    url = "https://youtube.googleapis.com/youtube/v3/commentThreads?" \
          "part=snippet&maxResults=100&videoId={videoId}&key={key}"
    url_next_token = "https://youtube.googleapis.com/youtube/v3/commentThreads?" \
                     "part=snippet&maxResults=100&pageToken={pageToken}&videoId={videoId}&key={key}"

    data = requests.get(url.format(key=key, videoId=video_id)).json()

    comments = []

    for i in range(0, len(data['items'])):
        data2 = data['items'][i]
        data3 = data2['snippet']['topLevelComment']
        data4 = data3['snippet']
        comments.append([i + 1, title, channel_title, published_at, data4['authorDisplayName'], data4['textOriginal'],
                         data4['updatedAt'], data4['likeCount']])

    num = i + 2
    print(comments)

    while 'nextPageToken' in data:
        data = requests.get(url_next_token.format(key=DEVELOPER_KEY, videoId=video_id,
                                                  pageToken=data['nextPageToken'])).json()
        for i in range(0, len(data['items'])):
            data2 = data['items'][i]
            data3 = data2['snippet']['topLevelComment']
            data4 = data3['snippet']
            comments.append([i + 1, title, channel_title, published_at, data4['authorDisplayName'],
                             data4['textOriginal'], data4['updatedAt'], data4['likeCount']])
            num += 1
    return comments


def save_excel(comments):
    wb = openpyxl.Workbook()
    ws = wb.active

    for row in comments:
        ws.append(row)

    wb.save('YCC.xlsx')


if __name__ == '__main__':

    VIDEO_ID = input("videoId를 입력하세요:")
    new_comments = get_comments(VIDEO_ID, DEVELOPER_KEY)
    save_excel(new_comments)
    
