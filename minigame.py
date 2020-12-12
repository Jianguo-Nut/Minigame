#-*-coding:utf8;-*-

import os
import re
import time

mgstarted=False
mgx=0
mgy=0
mgz=0
mgpos=0
mgdim=0



def on_load(server,old):
    server.add_help_message('!!mg ?', '查询现在是否有开启的小游戏')
    server.add_help_message('!!mg start', '启动一场小游戏并记录当前坐标为传送点')
    server.add_help_message('!!mg stop', '停止现有的小游戏')
    server.add_help_message('!!mg join', '加入现有的小游戏并传送至传送点')
    server.add_help_message('!!mg quit', '退出现有的小游戏并传送回原位')
    if not os.path.exists('./plugins/minigame/'):
      os.makedirs('./plugins/minigame/')

def on_user_info(server,info):
    PlayerInfoAPI = server.get_plugin_instance('PlayerInfoAPI')
    dimension_convert = {'0':'overworld','-1':'the_nether','1':'the_end','minecraft:overworld':'overworld','minecraft:the_nether':'the_nether','minecraft:the_end':'the_end'}
    global mgstarted
    global mgx
    global mgy
    global mgz
    global mgpos
    global mgdim


    
    if info.content == '!!mg ?':
        if mgstarted:
            server.tell(info.player,'§a[minigame]§e目前有一场小游戏，输入!!mg join以加入')
        if not mgstarted:
            server.tell(info.player,'§a[minigame]§e目前无小游戏，输入!!mg start以启动一场小游戏')
    
    if info.content == '!!mg stop':
        if not mgstarted:
            server.tell(info.player,'§a[minigame]§e当前无小游戏')
        if mgstarted:
            server.say( '§a[minigame]§e小游戏已由§f'+info.player+'§e结束，输入!!mg quit退出并传送')
            mgstarted=False
    
    if info.content == '!!mg start':
        if mgstarted:
            server.tell(info.player, '§a[minigame]§e已有一场小游戏')
        if not mgstarted:
            mgpos = PlayerInfoAPI.getPlayerInfo(server, info.player, path='Pos')
            mgdim = PlayerInfoAPI.getPlayerInfo(server, info.player, path='Dimension')
            mgx=mgpos[0]
            mgy=mgpos[1]
            mgz=mgpos[2]
            
            server.say( '§a[minigame]§e小游戏已由§f'+info.player+'§e启动，输入!!mg join加入并传送')
            mgstarted=True
    
    if info.content == '!!mg debug':
        server.say('mgx'+mgx)
        server.say('mgy'+mgy)
        server.say('mgz'+mgz)
        server.say('mgdim'+dimension_convert[str(mgdim)])
     
    
    if info.content == '!!mg join' and mgstarted:
        f=open('./plugins/minigame/'+info.player,mode='w')
        f.write('0|0|0|overworld|false')
        f.close()
        f = open('./plugins/minigame/' + info.player , 'r')
        pinfo = f.read()
        pinfo = pinfo.replace('\n', '').replace('\r', '')
        f.close()
        p = pinfo.split('|')
        if p[4] == 'false':
            server.tell(info.player , '§a[minigame]§e正在传送并修改模式，请不要走动!')
            time.sleep(1)
            
            pos = PlayerInfoAPI.getPlayerInfo(server, info.player, path='Pos')
            dim = PlayerInfoAPI.getPlayerInfo(server, info.player, path='Dimension')
            f = open('./plugins/minigame/' + info.player , 'w')
            f.write(str(pos[0])+'|'+str(pos[1])+'|'+str(pos[2])+'|'+dimension_convert[str(dim)]+'|'+'true')
            f.close()
            server.execute('gamemode adventure ' + info.player )
            server.execute('execute at '+info.player+ ' in minecraft:' + dimension_convert[str(mgdim)] + ' run tp '+info.player+' ' +str(mgx) + ' ' + str(mgy) + ' ' + str(mgz))
            server.tell(info.player, '§a[minigame]§e已传送,要退出小游戏输入!!mg quit')
        else:
            server.tell(info.player, '§a[minigame]§e你已加入过小游戏')
    
    if info.content == '!!mg join' and not mgstarted:
        server.tell(info.player , '§a[minigame]§e当前暂无小游戏，输入!!mg start以创建')
    

    if info.content == '!!mg quit':
        server.tell(info.player , '§a[minigame]§e正在传送并修改模式，请不要走动!')
        time.sleep(1)
        f = open('./plugins/minigame/' + info.player, 'r')
        pinfo = f.read()
        pinfo = pinfo.replace('\n', '').replace('\r', '')
        f.close()
        xyz = pinfo.split('|')
        f=open('./plugins/minigame/'+info.player,mode='w')
        f.write('0|0|0|overworld|false')
        f.close()
        os.remove('./plugins/minigame/'+info.player)
        server.execute('execute at ' + info.player + ' in minecraft:' + xyz[3] + ' run tp ' + info.player + ' ' + xyz[0] + ' ' + xyz[1] + ' ' + xyz[2])
        server.execute('gamemode survival ' + info.player)