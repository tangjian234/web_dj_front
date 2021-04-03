#!/usr/bin/env python

#------------------------------------------------------------------------>
"""
{Description}

This module process asin download json file from scrappy asin downloader : quotes_spider

{Classes} : 


{Methods} :  

  1. process_asin_json_files() :
      Process downloaded asin_file by asin download spider, save into a master file  
  
  2. load_asin_json() : 
      load the master file to visualize

  __author__ : Jian tang 
"""
#------------------------------------------------------------------------>

import string_lib
import json_lib
import logging
import pathlib

import utility_lib,time
from json_lib import write_json  
import json,os
from file_lib import clear_file, add_string_to_file,load_lines
from collections import namedtuple
  
import string_lib
import re 
import dict_lib 
import collections_lib  
import log_lib
import json
from json import dumps
import dict_lib

from log_lib import Logger
logger = Logger()

# Append JSON object to output file JSON array
#  process price

""" // MARK :  SECTION 1 : Processing and variant such as price and format them  """
 
def process_price(price_download):
  '''
  {Format price}
  Return : first of list of price with dollar sign in it. USD only. 
  '''

  if type(price_download) is list:
     price = list(filter(lambda var : '$' in var, price_download))[-1]
     price=price.replace("$","")
  else: 
    # default value 
    price='0.0'   
  return(price)

def process_rating(rating_download):
  '''
  {Format rating}
  Args : 
     rating_download
  Return : just number digit 
  '''  
  if type(rating_download) is list:
    _=rating_download[-1]
    # removal of word behind first space 
    rating_download=re.sub('\s+.*','',_)
  return(rating_download)

def process_comment(no_comment_download):
  '''
  {Format no_comment_download}
  Args : raw no_comment_download data 
  Return : just number digit 
  '''  
  if type(no_comment_download) == str:
    # removal of , 
    _=no_comment_download.replace(",","")
    # removal of word behind first space 
    no_comment_download=re.sub('\s+.*','',_)
  return(no_comment_download)

def process_bsr(bsr_download):
  '''
  {Format best seller rank. return formated dictionary} 
  Args : raw no_comment_download
  Return : formated dictionary  
  Example : dictionary  
  {0: 'category':'ab', 
      'rank':'30'  
   1: 'category':'cd',       
      'rank':'30'  
  }
  '''  
  bsr_download=re.findall('#(\d+)\s+in([^#]+)',bsr_download) 
  #list of matches in the format of [(group1: c1,r1),(c2,r2)]
  bsr=dict_lib.create_dict()
  for i in range(len(bsr_download)):
      bsr[i]['category']=bsr_download[i][1]
      bsr[i]['rank']=bsr_download[i][0]  
  return(bsr)

from pathlib import Path

""" // MARK : SECTION 2 : Process downloaded asin_file by asin download spider  """
bsr_ranking = namedtuple('bsr_ranking',['category','rank'])

