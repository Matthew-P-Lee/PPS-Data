from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('mysql://sassberto:bigkneez@ppsdata.c3btmdaoc32l.us-east-1.rds.amazonaws.com:3306/PPSdata')
metadata = MetaData(bind=engine)

PPStable = Table('PPSdata',metadata,autoload=True)

for c in PPStable.c:
    print c
