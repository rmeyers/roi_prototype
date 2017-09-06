# -*- coding: utf-8 -*-

inputs_data = {

    # *** PROJECT DETAILS ***
    'project': [{'var': 'project_name',
                 'type': 'text',
                 'name': 'Project Name',
                 'placeholder': '',
                 'value': 'Academic Facility Proposal',
                 'comment': 'A new biology research lab',
                 'tooltip': 'Input the name of this project.'},
                {'var': 'start_date',
                 'type': 'date',
                 'name': 'Project Life - Start Date',
                 'placeholder': '',
                 'value': '2018-01-01',
                 'comment': '',
                 'tooltip': 'Date when this project will commence its operating \
                 life.'},
                {'var': 'end_date',
                 'type': 'date',
                 'name': 'Project Life - End Date',
                 'placeholder': '',
                 'value': '2048-01-01',
                 'comment': '',
                 'tooltip': 'Date when this project will complete its operating \
                 life.'},
                {'var': 'originator',
                 'type': 'text',
                 'name': 'Project Originator',
                 'placeholder': '',
                 'value': 'Bob Willard',
                 'comment': 'In partnership with Ryan Meyers.',
                 'tooltip': 'Name of the individual who is heading up this \
                 proposal.'},
                {'var': 'department',
                 'type': 'text',
                 'name': 'Department',
                 'placeholder': '',
                 'value': 'Life Sciences',
                 'comment': '',
                 'tooltip': 'Name of the department that is responsible for this \
                 proposal.'},
                {'var': 'phone',
                 'type': 'tel',
                 'name': 'Phone Number',
                 'placeholder': '',
                 'value': '647-888-9999',
                 'comment': '',
                 'tooltip': 'Phone number for the primary contact of this \
                 proposal.'},
                {'var': 'location',
                 'type': 'text',
                 'name': 'Project Location',
                 'placeholder': '',
                 'value': 'Markham, Ontario, Canada',
                 'comment': '',
                 'tooltip': 'Location of the project being constructed.'}],

    # *** OPERATING COSTS ***


    'opex': [{'var': 'energy',
              'name': 'Savings on energy expenses',
              'cur_exp_tooltip': """Description:
               This is the total cost of electricity and fuel used by the company,
               including the cost of any renewable energy used.
               Estimation guidance: This cost is usually accounted for in general
               operating
               and overhead expenses" within Selling, General and Administrative
               (SG&A) expenses in the annual report. If they are available, utility
               bills may be helpful in identifying this expense. Depending on
               company size and sector, Energy expenses" are typically equivalent
               to 1% to 15% of revenue. For services companies, the percentage will
               be at the low end of the range; for manufacturing companies, it will
               be at the high end of the range. If this value is not known or
               available, edit this comment box to document your estimation logic
               and sources, for later verification. """,
              'cur_exp_type': 'number', 'cur_exp_value': 2107.81,
              'percent_tooltip': """Description: The potential percentage r""",
              'percent_type': 'text', 'percent_value': '24.4%',
              'percent_placeholder': '', 'comment': ''},
             {'var': 'carbon',
              'name': 'Savings on carbon expenses',
              'cur_exp_tooltip': """Description: This is the total cost to """,
              'cur_exp_type': 'number', 'cur_exp_value': 14461.79,

              'percent_tooltip': """Description: The potential percentage r""",
              'percent_type': 'text', 'percent_value': '74.6%',
               'comment': ''},
             {'var': 'shipping',
              'name': 'Savings on shipping / transportation expenses',
              'cur_exp_tooltip': """Description: These are expenses incurre""",
              'cur_exp_type': 'number', 'cur_exp_value': 81176.36,
              'percent_tooltip': """Description: The potential percentage r""",
              'percent_type': 'text', 'percent_value': '47.3%',
               'comment': ''},
             {'var': 'bus_travel',
              'name': 'Savings on business travel expenses',
              'cur_exp_tooltip': """Description: This is the cost of employ""",
              'cur_exp_type': 'number', 'cur_exp_value': 54036.22,
              'percent_tooltip': """Description: The potential percentage r""",
              'percent_type': 'text', 'percent_value': '76.8%',
               'comment': ''},
             {'var': 'maint',
              'name': 'Savings on maintenance expenses',
              'cur_exp_tooltip': """Description: This is the cost of parts """,
              'cur_exp_type': 'number', 'cur_exp_value': 50940.29,
              'percent_tooltip': """Description: The potential percentage r""",
              'percent_type': 'text', 'percent_value': '75.2%',
               'comment': ''},
             {'var': 'materials',
              'name': 'Lower materials expenses ',
              'cur_exp_tooltip': """Description: This the total cost of all""",
              'cur_exp_type': 'number', 'cur_exp_value': 1680.31,
              'percent_tooltip': """Description: The potential percentage r""",
              'percent_type': 'text', 'percent_value': '32%',
               'comment': ''},
             {'var': 'water',
              'name': 'Lower water expenses',
              'cur_exp_tooltip': """Description: This is the total cost of """,
              'cur_exp_type': 'number', 'cur_exp_value': 58259.95,
              'percent_tooltip': """Description: The potential percentage r""",
              'percent_type': 'text', 'percent_value': '86.9%',
               'comment': ''},
             {'var': 'waste',
              'name': 'Lower waste disposal expenses',
              'cur_exp_tooltip': """Description: This is the cost of waste """,
              'cur_exp_type': 'number', 'cur_exp_value': 712.67,
              'percent_tooltip': """Description: The potential percentage r""",
              'percent_type': 'text', 'percent_value': '40.4%',
               'comment': ''},
             {'var': 'insurance',
              'name': 'Lower insurance premiums ',
              'cur_exp_tooltip': """Definition: This is the cost premiums p""",
              'cur_exp_type': 'number', 'cur_exp_value': 39827.45,
              'percent_tooltip': """Description: The potential percentage r""",
              'percent_type': 'text', 'percent_value': '43.9%',
               'comment': ''},
             {'var': 'litigation',
              'name': 'Lower litigation expenses ',
              'cur_exp_tooltip': """Definition: This is the cost of fightin""",
              'cur_exp_type': 'number', 'cur_exp_value': 23409.72,
              'percent_tooltip': """Description: The potential percentage r""",
              'percent_type': 'text', 'percent_value': '19.3%',
               'comment': ''},
             {'var': 'compliance',
              'name': 'Lower compliance expenses ',
              'cur_exp_tooltip': """Definition: This is the cost of complyi""",
              'cur_exp_type': 'number', 'cur_exp_value': 67243.25,
              'percent_tooltip': """Description: The potential percentage r""",
              'percent_type': 'text', 'percent_value': '16.5%',
               'comment': ''},
             {'var': 'other',
              'name': '(Lower cost of other expense?) ',
              'cur_exp_tooltip': """Definition: This is the cost of complyi""",
              'cur_exp_type': 'number', 'cur_exp_value': 52447.95,
              'percent_tooltip': """Description: (Complete appropriately)""",
              'percent_type': 'text', 'percent_value': '16.5%',
               'comment': ''}]
        }

