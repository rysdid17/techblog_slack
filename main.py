import post_message
import in_token
import checkKakao
import checkWoowa

token = in_token.token
flagKakao = checkKakao.flagKakao
flagWoowa = checkWoowa.flagWoowa

if __name__ == "__main__":
    # 카카오
    if flagKakao:
        kakaoPost = checkKakao.todayPost
        post_message.send_message(token, '#chattest', "카카오 기술 블로그에 새로운 글이 올라왔습니다.")
        for link in kakaoPost:
            post_message.send_message(token, '#chattest', link)
    else:
        post_message.send_message(token, '#chattest', "카카오 기술 블로그에 새로운 글이 없습니다.")
    
    post_message.send_message(token, '#chattest', "---------------------------------------------")

    # 우아한 형제들
    if flagWoowa:
        WoowaPost = checkWoowa.todayWoowa
        post_message.send_message(token, '#chattest', "우아한 형제들 기술 블로그에 새로운 글이 올라왔습니다.")
        for link in WoowaPost:
            post_message.send_message(token, '#chattest', link)
    else:
        post_message.send_message(token, '#chattest', "우아한 형제들 기술 블로그에 새로운 글이 없습니다.")
