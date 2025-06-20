n = int(input())

class Region:
    def __init__(self,name,street_address,region):
        self.name = name
        self.street_address = street_address
        self.region = region


# Please write your code here.
citizen = []
for _ in range(n):
    n_i, s_i, r_i = input().split()
    citizen.append(Region(n_i,s_i,r_i))

max_name = max(citizen, key = lambda Region:Region.name)

print(f"name {max_name.name}")
print(f"addr {max_name.street_address}")
print(f"city {max_name.region}")