# """,'percent_type': 'text','percent_value': '50.7%%',cur_exp_value': '',comment': '',},"
#     'name': 'energy', 'cur_exp_tooltip': """Description:
#                 This is the total cost of electricity and fuel used by the company,
#                 including the cost of any renewable energy used.
#                 Estimation guidance: This cost is usually accounted for in general
#                 operating
#                 and overhead expenses" within Selling, General and Administrative
#                 (SG&A) expenses in the annual report. If they are available, utility
#                 bills may be helpful in identifying this expense. Depending on
#                 company size and sector, Energy expenses" are typically equivalent
#                 to 1% to 15% of revenue. For services companies, the percentage will
#                 be at the low end of the range; for manufacturing companies, it will
#                 be at the high end of the range. If this value is not known or
#                 available, edit this comment box to document your estimation logic
#                 and sources, for later verification. """, 'cur_exp_type': 'number',
#                 'cur_exp_value': 2107.81975095663,
#                 'percent_tooltip': """Description: The potential percentage
#                 reduction of the company's energy bills for electricity and
#                 fuel, as a direct or indirect result of the project.
#                 Context: Projects may reduce electricity and fuel used for
#                 lighting, heating and cooling, pumps and motors, equipment
#                 used in various processes, IT, travel, and transportation.
#                 Efficiencies usually come from a combination of changes in
#                 employee behavior, more energy-efficient technologies, and
#                 green building retrofits.
#                 Switching from fossil fuels to renewable energy to reduce
#                 the company's cost for its carbon footprint (see below) may
#                 also reduce the company's energy expense. As renewable
#                 energy costs plummet, any premium that used to be paid for
#                 renewable energy disappears. So, switching to new
#                 technologies (e.g. cogeneration, energy efficient equipment),
#                 upgrading insulation, and converting to renewable energy
#                 sources (e.g. solar, wind, geothermal, co-generation) may
#                 lower energy costs.
#                 Possibilities:
#                 Veriform, a small metal fabricating company in Ontario,
#                 used 42 projects to reduce its electricity usage by 58%
#                 and its natural gas usage by 90% in just 3 years, with an
#                 average payback period of 6.3 months for each initiative.
#                 As a direct result of these savings, it increased its profits
#                 by 76%. — "Manufacturer finds lighting energy efficiency
#                 convenient," Green Manufacturer, March 1, 2010 —
#                 * 53 of the Fortune 100 companies have collectively saved
#                 $1.1B annually and reduced their yearly CO2 emissions by
#                 more than 58M metric tonnes. For example, UPS saves $200M
#                 / year; Cisco Systems saves $151M / year; PepsiCo saves
#                 $120M / year; United Continental saves $104M / year; General
#                 Motors saves $73M / year; and IBM saved $34M / year by
#                 cutting energy consumption 6.4% / year between 2009-2012.
#                 — "Power Forward, How American Companies Are Setting Clean
#                 Energy Targets and Capturing Greater Business Value," report
#                 by Ceres, WWF, Calvert Investments, and David Gardiner &
#                 Associates, June 2014 —
#                 * Walmart saved $1M / year by removing light bulbs from soft
#                 drink machines in employee break rooms; it saved $2.6M /
#                 year by putting low-lead LEDs in freezers; and Walmart Canada
#                 saved $70M between 2010-2015 using low-wattage light bulbs,
#                 energy-efficient cooling systems, and solar panels. — "Walmart
#                 Will Increase Use of Renewables 600% Over 2010 Levels," Energy
#                 Manager Today, April 2013 —
#                 * Indoor and outdoor LED retrofits at Marriott International’s
#                 HQ in Bethesda, Md., will reduce electricity use by 66%, and
#                 save $120,000 / year in energy and maintenance costs, with a
#                 payback period of 2 years.  Energy expense savings will be
#                 $104,000 per year,  and maintenance mitigation will save
#                 another $210,000 over the decade. — "Marriott Headquarters’
#                 LED Retrofit to Save $120,000 Annually, Deliver 2-Year ROI,"
#                 Environmental Leader, April 2012 —
#                 * Energy savings may become >100% if the company provides its
#                 own on-site renewable energy, produces more energy than it
#                 needs, and sells its excess energy to the local utility or
#                 neighboring organizations. It transforms an expense to a
#                 revenue stream that goes straight to the bottom line.  —
#                 "Selling Power Back to the Grid," Bloomberg.com, July 6, 2006 —
#                 Estimation guidance: The ""% Change"" could be quite high, as
#                 indicated above, for companies in the manufacturing,
#                 distribution, and retail sectors because they typically
#                 have high energy bills. Companies in the service sector may
#                 find that there are fewer potential savings opportunities. Use
#                 this comment box to document assumptions behind your
#                 estimate. """, 'percent_type': 'text',
#                 'percent_value': '24.4%', 'percent_placeholder': '',
#                 'comment': ''}]
#     }

