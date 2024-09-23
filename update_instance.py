# https://qiita.com/y_kato_eng/items/ca0de5cf1224c807e7e5より

import datetime
import aiohttp
import asyncio
import ast

start = datetime.datetime.now()

urls_str = '''https://tube.mha.fi/
https://invidious.fdn.fr/
https://toob.unternet.org/
https://trashtube.tinfoil-hat.net/
https://invidious.projectsegfau.lt/
https://tube.mha.fi/
https://video.tlebear.win/
https://ztube.glitch.me/
https://y.com.cm/
https://vid.puffyan.us/
https://tube.cadence.moe/
https://invidious.grimneko.de/
https://invidious.rndsh.it:8443/
https://tube.meowz.moe/
https://tube.meowz.moe/
https://invidious.kavin.rocks/
https://invidious.snopyta.org/
https://invidious.zapashcanon.fr/
https://invidious.flokinet.to/
https://invidious.ethibox.fr/
https://iteroni.com/
https://invidious-us.kavin.rocks/
https://invidious.stemy.me/
https://invidious.namazso.eu/
https://invidious.snopyta.org/
https://invidious.otthorn.xyz/
https://invidious.flokinet.to/
https://yt.artemislena.eu/
https://youtube.076.ne.jp/
https://invidio.xamh.de/
https://invidious.sethforprivacy.com/search?q= 
https://invidio.xamh.de/
http://vid.mint.lgbt/
http://tube.connect.cafe/
http://max16k.invidious.icu/
http://invidious.privacy.gd/
http://invidious.weblibre.org/
http://inv.bp.mutahar.rocks/
http://invidious.exonip.de/
https://vid.wxzm.sx/
https://vid.puffyan.us/
https://invidious.osi.kr/
https://piped.based.quest/
https://piped.silkky.cloud/
https://piped.kavin.rocks/
https://test.invidious.io/
https://ytprivate.com/
https://au.ytprivate.com/
https://invidious.048596.xyz/
https://yt.512mb.org/
https://yt.didw.to/
https://yt.tesaguri.club/
https://invidious.himiko.cloud/
https://invidious.sp-codes.de/
https://inv.skyn3t.in/
http://144.126.251.186/
https://clips.im.allmendenetz.de/
https://fast.busyt.one/
https://lttb.xyz/
https://yt.d0.cx/
https://t.xtos.us/
https://www.browserling.com/browse/win/7/chrome/92/
https://youtube.com/
https://yt.dorper.me/
https://tube.mha.fi/
https://trashtube.tinfoil-hat.net/
https://yt.thechangebook.org/
https://invidious.reallyaweso.me/
https://sitep01.herokuapp.com/
https/tube.mha.fi/
https://tube.mha.fi/
https://toob.unternet.org/
https://inv.cthd.icu/
https://iv.catgurl.cloud/
https://invidious.xamh.de/
https://invidious.kavin.rocks/'''

def log(message):
    print(f'{(datetime.datetime.now() - start).seconds}秒経過', message)

async def fetch(session, url):
    """非同期にURLからデータを取得する関数"""
    print(f"Fetching {url}")
    async with session.get(url + 'api/v1/search?q=test&page=1&hl=jp') as response:
        return await response.text()

async def main():
    log("タスク開始")
    """メインの非同期処理を行う関数"""
    urls = ast.literal_eval(urls_str)
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        
        print("Starting tasks...")
        # 非同期タスクを開始する前にメッセージを出力
        print("Tasks are running in the background...")
        
        # 非同期タスクの結果を待つ
        results = await asyncio.gather(*tasks)
        
        print("Tasks completed. Results:")
        for result in results:
            print(result[:100])  # 結果の最初の100文字を表示
    
    log("タスク終了")

# asyncio.run()を使ってメイン関数を実行する
if __name__ == "__main__":
    asyncio.run(main())