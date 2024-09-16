// instances.txtに追加されていないインスタンスをapi_urlから取得
function checkInstance() {
  // apiからインスタンスを取得
  const api_url = 'https://api.invidious.io/instances.json?pretty=1&sort_by=type,users';
  const response_JSON = JSON.parse(UrlFetchApp.fetch(api_url));

  // instances.txtを取得
  const repositry_instances = getRepositryInstances();

  let not_added_instance = [];

  // 追加されていないものがあれば配列に追加
  for(let i = 0; i < response_JSON.length; i++){
    const instance_url = 'https://' + response_JSON[i][0] + '/';

    if(response_JSON[i][1]['api'] && !repositry_instances.includes(instance_url)){
      not_added_instance.push(instance_url);
      // console.log(instance_url);
    }
  }

  // 追加されていないインスタンスを配列でreturn（なければ空の配列）
  return not_added_instance;
}

// instances.txtから取得、整形しreturn
function getRepositryInstances() {
  const repositryInstances = UrlFetchApp.fetch('https://raw.githubusercontent.com/LunaKamituki/yukiyoutube-inv-instances/main/instances.txt');
  const str = repositryInstances.getContentText().replace('[', '').replace(']', '');

  return trim(str);
}

// コメントアウトされている箇所などを''にreplace
function trim(str){
  return str.replace(/#.*\s*/g, '').replace(/r"/g, '').replace(/"/g, '').replace(/\s/g, '').split(',');
}

// 結果を表示
Logger.log(checkInstance())
