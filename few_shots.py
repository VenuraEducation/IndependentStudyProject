obj1 = {
    'Question':"How many cmb users in the DimCustomer table?",
    'SQLQuery' : "Select count(*) from DimCustomer where DGL_Company = 'CMB'",
    'SQLResult' : "Result of the SQL query",
    'Answer' : "767"
}
obj2 = {
    'Question':"How many records in year 2023 in Job CountByJobOpenDate Table?",
    'SQLQuery' : "Select count(*) from JobCountByJobOpenDate where JobOpenDate >= DATEFROMPARTS(YEAR(GETDATE()) - 1, 1, 1) and JobOpenDate < DATEFROMPARTS(YEAR(GETDATE()), 1, 1)",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj3 = {
    'Question':"Last year Revenue by each company",
    'SQLQuery' : """SELECT Company,SUM(RevenueLocalcur) AS Revenue 
                    FROM AcctShipmentFact_ViewClient AS asf
                    WHERE RevRecDate BETWEEN DATEFROMPARTS(YEAR(GETDATE()) - 1, 1, 1) and DATEFROMPARTS(YEAR(GETDATE()) - 1, 12, 31)
                    GROUP BY Company""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj4 = {
    'Question':"Last year Profit by each company",
    'SQLQuery' : """SELECT Company,SUM(Profit_LocalCur) AS Revenue 
                    FROM AcctShipmentFact_ViewClient AS asf
                    WHERE RevRecDate BETWEEN DATEFROMPARTS(YEAR(GETDATE()) - 1, 1, 1) and DATEFROMPARTS(YEAR(GETDATE()) - 1, 12, 31)
                    GROUP BY Company""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj5 = {
    'Question':"Last year Cost by each company",
    'SQLQuery' : """SELECT Company,SUM(Cost_LocalCur) AS Revenue 
                    FROM AcctShipmentFact_ViewClient AS asf
                    WHERE RevRecDate BETWEEN DATEFROMPARTS(YEAR(GETDATE()) - 1, 1, 1) and DATEFROMPARTS(YEAR(GETDATE()) - 1, 12, 31)
                    GROUP BY Company""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj6 = {
    'Question':"Revenue by each year",
    'SQLQuery' : """SELECT YEAR(RevRecDate) AS Year,SUM(RevenueLocalcur) AS Revenue
                    FROM AcctShipmentFact_ViewClient
                    GROUP BY YEAR(RevRecDate)""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj7 = {
    'Question':"Revenue by each year In company CMB",
    'SQLQuery' : """SELECT YEAR(RevRecDate) AS Year,SUM(RevenueLocalcur) AS Revenue
                    FROM AcctShipmentFact_ViewClient
                    WHERE Company = 'CMB'
                    GROUP BY YEAR(RevRecDate)""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj8 = {
    'Question':"Revenue by each year In company IND",
    'SQLQuery' : """SELECT YEAR(RevRecDate) AS Year,SUM(RevenueLocalcur) AS Revenue
                    FROM AcctShipmentFact_ViewClient
                    WHERE Company = 'IND'
                    GROUP BY YEAR(RevRecDate)""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : "",
}
obj9 = {
    'Question':"How many Shipments were done with Customer FANNWOOD CO., LTD",
    'SQLQuery' : """SELECT COUNT(ShipmentNumber) FROM RevandVolume_ShipmentDate WHERE BillingClientName = 'FANNWOOD CO., LTD'""", 
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj10 = {
    'Question':"How many shipment we have exported to Paris in last 3 months",
    'SQLQuery':"""select count(RVM.ShipmentNumber) from RevandVolume_ShipmentDate RVM
        WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
        and DestCity = 'Paris'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj11 = {
    'Question':"How many shipment we have exported to France in last 3 months",
    'SQLQuery':"""select count(RVM.ShipmentNumber) from RevandVolume_ShipmentDate RVM
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCountry = 'France'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj12 = {
    'Question':"How many shipments have we imported from paris in last 3 months",
    'SQLQuery':"""select count(RVM.ShipmentNumber) from RevandVolume_ShipmentDate RVM
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and OriginCity = 'Paris'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj13 = {
    'Question':"How many shipments have we imported from France in last 3 months",
    'SQLQuery':"""select count(RVM.ShipmentNumber) from RevandVolume_ShipmentDate RVM
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and OriginCity = 'Freance'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj14 = {
    'Question':"Which customers do we work with for ship to Paris in last 3 months?",
    'SQLQuery':"""select distinct BillingClientName from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCity = 'Paris'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj15 = {
    'Question':"Which customers do we work with for ship to France in last 3 months?",
    'SQLQuery':"""select distinct BillingClientName from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCountry = 'Paris'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj16 = {
    'Question':"Which customers do we work with for ship from Paris in last 3 months?",
    'SQLQuery':"""select distinct BillingClientName from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and OriginCity = 'Paris'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj17 = {
    'Question':"Which customers do we work with for ship from France in last 3 months?",
    'SQLQuery':"""select distinct BillingClientName from RevandVolume_ShipmentDate
                WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                and OriginCountry = 'France'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj18 = {
    'Question':"Provide the earned revenue from the shipments we exported to Paris in the last 3 months?",
    'SQLQuery':"""select SUM(Revenue_USD) AS Revenue from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCity = 'Paris'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj19 = {
    'Question':"Provide the earned revenue from the shipments we exported to France in the last 3 months?",
    'SQLQuery':"""select SUM(Revenue_USD) AS Revenue from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCountry = 'France'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj20 = {
    'Question':"Provide the earned revenue from the shipments we imported from France in the last 3 months?",
    'SQLQuery':"""select SUM(Revenue_USD) AS Revenue from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and OriginCountry = 'France'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj21 = {
    'Question':"Provide the GP data for the shipments we exported to Paris in the last 3 months?",
    'SQLQuery':"""select SUM(Profit_USD) AS GrossProfit from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCity = 'Paris'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj22 = {
    'Question':"Provide the GP from the shipments we exported to France in the last 3 months?",
    'SQLQuery':"""select SUM(Profit_USD) AS GrossProfit from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCountry = 'France'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj23 = {
    'Question':"Provide the GP from the shipments we imported from France in the last 3 months?",
    'SQLQuery':"""select SUM(Profit_USD) AS GrossProfit from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and OriginCountry = 'France'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj24 = {
    'Question':"Provide the GP and GP margin for the shipments we exported to Paris in the last 3 months?",
    'SQLQuery':"""select SUM(Profit_USD) AS GrossProfit , SUM(Revenue_USD) / SUM(Profit_USD)   from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCity = 'Paris'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj25 = {
    'Question':"Give the Air freight tonnage of the shipment to Paris from other destination in last 3 months",
    'SQLQuery':"""select SUM(ChargebleWeight) as Chargeble_Weight from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCity = 'Paris'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj26 = {
    'Question':"Give the Air freight tonnage of the shipment from Paris to other destination in last 3 months",
    'SQLQuery':"""select SUM(ChargebleWeight) as Chargeble_Weight from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and OriginCity = 'Paris'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj27 = {
    'Question':"Give the Air freight rate given to customers from Colombo to Paris in last 3 months",
    'SQLQuery':"""select SUM(Revenue_USD) / SUM(ChargebleWeight) as Chargeble_Weight from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCity = 'Paris' and OriginCity = 'Colombo' 
                    and TransportMode = 'AIR'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj28 = {
    'Question':"Give the Air freight rate given to the customer from Paris to Colombo in last 3 months",
    'SQLQuery':"""select SUM(Revenue_USD) / SUM(ChargebleWeight) as Chargeble_Weight from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and OriginCity = 'Paris' and DestCity = 'Colombo'
                    and TransportMode = 'AIR'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj29 = {
    'Question':"Give the Air freight rate given to the customer from Paris to Colombo in last 3 months",
    'SQLQuery':"""select SUM(Revenue_USD) / SUM(ChargebleWeight) as Chargeble_Weight from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and OriginCity = 'Paris' and DestCity = 'Colombo'
                    and TransportMode = 'AIR' and PrepaidCollect = 'FREIGHT PREPAID'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj30 = {
    'Question':"Give the Air freight rate given to customers for Charges collect shipmennts from Colombo to Paris in last 3 months",
    'SQLQuery':"""select SUM(Revenue_USD) / SUM(ChargebleWeight) as Chargeble_Weight from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCity = 'Paris' and OriginCity = 'Colombo' 
                    and TransportMode = 'AIR' and PrepaidCollect = 'FREIGHT COLLECT'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj31 = {
    'Question':"give me the average rate for Ex-works shipment which is shipped to London from Delhi",
    'SQLQuery':"""select SUM(Revenue_USD) / SUM(ChargebleWeight) as Chargeble_Weight from RevandVolume_ShipmentDate
                WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                and DestCity = 'Paris' and OriginCity = 'Colombo' 
                and MainDepCode = 'FEA' and INCO = 'FOB'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj32 = {
    'Question':"Give me the incoterm wise airfreight rate for the shipmets that we have shiiped to Paris from Colombo",
    'SQLQuery':"""select INCO, INCOTermDesc,SUM(Revenue_USD) / SUM(ChargebleWeight) as Chargeble_Weight from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCity = 'Paris' and OriginCity = 'Colombo' 
                    and MainDepCode = 'FEA'
                    group by INCO, INCOTermDesc""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj33 = {
    'Question':"give the customer wise airfreight rate given for the shipment that we shipped to paris from colombo since last December",
    'SQLQuery':"""select ClientName,SUM(Revenue_USD) / SUM(ChargebleWeight) as Chargeble_Weight from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= '2023-12-31' AND ShipmentDate <= GETDATE()
                    and DestCity = 'Paris' and OriginCity = 'Colombo' 
                    and MainDepCode = 'FEA'
                    group by ClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj34 = {
    'Question':"list the customers by GP margin that we done shipmet from colombo to Paris",
    'SQLQuery':"""select ClientName, ( SUM(Profit_USD) / SUM(Revenue_USD)) as Chargeble_Weight from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= '2023-12-31' AND ShipmentDate <= GETDATE()
                    and DestCity = 'Paris' and OriginCity = 'Colombo' 
                    and MainDepCode = 'FEA'
                    group by ClientName 
                    order by ( SUM(Profit_USD) / SUM(Revenue_USD)) Desc""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj35 = {
    'Question':"Who are the Agents we work in England that used to handle the Ex work shipment during the last 6 months",
    'SQLQuery':"""select distinct AgentName from RevandVolume_ShipmentDate
                    WHERE AgentCountryName like 'United kingdom' and INCO = 'EXW'
                    and ShipmentDate >= DATEADD(MONTH, -6, GETDATE()) AND ShipmentDate <= GETDATE()""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj36 = {
    'Question':"Who are the Agents and their located city in England that weused to handle the Ex work shipment during the last 6 months",
    'SQLQuery':"""select distinct AgentName , AgentCity from RevandVolume_ShipmentDate
                    WHERE AgentCountryName like 'United kingdom' and INCO = 'EXW'
                    and ShipmentDate >= DATEADD(MONTH, -6, GETDATE()) AND ShipmentDate <= GETDATE()""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj37 = {
    'Question':"what are the Agent networks we used to work in England to handle in last year ",
    'SQLQuery':"""select distinct AgentNetwork , AgentName from RevandVolume_ShipmentDate
                    WHERE TradeCountry like '%united kingdom%'
                    and year(ShipmentDate) = YEAR(getdate()) - 1""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj38 = {
    'Question':"What is the Per TEU Avg rate given to customers from Colombo to Hamburg in last 3 months",
    'SQLQuery':"""select SUM(Revenue_USD) / SUM(TEUSum) as TEURate from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE() 
                    and DestCity = 'Hamburg' and OriginCity = 'Colombo'
                    and Packing_Mode = 'FCL'
                    and MainDepCode = 'FES'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj39 = {
    'Question':"what is the Per CBM average rate given to customers from Colombo to Hamburg in last 3 months",
    'SQLQuery':"""select SUM(Revenue_USD) / SUM(VolumeinM3) as TEURate from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE() 
                    and DestCity = 'Hamburg' and OriginCity = 'Colombo'
                    and Packing_Mode = 'LCL'
                    and MainDepCode = 'FES'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj40 = {
    'Question':"what is the average per TEU rate given to the customer from Hamburg to Colombo in last 3 months",
    'SQLQuery':"""select SUM(Revenue_USD) / SUM(TEUSum) as TEURate from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and OriginCity = 'Hamburg' and DestCity = 'Colombo'
                    and MainDepCode = 'FIS'
                    and Packing_Mode = 'FCL'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj41 = {
    'Question':"What is the Sea Per TEU rate of the prepaid shipments from Hamburg to Colombo in last 3 months",
    'SQLQuery':"""select SUM(Revenue_USD) / SUM(TEUSum) as REURate from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and OriginCity = 'Hamburg' and DestCity = 'Colombo'
                    and MainDepCode = 'FIS' and PrepaidCollect = 'FREIGHT PREPAID'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj42 = {
    'Question':"Give the Sea Freight rate given to customers for Charges collect shipmennts from Colombo to Hamburg in last 3 months",
    'SQLQuery':"""select SUM(Revenue_USD) / SUM(TEUSum) as TEURate from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and OriginCity = 'Hamburg' and DestCity = 'Colombo'
                    and MainDepCode = 'FIS' and PrepaidCollect = 'FREIGHT COLLECT'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj43 = {
    'Question':"give me the average rate for Ex-works shipment which is shipped to London from Delhi",
    'SQLQuery':"""select SUM(Revenue_USD) / SUM(TEUSum) as TEURate from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCity = 'Hamburg' and OriginCity = 'Colombo' 
                    and MainDepCode = 'FES' and INCO = 'FOB'""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj44 = {
    'Question':"Give me the incoterm wise SEA freight Per TEU rate for the shipmets that we have shiiped to Hamburg from Colombo",
    'SQLQuery':"""select INCO, INCOTermDesc,SUM(Revenue_USD) / SUM(TEUSum) as TEURate from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE()
                    and DestCity = 'Hamburg' and OriginCity = 'Colombo' 
                    and MainDepCode = 'FES'
                    group by INCO, INCOTermDesc""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj45 = {
    'Question':"give the customer wise Per TEU rate for the shipment that we shipped to Hamburg from colombo since last December",
    'SQLQuery':"""select ClientName,INCO,SUM(Revenue_USD) / SUM(TEUSum) as TEURate, Sum(TEUSum) from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= '2023-12-31' AND ShipmentDate <= GETDATE()
                    and DestCity = 'Hamburg' and OriginCity = 'Colombo' 
                    and MainDepCode = 'FES' and Packing_Mode = 'FCL' and ClientName is not null
                    group by ClientName,INCO""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj46 = {
    'Question':"list the customers by GP margin that we done shipmet from colombo to Paris",
    'SQLQuery':"""select ClientName, ( SUM(Profit_USD) / SUM(Revenue_USD)) as TEURate from RevandVolume_ShipmentDate
                    WHERE ShipmentDate >= '2023-12-31' AND ShipmentDate <= GETDATE()
                    and DestCity = 'Hamburg' and OriginCity = 'Colombo' 
                    and MainDepCode = 'FES' and ClientName is not null
                    group by ClientName 
                    order by ( SUM(Profit_USD) / SUM(Revenue_USD)) Desc""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}
obj47 = {
    'Question':"what are the top 5 sea freight destination from colombo",
    'SQLQuery':"""Select OriginCity , SUM(TEUSum), Count(*) from RevandVolume_ShipmentDate
                    where ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE() 
                    and DestCity = 'Colombo'
                    and MainDepCode = 'FES'
                    Group by OriginCity order by SUM(TEUSum) DESC""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj48 = {
    'Question':"Can you give me the total sales of the last three month and total outstanding value of the  GPV Lanka client?",
    'SQLQuery':"""select s.BillingClientName as ClientName, Sum(s.Revenue_USD) as CurrentYearSalesUSD, Sum(r.OutStanding_USD) as OutstandingUSD 
                    from RevandVolume_ShipmentDate s 
                    inner join ReceivableWithCreditLimit r on r.Oh_code = s.BillingClientCode where BillingClientName like '%GPV Lanka%' 
                    and s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE())  AND ShipmentDate <= GETDATE() group by s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj49 = {
    'Question':"Can you give me the total sales of the current year and total outstanding value of the  GPV Lanka client?",
    'SQLQuery':"""select s.BillingClientName as ClientName, Sum(s.Revenue_USD) as CurrentYearSalesUSD, Sum(r.OutStanding_USD) as OutstandingUSD 
                    from RevandVolume_ShipmentDate s 
                    inner join ReceivableWithCreditLimit r on r.Oh_code = s.BillingClientCode where BillingClientName like '%GPV Lanka%' 
                    and s.ShipmentDate >= DATEADD(yy, DATEDIFF(yy, 0, GETDATE()) - 1, -1) AND ShipmentDate <= GETDATE() group by s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj50 = {
    'Question':"Provide me with the total sales value for the last three months and the total outstanding value for the CIC Holdings client?",
    'SQLQuery':"""select s.BillingClientName as ClientName, Sum(s.Revenue_USD) as CurrentYearSalesUSD, Sum(r.OutStanding_USD) as OutstandingUSD 
                    from RevandVolume_ShipmentDate s 
                    inner join ReceivableWithCreditLimit r on r.Oh_code = s.BillingClientCode where BillingClientName like '%CIC Holdings%' 
                    and s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE() group by s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj51 = {
    'Question':"Can you give me the total sales of the current year and total outstanding value of the  Cargo Overseas client?",
    'SQLQuery':"""select s.BillingClientName as ClientName, Sum(s.Revenue_USD) as CurrentYearSalesUSD, Sum(r.OutStanding_USD) as OutstandingUSD 
                    from RevandVolume_ShipmentDate s inner join ReceivableWithCreditLimit r on r.Oh_code = s.BillingClientCode where BillingClientName like '%Cargo Overseas%' 
                    and s.ShipmentDate >= DATEADD(yy, DATEDIFF(yy, 0, GETDATE()) - 1, -1) AND ShipmentDate <= GETDATE() group by s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj52 = {
    'Question':"Provide me with the total sales value for the last three months and the total outstanding value for the Brandix Apparel client?",
    'SQLQuery':"""select s.BillingClientName as ClientName, Sum(s.Revenue_USD) as CurrentYearSalesUSD, Sum(r.OutStanding_USD) as OutstandingUSD 
                    from RevandVolume_ShipmentDate s 
                    inner join ReceivableWithCreditLimit r on r.Oh_code = s.BillingClientCode where BillingClientName like '%Brandix Apparel%' 
                    and s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE() group by s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj53 = {
    'Question':"Provide me with the total sales value for the past three months and the total outstanding value for the GPV Lanka client?",
    'SQLQuery':"""select s.BillingClientName as ClientName, Sum(s.Revenue_USD) as CurrentYearSalesUSD, Sum(r.OutStanding_USD) as OutstandingUSD 
                    from RevandVolume_ShipmentDate s 
                    inner join ReceivableWithCreditLimit r on r.Oh_code = s.BillingClientCode where BillingClientName like '%GPV Lanka%' 
                    and s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE())  AND ShipmentDate <= GETDATE() group by s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj54 = {
    'Question':"Could you provide the total outstanding balance for billing customers who listed MAS as the consignor over the last three months?",
    'SQLQuery':"""select s.BillingClientName as ClientName, Sum(s.Revenue_USD) as CurrentYearSalesUSD, Sum(r.OutStanding_USD) as OutstandingUSD 
                    from RevandVolume_ShipmentDate s 
                    inner join ReceivableWithCreditLimit r on r.Oh_code = s.BillingClientCode where s.ConsignorName like '%MAS Active%' 
                    and s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE())  AND ShipmentDate <= GETDATE() group by s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj55 = {
    'Question':"Can you provide the total outstanding of the billing customers who we worked with MAS as consignor in last 3 months?",
    'SQLQuery':"""select s.BillingClientName as ClientName, Sum(s.Revenue_USD) as CurrentYearSalesUSD, Sum(r.OutStanding_USD) as OutstandingUSD 
                    from RevandVolume_ShipmentDate s 
                    inner join ReceivableWithCreditLimit r on r.Oh_code = s.BillingClientCode where s.ConsignorName like '%MAS Active%' 
                    and s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE())  AND ShipmentDate <= GETDATE() group by s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj56 = {
    'Question':"Could you provide the total outstanding balance for billing customers who listed FLINTEC as the consignor over the last three months?",
    'SQLQuery':"""select s.BillingClientName as ClientName, Sum(s.Revenue_USD) as CurrentYearSalesUSD, Sum(r.OutStanding_USD) as OutstandingUSD 
                    from RevandVolume_ShipmentDate s 
                    inner join ReceivableWithCreditLimit r on r.Oh_code = s.BillingClientCode where s.ConsignorName like '%FLINTEC%' 
                    and s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE())  AND ShipmentDate <= GETDATE() group by s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj57 = {
    'Question':"Can you provide the total outstanding of the billing customers who we worked with Dipped Products as consignor in last 3 months?",
    'SQLQuery':"""select s.BillingClientName as ClientName, Sum(s.Revenue_USD) as CurrentYearSalesUSD, Sum(r.OutStanding_USD) as OutstandingUSD 
                    from RevandVolume_ShipmentDate s 
                    inner join ReceivableWithCreditLimit r on r.Oh_code = s.BillingClientCode where s.ConsignorName like '%MAS Active%' 
                    and s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE())  AND ShipmentDate <= GETDATE() group by s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj58 = {
    'Question':"Could you provide the total outstanding balance for billing customers who listed FLINTEC as the consignor over the last three months?",
    'SQLQuery':"""select s.BillingClientName as ClientName, Sum(s.Revenue_USD) as CurrentYearSalesUSD, Sum(r.OutStanding_USD) as OutstandingUSD 
                    from RevandVolume_ShipmentDate s 
                    inner join ReceivableWithCreditLimit r on r.Oh_code = s.BillingClientCode where s.ConsignorName like '%FLINTEC%' 
                    and s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE())  AND ShipmentDate <= GETDATE() group by s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj59 = {
    'Question':"Can you provide the total outstanding of the billing customers who we worked with Dipped Products as consignor in last 3 months?",
    'SQLQuery':"""select s.BillingClientName as ClientName, Sum(s.Revenue_USD) as CurrentYearSalesUSD, Sum(r.OutStanding_USD) as OutstandingUSD 
                    from RevandVolume_ShipmentDate s 
                    inner join ReceivableWithCreditLimit r on r.Oh_code = s.BillingClientCode where s.ConsignorName like '%MAS Active%' 
                    and s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) AND ShipmentDate <= GETDATE() group by s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj60 = {
    'Question':"Can you provide the total outstanding of the billing customers who we worked with Dipped Products as consignor in current year?",
    'SQLQuery':"""select s.BillingClientName as ClientName, Sum(s.Revenue_USD) as CurrentYearSalesUSD, Sum(r.OutStanding_USD) as OutstandingUSD 
                    from RevandVolume_ShipmentDate s 
                    inner join ReceivableWithCreditLimit r on r.Oh_code = s.BillingClientCode where s.ConsignorName like '%MAS Active%' 
                    and s.ShipmentDate >= DATEADD(yy, DATEDIFF(yy, 0, GETDATE()) - 1, -1)  AND ShipmentDate <= GETDATE() group by s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj61 = {
    'Question':"What is the total sales and outstanding balance for customers in the USA over the last year in a bar chart?",
    'SQLQuery':"""SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS TotalSalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD 
                    FROM RevandVolume_ShipmentDate s 
                    INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.CompanyCountryName = 'USA'  
                    AND s.ShipmentDate >= DATEADD(YEAR, -1, GETDATE()) GROUP BY s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj62 = {
    'Question':"Can you provide the revenue and outstanding amounts for shipments to Germany in the current financial year in a scatter plot?",
    'SQLQuery':"""SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS CurrentYearSalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD 
                    FROM RevandVolume_ShipmentDate s 
                    INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.DestCountry = 'Germany'  
                    AND s.ShipmentDate >= DATEADD(YEAR, DATEDIFF(YEAR, 0, GETDATE()), 0) GROUP BY s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj63 = {
    'Question':"What are the sales and outstanding balances for shipments that used air transport mode in the last six months?",
    'SQLQuery':"""SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS TotalSalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD 
                    FROM RevandVolume_ShipmentDate s 
                    INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.TransportMode = 'AIR' 
                    AND s.ShipmentDate >= DATEADD(MONTH, -6, GETDATE()) GROUP BY s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj64 = {
    'Question':"Can you give the total sales and outstanding value for clients based in Europe for shipments occurring in the last 2 months?",
    'SQLQuery':"""SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS SalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD 
                    FROM RevandVolume_ShipmentDate s 
                    INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.ClientContinent = 'Europe'  
                    AND s.ShipmentDate >= DATEADD(MONTH, -2, GETDATE()) GROUP BY s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj65 = {
    'Question':"What is the total revenue and outstanding amount for shipments to London in the last three months?",
    'SQLQuery':"""SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS RevenueUSD, SUM(r.OutStanding_USD) AS OutstandingUSD 
                    FROM RevandVolume_ShipmentDate s 
                    INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.DestCity = 'London'  
                    AND s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) GROUP BY s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj66 = {
    'Question':"Provide total sales and outstanding values for all shipments from Japan since the beginning of the current year.",
    'SQLQuery':"""SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS SalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD 
                    FROM RevandVolume_ShipmentDate s 
                    INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.OriginCountry = 'Japan'  
                    AND s.ShipmentDate >= DATEADD(YEAR, DATEDIFF(YEAR, 0, GETDATE()), 0) GROUP BY s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj67 = {
    'Question':"What are the sales and outstanding amounts for shipments to consignees in Canada over the last 12 months?",
    'SQLQuery':"""SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS SalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD 
                    FROM RevandVolume_ShipmentDate s 
                    INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.DestCountry = 'Canada'  
                    AND s.ShipmentDate >= DATEADD(MONTH, -12, GETDATE()) GROUP BY s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj68 = {
    'Question':"Can you show total sales and outstanding values for the shipping line 'Maersk' in the last three months?",
    'SQLQuery':"""SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS SalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD 
                    FROM RevandVolume_ShipmentDate s 
                    INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.ShipingLineName like '%Maersk%'  
                    AND s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) GROUP BY s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj69 = {
    'Question':"How much revenue and outstanding balances are associated with shipments carried via sea transport to Australia since last year?",
    'SQLQuery':"""SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS TotalSalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD 
                    FROM RevandVolume_ShipmentDate s  
                    INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.TransportMode = 'SEA' 
                    AND s.DestCountry = 'Australia'  AND s.ShipmentDate >= DATEADD(YEAR, -1, GETDATE()) GROUP BY s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj70 = {
    'Question':"How much revenue and outstanding balances are associated with shipments carried via sea transport to Australia since last year?",
    'SQLQuery':"""SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS TotalSalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD 
                    FROM RevandVolume_ShipmentDate s  
                    INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.TransportMode = 'SEA' 
                    AND s.DestCountry = 'Australia'  AND s.ShipmentDate >= DATEADD(YEAR, -1, GETDATE()) GROUP BY s.BillingClientName""",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj71 = {
    'Question' :"How much revenue and outstanding balances are associated with shipments carried via sea transport to Australia since last year?",
    'SQLQuery' : "SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS TotalSalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD FROM RevandVolume_ShipmentDate s  INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.TransportMode = 'SEA' AND s.DestCountry = 'Australia'  AND s.ShipmentDate >= DATEADD(YEAR, -1, GETDATE()) GROUP BY s.BillingClientName",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj72 = {
    'Question' : "What are the total sales and outstanding amounts for all shipments consigned by Jacobi carbons in the last six months?",
    'SQLQuery' : "SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS SalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD FROM RevandVolume_ShipmentDate s INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.ConsignorName like '%Jacobi carbons%'  AND s.ShipmentDate >= DATEADD(MONTH, -6, GETDATE()) GROUP BY s.BillingClientName",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj73 = {
    'Question' : "What are the sales and outstanding values for shipments from Europe to Asia in the last financial quarter?",
    'SQLQuery' : "SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS SalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD FROM RevandVolume_ShipmentDate s INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.OriginContinent = 'Europe' AND s.DestContinent = 'Asia'  AND s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) GROUP BY s.BillingClientName",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj74 = {
    'Question' : "What are the sales and outstanding values for shipments from Europe to Asia in the last financial quarter?",
    'SQLQuery' : "SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS SalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD FROM RevandVolume_ShipmentDate s INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.OriginContinent = 'Europe' AND s.DestContinent = 'Asia'  AND s.ShipmentDate >= DATEADD(MONTH, -3, GETDATE()) GROUP BY s.BillingClientName",
    'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj75 = {
    'Question' : "Provide the total sales and outstanding amounts for clients who used 'Dacsher' as their shipping agent in the last year.",
'SQLQuery' : "SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS SalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD FROM RevandVolume_ShipmentDate s INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.AgentName like '%Dacsher%' AND s.ShipmentDate >= DATEADD(YEAR, -1, GETDATE()) GROUP BY s.BillingClientName",
'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj76 = {
    'Question' : "Can you show total sales and outstanding amounts for all shipments to South America in the last 9 months?",
'SQLQuery' : "SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS TotalSalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD FROM RevandVolume_ShipmentDate s INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code = s.BillingClientCode WHERE s.DestContinent = 'South America'  AND s.ShipmentDate >= DATEADD(MONTH, -9, GETDATE()) GROUP BY s.BillingClientName",
'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj77 = {
    'Question' :"What is the total sales and outstanding balances for shipments handled by agents in the 'Global East Network' over the last month?",
'SQLQuery' :"SELECT s.BillingClientName AS ClientName, SUM(s.Revenue_USD) AS SalesUSD, SUM(r.OutStanding_USD) AS OutstandingUSD FROM RevandVolume_ShipmentDate s INNER JOIN ReceivableWithCreditLimit r ON r.Oh_code =  s.BillingClientCode WHERE s.AgentNetwork like '%WCA%'  AND s.ShipmentDate >= DATEADD(MONTH, -1, GETDATE()) GROUP BY s.BillingClientName",
'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj77 = {
    'Question' :"Give me the total outstanding of the agent group Flexport?",
'SQLQuery' : "SELECT SUM(OutStanding_USD) AS TotalOutstandingUSD  FROM ReceivableWithCreditLimit WHERE AgentGroup like '%Flexport%'",
'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj78 = {
    'Question' :"Give me the total outstanding of the agent group Flexport?",
'SQLQuery' : "SELECT SUM(OutStanding_USD) AS TotalOutstandingUSD  FROM ReceivableWithCreditLimit WHERE AgentGroup like '%Flexport%'",
'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj79 = {
   'Question' : "What is the total outstanding value more than 180 days for the Dart USA ?",
'SQLQuery' : "SELECT SUM(Days_180_More_Local) AS TotalOutstandingOver180Days FROM ReceivableWithCreditLimit WHERE CompanyCode= 'NYC' ",
'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj80 = {
   'Question' : "What is the total outstanding value more than 180 days for the Dart New York ?",
'SQLQuery' : "SELECT SUM(Days_180_More_Local) AS TotalOutstandingOver180Days FROM ReceivableWithCreditLimit WHERE CompanyCode= 'NYC' ",
'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj81 = {
   'Question' : "What is the total outstanding value more than 180 days for the Dart Viet Nam?",
'SQLQuery' : "SELECT SUM(Days_180_More_Local) AS TotalOutstandingOver180Days FROM ReceivableWithCreditLimit WHERE CompanyCode= 'VNM' ",
'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj82 = {
   'Question' : "What is the total outstanding value more than 180 days for the Dart India?",
'SQLQuery' : "SELECT SUM(Days_180_More_Local) AS TotalOutstandingOver180Days FROM ReceivableWithCreditLimit WHERE CompanyCode= 'IND' ",
'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj83 = {
  'Question' : "What is the total outstanding value more than 180 days for the Dart Indonesia?",
'SQLQuery': "SELECT SUM(Days_180_More_Local) AS TotalOutstandingOver180Days FROM ReceivableWithCreditLimit WHERE CompanyCode= 'IDN' ",
'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj84 = {
  'Question' : "What is the total outstanding value more than 180 days for the Dart Sri Lanka?",
'SQLQuery' : "SELECT SUM(Days_180_More_Local) AS TotalOutstandingOver180Days FROM ReceivableWithCreditLimit WHERE CompanyCode= 'CMB' ",
'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

obj85 = {
'Question' : "What is the total outstanding value more than 180 days for the Dart Colombo?",
'SQLQuery' : "SELECT SUM(Days_180_More_Local) AS TotalOutstandingOver180Days FROM ReceivableWithCreditLimit WHERE CompanyCode= 'CMB' ",
'SQLResult' : "Result of the SQL query",
    'Answer' : ""
}

few_shots = [obj1,obj2,obj3,obj4,obj5,obj6,obj7,obj8,obj9,obj10,
             obj11,obj12,obj13,obj14,obj15,obj16,obj17,obj18,obj19,obj20,
             obj21,obj22,obj23,obj24,obj25,obj26,obj27,obj28,obj29,obj30,
             obj31,obj32,obj33,obj34,obj35,obj36,obj37,obj38,obj39,obj40,
             obj41,obj42,obj43,obj44,obj45,obj46,obj47,obj48,obj49,obj50,
             obj51,obj52,obj53,obj54,obj55,obj56,obj57,obj58,obj59,obj60,
             obj61,obj62,obj63,obj64,obj65,obj66,obj67,obj68,obj69,obj70,
             obj71,obj72,obj73,obj74,obj75,obj76,obj77,obj78,obj79,obj80,
             obj81,obj82,obj83,obj84,obj85]