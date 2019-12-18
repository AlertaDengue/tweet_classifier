from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random

data = []
user_ids = ["vcbbio@hotmail.com", "sandrabiafe@gmail.com", "marcelo.gomes@fiocruz.br", "lucas_bianchi123@hotmail.com", "bmacedocoimbra@gmail.com", "marcelobbribeiro@gmail.com", "iasmimalmeida26@gmail.com", "felipebottega@gmail.com", "alfcury@yahoo.com", "biancadsloiola@gmail.com", "karinasantana.bqi@gmail.com", "catoper@gmail.com", "sheylacitrangulo@gmail.com", "nadja.lopes@gmail.com", "fccoelho@gmail.com", "emiledanielly@gmail.com", "claudia.codeco@gmail.com", "raquelmlana@gmail.com", "alfcury@yahoo.com.br"]
user_list = ['699682409839771649', '996505451964633088', '714844193181401088', '712805701349937153', '704038265322602496', '842035081862643716']
N = 50 # lenght of data and tweets table
      
def gen_tweet():
  global tweet, int_id, str_id, text, user
  user = anvil.users.get_user()['email']


  for row in range(N): #N
    if user == 'raquelmlana@gmail.com':
      tweets = app_tables.count.search(count=q.between(0,5),raquel_check=1)
    elif user == 'karinasantana.bqi@gmail.com':
      tweets = app_tables.count.search(count=q.between(0,5),karina_check=1)
    elif user == 'fccoelho@gmail.com':
      tweets = app_tables.count.search(count=q.between(0,5),flavio_check=1)
    elif user == 'claudia.codeco@gmail.com':
      tweets = app_tables.count.search(count=q.between(0,5),claudia_check=1)
    else: tweets = app_tables.count.search(count=q.between(0,5))
    count = random.randint(0,(len(tweets)-1)) # randomize row selection # N-1
    row = list(tweets)[count]
    str_id = row['str_id']
    if app_tables.classifications.get(str_id = str_id, uid = user) != None: 
      continue
    else:
      int_id = row['tid']
      tweet = app_tables.tweets.get(str_id = str_id)
      text = tweet['text']
      return text
      break
  return False
  
class User(UserTemplate):
  
  def check_text(self, text):
    if isinstance(text, str):
      self.tweet.text = text
    elif text == False: 
      self.tweet.text = "Nao ha mais tweets. Pode ser que voce tenha avaliado todos os tweets ou o numero minimo de tweets avaliados foi atingido. Em caso de duvidas fale com Marcelo: marcelobbribeiro@gmail.com"
      self.yes.visible = False
      self.no.visible = False
      self.uncertain.visible = False
      self.label_3.visible = False
      self.update.visible = False
      
  def __init__(self, **properties):   
    self.tweet.height = 130
    self.init_components(**properties)
    anvil.users.login_with_form()
    text = gen_tweet()
    self.check_text(text)
    
  def button_clicks(self, relevance):
    row = app_tables.count.get(str_id = str_id)
    if user == 'raquelmlana@gmail.com':
      row.update(raquel_check=-1)
    elif user == 'karinasantana.bqi@gmail.com':
      row.update(karina_check=-1)
    elif user == 'fccoelho@gmail.com':
      row.update(flavio_check=-1) 
    elif user == 'claudia.codeco@gmail.com':
      row.update(claudia_check=-1) 
    relevance = relevance
    anvil.server.call('update_tweet', int_id, relevance, user, str_id) # atualiza tabela counts
    text = gen_tweet()
    self.check_text(text)
    self.update.text = "Base de dados atualizada. Obrigado! Gerando novo tweet..."
 
  def button_yes_click(self, **event_args):
    relevance = True
    self.button_clicks(relevance)
    
  def button_no_click(self, **event_args):
    relevance = False
    self.button_clicks(relevance)
    
  def button_uncertain_click(self, **event_args):
    text = gen_tweet()
    self.tweet.text = text
    self.update.text = "Gerando novo tweet..."     

  def build_button_click(self, **event_args):
    """This method builds the database of tweets. Use it with extreme caution! """
    #method: feed tweets table
    for tweet in data:
      tid = tweet['id']
      text = tweet['message']
      feeder_count = tweet['count']
      anvil.server.call("feed_tweets", tid, text, feeder_count)
    #tweets = app_tables.tweets.search(count=q.less_than(5050))

  def expand_click(self, **event_args):
    #method: expand count
    #for i in [525,675]:
    for i in range(508, 1000):
      tweet = app_tables.tweets.get(count = i)
      tid = tweet['tid']
      str_id = tweet['str_id']
      anvil.server.call('expand_count', tid, str_id, count = i)
  
  def move_click(self, **event_args):
    anvil.server.call('move_rows')
    
    finished_list = app_tables.count_finished.search()
    for done_tweet in finished_list[645:]: #645 is last limit
      str_id = done_tweet['str_id']
      print(str_id)
      for user_id in user_ids:
        row = app_tables.classifications.get(str_id = str_id, uid = user_id)
        if row != None:
          print(user_id)
          app_tables.classifications_finished.add_row(tid=row['tid'], uid=row['uid'], date_classified=row['date_classified'], relevance=row['relevance'], str_id=row['str_id'])
          row.delete()
    
  def remove_error_click(self, **event_args):
    anvil.server.call('remove_error')

  def specify_user_click(self, **event_args):
    user = 'claudia.codeco@gmail.com'
    for str_id in user_list:
      row = app_tables.count.get(str_id = str_id)
      row.update(claudia_check=1)
      
  def build_button_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    if anvil.users.get_user()['email'] != 'marcelobbribeiro@gmail.com':
      self.build_button.visible = False
      self.delete_tweets.visible = False
      self.expand.visible = False
      self.remove_error.visible = False
      self.fix.visible = False
      self.specify_user.visible = False

#obsoleto
#   def fix_click(self, **event_args):
#     # method: fix ids
#     tweets = app_tables.tweets.search(count=q.less_than(1001))
#     #tweets = app_tables.tweets.search(count=133)
#     count = 1
#     for tweet in tweets:
#       str_id = tweet['str_id']
#       int_id = tweet['tid']
#       anvil.server.call("fix_tweets", str_id, int_id, count)
#       count+=1



    