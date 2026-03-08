# Betting Bot (IPL)

This project implements an automated betting bot targeting Indian Premier League (IPL) markets. The bot's goals are:
- Place bets objectively (no human bias).
- Prefer markets and strategies that allow exiting (cashout / in-play) before a match concludes.
- Support reproducible, auditable decision-making.

## Scope
- Prototype for automated bet selection and cashout-friendly strategies.
- NOT a guaranteed-money system; intended for research, automation, and strategy testing.
- Legal and regulatory compliance is the user's responsibility.

## Features (planned)
- Market data ingestion (odds, live match state).
- Strategy modules (configurable rules / ML models).
- Cashout / partial-exit decision logic.
- Logging, audit trail, and backtesting support.
- Safe execution layer with rate limits and error handling.

## Data & Assumptions
- Reliable real-time odds feed required.
- Exchange/bookmaker APIs for placing bets and cashouts.
- Assumes access to historical data for backtesting.

## Important Notes
- Check local laws and platform terms before using the bot.
- Start with simulation/backtesting before live deployment.
- Use risk limits and monitoring.

## Project layout
- src/  — core logic and strategies
- data/ — feeds and historical data
- tests/ — unit and integration tests
- docs/  — design and usage docs
