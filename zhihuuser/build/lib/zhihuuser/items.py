# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    url_token = Field()
    name = Field()
    avatar_url = Field()
    avatar_url_template = Field()
    type = Field()
    url = Field()
    headline = Field()
    description = Field()
    gender = Field()
    badge = Field()
    follower_count = Field()
    following_count = Field()
    mutual_followees_count = Field()
    answer_count = Field()
    question_count = Field()
    commercial_question_count = Field()
    articles_count = Field()
    favorite_count = Field()
    favorited_count = Field()
    thank_from_count = Field()
    thank_to_count = Field()
    thanked_count = Field()
    vote_from_count = Field()
    vote_to_count = Field()
    voteup_count = Field()
    cover_url = Field()
    following_columns_count = Field()
    pins_count = Field()

    following_favlists_count = Field()
    following_question_count = Field()
    following_topic_count = Field()
    marked_answers_count = Field()
    hosted_live_count = Field()
    participated_live_count = Field()

    locations = Field()
    educations = Field()
    employments = Field()
    business = Field()