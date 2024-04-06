# synthr-farming
![image](https://camo.githubusercontent.com/7ebfdd135aec70adf671b9ee085baef4a92ff8e3b7851e7a1e5062f0854504fc/68747470733a2f2f696d6775722e636f6d2f6e62426c31574d2e706e67)

Synthr ([mvp.synthr.io](https://mvp.synthr.io/)) action farming scripts

## Overview
This is a personal script, with the intention of performing farming actions in the protocol Synthr, currently on Arbitrum Sepolia. I am making it open source, in case any of my friends want to tinker with it as well.

## Getting Started
Create your virtual environment to run this script.

```bash
python3 -m venv .venv
```

and install requirements

```bash
source .venv/bin/activate && pip3 install -r requirements.txt
```

You will need to create a `.env` file, just like the `.env_sample` file and replace the fields with your parameters.

If you are looking for a free to use RPC URL, use [Chainlist.org](https://chainlist.org/?testnets=true&search=Arbitrum+Sepolia).

Ensure you play around with the application UI first, before running this script, such that you can tinker some of the parameters if need be (see comments).

## Contribution
This is GNU GENERAL PUBLIC LICENSE, do whatever you want! :). If you want to contribute in this project for some reason, just put a PR.