# mystring = inputs_data['opex'][0]['cur_exp_tooltip']
# try:
#     mystring.decode('ascii')
# except UnicodeDecodeError:
#     print "it was not a ascii-encoded unicode string"
# else:
#     print "It may have been an ascii-encoded unicode string"

#                 "{'name': 'carbon','cur_exp_tooltip': """
# Description: This is the total cost to the company for its carbon footprint.

# Context: A carbon expense is incurred because of either a carbon tax or a cap-and-trade approach in the jurisdiction in which the company operates, and from the purchase of carbon offsets by the company. Even if the company is not subject to a price on carbon today, 1,200+ companies have plans to, or currently, place a price on their carbon emissions as an approach to managing carbon risk, and 140+ of these companies are  embedding a carbon price deeper within business strategies and operations to help take tangible action on climate change. —  ""Embedding a carbon price into business strategy,"" CDP, September 2016 —

# Possibilities: If the value is not known it might be able to be estimated using an  analysis of ""carbon productivity"" for the S&P/TSX 60 which revealed an average of $3,361 of revenue per ton of carbon.
#  — Madelaine Drohan, ""Big country, small steps,"" Corporate Knights, Issue 35, Spring 2011 —

# This equates to 298 tons per $1 million of revenue, or approximately 300 tons of carbon / $1 million of revenue, as a rough rule of thumb. Multiply this estimated carbon footprint by the current cost of carbon in the jurisdiction in which the company operates. For example, if you assume that the price of carbon is $10 per tonne and use the above estimation approach, the cost of carbon = $10 / tonne X ( $millions of revenue X 300 tonnes per $million of revenue).

