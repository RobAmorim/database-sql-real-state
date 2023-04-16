import insert_data 
from queries import top_5_offices, top_5_agents, calculate_comssion, average_days_on_market, average_price


#TOP 5 OFFICES 
result = top_5_offices(4, 2023)
print("Rank of the 5 Offices with more Sales in April of 2023")
for i, data in enumerate(result):
    print(i + 1, data.Office.name, f'${data[1]}')

print("\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

#TOP 5 AGENTS 
result = top_5_agents(4, 2023)
print("Rank of the 5 Agents with more Sales in April of 2023")
for i, data in enumerate(result):
    print(i + 1, data.EstateAgent.name, data.EstateAgent.phone, data.EstateAgent.email, f'${data[1]}')
print("\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")


#Agents Commision
calculate_comssion(4, 2023)
print("\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")


#AVERAGE DAYS ON THE MARKET
print("Average amount of days for a houses to be sold in April of 2023 = ", average_days_on_market(4, 2023)) 
print("\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
#Average Sell Price 
print("Average sell price in April 2023 = ", f'${int(average_price(4, 2023))}')  
print("\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")






