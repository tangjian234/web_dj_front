 
import string_lib
import json_lib
import logging
import pathlib
logger = logging.getLogger(__name__)

"""
Function :  
  
Parameters :
  asin_list : 
  context   : 
 B07QDPRYYD; B088BHYN1M
 B07QDPRYYD__v1.json
 B088BHYN1M__v1.json

 "price": "38.99",
 "no_of_comments": "406 ratings",

"""
from json import dumps
""" // MARK : load_asin_json """
def load_asin_json(asin_list,context):
  
  """
  Function :  
      1. read asin_list in the string 
      2. load from asin_list from json form and put it and price data into context
  Parameters :
    asin_list : 
      string of ASIN Separated by "," 
    context   :  
      context['x_axis']= x_axis
      asin_dict : product directory 
        'price'
        'price_first_number'
        'no_of_comments'
        'no_of_comments_first_number'
        'rating'
        ..

    Input: Format 
      {Date_1:{ASIN_Key_parameter_Data}}
    Input: Example 
      C:\Local\Work\Web\web\amazon\download\json_result\B07QDPRYYD.json
    
  """
  
  # logger.warning('asin_list')
  # logger.warning(asin_list)
  # get the asin list  : eg. BSDNCD;BSSSN
  asin_list=asin_list.replace(' ', '').split(";")
  context['asin_list']=asin_list
 
  json_dir='./download/json_result'
  context['price']={}
  context['no_of_comments']={}
  context['asin_list']=asin_list
  asin_dict_list={}
  
  for a in asin_list:
    # Load json file ; combine and make a json file 
    asin=a
    file= a+'.json'
    file=pathlib.Path(json_dir,file)
    dict=json_lib.load_json(file)

    # time is time series : e.g date_1  
    x_axis=[time for time in dict.keys()]
    x_axis=",".join(x_axis)
    context['x_axis']= x_axis

    asin_dict={}
    
    # price 
    price=[dict[k]["price"] for k in dict.keys()]
    asin_dict['price_first_number']= price[0]
    asin_dict['price']= ",".join(price)
    
    # number_of_comments
    no_of_comments=[dict[k]["no_of_comments"].replace(" ratings","").replace(",","") for k in dict.keys()]
    asin_dict['no_of_comments_first_number']= no_of_comments[0]
    asin_dict['no_of_comments']= ",".join(no_of_comments)


    # rating : 
    rating=[dict[k]["rating"] for k in dict.keys()]
    # pre-processing : [['ab'], 'c'] -> ['ab', 'c']
    get_list_element=lambda r: r[0] if(isinstance(r, list)) else r 
    rating=[get_list_element(r) for r in rating]
    asin_dict['rating_first_number']= rating[0]
    asin_dict['rating']= ",".join(rating)


    # best_seller_rank
    best_seller_rank=[dict[k]["best_seller_rank"] for k in dict.keys()]
    asin_dict['best_seller_rank_first_number']= best_seller_rank[0]
    asin_dict['best_seller_rank']= ",".join(best_seller_rank)

    
    # date_first_available : does not change 
    date_first_available=[dict[k]["date_first_available"] for k in dict.keys()]
    asin_dict['date_first_available_first_number']= date_first_available[0]
    
    
    asin_dict_list[asin]= asin_dict

    logger.warning('no_of_comments')
    logger.warning(no_of_comments)


  context['asin_dict_list']=asin_dict_list  

  # for testing only, trial of transfer data as dictionary. 
  data = { 
        "Laugh": {"Cry":"f1"}, 
        "S3": {"M1":"L1"}, 
  } 
  #data = dumps(data) 
  context['data']=data
  context['asin_dict_list']=asin_dict_list
  return(context)

def read_asin_json(asin_list,context):

  """
  NOTE : **deprecated**
  Directly use load_asin_json 
  Function :  
    Read from asin_list from html form and put it and price data into context 
  Parameters :
    asin_list : string of ASIN Separated by "," 
    context   : 
  """

  context=load_asin_json(asin_list,context)
  """
  data_list=['123,50.3,49,48,52,51,47','35,59,30,81,46,55,30','45,59,0,81,46,55,30']
  i=0
  
  #for i,asin in enumerate(asin_list) : 
    #context['asin_string'][i]=asin
   # dict[asin]['price_first']= context['price'][asin].split(",")[0]
   # dict[asin]["no_of_comments_first"]= context['no_of_comments'].split(",")[0]
  
  #context['price_string_1']= data_list[0]
  #context['price_string_2']= data_list[1]
  
  # price accords time seperated by , : "23,24,21"
  #context['price_string_1']= context['asin_dict_list'][0]['price']
  #context['price_string_2']= context['asin_dict_list'][1]['price']

  # first date price 
  #context['price_1']=  context['price_string_1'].split(",")[0]
  
  #context['price_2']=  context['price_string_2'].split(",")[0]
  
  #logger.warning('price_1')

  #logger.warning(context['price_1'])
  #logger.warning(context['price_2'])

  ## number of comment accords time seperated by , : "23,24,21"  
  #context['no_of_comments_string_1']= context['asin_dict_list'][0]['no_of_comments'] 
  #context['no_of_comments_string_2']= context['asin_dict_list'][1]['no_of_comments'] 

  # first date number of comment
  #context['no_of_comments_first_1']= context['no_of_comments_string_1'].split(",")[0]
  #context['no_of_comments_first_2']= context['no_of_comments_string_2'].split(",")[0]


  #logger.warning('no_of_comments_first_1')

  #logger.warning(context['no_of_comments_first_1'])
  #logger.warning(context['no_of_comments_first_2'])

  #logger.warning('price_string_1')
  
  #logger.warning(context['price_string_1'])
  #logger.warning(context['price_string_2'])
  for a in asin_list: 
    context[a]= data_list[i]
    i=i+1
  return(context)

  """



