# Gas Alert Discord Bot

Gas Alert Discord Bot is a Python-based Discord bot that monitors the gas price on the Ethereum network and sends notifications to users when the gas price drops to or below a specified threshold.

## Prerequisites

- Python 3.6 or higher
- Discord.py library
- Requests library

## Installation

1. Clone the repository or download the source code.

```bash
git clone https://github.com/codeesura/gas-alert-discord-bot.git
```

2. Install the required dependencies using pip.

```bash
pip install -r requirements.txt
```


## Configuration

1. Obtain an API key from Etherscan. You can sign up on the Etherscan website to get an API key.

2. Open the `gas_alert_bot.py` file and replace `'YOUR_API_KEY'` with your actual Etherscan API key.

## Usage

1. Invite the bot to your Discord server.

2. Run the bot script using the following command:

```bash
python gas_alert_bot.py
```


3. Set the gas price to trigger the alert by using the `/gasalert` command in Discord. For example, to set the alert threshold to 50 Gwei, you can type `/gasalert 50`.

4. The bot will start monitoring the gas price every 60 seconds. If the gas price drops to or below the specified threshold, it will send a notification to the user who set the alert.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/codeesura/gas-alert-discord-bot/blob/main/LICENSE) file for more information.

