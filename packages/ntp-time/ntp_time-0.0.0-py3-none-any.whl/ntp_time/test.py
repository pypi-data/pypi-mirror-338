# nptサーバーによる正確な時刻 [ntp_time]
# 【動作確認 / 使用例】

import sys
import time
import ezpip
import arrow
import random
ntp_time = ezpip.load_develop("ntp_time", "../", develop_flag = True)

while True:
	# 正確な現在時刻の取得 [ntp_time]
	t = ntp_time.now()
	# 日付時刻表示
	str_t = str(arrow.get(t))
	print("%s (timestamp = %.2f)"%(str_t, t), end = "\r")
	time.sleep(0.01)
