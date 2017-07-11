#!/usr/bin/python3
#-*- coding: utf-8 -*-


#============================
#    常规用法
#============================
var1 = 'HelloWorld!'
print("var1[0]: ", var1[0])
print("var1[1:5]: ", var1[1:5])
print('\n')

# Python字符串更新
var2 = ' Python，从入门到放弃！'
var1 += var2
print( var1 )

# 字符转移
# \(在行尾时)	续行符
# \\	反斜杠符号
# \'	单引号
# \"	双引号
# \a	响铃
# \b	退格(Backspace)
# \e	转义
# \000	空
# \n	换行
# \v	纵向制表符
# \t	横向制表符
# \r	回车
# \f	换页
# \oyy	八进制数，yy代表的字符，例如：\o12代表换行
# \xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
print("一行", "\x0a", '新的一行\n又是新的一行\b', '\n')

#============================
#    字符串运算符
#============================
a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
# var[a:b] 从字符串指针为a的地方开始截取字符，到b的前一个位置（因为不包含b）
print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n', '\n')

#============================
#    Python字符串格式化
#============================
# % c
# 格式化字符及其ASCII码
# % s
# 格式化字符串
# % d
# 格式化整数
# % u
# 格式化无符号整型
# % o
# 格式化无符号八进制数
# % x
# 格式化无符号十六进制数
# % X
# 格式化无符号十六进制数（大写）
# % f
# 格式化浮点数字，可指定小数点后的精度
# % e
# 用科学计数法格式化浮点数
# % E
# 作用同 % e，用科学计数法格式化浮点数
# % g % f和 % e的简写
# % G % f
# 和 % E
# 的简写
# % p
# 用十六进制数格式化变量的地址

print ( "我叫 %s 今年 %d 岁!" % ('小明', 10) )
print('\n')
print( "格式化为八进制:%o 十六进制:%x 浮点小数二位:%6.2f" % (1024, 1024, 1.024) )
print('\n')
# 在f的前面出现了一个类似小数的6.2它表示的意思是，总共输出的长度为6个字符，其中小数2位。
print( "浮点小数二位，总字符6位：%6.2f" % 1.024 )
print( "浮点小数二位，总字符6位，前面补0：%06.2f" % 1.024 )

print('\n')
#先补空格
print("%10s字符的左边应该有空格" %('hello') )
# 字符串左对齐
print("%-10s字符的右边应该有空格" %('hello') )

# Python三引号
#下面是一段SQL语句
sql = '''
CREATE TABLE `tp_ad` (
  `ad_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '广告id',
  `pid` int(11) unsigned NOT NULL DEFAULT '0' COMMENT '广告位置ID',
  `media_type` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '广告类型',
  `ad_name` varchar(60) NOT NULL DEFAULT '' COMMENT '广告名称',
  `ad_link` varchar(255) NOT NULL DEFAULT '' COMMENT '链接地址',
  `orderby` smallint(6) DEFAULT '50' COMMENT '排序',
  `target` tinyint(1) DEFAULT '0' COMMENT '是否开启浏览器新窗口',
  `bgcolor` varchar(20) DEFAULT NULL COMMENT '背景颜色',
  `create_time` int(11) NOT NULL,
  `question_id` int(11) NOT NULL COMMENT '问题id',
  `status` tinyint(4) NOT NULL COMMENT '状态：1上线，0下线',
  PRIMARY KEY (`ad_id`),
  KEY `position_id` (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8;
'''
# print(sql)
print('\n')

#============================
#    字符串内置函数
#============================
# Unicode 字符串
# 在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。
# 在Python3中，所有的字符串都是Unicode字符串。

# count(str, beg= 0,end=len(string))
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

str = '在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位Unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u'
print('字符串str的长度：%d' % len(str) )
print('Unicode在字符串str中出现的开始位置：%d' % str.find('Unicode') )
print('Unicode在字符串str中第二次出现的位置：%d' % str.find('Unicode', 33) )
print('Unicode在字符串str中出现的次数：%d' % str.count('Unicode') )
print('Unicode在字符串str中出现的次数：%d' % str.count('Unicode', 33) )
print('Unicode在字符串str中出现的次数：%d' % str.count('Unicode', 33, 48) )
print('\n')

# split(str="", num=string.count(str))
# num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
print( str.split('Unicode') )
print( str.split('Unicode', 1) )