#def process_asin_json_files(download_output_list,master_file,task_id):  
def process_asin_json_files(task_id,context):  
  '''
  {Process downloaded asin_file by asin download spider. Save into a master file}
  Args    :
    1. download_output_list:   
    2. target_file_name :
  Return  : context : full downloaded information 
  Example : 
  '''
  # Create the file : 
  #download_output_list = "download_output_list_"+task_id+".txt"
  #target_file_name = "master_" + task_id+".json"
  #"download_output_list"+task_id+".txt" 
  download_output_list = Path(r'C:\Local\Work\Python\PyLib\scrapy\download\result\download_output_list-'+task_id+'.txt')
  print("Line No,:",log_lib.get_line_number(),download_output_list )
  target_file_name = Path(r"C:\Local\Work\Python\PyLib\scrapy\download\result\master_" + task_id+".json")
  print("Line No,:",log_lib.get_line_number(),target_file_name )

  
  file_list=load_lines(download_output_list)
  print("Line No,:",log_lib.get_line_number(),file_list)
  # Create dict to replace dict={} : dictionary of dictionaries 
  
  s=dict_lib.create_dict()
  for fname in file_list:
    # Put all into dictionary indexed by ASIN and download time 
    # fname example : C:\Local\Work\Python\PyLib\scrapy\download\result\B07QDPRYYD__03-25-2021--06_50_22.json
    # Way 1 : 
    #ftime=string_lib.get_mid_string_in_between(fname, "__",".json")
    #asin=fname.split("\\")[-1].split("__")[0]
    # Way 2 : regex  
    p=".*/(.*)__(.*--.*).json"
    #only have one match 
    (asin,download_time,)=re.findall(p,fname)[0]

    with open(fname) as f:
      dict = json.load(f)
    s[asin][download_time]= dict  

  # time is time series : e.g date_1  : last asin
  x_axis=[time for time in s[asin]]
  context['x_axis'] =",".join(x_axis)

  # Rearrange and compression 
  # Seperate into invariant one : feature_list etc and variant ones ,  
  invariant_list=['ASIN','title','feature_list','producer','brand','date_first_available']
  context['asin_list']= list(s.keys())
  
  for asin in s.keys():
      first_time=list(s[asin].keys())[0]
      s[asin]['_invarant']= collections_lib.create_dict()
      for v in invariant_list :
        s[asin]['_invarant'][v] = s[asin][first_time][v]    
      for t in s[asin].keys():
        if '--' in t : 
        #is a time tag, pop out 
          # delete invariant_list 
          for v in invariant_list :
            s[asin][t].pop(v,None) 
          #  process price, bsr,no_comment  in the variant_list
          s[asin][t]['price']=process_price(s[asin][t]['price'])         
          s[asin][t]['best_seller_rank']=process_bsr(s[asin][t]['best_seller_rank'])          
          s[asin][t]['no_of_comments']=process_comment(s[asin][t]['no_of_comments']) 
          s[asin][t]['rating']=process_rating(s[asin][t]['rating']) 
  print("Line No,:",log_lib.get_line_number(),s)
  write_json(s,target_file_name)

      #price=[s[t]["price"] for t in s[asin].keys() if '--' in t]
     
      #s['price_first_number']= price[0]
      #s['price_list']= ",".join(price)

  variant_list=['price','no_of_comments','rating']
  # mark TODO :'best_seller_rank'] hwo to process 
  #asin_dict_list=dict_lib.create_dict()
  asin_dict_list={}
  for asin in s.keys():     
    #asin_dict=dict_lib.create_dict()
    asin_dict={}
    for v in variant_list:
      # price 
      _=[s[asin][t][v] for t in s[asin].keys() if '--' in t]      
      asin_dict[v+'_first_number']= _[0]
      asin_dict[v]= ",".join(_)
    # best_seller_rank
    asin_dict_list[asin]= asin_dict

  context['asin_dict_list']=asin_dict_list
  print("Line No,:",log_lib.get_line_number(),context['asin_dict_list'])

  return(context)


""" // MARK : SECTION 3 : Load the processed asin file into dict and visualize (Old version )


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

def load_asin_master (context,master_file):
  pass

def load_asin_json(asin_list,context):
  """ <

    Args:
        <>:
        <>:

    Returns:
      list: a list of strings representing the header columns
  """   
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

    #logger.warning('no_of_comments')
    #logger.warning(no_of_comments)


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


# See Package N : Task Result file design 
def create_task_result_json(scrapy_data): 

  """
  scrapy_data['result_dict']={
    # 1. Meta data : Same as task model data
    
    "Meta_data":{
      "task_id":scrapy_data["task_id"],
      "start_time":scrapy_data["start_time"],
      "end_time":scrapy_data["end_time"],
      "asin_list":scrapy_data["asin_list"]
      },
    # 2. Invariant part of listing : 
      "Invariant_data":{},
      "Variant_data":{},
      }
  """
  scrapy_data['result_dict']={"a":1}
 
  logger.worker.warning(scrapy_data)

  return(scrapy_data)
if __name__ == '__main__':
  task_id =""
  context=dict_lib.create_dict()
  process_asin_json_files(task_id,context)
  #process_asin_json_files(original_file_name,target_file_name)    
  #create_task_result_json("B1")

    