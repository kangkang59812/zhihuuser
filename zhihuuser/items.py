# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class UserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()                                #知乎数据库中用户的ID
    name = Field()                              #用户名
   # avatar_url = Field()                        #头像网址
    headline = Field()                          #用户名后面的一串简介
    description = Field()                       #个人简介
    url = Field()                               #http://www.zhihu.com/api/v4/people/+id，此url无法访问
    url_token = Field()                         #www.zhihu.com/people/{url_token}/activities，浏览器访问个人主页
    gender = Field()                            #性别，男：1，女：0，未填写：-1
 #   cover_url = Field()                         #
    type = Field()                              #people
    badge = Field()                             #知乎认证的信息

    answer_count = Field()                      #回答数量
    articles_count  = Field()                   #发表文章数量
 #   commercial_question_count = Field()         #付费提问次数
    favorite_count = Field()                    #收藏
    favorited_count = Field()                   #被收藏次数
    follower_count = Field()                    #关注者数量
    following_columns_count = Field()           #关注专栏数量
    following_count = Field()                   #关注了多少用户
    #pins_count = Field()                        #想法，类似于空间发个说说
    question_count = Field()                    #提问数量
    thank_from_count = Field()                  #A收到B感谢多少次（需要登陆）A在B的主页中看
    thank_to_count = Field()                    #A对B感谢多少次（需要登陆）A在B的主页中看
    thanked_count = Field()                     #获得多少次感谢
    vote_from_count = Field()                   #A收到B赞同多少次（需要登陆）A在B的主页中看
    vote_to_count = Field()                     #A对B赞同多少次（需要登陆）A在B的主页中看
    voteup_count = Field()                      #获得多少次赞同
    following_favlists_count = Field()          #关注的收藏夹
    following_question_count = Field()          #关注多少问题
    following_topic_count = Field()             #关注多少话题

   # marked_answer_count = Field()               #
   # mutual_followees_count = Field()            #
  #  hosted_live_count  = Field()                #举办live的数量
  #  participated_live_count = Field()           #参加live的数量
    loactions = Field()                         #居住地
    educations = Field()                        #教育经历
    employments = Field()                       #职业情况

    included_answers_count = Field()            #被知乎收藏的答案数量
   # included_articles_count = Field()           #被知乎收藏的文章数量
    #included_text = Field()



