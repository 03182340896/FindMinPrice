"""
Problem Statement:
Because it is the Internet Age, but also it is a recession,
the Comptroller of the town of Jurgensville has decided to publish the
prices of every item on every menu of every restaurant in town, all in
a single CSV file (Jurgensville is not quite up to date with modern
data serializationmethods).  In addition, the restaurants of
Jurgensville also offer Value Meals, which are groups of several items,
at a discounted price.  The Comptroller has also included these Value
Meals in the file.

The file's format is:

for lines that define a price for a single item:
restaurant ID, price, item label

for lines that define the price for a Value Meal (there can be any
number of items in a value meal)

restaurant ID, price, item 1 label, item 2 label, ...

All restaurant IDs are integers, all item labels are lower case letters
and underscores, and the price is a decimal number.

Because you are an expert software engineer, you decide to write a
program that accepts the town's price file, and a list of item labels
that someone wants to eat for dinner, and outputs the restaurant they
should go to, and the total price it will cost them.  It is okay to
purchase extra items, as long as the total cost is minimized.

Here are some sample data sets, program inputs, and the expected result:

----------------------------
Data File data.csv

1, 4.00, burger
1, 8.00, tofu_log
2, 5.00, burger
2, 6.50, tofu_log

Program Input
program data.csv burger tofu_log

Expected Output
=> 2, 11.5

---------------------------
"""
import sys
import csv
import os
from collections import defaultdict
from itertools import product

class FindMinPrice():
    def __init__(self,datafile,items_required):
        self.min_price = sys.float_info.max
        self.rest_id = -1

        self.avaliable_restaurants = set()
        self.items_required = items_required

        ## rest_id:menu where menu is dictionary
        ## menu = {(item1,item2):price1, item3: price2}
        self.restaurants = defaultdict(dict)

        ## Avaliable restaurants item_name:[rest_id1,rest_id2...]
        self.item_restrs = defaultdict(list)
        self._load_data(datafile)

    def _load_data(self,datafile):
        with open(os.path.join(os.curdir, datafile), 'rb') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if len(row) >= 3:
                    rest_id = row[0].strip()
                    price = float(row[1].strip())
                    items = []
                    for item in row[2:]:
                        self.item_restrs[item.strip()].append(rest_id)
                        items.append(item.strip())
                    if len(items) > 1:
                        self.restaurants[rest_id][tuple(items)] = price
                    else:
                        self.restaurants[rest_id][items[0]] = price

            for item in self.items_required:
                self.avaliable_restaurants |= set(self.item_restrs[item])

    def _get_min_rest(self, rest_menu):
        possible_sol = defaultdict(list)
        ## Task is to find in combos and single Items for best Price
        ## Combo are those which has key as tuple
        for item in self.items_required:
            possible_sol[item] = [key for key in rest_menu.keys() \
                                                        if item in key]

        sols = [set(i) for i in product(*possible_sol.values())]

        min_value = sys.float_info.max
        for sol in sols:
            total_price = 0
            for key in sol:
                total_price += rest_menu[key]
            if total_price < min_value:
                min_value = total_price
        return min_value

    def get_best_price(self):
        for rest_id in self.avaliable_restaurants:
            rest_min = self._get_min_rest(self.restaurants[rest_id])
            if (self.min_price > rest_min):
                self.rest_id = rest_id
                self.min_price = rest_min
        return (self.rest_id,self.min_price)

if __name__ == "__main__":
    ## Given Items will be different...
    if len(sys.argv) <= 2:
        print "USAGE :python minprice.py filename.csv item1 item2..."
    else:
        minp = FindMinPrice(sys.argv[1],list(sys.argv[2:]))
        best_price = minp.get_best_price()
        if best_price[0] == -1:
            print "All Items are not available in single resaurant \
                                                            or at all"
        else:
            print best_price
