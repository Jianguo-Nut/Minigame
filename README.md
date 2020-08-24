# minigame

> 一个在MCDReforged中使用的，用于在原版服务器中启动小游戏的插件

于`MCDReforged0.9.5`中测试通过

之前在生电服玩红石小游戏，pvp类的小游戏经常有人在不知不觉中破坏了机器和地形，影响到小游戏的正确进行，另外，赶到小游戏区一般也要不少时间，最近刚学了python三个礼拜，于是我突发奇想写了这么个玩意。

注意，此插件需要使用[PlayerInfoAPI](https://github.com/TISUnion/PlayerInfoAPI)

# 用法

- 把它和[PlayerInfoAPI](https://github.com/TISUnion/PlayerInfoAPI)一起放入plugins并重启服务端(暂时还不能热重载，至少不能有玩家在线)
- 在游戏内，输入`!!mg ?`来查看是否有运行中的小游戏。
- 如果没有，由一位玩家前往小游戏机器，并输入`!!mg start`开启一场小游戏并记录传送点(该玩家所在位置)。
- 此时，全服玩家可以输入`!!mg join`以加入小游戏，加入后，玩家会被传送至传送点并切换为冒险模式，不会误伤地形机器。
- 输入`!!mg quit`退出小游戏并被传送回原位且切换为生存模式。
- 输入`!!mg stop`以停止当前的小游戏，以启动别的小游戏。
