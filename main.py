import post_message
import in_token
import checkKakao

token = in_token.token
flagKakao = checkKakao.flagKakao

if __name__ == "__main__":
    if flagKakao:
        kakaoPost = checkKakao.todayPost
        post_message.send_message(token, '#chattest', "카카오 기술 블로그에 새로운 글이 올라왔습니다.")
        for link in kakaoPost:
            post_message.send_message(token, '#chattest', link)
    
