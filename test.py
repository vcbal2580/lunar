#encoding:utf-8
import sys
sys.path.append('/Users/zhaoyunlai/Downloads/lunar-master/')#下载路径

import Lunar

myBZ = Lunar.BazhiDate(1978,7,2,11,23,1)
print (u'阳历：',myBZ.trueSunDatetime)
print (u'农历：',myBZ.lunarDate_cn())
print (u'八字：',myBZ.ganzhiList())
print (u'属相：',myBZ.shuXiang)
print (u'大运日期',myBZ.daYun_date)
print (u'大运生日后',myBZ.daYunAfterBirth)
print (u'旬空：',myBZ.xunKong_list)

# print (myBZ.naYinList)
#
# print u"属相",myBZ.shuXiang
