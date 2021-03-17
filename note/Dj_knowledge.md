

# Django Form 


## Basic Knowledged

https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#

### Tags : 
####  Format : 
{% xxxx content  %}

#### Key tags 
##### load 
Loads a custom template tag set.
{% load somelibrary package.otherlibrary %}


### Filters

{{ variable_name | filter_name }}
https://www.geeksforgeeks.org/django-template-filters/

- Filter : Work on a variable : change its value : 

- Example : 
  {{ value | length }}
  If value is [‘a’, ‘b’, ‘c’, ‘d’], the output will be 4.  


Django Template Engine provides filters which are used to transform the values of variables;es and tag arguments. We have already discussed major Django Template Tags. Tags can’t modify value of a variable whereas filters can be used for incrementing value of a variable or modifying it to one’s own need.