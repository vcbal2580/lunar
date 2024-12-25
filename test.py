#encoding:utf-8
import sys
sys.path.append('/f:/py_luna/lunar/')  # 确保路径正确

import Lunar

myBZ = Lunar.BazhiDate(2024, 12, 5, 15, 7, 0)
print(u'阳历：', myBZ.trueSunDatetime)
print(u'农历：', myBZ.lunarDate_cn())
print(u'八字：', myBZ.ganzhiList())
print(u'属相：', myBZ.shuXiang)
print(u'大运日期', myBZ.daYun_date)
print(u'大运生日后', myBZ.daYunAfterBirth)
print(u'小运', myBZ.xiaoYun_list)
print(u'旬空：', myBZ.xunKong_list)
print(u'纳音', myBZ.naYinList)