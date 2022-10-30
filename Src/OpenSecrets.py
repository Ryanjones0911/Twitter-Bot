from crpapi import *
from TwitterFunctions import GetTweetText


crp = CRP("45b23b770058e0bbcdabd38904375366")


def GetName():
    candidate = crp.candidates.get('N00007360')
    name = candidate['@attributes']['firstlast']
    return name

contribs = crp.candidates.contrib('N00007360', '2016')
print(contribs)