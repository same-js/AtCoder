<?php
# 文字列の入力
fscanf(STDIN, "%s", $s);

$arr = str_split($s);
$past = '';
$result = false;
foreach ($arr as $k => $v) {
  if ($k != 0 && strcmp($v, $past) != 0 ) {
    echo 'Lost';
    exit;
  }
  $past = $v;
}
echo 'Won';
