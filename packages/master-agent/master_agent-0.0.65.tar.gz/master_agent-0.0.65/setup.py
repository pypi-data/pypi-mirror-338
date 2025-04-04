from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='master_agent',
    version='0.0.65',
    author='Stevo Huncho',
    author_email='stevo@stevohuncho.com',
    description='A library providing the tools to solve complex environments in Minigrid using LgTS',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="reinforcement learning, actor-critic, a2c, ppo, multi-processes, gpu, teacher student, ts",
    packages=["master_agent", "master_agent.llm", "master_agent.envs", "master_agent.rl"],
    package_data={
        'master_agent.llm': [
            'dataset/files/*.py',
            'dataset/imgs/*.png',
        ],
    },
    include_package_data=True,
    install_requires=[
        'torch',
        'minigrid',
        'numpy',
        'gymnasium',
        'stable_baselines3',
        'opencv-python',
        'imageio',
        'matplotlib',
    ],
)