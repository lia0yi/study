import os
import time
# 1.需要备份的文件与目录将被指定在一个列表中
# 例如在Windows	下：
source = ['"d:\\py_t\\study\\__pycache__"', 
			'd:\\py_t\\study\\byte-of-python-master\\styles']

#又例如在 Mac OS X	与 Linux	下：
#source=['/User/swa/note']
#在这里要注意到我们必须在字符串中使用双引号
#用以括起其中包含空格的名称。


#2.	备份文件必须存储在一个主备份目录中
#例如在	Windows	下：
target_dir = 'D:\\py_t\\backup'
#又例如在	Mac OS X 和 Linux 下：
#target_dir	= '/Users/swa/backup'
#要记得将这里的目录地址修改至你将使用的路径

#如果目标目录还不存在，则进行创建
if	not	os.path.exists(target_dir):
	os.mkdir(target_dir)	#创建目录
#3. 备份文件将打包压缩成 zip 文件。
#4. zip	压缩文件的文件名由当前日期与时间构成。
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 将当前时间作为 zip 文件的文件名
now = time.strftime('%H%M%S')

# zip 文件名称格式
target = today + os.sep + now + '.zip'

# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)
# target=target_dir+os.sep+\
# time.strftime('%Y%m%d%H%M%S')+'.zip'


#5.	我们使用 zip 命令将文件打包成 zip 格式
zip_command	='zip -r {0} {1}'.format(target,' '.join(source))

#	运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)==0:
	print('Successful backup to',target)
else:
	print('Backup FAILED')
