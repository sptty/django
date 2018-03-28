# -*- coding:utf-8 -*-
# __author__ = 'sean'

# 定义实现功能的类


class  Person:
    # 构造函数，类实例化时 自动执行。
    def __init__(self, name, gen, age, fight):
        self.name = name
        self.gen = gen
        self.age = age
        self.fight = fight


    def fight_in_grass(self):
        # 在草丛作战
        self.fight = self.fight - 200

    def self_practice(self):
        # 自我修炼
        self.fight = self.fight + 100

    def multi_fight(self):
        self.fight = self.fight - 500

    def detail(self):
        # 当前对象详细情况
        temp = "姓名：%s;性别：%s; 年龄： %s ; 战斗力：%s " % (self.name,self.gen, self.age,self.fight)
        print(temp)

# 开始游戏
#对类Person实例化的过程就是创建游戏角色
can = Person('苍井空','女',20,160)
ken = Person('Ken','南',24,445)

# 输出所有人当前详细情况
can.detail()
ken.detail()

# 开始游戏
can.multi_fight() # can参加了一次多人战斗
ken.self_practice() # ken自我修炼一次


# 输出所有人当前详细情况
can.detail()
ken.detail()

