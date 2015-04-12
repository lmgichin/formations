

jaccard = lambda a,b: 1.0*len(a|b)/len(a&b)

s1 = {2,3,5,7,4,8,5,6,9,8,7,4,2}
s2 = {6,6,4,4,7,6,6,1,4,4,7,6,9,3,6,1}

print "Premier ensemble : ", s1
print "Second ensemble  : ", s2
print "Union            : ", s1 | s2
print "Intersection     : ", s1 & s2
print "Ressemblance     : ", jaccard(s1,s2)