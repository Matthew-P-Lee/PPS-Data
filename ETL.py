from models import *

#defs = PpsDataTable.query.limit(100).all()

# for row in defs:
# 	row.Average_Covered_Charges = row.Average_Covered_Charges.replace('$','')
# 	try:
# 		print 'Committing...'
# 		db.session.add(row)
# 		db.session.commit()
# 	finally:
# 		print 'added ' + row.Provider_Name		

# print 'Done adding rows'

'''
connection = db.session.connection()

# recommended
cmd = """select DISTINCT 
			DRG_Definition
		FROM PPSdata;"""
res = connection.execute(text(cmd))

for row in res:
	print row.DRG_Definition
	#p = Procedure()
	#p.DRG_Definition = row.DRG_Definition
'''
