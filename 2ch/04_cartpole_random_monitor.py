
import gym
# from gym.wrappers.monitoring.video_recorder import VideoRecorder
from gym.wrappers import RecordVideo, RecordEpisodeStatistics

if __name__ == "__main__":
    env = gym.make("CartPole-v1", render_mode="rgb_array")
    # env = gym.wrappers.Monitor(env, "recording")
    # Wrap the environment with the recording wrappers
    env = RecordVideo(env, 'video.mp4')  # Record video of the episodes
    env = RecordEpisodeStatistics(env)   # Record episode statistics

    total_reward = 0.0
    total_steps = 0
    obs = env.reset()

    while True:
        action = env.action_space.sample()
        obs, reward, done, truncated, _ = env.step(action)
        total_reward += reward
        total_steps += 1
        if done:
            break

    print("Episode done in %d steps, total reward %.2f" % (
        total_steps, total_reward))
    env.close()
    env.env.close()
