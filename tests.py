import unittest
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class TestPPSData(unittest.TestCase):

    def test_split_DRG(self):
        strDRG = '064 - INTRACRANIAL HEMORRHAGE OR CEREBRAL INFARCTION'
        id = strDRG.split(' - ')[0]

        strDRG2 = '064 - INTRACRANIAL HEMORRHAGE OR CEREBRAL INFARCTION'

        strOut = ''

        if ' W ' in strDRG2: 
            ls = strDRG2.split(' W ')[1]
            strOut = ls[0]          
        
        strOut = strDRG2.split(' - ')[1].strip()

        print strOut

        self.assertTrue(id > 0)


    #copy the tabular rows to the DRG tables
    def test_copy_to_DRG(self):
        
        DRGList = list()  

        tbl = PpsDataTable.query.limit(50).all()

        for row in tbl:
            DRG_mod = ''
            DRG_def = ''

            if ' W ' in row.DRG_Definition:
                DRG_mod = row.DRG_Definition.split(' W ')[1]

            DRG_def = row.DRG_Definition.split(' - ')[1].strip()

            d = DRG(
                DRG_Definition = DRG_def,
                DRG_Id = row.DRG_Definition.split(' - ')[0],
                DRG_Modifier = DRG_mod
            )

            DRGList.append(d)
            
            self.assertTrue(len(d.DRG_Definition) >0)

        self.assertTrue(len(DRGList) > 0)    
    
        existing_records = DRG.query.all()

        for new_record in DRGList: 
            is_new = True
            foundMatch = False

            #check the list of existing providers
            for existing_record in existing_records:
                #update    
                if new_record.DRG_Definition == existing_record.DRG_Definition:                 
                    foundMatch = True
                    break;
 
            if foundMatch:
                #for now do nothing
                is_new = False 
                print '\tSkipping: ' + new_record.DRG_Definition
                #do something here
                #newprovider = existing_provider
           
            #else insert
            if (is_new == True):
                print '\tAdding: ' + new_record.DRG_Definition
                db.session.add(new_record)
                db.session.commit()
                #add it to the list of existing providers so we dont re-add it
                existing_records.append(new_record)
             
            #print db.session.query(func.count(Provider.Provider_Id))


    def test_copy_to_Procedure(self):
        
        procedureList = list()  

        tbl = PpsDataTable.query.limit(50).all()

        for row in tbl:
            p = Procedure(
                DRG_Id = row.DRG_Definition.split(' - ')[0],
                Provider_Id = row.Provider_Id,
                Total_Discharges = row.Total_Discharges,
                Average_Covered_Charges = row.Average_Covered_Charges,
                Average_Total_Payments = row.Average_Total_Payments
            )

            procedureList.append(p)
            
            self.assertTrue(p.Provider_Id >0)

        self.assertTrue(len(procedureList) > 0)    
    
        existing_procedures = Procedure.query.all()

        for new_procedure in procedureList: 
            is_new = True
            foundMatch = False

            #check the list of existing providers
            for existing_procedure in existing_procedures:

                #update    
                if (int(new_procedure.DRG_Id) + int(new_procedure.Provider_Id)) == (int(existing_procedure.DRG_Id + existing_procedure.Provider_Id)):
                    foundMatch = True
                    break;
 
            if foundMatch:
                #for now do nothing
                is_new = False 
                print '\tSkipping: ' + new_procedure.DRG_Id
                #do something here
                #newprovider = existing_provider
           
            #else insert
            if (is_new == True):
                print '\tAdding: ' + new_procedure.DRG_Id
                db.session.add(new_procedure)
                db.session.commit()
                #add it to the list of existing providers so we dont re-add it
                existing_procedures.append(new_procedure)
             
            #print db.session.query(func.count(Provider.Provider_Id))


    def test_copy_to_Provider(self):
        
        providerList = list()  

        tbl = db.session.query(
            PpsDataTable.Provider_Id.distinct(),
            PpsDataTable.Provider_Name,
            PpsDataTable.Provider_Street_Address,
            PpsDataTable.Provider_City,
            PpsDataTable.Provider_State,
            PpsDataTable.Provider_Zip_Code
        ).limit(10).all()

        for row in tbl:
            p = Provider(
                Provider_Id = row[0],
                Provider_Name = row[1],
                Provider_Street_Address = row[2],
                Provider_City = row[3],
                Provider_State = row[4],
                Provider_Zip_Code = row[5]   
            )

            providerList.append(p)
            
            self.assertTrue(len(p.Provider_Name) >0)

        self.assertTrue(len(providerList) > 0)    
    
        existing_providers = Provider.query.all()

        for newprovider in providerList: 
            is_new_provider = True
            foundMatch = False

            #check the list of existing providers
            for existing_provider in existing_providers:
                #update    
                if newprovider.Provider_Id == existing_provider.Provider_Id:                 
                    foundMatch = True
                    break;
 
            if foundMatch:
                #for now do nothing
                is_new_provider = False 
                print '\tSkipping: ' + newprovider.Provider_Name
                #do something here
                #newprovider = existing_provider
           
            #else insert
            if (is_new_provider == True):
                print '\tAdding: ' + newprovider.Provider_Name
                db.session.add(newprovider)
                db.session.commit()
                #add it to the list of existing providers so we dont re-add it
                existing_providers.append(newprovider)
             

    def test_SQLAlchemy_setup(self):
        tbl = PpsDataTable.query.limit(50).all()

        for row in tbl:
            self.assertTrue(row.DRG_Definition)

if __name__ == '__main__':
    unittest.main()