#-*- coding:utf-8 -*-
import os
from fabric.api import *
#远程包名称
_TAR_FILE = 'scrapy_yishiwenda.tar.gz'
#远程包地址
_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE
#远程项目目录
_BASE_DIR = '/www/lern_scrapy'
# env.user = 'root'
# env.sudo_user = 'root'
env.roledefs = {
    'dev': ['root@147.104.72.77:22'],
    'release': ['root@47.104.72.77:22']
}
#多密码
env.passwords = {'dev':'Dahai881021',
                'root@47.104.72.77:22':'Dahai881021'
}
# env.hosts = ['47.104.72.77']
#单密码
# env.password = 'Dahai881021'
# 获取当前目录
def _current_path():
    return os.path.abspath('./fabfile.py')
def my_task():
    print 'sss'
    # out_put = local('ls -l ',capture=True)
    # print out_put
    run('pwd')
    run('ls -l')
    get('a.py','a.py')
def _do_deploy():
    run('ls -l')
    #删除远程临时包
    run('rm -f %s'%_REMOTE_TMP_TAR)
    #上传新包到远程服务器
    put('./pack/%s'%_TAR_FILE,_REMOTE_TMP_TAR)
    #备份老版本
    #部署新版本
    with cd(_BASE_DIR):
        run('pwd')
        run('tar -xzvf %s'%(_REMOTE_TMP_TAR))
    # with cd (_BASE_DIR):


    #启动项目

def _build():
    print _current_path()
    print os.path.split(_current_path())
    includes = ['myscrapy','*.py','*.md']
    excludes = ['*.pyc','*.pyo']
    print os.path.isdir('./pack')
    if not os.path.isdir('./pack'):
        local('mkdir pack')
    local('rm -rf ./pack/*')
    cmd = ['tar','-czvf','./pack/%s'%_TAR_FILE]
    cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
    cmd.extend(includes)
    tar_cmd = ' '.join(cmd)
    local(tar_cmd)
@roles('release')
def release_deploy():
    execute(_do_deploy)
def deploy(version):
    _build()
    if version == 'release':
        # release_deploy()
        execute(release_deploy)#execute 执行任务
    elif version == 'dev':
        pass
    else:
        print 'plaese input release or dev'




    # with lcd(os.path.join(_current_path(),'myscrapy')):
    #     pass

