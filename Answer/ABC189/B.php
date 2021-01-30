<?php
// 途中で Python での回答に切り替えたので、こちらは未完成（浮動小数点の演算による誤差が解消できていない）

// n=お酒の杯数、 x=アルコール限界値ml
fscanf(STDIN, "%d %d", $n, $x);

$now = 0;

for($i = 0 ; $n > $i ; $i++) {
  // v=量ml、 p=アルコール度数%
  fscanf(STDIN, "%d %d", $v, $p);

  $now = $now + ($v * ($p / 100));
  echo "v:".$v."|now:".$now."\n";

  // 判定
  if ($now > $x) {
    echo ($i+1);
  	exit;
  }
}
echo -1;