# Estimation guidance: If this value is not known, available, or is estimated using the above approach, edit this comment box to document your estimation logic and sources, for later verification. """,'cur_exp_type': 'number','cur_exp_value': 14461.792374299,cur_exp_value': '','percent_tooltip': '
# Description: The potential percentage reduction of the company's cost of carbon, as a direct or indirect result of the project.

# Context: This expense includes carbon taxes or payments through a cap-and-trade mechanism in jurisdictions in which the company operates, purchases of carbon offsets, and purchases of renewable energy credits (RECs). If the company is not subject to a price on carbon today, this could be an estimate of what the cost would be if a price on carbon were implemented in its jurisdiction. Otherwise, assume the cost of carbon today is zero.

# There are two ways that a company can reduce the cost of its carbon footprint.
# 1. Reduce the amount of energy from fossil fuels used in its value chain. That is, conserve energy sourced from fossil fuels, reduce travel, etc. (see ""Savings on Energy Expenses"" comment, above). The less fossil fuel energy that is used, the lower the carbon expense, the cost of offsets, and the cost of RECs.
# 2. Replace any remaining fossil fuel used with renewable energy. Switching from fossil fuels to renewable energy (e.g. solar, wind, geothermal, co-generation) reduces the company's carbon footprint and associated carbon expenses.

# Possibilities:
# * RE100 is a collaborative effort of the Carbon Disclosure Project (CDP), the International Renewable Energy Agency (IRENA), and the Climate Group. As of August 2017, over 100 brand name companies have made a commitment to go '100% renewable.' — See re100.org —  If there is no biomass in the renewable energy mix, they will be carbon neutral when they reach their goal and will have eliminated any cost of carbon.

# * Carbon savings may become >100% if the company provides its own on-site renewable energy and generates carbon credits that it sells to other companies. It transforms an expense to a revenue stream that goes straight to the bottom line. — ""Selling Power Back to the Grid,"" Bloomberg.com, July 6, 2006 —

# Estimation guidance:  The percentage reduction in carbon expense should correlate well with the percentage reduction in energy expenses, above. The ""% Change"" could be quite high for companies in the extractive and manufacturing sectors because they typically have high carbon footprints. Companies in the service sector may find that there are fewer potential savings opportunities. Use this comment box to document assumptions behind your estimate.','percent_type': 'text','percent_value': '74.6%%',cur_exp_value': '',comment': '',},"
# "{'name': 'shipping','cur_exp_tooltip': """
# Description: These are expenses incurred by the company to ship its goods from its suppliers to company locations, between company locations, and between company facilities and distribution centers and retail outlets.

# Context: As companies reconfigure their value chains to avoid risks of disruptions caused by climate destabilization, and support the local economy by buying from local suppliers and selling to more local customers, shipping and transportations expenses may be reduced as distances are reduced.

# Estimation guidance: For companies in the manufacturing and retail sectors, this may be a relatively significant expense; for companies in the service sector, it could be less significant. We are not aware of any rules of thumb for estimating what this expense might be. If this value is not known or available, edit this comment box to document your estimation logic and sources, for later verification. """,'cur_exp_type': 'number','cur_exp_value': 81176.3655758421,cur_exp_value': '','percent_tooltip': '
# Description: The potential percentage reduction in shipping and transportation expenses for which the company is responsible, as a direct or indirect result of the project.

# Context: Shipping and transportation expenses may be reduced as companies reconfigure their supply chains to avoid risks of disruptions from climate change and social unrest, use less carbon intensive modes of transportation, use more local suppliers and foster local customers.

# Possibilities:
# By the end of 2014, Wal-Mart used better routing, truck loading, driver training, and advanced technologies to improve fuel efficiency by 87% compared to a 2005 baseline, resulting in 15,000 metric tons of CO2 emissions avoided and savings of nearly $11 million. — Tensie Whelan and Carly Fink, "The Comprehensive Business Case for Sustainability," Harvard Business Review, October 2016 —

# Estimation guidance: The ""% Change"" could be worth recording for companies in the manufacturing, distribution, and retail sectors because they typically have higher shipping costs. Companies in the service sector may find that there are few, if any, potential savings opportunities. Use this comment box to document assumptions behind your estimate. ','percent_type': 'text','percent_value': '47.3%%',cur_exp_value': '',comment': '',},"
# "{'name': 'bus_travel','cur_exp_tooltip': """
# Description: This is the cost of employee business trips.

# Context: These expenses include the cost of air and train fares, taxis, hotels, meals, and incidentals for employees' business trips.

