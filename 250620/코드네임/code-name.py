MAX_N = 5

#codenames = []
scores = []

# Please write your code here.
class Agent:
    def __init__(self,name,score):
        self.name = name
        self.score = score

agents= []
for _ in range(MAX_N):
    codename, score = input().split()
    #codenames.append(codename)
    scores.append(int(score))
    agents.append(Agent(codename,score))

find_agent_idx = scores.index(min(scores))
print(agents[find_agent_idx].name,agents[find_agent_idx].score)

