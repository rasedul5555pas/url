


 # """
 # convert it to lower case
 # replace blank space with - (dash)
 # convert it to function
 # """

#
# def url_top(string):
#   """
#  this function will convert string to url
#  :param string:
#  :return: url
#  """
#   striped_st = string.strip()
#   lower_case = striped_st.lower()
#   url = lower_case.replace(' ','-')
#   return url
#
#
# print(url_top('Md Rashedul Islam '))

#f(x) = x^2 +2x + 6
#f(2) = x**2 +2*2 +6 = 14
#
# def singlevariable(x):
#  res_lt = x**2 +2*x +6
#  return  res_lt
#
# #print(singlevariable(20))
#
# def plus(x,y):
#  result = x +y
#  return result
# print(plus(10,20))

def slugify(text):
 slug = text.strip().lower().replace(' ','-')
 while ('--') in slug:
  slug = slug.replace('--', '-')
 return slug

title = input('Enter Title: ')

slug = slugify(title)
print(slug)

















