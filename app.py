#{
 #   "python.pythonPath": "c:\\users\\akk03\\documents\\pyhton_bot_chat\\line\\lib\\site-packages"
#}
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
app = Flask(__name__)

line_bot_api = LineBotApi('zpXUsKEj+V2H//r2C3xfTVTJhKnVO6ZxmiFlxPZdXA1E4H0CfX1Op2n37QCmHDmEISOAzDQ0HTvdpkbUhxMmJv+2TIfuitComiPLPEeVaBNloj1x+F09y2J5YkWn7yVFQGEjTrPTVsTogzs5sHZ7CgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('025236ef91d38f451fb7eaa4529c63aa')

@app.route("/")
def test():
    return "OK"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

from bs4 import BeautifulSoup
import codecs
import requests
import csv
class Article:
    def __init__(self, title, url, search_keyword):
        self.title = title
        self.url = url
        self.search_keyword = search_keyword

#def write_csv(sps):
#    with open('c:/Users/akk03/Documents/pyhton_bot_chat/search_kandai_sample.csv', 'w', encoding='UTF-8') as f:
#        writer = csv.writer(f)
#        writer.writerow([sps,i])

#def kamokumei(target_url):
#    r = requests.get(target_url)
#    soup = BeautifulSoup(r.content, "html.parser")#(r.content, "html.parser") #(r.content, 'lxml')
#    kamoku = soup.find(id="kamoku").text
#    return kamoku

#keywords = input()
#    for i in url_array:
#        s1 = kamokumei(i)
#    if(keywords == s1):
#        r = requests.get(i)
#        soup = BeautifulSoup(r.content, "html.parser")
#        sps = soup.find(id="hyokahouhou").text
#        #write_csv(sps)
#        print('Program Finished') 

#f = codecs.open('test', 'ab', 'cp932', 'ignore')
#s = '\xa0'
#f.write(sps) # codecsを使うとstrのままwriteできる
#f.close()


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
#================================シラバス=================================================================================-
    url_array = ['http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/00/170002.html', # 0 哲学
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/00/170008.html', # 1 言語学
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/05/170591.html', # 2 心理学
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/08/170870.html', # 3 社会学
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/00/170013.html', # 4 情報と職業
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/09/170970.html', # 5 法学
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/04/170406.html', # 6 日本国憲法
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/00/170017.html', # 7 政治学
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/00/170019.html', # 8 経済学
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/00/170020.html', # 9 経営学
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/00/170037.html', # 10 統計学
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171549.html', # 11 データサイエンスの基礎
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/00/170033.html', # 12 基礎数学（確率・統計）
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171494.html', # 13 基礎数学（線形代数）
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/05/170592.html', # 14 基礎数学（代数）
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/05/170594.html', # 15 基礎数学（幾何）
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/05/170567.html', # 16 情報社会論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/00/170052.html', # 17 情報と倫理
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/00/170061.html', # 18 コンピュータの言語
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/13/171303.html', # 19 コンピュータネットワークの基礎
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/13/171373.html', # 20 情報システムの基礎
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171081.html', # 21 プログラミング入門
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/09/170985.html', # 22 認知科学
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/09/170930.html', # 23 コミュニケーションと能力
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171480.html', # 24 メディアカルチャー論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171402.html', # 25 パブリック・アドミニストレーション論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171546.html', # 26 組織意思決定論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171524.html', # 27 数理意思決定論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/09/170999.html', # 28 認知心理学
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/05/170597.html', # 29 情報行動論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171083.html', # 30 インターネットと心理
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171471.html', # 31 コミュニケーションと行為
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/12/171226.html', # 32 現代社会論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/12/171227.html', # 33 情報・文化・コミュニケーション
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171573.html', # 34 情報メディア論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/00/170090.html', # 35 メディア産業論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171074.html', # 36 メディア表現論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171526.html', # 37 映像メディアと現代社会
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171064.html', # 38 メディアアート論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/09/170989.html', # 39 ポピュラーカルチャー論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171085.html', # 40 社会調査方法論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/11/171192.html', # 41 質的調査法
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171478.html', # 42 知的財産法（産業財産権）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171451.html', # 43 知的財産法
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/12/171287.html', # 44 情報セキュリティ論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/09/170932.html', # 45 Ｗｅｂマーケティング
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171090.html', # 46 マーケティング・リサーチ
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/08/170891.html', # 47 ベンチャービジネス論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/09/170991.html', # 48 経営戦略と組織
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/09/170995.html', # 49 経営行動分析
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/01/170103.html', # 50 会計情報論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/01/170104.html', # 51 経営情報システム論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/11/171136.html', # 52 非営利組織論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171473.html', # 53 政治過程論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171403.html', # 54 政策過程論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/01/170108.html', # 55 公共政策論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/01/170109.html', # 56 ミクロ経済モデル
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/11/171130.html', # 57 金融論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/12/171231.html', # 58 国際経済学
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/05/170589.html', # 59 ゲーム理論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171551.html', # 60 社会現象と数理モデル
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/07/170799.html', # 61 コンピュータ・シミュレーション
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171405.html', # 62 ソフトウェア開発の基礎
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171456.html', # 63 応用数学（解析）
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/01/170113.html', # 64 数理計画法
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/06/170601.html', # 65 数値・数量解析
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/01/170156.html', # 66 アルゴリズム解析・設計
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171527.html', # 67 プログラミング方法論
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/11/171158.html', # 68 オブジェクト指向プログラミング（Ｊａｖａ）
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/12/171288.html', # 69 モバイル・コンピューティング
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171406.html', # 70 リスク情報論

                #=======================================3年次配当====================================================================
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/12/171290.html', # 71 事故・災害リスク情報論
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/13/171305.html', # 72 情報デザイン
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/01/170126.html', # 73 コンピュータ・グラフィックス
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171469.html', # 74 自然言語処理
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/08/170871.html', # 75 言語情報論
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171457.html', # 76 マルチメディア教育論
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171499.html', # 77 ヴィジュアルコミュニケーション・デザイン論
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/01/170128.html', # 78 プリント・メディア制作論
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171523.html', # 79 広告実践論
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/12/171233.html', # 80 メディアイベント論
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171006.html', # 81 ネットジャーナリズム論
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/06/170609.html', # 82 地域メディア論
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171531.html', # 83 ビジネス文書管理
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/09/170933.html', # 84 文書処理
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/13/171322.html', # 85 社会心理学
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171078.html', # 86 ビジネス・イノベーション
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171008.html', # 87 リスクマネジメント論
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/06/170610.html', # 88 マクロ政治分析
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/13/171388.html', # 89 画像情報処理
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/01/170122.html', # 90 音声情報処理
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171500.html', # 91 感性情報処理
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/01/170154.html', # 92 ファジィ情報処理
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/08/170810.html', # 93 関数解析
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/11/171166.html', # 94 情報伝送の物理
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171045.html', # 95 インタフェース工学
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/13/171310.html', # 96 数学演習（解析）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171575.html', # 97 テーマ別研究（数理思想史）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171571.html', # 98 テーマ別研究（経営情報からみる企業のミクロ分析とマクロ分析）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171565.html', # 99 テーマ別研究（エッシャーの数理）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171570.html', # 100 テーマ別研究（情報空間における身体表現と表象文化の実践）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171568.html', # 101 特別講義（スポーツインテリジェンス）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171569.html', # 102 特別講義（情報空間と身体表現）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171514.html', # 103 ソフトウェア実習
                #===========================================3年次配当====================================================================

                #===========================================↓↓実習↓↓====================================================
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/12/171247.html', # 104 プログラミング基礎実習
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/09/170939.html', # 105 制作実習（映像基礎）
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/11/171100.html', # 106 グラフィックス基礎実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/13/171389.html', # 107 データリテラシー実習
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/12/171252.html', # 108 ネットワーク実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/12/171270.html', # 109 科学リテラシー実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171517.html', # 110 制作実習（ヴィジュアルコミュニケーション）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/01/170191.html', # 111 制作実習（広告）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/01/170167.html', # 112 制作実習（マルチメディア）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/13/171307.html', # 113 制作実習（映像応用）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171021.html', # 114 ＣＧ実習（制作基礎）
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/12/171258.html', # 115 デジタルアーカイブ実習
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/08/170812.html', # 116 データ分析実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171465.html', # 117 質的調査実習
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/11/171179.html', # 118 モデル分析実習
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171543.html', # 119 テキストマイニング実習
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171553.html', # 120 プログラミング実習（Ｐｙｔｈｏｎ）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/11/171168.html', # 121 オブジェクト指向プログラミング実習（Ｊａｖａ）
                #===========================================↑↑実習↑↑====================================================

                #========================================↑↑実習(3.4年)↑↑====================================================
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171039.html', # 122 制作実習（映像プロフェッショナル）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171044.html', # 123 制作実習（地域コンテンツ）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/10/171042.html', # 124 ネットジャーナリズム実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/11/171111.html', # 125 インタラクティブアート実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/13/171317.html', # 126 ＣＧ実習（３Ｄコンテンツ開発）
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/11/171173.html', # 127 行動科学実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/02/170216.html', # 128 法情報処理実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/11/171115.html', # 129 マクロ政治データ分析実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/02/170218.html', # 130 経営情報処理実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171519.html', # 131 経営分析実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171555.html', # 132 フィジカルコンピューティング実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/14/171468.html', # 133 サウンドインタラクション実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/11/171142.html', # 134 ロボットブレインコンピューティング実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/08/170885.html', # 135 アプリケーション開発実習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/15/171561.html', # 136 専門演習
                #'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/13/171378.html', # 137 卒業研究
                #========================================↑↑実習(3.4年)↑↑====================================================
                
                'http://syllabus3.jm.kansai-u.ac.jp/syllabus/search/ref/1/7/11/171190.html', # 136 社会調査実習
                ]
#================================シラバス================================================================================
    #soup = BeautifulSoup(r.content, "html.parser") #soup.find(id="kamoku").text 
    found  = 0
    for i in url_array:
        r = requests.get(i)
        if event.message.text != BeautifulSoup(r.content, "html.parser").find(id="kamoku").text:
            pass
        elif event.message.text == BeautifulSoup(r.content, "html.parser").find(id="kamoku").text:
            found = 1
            r = requests.get(i)
            soup = BeautifulSoup(r.content, "html.parser")
            sps = soup.find(id="hyokahouhou").text
            url = i
            break
            
    if  found == 1:
        reply_message = f"その科目の評価方法は,\n「{sps}」\nです.\n{url}"
    elif event.message.text != BeautifulSoup(r.content, "html.parser").find(id="kamoku").text:
        reply_message = f"すみません. \n関大総情秋学期の講義にのみ対応しています. もう一度送信内容をご確認ください."

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_message))
#event.message.textに相手の言った言葉がはいっている
    
if __name__ == "__main__":
    app.run()
    