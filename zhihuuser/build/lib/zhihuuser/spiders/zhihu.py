# -*- coding: utf-8 -*-
import json

import scrapy

from zhihuuser.items import UserItem
from scrapy_redis.spiders import RedisSpider

class ZhihuSpider(RedisSpider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    # start_urls = ['http://www.zhihu.com/']
    redis_key = 'zhihu:start_urls'
    start_user = 'reallysugar'
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'data[*].answer_count,locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'
    followees_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    followees_query = 'data[*].answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge[%3F(type%3Dbest_answerer)].topics'
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    followers_query = 'data[*].answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge[%3F(type%3Dbest_answerer)].topics'

    def start_requests(self):
        yield scrapy.Request(self.user_url.format(user=self.start_user, include=self.user_query),
                             callback=self.parse_user, dont_filter=True)

    def parse_user(self, response):
        result = json.loads(response.text)
        item = UserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
                if field == 'url':
                    item[field] = item[field].replace('/api/v4/', '/')
        yield item
        yield scrapy.Request(
            url=self.followees_url.format(user=result.get('url_token'), include=self.followees_query, offset=0,
                                          limit=20), callback=self.parse_followees, dont_filter=True)
        yield scrapy.Request(
            url=self.followers_url.format(user=result.get('url_token'), include=self.followers_query, offset=0,
                                          limit=20), callback=self.parse_followers, dont_filter=True)

    def parse_followees(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield scrapy.Request(url=self.user_url.format(user=result.get('url_token'), include=self.user_query),
                                     callback=self.parse_user, dont_filter=True)
        if 'paging' in results.keys() and results.get('paging').get('is_end') is False:
            next_page = results.get('paging').get('next')
            yield scrapy.Request(url=next_page, callback=self.parse_followees, dont_filter=True)

    def parse_followers(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                yield scrapy.Request(url=self.user_url.format(user=result.get('url_token'), include=self.user_query),
                                     callback=self.parse_user, dont_filter=True)
        if 'paging' in results.keys() and results.get('paging').get('is_end') is False:
            next_page = results.get('paging').get('next')
            yield scrapy.Request(url=next_page, callback=self.parse_followers, dont_filter=True)