# Estimation guidance: For companies in the service sector, this may be a relatively significant expense; for companies in the manufacturing sector, it could be less significant.  We are not aware of any rules of thumb for estimating what this expense might be. If this value is not known or available, edit this comment box to document your estimation logic and sources, for later verification. """,'cur_exp_type': 'number','cur_exp_value': 54036.2215796982,cur_exp_value': '','percent_tooltip': '
# Description: The potential percentage reduction in the total amount spent by the company on employee business-related trips, as a direct or indirect result of the project.

# Context: Travel expenses are one of the top two cost-cutting measures by companies in difficult economic times – the other is employee education and training. Savings on travel expenses (air and train fares, taxis, hotels, meals, and incidentals) are also a happy by-product of efforts to use more local supply and customer chains. Efforts to improve employee engagement and productivity by substituting virtual meetings for many face-to-face meetings also reduce travel costs. As customers become more local and as virtual meetings become more effective, travel budgets could be slashed dramatically. Breakthroughs in ""beam me up"" holography technology would also help.  ☺

# Estimation guidance: The ""% Change"" could be quite high for services companies, especially consulting companies with distant clients. For companies in the manufacturing, distribution, and retail sectors, it would probably be less. Use this comment box to document assumptions behind your estimate.','percent_type': 'text','percent_value': '76.8%%',cur_exp_value': '',comment': '',},"
# "{'name': 'maint','cur_exp_tooltip': """
# Description: This is the cost of parts and labor to keep machinery and equipment in good working order.

# Context: It includes unscheduled and scheduled preventative maintenance costs for mechanical, plumbing and electrical devices.

# Estimation guidance: This may be available in annual reports. For companies in the service sector, this may be a relatively minor expense and may not be worth including. For companies in the manufacturing sector, it could be more significant and worth sizing with help from company labor and repair accounts. We are not aware of any rules of thumb for estimating what this expense might be. If this value is not known or available, edit this comment box to document your estimation logic and sources, for later verification. """,'cur_exp_type': 'number','cur_exp_value': 50940.2909523847,cur_exp_value': '','percent_tooltip': '
# Description: The potential percentage reduction in the company's building and equipment maintenance bills, as a direct or indirect result of the project.

# Context: The cost of parts and labor required to maintain green buildings and equipment is reduced as a by-product of efforts to reduce energy and carbon footprints. Maintenance savings after green building retrofits are usually greater than energy expense savings. CFL and LED lighting has a longer life so require less maintenance. New, more energy efficient equipment may also require less preventative maintenance. Equipment and appliances are turned off when not in use, reducing wear and tear.

# The savings could be surprisingly high – they could be in the range of the savings in electricity (not all energy) expenses. In some sectors, maintenance expenses as a separate line item could approach zero, especially for leased facilities and equipment under contracts that include regular preventative maintenance.

# Estimation guidance: The ""% Change"" could be quite high for companies in the manufacturing, distribution, and retail sectors because they have more equipment and appliances to maintain. It would probably be less for companies in the service sector. Use this comment box to document assumptions behind your estimate.','percent_type': 'text','percent_value': '75.2%%',cur_exp_value': '',comment': '',},"
# "{'name': 'materials','cur_exp_tooltip': """
# Description: This the total cost of all materials used by the company to produce its products and to provide its services.

# Context: The materials may be virgin, recycled, or within subassemblies produced for the company by its supply chains.

# Estimation guidance: Depending on company size and sector, ""Materials expense"" is usually equivalent to 5% to 35% of revenue. For services companies, it will be at the low end of the range; for manufacturing companies, it will be at the high end of the range.  If this value is not known or available, edit this comment box to document your estimation logic and sources, for later verification. """,'cur_exp_type': 'number','cur_exp_value': 1680.31403968459,cur_exp_value': '','percent_tooltip': '
# Description: The potential percentage reduction in the company's cost of product input materials, as a direct or indirect result of the project.

# Context:
# The company can reduce the quantity and cost of materials used for products and packaging through dematerialization, substitution, recycling on-site waste, and product take-back. The materials that it still requires derive from sources that respect the welfare of ecosystems, people and animals.

# As part of its efforts to improve customer wellbeing, the company may use less packaging and healthier materials that are less expensive. In a circular economy, non-renewable materials are from recycled sources and renewable materials are sustainably harvested.

# The cost of materials can be affected by climate change impacts on natural resources, on supplier operations in the value chain, and on transportation routes in the supply chain. Prices may rise if climate change causes shortages of renewable materials from crops destroyed by severe weather events and shortages of non-renewable materials that are more difficult to access because of the impacts of severe weather events (e.g. wildfires, floods, or severe storms that destroy facilities at extraction locations).

