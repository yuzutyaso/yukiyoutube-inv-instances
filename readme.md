[instances.txt]はInvidiousのインスタンスが、Python3のlist（str）で入っています。<br>
<a href="https://api.invidious.io">InvのAPI</a><br>
<a href="https://api.invidious.io/instances.json?pretty=1&sort_by=type,users">そのJSON版</a>

## 既存のリポジトリで使用する
  1.使用したいリポジトリでmain.pyを開く
  2.最上部に```import ~~~```と並んでいるので、そこの下に```import ast```と書く。
  3.その下にある、```apis = [r"https:// ..（以下略）```となっている部分を
  ```apis = ast.literal_eval(requests.get('https://raw.githubusercontent.com/LunaKamituki/yukiyoutube-inv-instances/main/instances.txt').text)```に置き換える。
  
  4.（設定によっては自動で行われる）deployする（方法等は調べて下さい。）
