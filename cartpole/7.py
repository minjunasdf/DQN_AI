import gym
import random

env = gym.make('CartPole-v1')

max_time_step = 100

observation = env.reset()

for time_step in range(max_time_step):

    env.render()

    if observation[2] > 0:
        action = 1
    elif observation[2] < 0:
        action = 0
    else:
        action = random.randrange(0, 2)

    observation, reward, done, info = env.step(action)
    print(observation, reward, done)

    if done:
        print("Max Time Step :", time_step + 1)
        break

env.close()