# As part of their climate change adaptation efforts, smart companies reconfigure their supply chains to anticipate these temporary or permanent severe weather-related disruptions. They may find that their materials costs are lower if they make these backup changes and substitutions in a planned and strategic way, since they are able to avoid expensive alternate arrangements made in the heat of an emergency materials shortage when their bargaining position would be weaker.

# Estimation guidance: The ""% Change"" could be quite high for companies in the manufacturing, distribution, and retail sectors because they require materials for their products. For companies in the service sector, this saving would be minimal and not be worth including. Use this comment box to document assumptions behind your estimate.','percent_type': 'text','percent_value': '32%%',cur_exp_value': '',comment': '',},"
# "{'name': 'water','cur_exp_tooltip': """
# Description: This is the total cost of water used by the company.

# Context: It is usually lumped into ""Utilities"" in ""general operating and overhead expenses"" within Selling, General and Administrative (SG&A) expenses in the companies annual report, so it may not be readily available. Water is usually a low expense unless the company is in water-intensive industry sector like beverages or agriculture, or the company is operating in a high water-risk area.

# Estimation guidance: We not aware of any rules of thumb for estimating what this expense might be. If this value is not known or available, edit this comment box to document your estimation logic and sources, for later verification.""",'cur_exp_type': 'number','cur_exp_value': 58259.9501948612,cur_exp_value': '','percent_tooltip': '
# Description: The potential percentage reduction in the company's cost of water, as a direct or indirect result of the project.

# Context: The total cost of water includes the cost of water purchases from municipal supply or elsewhere, the cost of pre-treating water before it used, the cost of treating waste water before it is discharged, and charges for use of municipal sewer infrastructure to treat water after it is discharged from the company facilities.

# The cost of water can be affected by severe weather events caused by climate change. Sources of supply can be made temporarily or permanently unusable because of flooding and other storm damage, or droughts. As part of their climate change adaptation efforts, smart companies reconfigure their water supply chains to anticipate these temporary or permanent disruptions.

# Possibilities:
# Technological initiatives and conservation efforts reduce the amount of water used to clean facilities and equipment, used for employee sanitation, lost through evaporation, and embedded within products.

# * PepsiCo’s Frito-Lay snacks facility in Casa Grande, Arizona, recycles 75% of process water, reducing its annual water use by 100 M gallons. PepsiCo’s water conservation efforts saved the company more than $80M between 2011-2015. It accomplished this with increased efficiencies (fixing leaks, recycling, reusing) and new waste water treatment technologies (biological treatments, capacitive deionization and forward osmosis).  — "How PepsiCo Saved $80 Million by Cutting Water Use 26%," Environmental Leader, September 2016 —

# * Coca-Cola had a 27% improvement in water efficiency since 2004.  It has a 2020 goal to improve water efficiency in manufacturing operations by 25%, compared with a 2010 baseline. — ""Coca-Cola CEO: Reducing Water Use Inside Our Operations Isn’t Enough,"  Environmental Leader, August 2016  —

# * Since 1994, Dow has invested nearly $2 billion in improving resource efficiency and has saved $9.8 billion from reduced energy and wastewater consumption in manufacturing.  By 2013, GE had reduced greenhouse gas emissions by 32% and water use by 45% compared to 2004 and 2006 baselines, respectively, resulting in $300 million in savings. — Tensie Whelan and Carly Fink, "The Comprehensive Business Case for Sustainability," Harvard Business Review, October 2016 —

# * GM Detroit-Hamtramck Assembly will save nearly $2 M annually by reusing captured rainwater for manufacturing processes. GM expects to see a return on investment in a little over a year. The process eliminates over 20% of the plant’s water bill and saves over $140,000 annually in storm water discharge fees from the city of Detroit. Those fees made up 14% of the entire plant’s utility budget. — "GM Plant Will Save Millions of Dollars by Capturing Rainwater," Environmental Leader, August 2016 —

# Estimation guidance: The ""% Change"" could be quite high for companies in the agriculture, manufacturing, and retail sectors which use a lot of water. For companies in the service sector, this saving would be minimal and not be worth including. Use this comment box to document assumptions behind your estimate.','percent_type': 'text','percent_value': '86.9%%',cur_exp_value': '',comment': '',},"
# "{'name': 'waste','cur_exp_tooltip': """
# Description: This is the cost of waste treatment and disposal.

