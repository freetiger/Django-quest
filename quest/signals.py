#coding=utf-8
from django.dispatch import Signal

question_submit_done=Signal(providing_args=['obj','user'])
answer_submit_done=Signal(providing_args=['obj','user','question'])
vote_submit_done=Signal(providing_args=['instance','user','optype'])
follow_question_done=Signal(providing_args=['instance','user','optype'])
comment_submit_done=Signal(providing_args=['instance','user','commenttype','optype'])
#vote_delete_done=Signal(providing_args=['instance_id','user'])
#question_submit_done=Signal(providing_args=['obj','user'])

save_activity=Signal(providing_args=['obj','user'])
