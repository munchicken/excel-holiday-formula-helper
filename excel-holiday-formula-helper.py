"""
Excel Holiday Formula Helper

Helper app to create formula pieces for holiday formatting in Excel
"""

holidays = [ 'WBI', 'SB', 'THK', 'WBII' ] #list of holiday labels
final = [] #output

for holiday in holidays:
    final.append( 'AND(' + holiday + '-B<>"",' + holiday + '-E<>"",B6>=' + holiday + '-B,B6<=' + holiday + '-E),')

print(final)
