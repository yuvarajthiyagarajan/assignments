#function to define the resource allocator
def resourceAllocator(no_of_hours, capacity_to_run):
	country_list = ['New York', 'India', 'China']
	output = []
	ret_dict = {}

	#Cost per hour for running machines across the countries.
	new_york_cost = {'Large': 120, 'XLarge': 230, '2XLarge': 450, '4XLarge': 774, '8XLarge': 1400, '10XLarge': 2820}
	india_cost = {'Large': 140, 'XLarge': None, '2XLarge': 413, '4XLarge': 890, '8XLarge': 1300, '10XLarge': 2970}
	china_cost = {'Large': 110, 'XLarge': 200, '2XLarge': None, '4XLarge': 670, '8XLarge': 1180, '10XLarge': None}
	
	for country in country_list:
		cap_req = {}
		sol_key = 'method'
		sol_val = 0

		#Capcity of each machines based on the units it can run.
		capacity_per_machines = {'Large': 10, 'XLarge': 20, '2XLarge': 40, '4XLarge': 80, '8XLarge': 160, '10XLarge': 320}
		
		# Deleting the Machine from the dictionary of machines which doesn't have a cost of value in the list.
		if country == 'India':
			del capacity_per_machines['XLarge'] 
		elif country == 'China':
			del capacity_per_machines['2XLarge']
			del capacity_per_machines['10XLarge']

		# Iterating through the machines to find the cost of the capacity which is minimum

		for cap in capacity_per_machines:

			temp = capacity_to_run % capacity_per_machines[cap]
			if temp == 0:
				sol_val += 1
				#Adding each different probability of cases into a dictionary for finding the best allocation
				cap_req[sol_key+str(sol_val)] = {cap:capacity_to_run / capacity_per_machines[cap]}
			else:
				sol_val += 1
				# Second loop to further reducing the cost to multiple machine with varios no. of units		
				for cap2 in capacity_per_machines:
					if temp >= capacity_per_machines[cap2]:
						
						temp2 = temp % capacity_per_machines[cap2]
						if temp2 == 0:
							cap_req[sol_key+str(sol_val)] = {cap:(capacity_to_run - temp) / capacity_per_machines[cap], cap2:temp / capacity_per_machines[cap2]}
						else:
							# Running through the third loop for iterating the till the no. of machine meets the capacity to run for the given hours
							for cap3 in capacity_per_machines:
								if temp2 >= capacity_per_machines[cap3]:
									temp3 = temp2 % capacity_per_machines[cap3]
									if temp3 == 0:
										cap_req[sol_key+str(sol_val)] = {cap:(capacity_to_run - temp) / capacity_per_machines[cap], 
																		cap2:(temp - temp2) / capacity_per_machines[cap2],
																		cap3:temp2 / capacity_per_machines[cap3]}
									else:
										None
		best_method = ''
		cost_eff_cap = 0
		multiplier = 0
		# Iterating through the possible methods to find the best method
		for methods in cap_req:
			sum_of_vals = 0
			for met in cap_req[methods]:
				if country == 'New York':
					multiplier = new_york_cost[met]
				elif country == 'India':
					multiplier = india_cost[met]
				elif country == 'China':
					multiplier = china_cost[met]
				# Formula to summing the values of each machine in the method and multiplied with given hours and the cost in the region per hour
				sum_of_vals = (multiplier * no_of_hours * cap_req[methods][met]) + sum_of_vals

			if sum_of_vals < cost_eff_cap or cost_eff_cap == 0:
				cost_eff_cap = sum_of_vals
				best_method = methods

		machines = [] #Empty list to add each machines in each region
		total_cost = '$'+str(int(cost_eff_cap))
		for machine in cap_req[best_method]:
			# Appending each region machines into the list of machines across the regions
			machines.append(tuple((machine, int(cap_req[best_method][machine]))))
		
		# Appending all the values like region, totals, machines list to the dictionary
		output.append({"region": country, "total_cost": total_cost, "machines": str(machines)})

	ret_dict = {"Output": output}
	
	return ret_dict
