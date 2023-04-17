import insert_data 
from queries import top_5_offices, top_5_agents, calculate_comssion, average_days_on_market, average_price

#Month Period
month = 4 
year = 2023

#TOP 5 OFFICES 
result = top_5_offices(month, year)
print("Rank of the 5 Offices with more Sales in the month")
for i, data in enumerate(result):
    print(i + 1, data.Office.name, f'${data[1]}')

print("\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

#TOP 5 AGENTS 
result = top_5_agents(month, year)
print("Rank of the 5 Agents with more Sales in the month")
for i, data in enumerate(result):
    print(i + 1, data.Agent.name, data.Agent.phone, data.Agent.email, f'${data[1]}')
print("\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")


#AGENTS COMISSION
calculate_comssion(month, year)
print("\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")


#AVERAGE DAYS ON THE MARKET
print("Average amount of days for a houses to be sold in the month = ", average_days_on_market(month, year)) 
print("\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

#Average Sales Price 
print("Average sell price in the month = ", f'${int(average_price(month, year))}')  
print("\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")






