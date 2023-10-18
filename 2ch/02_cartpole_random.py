import gym
import pdb

if __name__ == "__main__":
    env = gym.make("CartPole-v0")

    total_reward = 0.0
    total_steps = 0
    obs = env.reset()

    while True:
        action = env.action_space.sample()
        obs, reward, done, truncated, _ = env.step(action)
        total_reward += reward
        total_steps += 1
        if done or truncated:
            break

    print("Episode done in %d steps, total reward %.2f" % (
        total_steps, total_reward))