# Context: The ""Cost of waste treatment and disposal"" is about 10% of the total cost of waste as shown in this list of contributors to the total cost of waste:
# * 60%: Cost of materials purchased, but later wasted
#    This includes raw materials, auxiliary materials, and packaging materials.
# * 20%: Cost of processing the materials before they are wasted
# * 10%: Cost of waste prevention and environmental management
#    This includes the cost of personnel and external services for environmental management;
#    environmental monitoring, assessment, audits, and wildlife habitat protection.
# * 10%:  Cost of waste treatment and disposal
#    This includes haulage and tipping fees, charges, taxes; fines and penalties; related personnel
#    expenses; insurance for environmental liabilities; provisions for clean-up costs, remediation,
#    reclamation, and decommissioning.
# ― ""Environmental Management Accounting Procedures and Principles,"" United Nations Division for Sustainable Development, 2001. ―

# Possibilities: Studies show that 60-90% of materials that companies buy and "consume" in their manufacturing processes never end up in saleable products at all. If we conservatively assume that 70% of product input materials purchased by the company actually end up in sold products, then 30% of the materials are wasted. That is, as shown by the above four waste factors, 30% of the cost of materials = 60% of the total cost of waste. Therefore, (30% of materials cost ÷ 60%) = the total cost of waste. Since the ""Cost of waste treatment and disposal"" is 10% of the total cost of waste, we might use that estimated value here.

# Estimation guidance: If this value is not known or available, edit this comment box to document your estimation logic and sources, for later verification. """,'cur_exp_type': 'number','cur_exp_value': 712.6703055925,cur_exp_value': '','percent_tooltip': '
# Description: The potential percentage reduction in the company's cost of disposing of waste, as a direct or indirect result of the project.

# Context: The cost of waste treatment and disposal is about 10% of the total cost of waste. ― ""Environmental Management Accounting Procedures and Principles,"" United Nations Division for Sustainable Development, 2001 ―

# Possibilities:
# Procter & Gamble, Unilever, Interface, Wal-Mart, Kraft, Ford, Kimberly Clark, and many others are achieving zero waste to landfill at  facilities, resulting in enormous savings and even new revenue streams. GM’s various recycling activities generated more than $2.5 billion in revenue between 2007 and 2010. It now earns $1 billion a year from selling scrap that it used to pay to have hauled away. That is on top of the value the company has achieved by reusing and repurposing materials within its own operations. ― "The Business Case for Zero Waste," GM News, October 2012 ―

# Estimation guidance: The ""% Change"" could be quite high for companies in the extractive, agriculture, manufacturing, and retail sectors which generate a lot of waste. For companies in the service sector, this saving would be minimal and not be worth including. Use this comment box to document assumptions behind your estimate.','percent_type': 'text','percent_value': '40.4%%',cur_exp_value': '',comment': '',},"
# "{'name': 'insurance','cur_exp_tooltip': """
# Definition: This is the cost premiums paid on all company insurance policies.

# Context: It includes premiums for business liability insurance to cover damages to third parties, property insurance to cover damage to business property, business interruption insurance to cover loss of income after a disaster, directors and officers insurance, employee life insurance, and workers' compensation to cover on-the-job injuries to employees.

# Estimation guidance: This could be any value. We are not aware of a good rule of thumb or ratio to estimate what it might be. If this value is not known or available, edit this comment box to document your estimation logic and sources, for later verification.  """,'cur_exp_type': 'number','cur_exp_value': 39827.4556928668,cur_exp_value': '','percent_tooltip': '
# Description: The potential percentage reduction in insurance premiums paid by the company, as a direct or indirect result of the project.

# Context: Insurance coverage includes property insurance to cover damage to business property and business interruption insurance to cover loss of income after a disaster. Both situations could be triggered by severe weather events caused by climate change that also result in severe materials or water shortages and pollution accidents. If companies are positioned to thrive in the face of global climate destabilization, they may be deemed to be low-risk insurance clients, leading to lower premiums for business liability insurance, property insurance, and business interruption insurance.

# If companies use less materials and water, supplied from less risky sources, they may be deemed to be low-risk insurance clients, leading to lower premiums for business liability insurance, property insurance, and business interruption insurance.

# Insurance coverage includes premiums for business liability insurance to cover damages to third parties, like communities, and directors and officers insurance. If the company ensures it improves the wellbeing of communities, its insurance premiums may be lower.

# Insurance such as employee life insurance and workers' compensation to cover on-the-job injuries to employees may be reduced if the company ensures a safe and healthy workplace.

