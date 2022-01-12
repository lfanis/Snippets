# These can be changed to match whatever is required by your case. Unfortunatly the values i use are of no use if you do not live in the same area as i do / have the same type of expenses
# TODO
# - Pension value should be pulled up automatically via API
# - House valuation pulled automatically
# - Divident/investments pulled from deGiro/trade212 via API etc..
# - get credit card full statement API?
# - Get amazon purchases?
# - get paypal purchases?

## Wants are assume to be anything not in Needs nor in Investments 
category_in_Budget = {'Needs': {'Groceries','Mortgage','Health Insurance','Health Addition cost', 
                        'House Insurance','House DIY','House Maintenance','Utilities Gas and Electricity','Utilities Water','Utilities City Hall, ground,  Trash','House taxes' ,
                        'Car Payment','Car Fuel','Car Maintenance','Car Insurance','Car taxes'
                        },
                        'Wants':{},
                        'Investment':{'Investments','Savings'}}

card_owner = {'PERSON1':{'PAS111','PAS112'},
                'PERSON2':{'PAS220','PAS221'}
                }

shops_in_category = {
        'Salary' : {'MEGACORP'},
        'Dividends' : {'DIVIDEND MEGACORP'},
        'IBusiness' : {},
        'Refunds' : {},
        'Pension' : {},
        'OtherIncome' : {},
        'Investments' : {'Robeco','Traded212','DeGiro'},
        'Savings' : {'Move to saving','Pulled for use'} ,
        'Pulled from savings': {'move to use'},
        'Taxe Services' : {'TAX SERVICES CO'},
        'Health Insurance' : {},
        'Health Addition cost' : {},
        'Mortgage' : {},  
        'Paperwork': {},
        'Rent' : {},        
        'Insurances' :{},
        'House Insurance' : {},
        'House Maintenance' : {},
        'House Improvement' : {'IKEA '},
        'House DIY': {},
        'Cash out':{},
        'Credit Card':{'ICS-klantnummer'},
        'Utilities Gas and Electricity' : {},
        'Utilities Water' : {},
        'Utilities City Hall, ground,  Trash' : {},
        'House taxes' : {},
        'Utilities Internet and Phone' : {},
        'Utilities Banking' : {},
        'Car Payment' : {},
        'Car Insurance' : {},
        'Car Fuel' : {},
        'Car Maintenance' : {'ANWB B.V.'},
        'Car Registrations Licences' : {},
        'Car taxes' : {},
        'Car additional cost, eg parking' : {},
        'Educational' : {},
        'Public Transport' : {},
        'Dinning Out' : {},
        'Groceries' : {},
        'Gifts' :{},
        'Clothing' : {},
        'Health and Beauty Shops' : {},
        'Pet' : {},
        'Entertainment Media' : {'GOG Sp','Humble Bundle','Steampowered'},
        'Entertainment Outside' : {},
        'Entertainment Hobby' : {},
        'Fitness':{},
        'Vacation In an Exotic place':{},
        'Unknown and or minor catch all': {}
}
