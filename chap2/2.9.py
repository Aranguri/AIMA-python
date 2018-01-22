import random

class Environment(object):
    def __init__(self, size):
        self.agent_pos = 0
        self.agent_reward = 0
        self.agent_step = 0
        self.size = size
        self.map = [False] * self.size

    def add_random_dirt(self):
        for i in range(int(self.size / 5) + 1):
            index = random.randrange(len(self.map))
            self.map[index] = True

    def percept(self):
        self.add_random_dirt()
        is_dirty = self.map[self.agent_pos]
        return [self.agent_pos, is_dirty]

    def act(self, action):
        self.agent_step += 1

        if action == 'left-right':
            action = random.choice(['left', 'right'])

        if action == 'left' and self.agent_pos != 0:
            self.agent_pos -= 1
        elif action == 'right' and self.agent_pos != self.size - 1:
            self.agent_pos += 1
        elif action == 'suck' and self.map[self.agent_pos]:
            print (self.agent_step, self.agent_reward)
            self.agent_reward += 1
            self.map[self.agent_pos] = False

class Agent(object):
    def __init__(self, env):
        self.env = env
        self.rules = {}
        for i in range(self.env.size):
            self.rules[i] = {True: 'suck', False: 'left-right'}
        #self.rules[0] = {True: 'suck', False: 'right'}
        #self.rules[1] = {True: 'suck', False: 'left'}

    def live(self):
        while True:
            pos, is_dirty = self.env.percept()
            action = self.rules[pos][is_dirty]
            self.env.act(action)

env = Environment(2)
agent = Agent(env)
agent.live()