# Estimation guidance: The ""% Change"" could be quite high for companies in the agriculture, manufacturing, and retail sectors which could be impacted by severe weather events caused by climate destabilization. For companies in the service sector, this saving would be minimal and not be worth including. Use this comment box to document assumptions behind your estimate.','percent_type': 'text','percent_value': '43.9%%',cur_exp_value': '',comment': '',},"
# "{'name': 'litigation','cur_exp_tooltip': """
# Definition: This is the cost of fighting and settling law suits related to environmental / pollution and social issues.

# Context: These costs include lawyer fees, court fees, penalties, settlement charges and remediation costs from litigation brought forward by regulators and activist stakeholders for company environmental and social impacts. Remediation costs may include expensive retrofits. Expenses include time spent by company staff and executives during the case and time spent to mitigate the reputational fallout during and after the case.

# Estimation guidance: These could be big lump sum expenses so they are difficult to estimate. If this value is not known or available, edit this comment box to document your estimation logic and sources, for later verification. """,'cur_exp_type': 'number','cur_exp_value': 23409.7285352831,cur_exp_value': '','percent_tooltip': '
# Description: The potential percentage reduction in litigation expenses paid by the company, as a direct or indirect result of the project.

# Context: Litigation costs include lawyer fees, court fees, penalties, settlement charges and remediation costs from litigation brought forward by regulators and activist stakeholders for company environmental and social impacts. Remediation costs may include expensive retrofits. Expenses include time by company staff and executives during the case and to mitigate the reputational fallout.

# Laggard companies on environmental, social, and labor issues may face lawsuits by regulators and activists. For example, companies could be held accountable for damages caused by climate change to which they knowingly contributed (i.e. with significant Scope 1, 2, and 3 greenhouse gas emissions), for delaying regulatory action on climate change (i.e. by lobbying hard for no action), for knowingly deceiving the public about climate change science (i.e. sowing seeds of doubt about climate scientist's credibility and the likely impacts if they are right), and for not mitigating impacts of climate change to its operation that it should have anticipated (e.g. breaching of earthen dams containing its tailing ponds).

# Estimation guidance: The ""% Change"" could be quite high for companies in the extractive, agriculture, and manufacturing sectors since they might be held accountable / liable for carbon, materials, water, and pollution footprints and labor conditions. For companies in the service sector, this saving would be minimal and not be worth including. If a company has not already incurred such litigation expenses, the ""% Change"" would be zero – the possibility of such expenses is accounted for in the risk section, below. Use this comment box to document assumptions behind your estimate.','percent_type': 'text','percent_value': '19.3%%',cur_exp_value': '',comment': '',},"
# "{'name': 'compliance','cur_exp_tooltip': """
# Definition: This is the cost of complying with new environmental or social / workplace regulations.

# Context: These costs include end-of-pipe or process retrofits required to meet new environmental and pollution control standards, as well as expenses associated with meeting new regulations about health, safety, and employee wellbeing. The expenses include time spent by company staff to implement the changes and to verify with regulators that the company is now compliant.

# Estimation guidance: These could be lump sum expenses that are dependent on how closely the company already is to being in compliance. so they are difficult to estimate. If this value is not known or available, edit this comment box to document your estimation logic and sources, for later verification. """,'cur_exp_type': 'number','cur_exp_value': 67243.2536410072,cur_exp_value': '','percent_tooltip': '
# Description: The potential percentage reduction in compliance expenses paid by the company, as a direct or indirect result of the project.

# Context: These costs include end-of-pipe or process retrofits required to meet new environmental and pollution control standards, as well as expenses associated with meeting new regulations about product health and safety. The expenses include time spent by company staff to implement the changes and to verify with regulators that the company is now compliant.

# This benefit could be very indirect. For example, if one of the ways the company contributes to community wellbeing is to be an environmentally and socially responsible corporate citizen, there may be less need for regulators to introduce new regulations to force the company to clean up its act.

# Estimation guidance: The ""% Change"" could be quite high for companies in the agriculture, manufacturing, and retail sectors since they might be  impacted by regulations about climate change. For companies in the service sector, this saving would be minimal and not be worth including. Use this comment box to document assumptions behind your estimate.','percent_type': 'text','percent_value': '16.5%%',cur_exp_value': '',comment': '',},"
# "{'name': 'other','cur_exp_tooltip': """None""",'cur_exp_type': 'number','cur_exp_value': 52447.9577876519,cur_exp_value': '','percent_tooltip': '
# Description: (Complete appropriately)

# Context: (Complete appropriately)

# Possibilities: (Complete appropriately, if available)

# Estimation guidance: (Complete appropriately)','percent_type': 'text','percent_value': '50.7%%',cur_exp_value': '',comment': '',},"


