"""
Excel Holiday Formula Helper

Helper app to create formula pieces for holiday formatting in Excel
"""

holidays = [ 'WBI', 'SB', 'THK', 'WBII' ] #list of holiday labels
final = [] #output

for holiday in holidays:
    final.append( 'AND(' + holiday + '_B<>"",' + holiday + '_E<>"",B6>=' + holiday + '_B,B6<=' + holiday + '_E),')

for afinal in final:
    print(afinal)
